# def rotate(self, matrix: list[list[int]]) -> None:
#     n = len(matrix[0])
#     for i in range(n // 2 + n % 2):
#         for j in range(n // 2):
#             tmp = matrix[n - 1 - j][i]
#             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
#             matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
#             matrix[j][n - 1 - i] = matrix[i][j]
#             matrix[i][j] = tmp
#     print(matrix)
# print(rotate(rotate,[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))


#another approach 
#first transpose it and then reverse it 
def rotate(self, matrix):
    transpose(transpose, matrix)
    reverse(reverse, matrix)
    print(matrix)

def transpose(self, matrix):
    n=len(matrix) 
    for i in range(len(matrix)):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
    

def reverse(self, matrix):
    n=len(matrix)
    for i in range(len(matrix)):
        for j in range(n//2):
            matrix[i][j], matrix[i][-j-1]= matrix[i][-j-1], matrix[i][j]
    
rotate(rotate,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])










    #[[1,2,3],[4,5,6],[7,8,9]]
    #[[7,4,1],[8,5,2],[9,6,3]]