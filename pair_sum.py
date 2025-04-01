from typing import List, Set, Tuple

def find_pairs_with_target(target: int, list: List[int]) -> List[Tuple[int, int]]:
    """
        Identifies number pairs in an array summing to a target.
    """
    seen: Set[int] = set()
    pairs: List[Tuple[int, int]] = []
    
    for elem in list:
        complement: int  = target - elem
        
        if complement in seen:
            pairs.append(tuple(sorted((elem, complement)))) # Store as tuple and sort to avoid duplicates like (2, 4) (4, 2)
        
        seen.add(elem)

    return set(pairs) # Remove duplicate pairs

if __name__ == '__main__':
    print(find_pairs_with_target(6, [4, 2, 2, 7, 1, 9, 5]))