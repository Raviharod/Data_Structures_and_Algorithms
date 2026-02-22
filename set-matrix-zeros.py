#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#brute force soln
def set_mat_zeros(nums):
  rows = len(nums)
  cols = len(nums[0])
  indexes = []
  for i in range(0,rows):
    for j in range(0,cols):
      if nums[i][j] == 0:
        indexes.append([i,j])
  for list in indexes:
    for r in range(0,rows):
      nums[r][list[1]] = 0
    for c in range(0,cols):
      nums[list[0]][c] = 0
  for i in range(0,rows):
    for j in range(0,cols):
      print(nums[i][j], end=" ")
    print()

nums = [[7,9,2,3], [20,8,0,10], [29,0,-10,5], [4,14,6,7]]
set_mat_zeros(nums)

#optimal solution
def set_matrix_zeros(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  rowTrack = [0 for _ in range(0,rows)]
  colTrack = [0 for _ in range(0,cols)]

  for i in range(0,rows):
    for j in range(0,cols):
      if matrix[i][j] == 0:
        rowTrack[i] = -1
        colTrack[j] = -1
  
  for i in range(0,rows):
    for j in range(0,cols):
      if rowTrack[i] != 0 or colTrack[j] != 0:
        matrix[i][j] = 0
  
  print(matrix)

matrix = [[7,9,2,3], [20,8,0,10], [29,0,-10,5], [4,14,6,7]]
set_matrix_zeros(matrix)