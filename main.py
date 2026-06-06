from tools.check_balance import is_balanced


if __name__ == '__main__':
    user_input = input("Enter a sequence of parentheses to check: ")
    
    result = is_balanced(user_input)
    
    print(result)

