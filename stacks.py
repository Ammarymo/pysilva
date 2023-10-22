class Stack():
    def __init__(self):
        self.list_stack = []
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
    def push(self,item):
        return self.list_stack.append(item)
    def pop(self):
        return self.list_stack.pop()
    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
    def __repr__(self):
        return repr(self.list_stack)
    
user_input = input("Your brackets").strip()
user_list = []
symbols = {
    "{":"}",
    "[":"]",
    "(":")",
    "}":"{",
    ")":"(",
    "]":"["
    }

for i in user_input: 
    if i in symbols.keys():
        user_list.append(i)


new_stack = Stack()
for i in range(len(user_list)//2):
    new_stack.push(user_list[i])
flag = False
for i in range(len(user_list)//2,len(user_list)):
    if symbols[user_list[i]] == new_stack.peek():
        new_stack.pop()
        flag = True
    else:
        flag = False

if flag:
    print("success")
else:
    print("failure")



