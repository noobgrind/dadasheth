def longest_word():
    str=input("Enter string : ")
    s=str.split()
    n=len(str)
    max=0
    for i in s:
        if(len(i)>max):
            max=len(i)
            max_word=i
    print("maximum word is : ",max_word)

def frequency():
    str=input("Enter the string : ")
    ch=input("Enter the character : ")
    n=len(str)
    count=0
    for i in range(n):
        if(str[i]==ch):
            count = count +1 
    print("frequency count of character ",ch," is : ",count)

def palindrome():
    str=input('Enter the string : ')
    if(str==str[::-1]):
        print(str," is palindrome ")
    else:
        print(str," is not palindrome")

def apperance():
    str=input("Enter the string : ")
    sub=input("Enter sub string to be search : ")
    if(str.find(sub)!=-1):
        print(sub," string are found in main string at index ",str.find(sub)) 
    else:
        print(sub," string are not found in main string !")       

def word_occurance():
    str=input("Enter the string : ")
    #word=input("Enter the word : ")
    s=str.split()
    i=0
    while(i<len(s)):
        count=0
        for j in s:
            if(s[i]==j):
                count += 1
        print(s[i]," word ",count) 
        i=i+1   

def main():
    while True:
        print("*****STRING OPERATION*****")
        print("\n\t1: find longest word in string\n\t2: find frequency of character\n\t3: palindrome or not\n\t4: find substring in main string\n\t5: occurance of word in string\n\t6: exit::")
        choice=int(input("Enter your choice : "))
        if(choice==6):
            print("end of program")
        elif(choice==1):
            longest_word()
        elif(choice==2):
            frequency()
        elif(choice==3):
            palindrome()
        elif(choice==4):
            apperance()
        elif(choice==5):
            word_occurance()
        else:
            print("invalid choice try again!!")
            
main()



