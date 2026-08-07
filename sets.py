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


nums = [2,7,11,15]
target = 9 
# Output: [0,1]
 
def twosum(nums , target):
    for i , b in enumerate(nums):
        hashmap  = {}
        for i , n in enumerate(nums):
            numbers = target - n 
            if numbers in hashmap:
                return [hashmap[numbers] , i ]
            hashmap[n] = i 

cl = twosum(nums , target)
print(cl)


def printnumber():
    for i in range(1 ,5):
        yield i 

obj = printnumber()

for i in obj:
    print(i)


# return the listcontain duplicated or not 
    
numbers = [1 ,3,4,5]

# if lens(Set) = 4 and orinal num = 4  
def checkduplicated(nums):
    if (len(set(nums)) != len(nums)):
        return True
    return False


objects = checkduplicated(numbers)

print(objects)

def containduplicated(nums):
    hashmap = set()

    for i in nums:
        if i in hashmap: # if the data is already present then but firrst time of course empty 
            return True
        hashmap.add(i) # first time data will be added here 
    return False

listdata = [1 ,2 , 1,3]

result = containduplicated(listdata)
print(result)
print()