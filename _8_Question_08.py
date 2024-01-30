# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def Bracket(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
    if Bracket(expr):
        print("All Brackets are Closed")
    else:
        print("Still Open")
