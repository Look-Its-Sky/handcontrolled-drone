def getDeltaPoint(start: tuple, end: tuple) -> tuple:
    return (end[0] - start[0], end[1] - start[1])

def getDirection(start: tuple, end: tuple, threshold: float) -> tuple:
    deltaPoints = getDeltaPoint(start, end)
    temp = [None, None]

    if deltaPoints[0] > threshold or deltaPoints[0] < -threshold:
        if deltaPoints[0] > 0:
            temp[0] = -1

        elif deltaPoints[0] < 0:
            temp[0] = 1

        else:
            temp[0] = 0

    if deltaPoints[1] > threshold or deltaPoints[1] < -threshold:
        if deltaPoints[1] > 0:
            temp[1] = 1
        
        elif deltaPoints[1] < 0:
            temp[1] = -1

        else:
            temp[1] = 0

    return (temp[0], temp[1])