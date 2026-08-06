n = [1 ,2,3,4]

m = [2,1,4,5]

setsa = set(n)
setsb = set(m) # union is present in the sets only bhai 
setsc = range(1 ,9)
 
print(setsa)
# here u can add many more okay 
#print("this is union of thisn  things is right " , setsa.union(setsb).union(setsc))

import copy

def copymethods():
    orinals = [[1,2] , [4,5]]

    shallow = copy.copy(orinals)

    deep = copy.deepcopy(orinals)

    shallow[0][0] = 10 
    deep[1][1] = 20

    print("originals " , orinals )
    print("shalloww" , shallow)
    print("deep" , deep)

def function():
    return "this is sets okay "



if __name__ == "__main__":
    print(function())
 

