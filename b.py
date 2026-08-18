# inputs = ["eat","tea","tan","ate","nat","bat"]

# Output = [["bat"],["nat","tan"],["ate","eat","tea"]] 


# def groupsanagram(inputs : list[str]):

#     groups = {}

#     for i in inputs:
#         key = ''.join(sorted(i))

#         if key not in groups:  
#             groups[key] = []

#         groups[key].append(i)
    
#     print(groups)
#     return list(groups.values())


# result = groupsanagram(inputs)

# print(result)

# inputs = ["flower" , "flow" , "flight"]

# # longest fl is 

# def validateanagrams(data : list[str]):

#     res = ""

#     for i in range(len(data[0])):

#         for n in data:
#             if i == len(n) or n[i] != data[0][i]: 
#                 return res
#         res+=data[0][i]  
#     return res 

# rs = validateanagrams(inputs)
# print(rs)
# from dotenv import load_dotenv

# load_dotenv()


# from langchain_core.tools import tool

# @tool
# def addnumber(d:int , c:int):
#     """this function is used for add numbers """
#     return d+c 

# from langchain_groq import ChatGroq

# models = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0,
# )

# result =models.bind_tools([addnumber])

# res = models.invoke('what is full form of ai')
# print(res.content)

