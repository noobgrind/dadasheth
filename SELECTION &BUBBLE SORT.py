
def accept(A):
    t=int(input("enter total nmber of student : "))
    for i in range(t):
        x=int(input("Enter percentage of student : "))
        A.append(x)
    print("\n")
def selection(A):
    n=len(A)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(A[j]<A[min]):
                min=j
        temp=A[i]
        A[i]=A[min]
        A[min]=temp
    for i in range(n):
        print(A[i],end=' ') 
    print("\n\n")  
def bubble(A):
    n=len(A)
    for i in range(1,n):
        for j in range(n-i):
            if(A[j] < A[j+1]):
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
    for i in range(n):
        print(A[i],end=' ') 
    print("\n")
    print("the top five score is : \n")
    if(n>=5):
        for i in range(5):
            print(A[i],end=' ')         

def main():
    A=[]
    n=len(A)
    while True:
        print("\n\t1: for accept percentage ofstudent \n\t2: for sort array acendind using insertion sort \n\t3: for decending using bubble fort and display top 5 score \n\t4:exit:")
        print("Enter your choice")
        choice=int(input())
        if(choice==1):
            accept(A)
        elif(choice==2):
            selection(A)
        elif(choice==3):
            bubble(A)
            
                    
        elif(choice==4):
            print("Exit::")
        else:
            print("Invalid choice try again")

main()     




