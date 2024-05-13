from stack import Stack

class Reverser:
    
    @staticmethod
    def do_reverse(input_str: str) -> str:
        stack: Stack[str] = Stack()
        output_str: str = ""
        
        for char in input_str:
            stack.push(char)
            
        while not stack.is_empty():
            output_str += stack.pop()
            
        return output_str
        
if __name__ == '__main__':
    reversed_str = Reverser.do_reverse('part')
    print(reversed_str)
            
