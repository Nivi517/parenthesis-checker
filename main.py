def check(n):
    stack=[]
    for i in n:
        if (i=='(' or i=='{' or i=='['):
           stack.append(i)
        else:
            if (stack and((stack[-1]=='(' and i==')')or (stack[-1]=='{' and i=='}' )or( stack[-1]=='[' and i==']'))):
                stack.pop()
    if(not stack):
        return True
    else:
        return False
        
string=input()
if check(string):
    print("Balanced")
else:
    print("Not balanced")