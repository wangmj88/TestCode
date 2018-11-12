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

#冒泡排序
def buble_sort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
    return array
l = [1,3,5,7,9,2,4,6,8,0]
print(buble_sort(l))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#快速排序

def quick_sort(array):
    def recursive(begin,end):
        if begin > end:
            return
        l,r = begin,end
        pivot = array[l]
        while l < r and array[r] > pivot:
            r -= 1
        while l < r and array[l] <= pivot:
            l += 1
        array[l],array[r] = array[r],array[l]
        recursive(begin,l - 1)
        recursive(r + 1,end)
    recursive(0,len(array) - 1)
    return array





