#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#brute force approach
def rotate_matr_90(matrix):
  n = len(matrix)
  result = [[0 for _ in range(0,n)] for _ in range(0,n)]
  for i in range(0,n):
    for j in range(0,n):
      result[j][(n-1)-i] = matrix[i][j]
  
  for i in range(0,n):
    for j in range(0,n):
      print(result[i][j], end=" ")
    print()

matrix = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
rotate_matr_90(matrix)


#optimal solution
def rot_matr_90(matrix):
  n = len(matrix)
  for i in range(0,n-1):
    for j in range(i+1,n):
      matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]
  
  for i in range(0,n):
    matrix[i].reverse()
  for i in range(0,n):
      for j in range(0,n):
        print(matrix[i][j], end=" ")
      print()

matrix1 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
rot_matr_90(matrix1)