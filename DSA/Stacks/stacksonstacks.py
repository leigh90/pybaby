# A stack is similar to a physical stack - stack data structure allows us to place any programming artifact, variable or object on it

# Stack operations
# 1. push() 
# Used to Insert elements. this adds the elements on top of the previous top element. and the new element becomes the top element. it foloows a FILO policy
# FILO - First In Last Out - so say we do a pop() the last element is what will be removed

# 2. pop()
# removes the top element (the last one to go in)

# 3. peek()
# you can ask the stack what the tope element is. it doesnt remove it just tells you what it is.
# you can also check if a stck is empty


#  Creating a stack
class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self,item):
        self.items.append(item)
        # append adds items to a list at the end

    def pop(self):
        return self.items.pop()
        # pop is method that returns the last element of the list

    def get_stack(self):
        return self.items
    
    def check_stack(self):
        return self.items == []
    
    def peek(self):
        if not self.check_stack():
            return self.items[-1]
    

thique = Stack()
print(thique.check_stack())
thique.push("Beyonce")
thique.push("Aya Nakamura")
thique.push({"Carment Santiego":"where in the world"})
print(thique)
print(thique.get_stack())
print(thique.check_stack())
print(thique.peek())


# # Quick note - checking that brackets are balanced - to avoid syntax errors

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))


# Reverse String using a stack
def reverse_string(stack, input_str):
    reverse_list = []
    rev_str = ""
    # 1. take the characters from the input_str and push onto the stack
    for char in input_str:
        rack.push(char)
    while not stack.check_stack():
        rev_str += stack.pop()
    print(rev_str)
        
    

    

    





rack = Stack()
reverse_string(rack, "hello")








