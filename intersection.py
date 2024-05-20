from typing import List

def intersection(first_list: List[int], second_list: List[int]) -> List[int]:
    result: List[int] = []
    
    for i in range(len(first_list)):
        for j in range(len(second_list)):
            if first_list[i] == second_list[j] and first_list[i] not in result:
                result.append(first_list[i]) 
                
    return result


if __name__ == '__main__':
    list1: List[int] = [1, 2, 2, 2, 3]
    list2: List[int] = [2, 3, 3, 4, 5, 5]

    print(intersection(list1, list2))