# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse(list1):
    last=len(list1)-1
    for i in range(len(list1)//2):
        temp=list1[i]
        list1[i]=list1[last]
        list1[last]=temp
        last-=1
        
size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    print("enter your",i,"element: ",end="")
    list1.append(int(input()))
    
reverse(list1)
print(list1)

