from typing import List

def bubble_sort(list: List[int]) -> List[int]:
    swapped: bool = False

    for i in range(len(list) - 1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
                
        if not swapped:
           break
       
    return list

if __name__ == '__main__':
    print(bubble_sort([3, 2, 1, 4, 9, 0, 0, 8]))
    