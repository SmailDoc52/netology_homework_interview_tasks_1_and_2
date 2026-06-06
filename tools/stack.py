class Stack:
    """A class that implements a list-based Stack data structure.
    
    It works according to the LIFO principle (Last In, First Out — last in, first out).
    It is used to store items in the order they were added with the possibility of
    quick access to the top element.
    """
    def __init__(self):
        """Initializes the stack.
        """
        self.stack = []
    
    def is_empty(self):
        """Checks if the stack is empty.
        
        Returns:
            True - the stack is empty.
            False - the stack is not empty.
        """
        return not self.stack
    
    def push(self, elem):
        """Adds an item to the stack.

        Args:
            elem: An element to add to the stack.
        """
        self.stack.append(elem)
    
    def pop(self):
        """Removes and returns the top item from the stack. 
            If the stack is empty, there will be an error.

        Returns: a deleted item
        """
        return self.stack.pop()
    
    def peek(self):
        """Returns the top item in the stack.
            If the stack is empty, there will be an error.

        Returns: the top item in the stack
        """
        return self.stack[-1]
        
    def size(self):
        """Returns the number of items in the stack (size).

        Returns: Returns the stack length
        """
        return len(self.stack)
