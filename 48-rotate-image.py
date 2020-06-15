"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(i,len(matrix)-i-1):
                first_element = matrix[i][j]
                second_element = matrix[j][-i-1]
                third_element = matrix[-i-1][-j-1]
                fourth_element = matrix[-j-1][i]
                
                matrix[j][-i-1] = first_element
                matrix[-i-1][-j-1] = second_element
                matrix[-j-1][i] = third_element
                matrix[i][j] = fourth_element