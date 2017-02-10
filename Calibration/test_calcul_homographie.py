from Calcule_homographie import *
import numpy as np

#Test build_A
print(build_A([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
  ]))

#Test build_b
print(build_b([[1,2],[3,4],[5,6],[7,8]]))

#Test build_H
print(build_H(np.matrix([[1,2,3,4,5,6,7,8,9,10,11,12]])))

#Test homography
# Lx =[[10,20],[35,41],[29,63], [53,69]]
# LX =[[30, 65],[110,115],[81, 175], [150,210]]
# H = homography(Lx,LX)
# print(H)

# Generate set of test data
# Points sur le sol
LX = np.array([
              [0, 0, 0, 1],
              [20, 10, 0, 1],
              [35, 41, 0, 1],
              [-29, 63, 0, 1]])
H = np.array([[50, 0, 0, 0],
              [0, 50, 0, 0],
              [0, 0, 1, 1]])
Lx = np.empty( (len(LX), 3) )
for i in range(0, len(LX)):
    # print(LX[i])
    Lx[i] = np.dot(H, LX[i])

H_computed = np.linalg.lstsq(build_A(LX), build_b(Lx))[0]

# Testing
# np.dot(H_computed.reshape(3,4), LX[2]) - Lx[2]