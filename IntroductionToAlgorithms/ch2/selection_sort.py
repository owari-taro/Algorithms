def selection_sort(array:list):
    for i in range(len(array)):
        #tmp=array[i]
        tmp_value=float("inf")
        tmp_index=None
        for j in range(i,len(array)):
            if array[j]<tmp_value:
                tmp_value=array[j]
                tmp_index=j
        if tmp_index:
            #入れ替え
            array[i],array[tmp_index]=array[tmp_index],array[i]
    print(array)

if __name__=="__main__":
    selection_sort([3,2,1,4,5,6,17,13])