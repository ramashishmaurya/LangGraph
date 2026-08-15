
inputs = int(input("Enter the query "))

# 123 
var = inputs
store = 0 

while inputs > 0 :
    lastdigits = inputs % 10
    store = store*10 +  lastdigits
    inputs = inputs // 10 

if var == store:
    print('this is plaindrome number ')
else:
    print('not palindrome number')


nums = [5,2,3,1]
p = [1,2,3,5]

def sortingalgo(nums:list[int]):
    for i in range(len(nums)-1): 
         nums[i] = nums[i+1]  
    return nums
      
#abc  = sortingalgo(nums)



# bubblesort as  n - square worst case best case o(n)

class solution: 
     def SortArray(self , nums):
          if len(nums) <=1:
               return nums
          
          mid = len(nums) // 2 

          left = self.SortArray(nums[:mid])
          right = self.SortArray(nums[mid:])
          i = j = []

from fastapi import FastAPI

app = FastAPI()

@app.get('/api')
def getuser():
     return ({
          'naem' : 'ashish' , 
          'class' : 12 
     })


# how this is made is to make sne right bhaihow this is need is to make sense  as posisble ways to righ has to make sense as right bhai how i needed to make sense bhaohow thisnis make sende as possible ways is to make sense  as followed right okay how thisnis right okay how this is main focused how this is good to runs bhasi 