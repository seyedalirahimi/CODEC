# importing libraries
import cv2
import numpy as np

from utils import runLength, inverse_runLength

quantmatrix = 1
blockSize = 8
floatScale = 255.0

width = 536
height = 960


def encode(frame):
    output = np.zeros((width, height))

    for i in range(0, width, blockSize):
        for j in range(0, height, blockSize):
            output[i:i + blockSize, j:j + blockSize] = internalEncode(frame[i:i + blockSize, j:j + blockSize])

    runLengthOutput = runLength(output)

    return runLengthOutput

def internalEncode(frame):
    imf = np.float32(frame) / floatScale  # float conversion/scale

    dct = cv2.dct(imf, )  # the dct
    if dct.min() < 0:
        dct = dct - dct.min()

    # Quantization
    quantizationFrame = np.round(dct / quantmatrix)
    return quantizationFrame

def decode(frame, width, height):
    inverseRunLengthFrame = inverse_runLength(frame, width, height)
    output = np.zeros((width, height), dtype=np.uint8)

    for i in range(0, width, blockSize):
        for j in range(0, height, blockSize):
            output[i:i + blockSize, j:j + blockSize] = internalDecode(
                inverseRunLengthFrame[i:i + blockSize, j:j + blockSize])

    return output

def internalDecode(frame):
    quantizationFrame = frame * quantmatrix

    idct = cv2.idct(quantizationFrame)  # the dct

    iOutFrame = np.uint8(idct * floatScale)  # convert back to int
    return iOutFrame


# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('a.avi')

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video  file")

# Read until video is completed
"""
ENCODE
"""
encodedFrames = []
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayFrame = grayFrame[:width][:height]
        encodeFrame = encode(grayFrame)
        encodedFrames.append(encodeFrame)

    # Break the loop
    else:
        break


"""
SAVE TO FILE
"""
with open("file.txt", "w") as f:
    for frame in encodedFrames:
        for element in frame:
            f.write(f'{int(element[0])},{int(element[1])}\t')
        f.write('\n')


"""
LOAD FROM FILE
"""
loadFrames = []
with open("file.txt", "r") as f:
    for line in f:
        temp = []
        sp = line.split('\t')
        for s in sp:
            if s == '\n': continue
            x = s.split(',')
            temp.append([int(x[0]), int(x[1])])
        loadFrames.append(temp)

"""DECODE"""
for frame in loadFrames:

    decodeFrame = decode(frame, width, height)
    print('show')
    # Display the resulting frame
    cv2.imshow('decodeFrame', decodeFrame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
