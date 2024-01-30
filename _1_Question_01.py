# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def pairs(list1,find):
    list2=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j]==find:
                touple1=(list1[i],list1[j])
                list2.append(touple1)
    return list2
        

size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    print("enter your",i,"element: ",end="")
    list1.append(int(input()))
find=int(input("enter your element :"))
print(pairs(list1,find))

