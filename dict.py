dict_data = {"title":"ragam","author":"manu","year":"2026","pages":"20","rating":"5"}
print(dict_data)
for key,value in dict_data.items():
    
    print(f"{key} : {value}")

dict_data["rating"]=4.5


dict_data['genre']="novel"

for key in dict_data:
    print(f"{key}: {dict_data[key]}")

if "publish" in dict_data:
    print("exists")
else:
    dict_data['publish']="ABC"
    print(dict_data)
dict_data.pop("year")
print(dict_data)
if "publish" in dict_data:
    print("exists")
else:
    dict_data['publish']="ABC"
    print(dict_data)