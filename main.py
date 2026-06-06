from tools.check_balance import is_balanced


if __name__ == '__main__':
    balanced_rows = [
        "(((([{}]))))", 
        "[([])((([[[]]])))]{()}", 
        "{{[()]}}"
    ]
    
    unbalanced_rows = [
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]
    
    for row in balanced_rows:
        assert is_balanced(row) == "Сбалансированно"

    for row in unbalanced_rows:
        assert is_balanced(row) == "Несбалансированно"

