from typing import List

def selection_sort(list: List[int]) -> List[int]:
    min: int
    
    for i in range(0, len(list) - 1):
        # minimum
        min = i 
        
        for j in range(i + 1, len(list)):
            # if min is greater we have a new min
            if list[j] < list[min]:  
                min = j
        
        if min != i:
            list[i], list[min] = list[min], list[i] 
        
    return list

if __name__ == '__main__':
    print(selection_sort([3, 2, 1, 4, 9, 0, 0, 8]))