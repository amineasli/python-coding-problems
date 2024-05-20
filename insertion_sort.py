from typing import List

def insertion_sort(list: List[int]) -> List[int]:
    for i in range(1, len(list)):
        temp = list[i]
        j = i
        
        while j > 0 and list[j-1] > temp:
            # shift item right
            list[j] = list[j-1] 
            j -= 1
            
        list[j] = temp

    return list

if __name__ == '__main__':
    print(insertion_sort([3, 2, 1, 4, 9, 0, 0, 8]))