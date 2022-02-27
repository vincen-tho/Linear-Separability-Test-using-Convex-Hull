import numpy as np
import math

class ConvexHull:
    def __init__(self, arrayOfPoints):
        def vertices(arrayOfPoints):
            idxMin, idxMax = extremePoint(arrayOfPoints)
            above = np.array([])
            below = np.array([])
            above, below = groupPoints(idxMin, idxMax, arrayOfPoints)

            aboveHull = findHull(above, idxMin, idxMax, arrayOfPoints)
            belowHull = findHull(below, idxMax, idxMin, arrayOfPoints)

            vertices = np.array([idxMin])
            for i in aboveHull:
                vertices = np.append(vertices, i)

            vertices = np.append(vertices, [idxMax])
            for i in belowHull:
                vertices = np.append(vertices, i)

            return vertices

        def simplices(vertices):
            simplices = np.array([[]])
            for i in range(len(vertices)):

                last = len(vertices) - 1
                if i != last:
                    simplices = np.append(simplices, [vertices[i], vertices[i + 1]])
                else:
                    simplices = np.append(simplices, [vertices[i], vertices[0]])

            simplices = np.reshape(simplices, (-1, 2))
            simplices = simplices.astype(int)

            return simplices

        def extremePoint(arrayOfPoints):
            idxMin = 0
            idxMax = 0

            for i in range(len(arrayOfPoints)):
                if arrayOfPoints[i][0] < arrayOfPoints[idxMin][0]:
                    idxMin = i
                elif arrayOfPoints[i][0] == arrayOfPoints[idxMin][0]:
                    if arrayOfPoints[i][1] < arrayOfPoints[idxMin][1]:
                        idxMin = i

                if arrayOfPoints[i][0] > arrayOfPoints[idxMax][0]:
                    idxMax = i
                elif arrayOfPoints[i][0] == arrayOfPoints[idxMax][0]:
                    if arrayOfPoints[i][1] > arrayOfPoints[idxMax][1]:
                        idxMax = i

            return idxMin, idxMax

        def groupPoints(idxLeft, idxRight, arrayOfPoints):
            left = arrayOfPoints[idxLeft]
            right = arrayOfPoints[idxRight]

            left = np.insert(left, 2, 1)
            right = np.insert(right, 2, 1)

            above = np.array([])
            below = np.array([])

            for i in range(len(arrayOfPoints)):
                if i != idxLeft and i != idxRight:
                    point = arrayOfPoints[i]
                    point = np.insert(point, 2, 1)

                    det = np.linalg.det([left, right, point])
                    if det > 0:
                        above = np.append(above, i)
                    else:
                        below = np.append(below, i)

            above = above.astype(int)
            below = below.astype(int)

            return above, below

        def distanceBetweenPointAndLine(left, right, point):
            x1 = left[0]
            y1 = left[1]
            x2 = right[0]
            y2 = right[1]
            x0 = point[0]
            y0 = point[1]

            a = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
            b = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            return a / b

        def findHull(arrayOfIndexes, idxMin, idxMax, arrayOfPoints):
            if len(arrayOfIndexes) == 0 or len(arrayOfIndexes) == 1:
                return arrayOfIndexes
            else:
                left = arrayOfPoints[idxMin]
                right = arrayOfPoints[idxMax]

                maxDistIdx = int(arrayOfIndexes[0])
                maxDistPoint = arrayOfPoints[maxDistIdx]
                maxDist = distanceBetweenPointAndLine(left, right, maxDistPoint)

                for i in arrayOfIndexes:
                    index = i
                    point = arrayOfPoints[index]
                    dist = distanceBetweenPointAndLine(left, right, point)

                    if dist > maxDist:
                        maxDistIdx = index
                        maxDist = dist

                above1, below1 = groupPoints(idxMin, maxDistIdx, arrayOfPoints)
                hull1 = findHull(above1, idxMin, maxDistIdx, arrayOfPoints)
                above2, below2 = groupPoints(maxDistIdx, idxMax, arrayOfPoints)
                hull2 = findHull(above2, maxDistIdx, idxMax, arrayOfPoints)

                hull = np.concatenate((hull1, [maxDistIdx], hull2))

                return hull

        self.vertices = vertices(arrayOfPoints)
        self.simplices = simplices(self.vertices)

