import sys

def insertionSortR(collection: list, n: int):
    if(len(collection) <= 1 or n <= 1):
        return
    insertNext(collection, n-1)
    insertionSortR(collection, n-1)

def insertNext(collection: list, index: int):
    if(index >= len(collection) or collection[index-1] <= collection[index]):
        return
    collection[index-1], collection[index] = (
        collection[index],
        collection[index - 1]
        
        )
    insertNext(collection, index + 1)


def bubbleSort(lstData: list, length: int=0) -> list:
    length = length or len(lstData)
    swapped = False
    for i in range(length - 1):
        if(lstData[i] > lstData[i+1]):
            lstData[i], lstData[i+1] = lstData[i+1], lstData[i]
            swapped = True

    return lstData if not swapped else bubbleSort(lstData,length-1)

nums = [5,90,43,5,4,3,2,1]
print(nums)
bubbleSort(nums,len(nums))
print(nums)

















