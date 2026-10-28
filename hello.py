print("Hello Python")

dic=[
   {"name":"nimmi","age":"30"},
   {"names":"raj","ages":"40"}
]

print(dic[0]['name'])
print(dic[0].keys())
print(dic[0].values())

for i in dic:
    print(i.keys())

for i in dic:
    print(i.items())

for i in dic:
    for key,value in i.items():
        print(key,value)
        print(f"{key}:{value}")

del dic[0]["age"]
print(dic)
dic[1].pop("ages")
print(dic)
dic.clear()
print(dic)