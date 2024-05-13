from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return  self.items.pop()
    
    def peek(self) -> T:
        return self.items[-1]
    
    def is_empty(self) -> bool:
        return not self.items