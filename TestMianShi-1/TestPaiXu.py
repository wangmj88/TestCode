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

'''
https://blog.csdn.net/weixin_42206504/article/details/82693453
    快速排序是原址排序，不用新增某一序列用于存储在排序过程中的临时变量。原址排序就是在原来的数组上进行操作。

主要分为两步

分解：对于一个数组A[p.....r]排序，
     将其划分为两个子数组A[p.....q-1]和A[q+1.....r]，
     使得A[p.....q-1]中的每一个元素都小于等于A[q]，
     而A[q]也小于等于A[q+1.....r]中的每一个元素。
     此时我们就能将A[q]在正确排序后的正确下标索引解出来。对应下面程序的partition函数。

解决：通过递归调用快速排序，因为上一步已经把A[q]的正确位置找出，并且左边小于等于A[q]，右边严格大于A[q]，只要分别对左右两边再调用快速排序算法即可。
--------------------- 
作者：风卷残荷hust 
来源：CSDN 
原文：https://blog.csdn.net/weixin_42206504/article/details/82693453 
版权声明：本文为博主原创文章，转载请附上博文链接！
关于partition函数：其主要作用将数组分成两部分，并找到A[r]的正确位置，并且将数组分为三个区域(1)若p<=k<=i,a[k]<=x.(2)若i+1<=k<=j-1,a[k]>x.(3)若k==r,a[k]=x.
'''
def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1
def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)






