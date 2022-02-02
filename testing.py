list_A = [1,2,3,4,5]
list_B = ["A","B","C","D","E"]

list_C = zip(list_B,list_A)

Dict = dict(list(list_C))
new_list = []


for key,value in Dict.items():
    if value == 4:
        print("4 is in the dictionary")
        new_list.append((value,key))
    elif key == "C":
        print(f"Found key {key} in the dictionary")
        new_list.append((value,key))
        
print(dict(new_list))



    
    
    

