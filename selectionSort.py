def selectionSort(list):
    for  i in range(len(list)):
        lowestNumber = i
        j = i+1
        for j in range(len(list)-1):
            if list[j]>list[lowestNumber]:
                lowestNumber = j
            if lowestNumber!=i:
                temp = list[i]
                list[i]=list[lowestNumber]
                list[lowestNumber] = temp

    return list

list = [1,5,8,3,4,6]
selectionSort(list)
print(list)
