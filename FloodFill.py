class Solution():
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]
        if old_color != color:
            self.find(image,sr,sc,old_color,color)

        return image

    def find(self, image, i, j, old, new):

        if i < 0 or i > len(image) - 1:
            return

        if j < 0 or j > len(image[0]) - 1:
            return

        if image[i][j] != old:
            return
        else:
            image[i][j] = new
            self.find(image, i, j-1, old, new)
            self.find(image, i, j+1, old, new)
            self.find(image, i-1, j, old, new)
            self.find(image, i+1, j, old, new)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
s = Solution()
print(s.floodFill(image,sr,sc,color))