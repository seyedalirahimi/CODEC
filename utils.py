# Zigzag scan of a matrix
# Argument is a two-dimensional matrix of any size,
# not strictly a square one.
# Function returns a 1-by-(m*n) array,
# where m and n are sizes of an input matrix,
# consisting of its items scanned by a zigzag method.
#
# Matlab Code:
# Alexey S. Sokolov a.k.a. nICKEL, Moscow, Russia
# June 2007
# alex.nickel@gmail.com

import numpy as np


def zigzag(input):
    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    vmax = input.shape[0]
    hmax = input.shape[1]

    # print(vmax ,hmax )

    i = 0

    output = np.zeros((vmax * hmax))
    # ----------------------------------

    while (v < vmax) and (h < hmax):

        if ((h + v) % 2) == 0:  # going up

            if v == vmin:
                # print(1)
                output[i] = input[v, h]  # if we got to the first line

                if h == hmax:
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif (h == hmax - 1) and (v < vmax):  # if we got to the last column
                # print(2)
                output[i] = input[v, h]
                v = v + 1
                i = i + 1

            elif (v > vmin) and (h < hmax - 1):  # all other cases
                # print(3)
                output[i] = input[v, h]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # going down

            if (v == vmax - 1) and (h <= hmax - 1):  # if we got to the last line
                # print(4)
                output[i] = input[v, h]
                h = h + 1
                i = i + 1

            elif h == hmin:  # if we got to the first column
                # print(5)
                output[i] = input[v, h]

                if v == vmax - 1:
                    h = h + 1
                else:
                    v = v + 1

                i = i + 1

            elif (v < vmax - 1) and (h > hmin):  # all other cases
                # print(6)
                output[i] = input[v, h]
                v = v + 1
                h = h - 1
                i = i + 1

        if (v == vmax - 1) and (h == hmax - 1):  # bottom right element
            # print(7)
            output[i] = input[v, h]
            break

    # print ('v:',v,', h:',h,', i:',i)
    return output


# Inverse zigzag scan of a matrix
# Arguments are: a 1-by-m*n array,
# where m & n are vertical & horizontal sizes of an output matrix.
# Function returns a two-dimensional matrix of defined sizes,
# consisting of input array items gathered by a zigzag method.
#
# Matlab Code:
# Alexey S. Sokolov a.k.a. nICKEL, Moscow, Russia
# June 2007
# alex.nickel@gmail.com
def inverse_zigzag(input, vmax, hmax):
    # print input.shape

    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    output = np.zeros((vmax, hmax))

    i = 0
    # ----------------------------------

    while (v < vmax) and (h < hmax):
        # print ('v:',v,', h:',h,', i:',i)
        if ((h + v) % 2) == 0:  # going up

            if v == vmin:
                # print(1)

                output[v, h] = input[i]  # if we got to the first line

                if h == hmax:
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif (h == hmax - 1) and (v < vmax):  # if we got to the last column
                # print(2)
                output[v, h] = input[i]
                v = v + 1
                i = i + 1

            elif (v > vmin) and (h < hmax - 1):  # all other cases
                # print(3)
                output[v, h] = input[i]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # going down

            if (v == vmax - 1) and (h <= hmax - 1):  # if we got to the last line
                # print(4)
                output[v, h] = input[i]
                h = h + 1
                i = i + 1

            elif h == hmin:  # if we got to the first column
                # print(5)
                output[v, h] = input[i]
                if v == vmax - 1:
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1

            elif (v < vmax - 1) and (h > hmin):  # all other cases
                output[v, h] = input[i]
                v = v + 1
                h = h - 1
                i = i + 1

        if (v == vmax - 1) and (h == hmax - 1):  # bottom right element
            output[v, h] = input[i]
            break

    return output


def runLength(input):
    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    vmax = input.shape[0]
    hmax = input.shape[1]

    # print(vmax ,hmax )

    numberOfZero = 0

    output = []
    # ----------------------------------

    while (v < vmax) and (h < hmax):

        if ((h + v) % 2) == 0:  # going up

            if v == vmin:
                # print(1)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                if h == hmax:
                    v = v + 1
                else:
                    h = h + 1


            elif (h == hmax - 1) and (v < vmax):  # if we got to the last column
                # print(2)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                v = v + 1

            elif (v > vmin) and (h < hmax - 1):  # all other cases
                # print(3)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                v = v - 1
                h = h + 1


        else:  # going down

            if (v == vmax - 1) and (h <= hmax - 1):  # if we got to the last line
                # print(4)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                h = h + 1


            elif h == hmin:  # if we got to the first column
                # print(5)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                if v == vmax - 1:
                    h = h + 1
                else:
                    v = v + 1



            elif (v < vmax - 1) and (h > hmin):  # all other cases
                # print(6)
                if abs(input[v, h]) != 0:
                    output.append([numberOfZero, input[v, h]])
                    numberOfZero = 0
                else:
                    numberOfZero += 1

                v = v + 1
                h = h - 1

        if (v == vmax - 1) and (h == hmax - 1):  # bottom right element
            # print(7)
            output.append([numberOfZero, input[v, h]])

            break
    return output


def inverse_runLength(input, vmax, hmax):
    # print input.shape

    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    output = np.zeros((vmax, hmax))

    currentElement = input.pop(0)
    # ----------------------------------

    while (v < vmax) and (h < hmax):
        if currentElement[0] < 0:
            currentElement = input.pop(0)

        if currentElement[0] == 0:
            currentValue = currentElement[1]
        else:
            currentValue = 0
        currentElement[0] -= 1

        # print ('v:',v,', h:',h,', i:',i)
        if ((h + v) % 2) == 0:  # going up

            if v == vmin:
                # print(1)

                output[v, h] = currentValue  # if we got to the first line

                if h == hmax:
                    v = v + 1
                else:
                    h = h + 1


            elif (h == hmax - 1) and (v < vmax):  # if we got to the last column
                # print(2)
                output[v, h] = currentValue
                v = v + 1

            elif (v > vmin) and (h < hmax - 1):  # all other cases
                # print(3)
                output[v, h] = currentValue
                v = v - 1
                h = h + 1


        else:  # going down

            if (v == vmax - 1) and (h <= hmax - 1):  # if we got to the last line
                # print(4)
                output[v, h] = currentValue
                h = h + 1

            elif h == hmin:  # if we got to the first column
                # print(5)
                output[v, h] = currentValue
                if v == vmax - 1:
                    h = h + 1
                else:
                    v = v + 1

            elif (v < vmax - 1) and (h > hmin):  # all other cases
                output[v, h] = currentValue
                v = v + 1
                h = h - 1

        if (v == vmax - 1) and (h == hmax - 1):  # bottom right element
            output[v, h] = currentValue
            break

    return output


