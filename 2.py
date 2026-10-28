# Write a Python function that receives a list of dictionaries representing API responses,
#  merges them into a single dictionary (combining values for duplicate keys into lists), and returns the result.

# Example input:

# [

# {'id': 1, 'name': 'A'},

# {'id': 2, 'name': 'B'},

# {'id': 1, 'status': 'active'}

# ]Expected output:

# {'id': [1, 2, 1], 'name': ['A', 'B'], 'status': 'active'}

def Mergedict(self,a,b):
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def merge(self):
        m=self.a+self.b
        print(m)

obj=  Mergedict({'id': 1, 'name': 'A'},{'id': 2, 'name': 'B'})
obj.merge()      
