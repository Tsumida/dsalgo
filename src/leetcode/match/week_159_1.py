# 2019-10-20

class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        coordinates.sort(key=lambda p: (p[0], p[1]))
        #co = 0.0
        #print(coordinates)
        n = len(coordinates)
        is_ver = False
        coors = []
        for i in range(1, n):
            p1, p2 = coordinates[i], coordinates[i-1]
            # 竖直线, 分母为0
            if p1[0] == p2[0]:
                is_ver = True
                break
            else:
                # 斜率
                coors.append(
                    float((p1[1] - p2[1]) / (p1[0] - p2[0]))
                )


        if is_ver:
            x = coordinates[0][0]
            if all(x == p[0] for p in coordinates):
                return True
            else:
                return False

        co = coors[0]
        if all(co == a for a in coors):
            return True

        return False

s = Solution()
assert True == s.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
assert False == s.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
assert True == s.checkStraightLine(coordinates= [[2, 1], [3, 2], [4, 3]])
assert False == s.checkStraightLine(coordinates=[[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]])
