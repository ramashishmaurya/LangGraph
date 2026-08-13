class Hashmap:
    def __init__(self):
        self.size = 4 
        self.bucket = [[] for _ in range(self.size)]

abc = Hashmap() 

print(abc.size)

