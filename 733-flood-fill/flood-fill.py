class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        n, m = len(image), len(image[0])
        cur = image[sr][sc]
        if cur == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                if 0 <= ni < n and 0 <= nj < m and image[ni][nj] == cur:
                    image[ni][nj] = color
                    q.append((ni, nj))
        return image 