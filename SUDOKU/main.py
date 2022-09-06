# main process

from texttable import Texttable as tt
import numpy as np

blank = np.zeros((3,3))
print(blank)

# 1~9 * 9
# t = tt().add_rows([["SU","DO","KU"],[[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]],[[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]],[[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]])
# [0,0,0] * 3 * 9
t = tt().add_rows([["SU","DO","KU"],blank,blank,blank,blank,blank,blank,blank,blank,blank])
print(t.draw())

