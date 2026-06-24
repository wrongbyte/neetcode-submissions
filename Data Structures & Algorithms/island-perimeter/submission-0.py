# create a set containing the coordinates of all squares that contain land.
# the "initial" perimeter of a square is 4, for each square adjacent to it
# we subtract 1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        land_squares = set([])
        LAND = 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == LAND:
                    land_squares.add((i,j))

        for (i,j) in land_squares:
            square_perimeter = 4 
            #up
            if (i-1, j) in land_squares:
                square_perimeter -= 1
            #down
            if (i+1, j) in land_squares:
                square_perimeter -= 1
            #left
            if (i, j - 1) in land_squares:
                square_perimeter -= 1
            #right
            if (i, j + 1) in land_squares:
                square_perimeter -= 1

            perimeter += square_perimeter

        return perimeter
