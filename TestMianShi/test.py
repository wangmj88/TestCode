import random

def buble_sort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] < array[j]:
                array[i],array[j] = array[j],array[i]
    return array

if __name__ =='__main__':
    array = []
    for i in range(30):
        array.append(random.randrange(20))
    print(array)
print(buble_sort(array))

