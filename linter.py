from stack import Stack

class Linter:
    def __init__(self) -> None:
        self.braces: dict[str, str] = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        
        self.stack: Stack[str] = Stack()
    
    def is_opening_braces(self, char: str) -> bool:
        return char in self.braces.keys()
    
    def is_closing_braces(self, char: str) -> bool:
        return char in self.braces.values()
    
    def is_a_match(self, opening_brace: str, closing_brace: str) -> bool:
        return (opening_brace, closing_brace) in self.braces.items()

    def lint(self, text: str) -> bool:
        for idx, value in enumerate(text):
            # If the character is an opening brace, we push it onto the stack
            if self.is_opening_braces(value):
                self.stack.push(value)
                
            # If the character is a closing brace we pop and check   
            elif self.is_closing_braces(value):
               
                if not self.stack.is_empty():
                    opening_brace: str = self.stack.pop()
                    # Check if the popped opening brace doesn't match the current closing brace
                    if not self.is_a_match(opening_brace, value):
                        print(f'Error {value} at {idx}')
                        return False
                    
                else:
                    print(f'Error {value} at {idx}')
                    return False
        
        return True
           
if __name__ == '__main__':
    linter = Linter()
    print(linter.lint('(( var x = { y: [(1, 2, 3] } ))'))
    print(linter.lint('([ var x = { y: [1, 2, 3] } ])'))