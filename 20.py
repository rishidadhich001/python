def Remove(duplicate):
    list=[]
    for i in duplicate:
        if i not in list:
            list.append(i)
            return list
        
duplicate=[3,4,5,6,4,6,5,5,3]
print(Remove(duplicate))