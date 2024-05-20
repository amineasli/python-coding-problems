def is_palindrome(input_str: str) -> bool:
    left_index = 0
    right_index = len(input_str) - 1
    
    while left_index < len(input_str) / 2:
        if input_str[left_index] != input_str[right_index]:
            return False
        
        left_index += 1
        right_index -= 1
    
    return True

if __name__ == '__main__':
    print(is_palindrome('kayak'))