class Solution(object):
    def checkStraightLine(self, coordinates):
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            dyp = coordinates[i][1] - coordinates[0][1]
            dxp = coordinates[i][0] - coordinates[0][0]
            if dy * dxp != dx * dyp:
                return False
        return True

s = Solution()
if s.checkStraightLine([[0,1],[1,3],[2,5]]) == True:
    print("It's a line")
else:
    print("It's not a line")