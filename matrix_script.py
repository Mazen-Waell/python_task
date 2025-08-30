
import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
text=''

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m) :
    for j in  range(n) :
        text +=matrix[j][i] 

# symbols=['!','@','#','$','%','&']
# for i in range(len(text)) :
#     if text[i] in symbols :
#         text=text.replace(text[i]," ")

result = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', text)

print(result)