from typing import TypeVar, Generic, Deque
T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: Deque[T] = Deque()
    
    def enqueue(self, item: T) -> None:
        self.items.append(item)
    
    def dequeue(self) -> T:
        return self.items.popleft()
    
    def is_empty(self) -> bool:
        return not self.items
