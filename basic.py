nums = [3,2,2,3]
val = 3
Output = []

def removeelement(nums , val):

    k = 0 

    for  i in range(len(nums)):
        if nums[i] != val :
            nums[k] = nums[i]
            Output.append(nums[k])
            k+= 1 
        
    print(Output)
    return k 


print(removeelement(nums , val))


nums = [2,2,1,1,1,2,2]
Output =  2



def maxrepatedvalues(nums):
    hashmap ={}

    for i in nums:
        hashmap[i] = 1 + hashmap.get(i,0)
    
    for num in hashmap:
        if hashmap[num] > len(nums) // 2 :
            return num 


result = maxrepatedvalues(nums)
print(result)

# how i needed to make surew how  i how this 