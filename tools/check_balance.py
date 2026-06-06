from tools.stack import Stack


def is_balanced(string: str):
    """Checks rows with parentheses for balance.
        If the string is empty, it is considered balanced.

        Args:
            string (str): A string to check for balance.

        Returns:
            "Сбалансированно": str if string is balanced
            "Несбалансированно": str if string is not balanced
            
    """
    brackets = {
        ']': '[',
        '}': '{',
        ')': '('   
    }
    stack = Stack()
    
    for char in string:
        if char not in brackets.keys() and char not in brackets.values():
            continue
        if char in brackets.values():
            stack.push(char)
        elif stack.is_empty() or stack.pop() != brackets[char]:
            return "Несбалансированно"
    
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"
    