def accept(A):
    n=int(input("Enter the total number of student"))
    for i in range(n):
        x=float(input("Enter second year marks of student %d : "%(i+1)))
        A.append(x)
    print("Array accepted successfully \n\n")
def display(A):
    n=len(A)
    if(n==0):
        print("\n No record in database ")
    else:
        print("Array of se marks : ",end=' ')
        for i in range(n):
            print(A[i],end=' ')
        print("\n")
def insertion(A):
    n=len(A)
    
    for i in range(1,n):
        element=A[i]
        j=i-1
        while(j>=0):
            if(A[j]<=element):
                break
            else:
                A[j+1]=A[j]
                j=j-1
        A[j+1]=element
def insertiongap(A,n,gap,s):
    for i in range(s+gap,n,gap):
        element=A[i]
        j=i-gap
        while(j>=0):
            if(A[j]<=element):
                break
            else:
                A[j+gap]=A[j]
                j=j-gap
        A[j+gap]=element
def shell(A):
    n=len(A)
    gap=int(n/2)
    while(gap>0):
        for s in range(gap):
            insertiongap(A,n,gap,s)
        gap=int(gap/2)
def main():
    A=[]
    while True:
        print("\t1 : Accept and Display the SE marks \n\t2 : insertion sort acending order \n\t3 : shell sort acending short and display top 5 scores \n\t4 : Exit. ")
        ch=int(input("Enetr your choice : "))
        if(ch==4):
            print("Exit")
            quit()
        elif(ch==1):
            A=[]
            accept(A)
            display(A)
        elif(ch==2):
            print("Before sorting ")
            display(A)
            insertion(A)
            print("After sorting")
            display(A)
        elif(ch==3):
            print("before sorting")
            display(A)
            shell(A)
            print("After sorting")
            display(A)
            n=len(A)
            if(n>=5):
                print("Top five Scores : ")
                for i in range(n-1,n-6,-1):
                    print(A[i])
            else:
                print("top five scores : ")
                for i in range(n-1,-1,-1):
                    print(A[i])
        else:
            print("Wrong choice intered ! try again ")

            
main()





