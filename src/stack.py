

class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el) 

    def pop(self):
        popped_item = self.items.pop()    
        return popped_item;

    def get_peek(self):   
        return self.items[-1]; 

    def get_stack_size(self):   
        return len(self.items)
    
    def is_empty(self):   
        return len(self.items) == 0 
    
    def get_stack_elements(self):
        return self.items

