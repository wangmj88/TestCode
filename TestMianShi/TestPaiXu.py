#直接插入排序
def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            # if array[i] < array[j]:
            if array[i] > array[j]:
                array.insert(j,array.pop(i))
    return array

l = [1,3,5,7,9,2,4,6,8,0]
print(insert_sort(l)) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


