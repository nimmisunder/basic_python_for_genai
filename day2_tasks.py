list_add=[]
print(list)
while True:
    status=input("Do you want to  add y/n :")
    if status=="y":
        next=input("add one : ")
        list_add.append(next)
        print(list_add)
    else:
        print(f"final list : {list_add}")
        print(f"No of items : {len(list_add)}")
        print(f"first item : {list_add[0]}")
        print(f"last item : {list_add[-1]}")
        print(f"sorted list : {list_add[-1]}")
        print(f"final list : {list_add[-1]}")

        break
while True:
    statusremove=input("Do you want to remove any item y/n :")
    if statusremove == "y":
        remove = input("which one to remove ? ")
        list_add.remove(remove)
        print(list_add)
    else:
        break