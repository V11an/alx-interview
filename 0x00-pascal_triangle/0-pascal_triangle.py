#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):

  if n <= 0:
    return []  # Handle edge case: return empty list for n <= 0

  triangle = []
  # First row is always [1]
  triangle.append([1])

  # Iterate for subsequent rows (starting from row 2)
  for i in range(1, n):
    row = [1]  # Each row starts with 1
    # Calculate middle elements using elements from the previous row
    for j in range(1, i):
      row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)  # Each row ends with 1
    triangle.append(row)

  return triangle
