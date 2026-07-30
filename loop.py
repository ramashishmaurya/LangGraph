
# *********
#  *******
#   *****
#    ***
#     *

nrows = 5 
ncols = 9 
for i in range(nrows):
    for space in range(i):
        print(" " , end=" ")
    for start in range(  - i*2):
        print("*" , end=" ")
    print(" ")


