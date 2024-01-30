# Q4. Write a program to print the first non-repeated character from a string?

def non_repeated(input_str):
    count = {}
    
    for ele in input_str:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1

    for ele in input_str:
        if count[ele] == 1:
            return ele

    return None

user_input = input("Enter a string: ")
print("First non-repeated character in the string is",non_repeated(user_input))

