def minMoves(arr):
    swapZeroRight = []
    swapZeroLeft = []
    countRight = 0
    countLeft = 0

    for i in arr:
        swapZeroRight.append(i)
        swapZeroLeft.append(i)

    for i in range(0, (len(swapZeroRight) - 1)):
        j = (len(swapZeroRight) - 1)
        if swapZeroRight[i] < swapZeroRight[j]:
            countRight += 1
            temp = swapZeroRight[j]
            swapZeroRight[j] = swapZeroRight[i]
            swapZeroRight[i] = temp
            print(swapZeroRight)

            j -= 1
        else:
            j -= 1

    for i in range(0, (len(swapZeroLeft) - 1)):
        j = (len(swapZeroLeft) - 1)
        if swapZeroLeft[i] > swapZeroLeft[j]:
            countLeft += 1
            tempValue = swapZeroLeft[j]
            swapZeroLeft[j] = swapZeroLeft[i]
            swapZeroLeft[i] = tempValue
            print(swapZeroLeft)
            j -= 1
        else:
            j -= 1

    print(countLeft)
    print(countRight)
    if countRight < countLeft:
        return countRight
    else:
        return countLeft

minMoves([1,1,1,0])