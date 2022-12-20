
#################################################
########      Simple Way with for loop ##########
#################################################
'''
def addition(*args):
    sum_n = 0
    for num in args[0]:
        sum_n += num

    return sum_n

numbers = [5,6,7,44,5,2,3,6,5,2,6,66,89]

summition = addition(numbers)
print(summition)

'''

#####################################################
###########        USING RECURSION      #############
#####################################################

###########  addition function ################

def sum_numbers(*numbers):
    num = numbers[0]
    if len(num) == 0:
        return 0
    return num[0] + sum_numbers(num[1:])

#x=sum_numbers(numbers)
#print('add : ',x)

############  subtraction ######################

def subtr(*numbers):
        num = numbers[0]
        num.sort(reverse=True)
        x=num[0]
        for i in range(1,len(num)):
            x = x - num[i]
        return x


#s=subtr(numbers)
#print('subt : ',s)

######### multiplication #################
def multi(*args):
    num = args[0]
    if len(num) == 0:
        return 1
    else:
        return num[0] * multi(num[1:])


#s = multi(numbers)
#print('multi : ',s)

############# division ##################

def divi(*numbers):
        num = numbers[0]
        num.sort(reverse=True)
        x=num[0]
        for i in range(1,len(num)):
            x = x / num[i]
        return float('{:.4f}'.format(x))

#s = divi(numbers)
#print('divi : ',s)


############## check even or odd ############

def ev_od_check(*numbers):
        num = numbers[0]

        for i in num:
            if i % 2 == 0:
                print(f'{i} is even')
            else:
                print(f'{i} is odd')

#ev_od_check(numbers)

################ factorial ###############

def fact(num):
    if num == 1:
        return 1
    elif num == 0 :
        return 0
    return num * fact(num-1)

#x= fact(10)
#print(x)

############## Fibonacci ###################


i=0
seq=[0,1]
def febonacci(n):

    global i

    if n<0:
        print("\nEnter positive number ")
        a=input("write 'y' to try agin 'n' to exit ")
        if a.lower() == 'y':
            return febonacci(int(input("\nEnter number of Repetition : ")))
        elif a.lower() == 'n':
            print("\n E  X  I  T")
        else:
            print("\nIts not a joke write the F U C K I N G true answer : ")
            return febonacci(n)
    elif n==0:
        print("\nFebonacci sequence is : ")
        return seq
    else:
        sum = seq[i] + seq[i+1]
        seq.append(sum)
        i+=1
        return febonacci(n-1)


#n = int(input("Enter number of Repetition : "))
#x= febonacci(n)
#print(x)

######################################################################################################################
######################################################################################################################
##################                   M Y    C  A  L  C  U  L  A  T  O  R           ###################################
######################################################################################################################
######################################################################################################################

def calculator():
    op_en = input("\nHi, would you prefer to use a calculator ? \nwrite 'y' to use it or 'n' to exite : ")
    if op_en.lower() == 'n':
        return "\nE X I T"
    elif op_en.lower() == 'y':
        operation = int(input("Enter Number Of Operation : \n 1- Addition \n 2- Subtraction \n 3- Multiplication \n 4- Division \n 5- Check even or odd \n 6- Factorial \n 7- Fibonacci \n"))

        if operation in [1,2,3,4,5]:
            n=1
            numbers=([],)
            while n!=0:
                n = int(input("\n--> Enter your number: \n--> Write 0 to stop : "))
                if n !=0 :
                    numbers[0].append(n)

        if operation ==   1 :
            x=numbers[0]
            for i in x :
                print(f'+ {i }  ',end='')
            print("= ",end='')
            return sum_numbers(*numbers)

        elif operation == 2 :
            x=numbers[0]
            for i in x :
                print(f'- {i }  ',end='')
            print("= ",end='')
            return subtr(*numbers)

        elif operation == 3 :
            x=numbers[0]
            for i in x :
                print(f'* {i }  ',end='')
            print("= ",end='')
            return multi(*numbers)

        elif operation == 4 :
            x=numbers[0]
            for i in x :
                print(f'/ {i }  ',end='')
            print("= ",end='')
            return divi(*numbers)

        elif operation == 5 :
            return ev_od_check(*numbers)

        elif operation == 6 :
            num=int(input("Enter the number : "))
            print(f"Factorial of !{num} = ",end='')
            return fact(num)

        elif operation == 7 :
            num=int(input("Enter the number : "))
            if num >=0:
                print(f"Febonacci of {num}'s = ",end='')
            return febonacci(num)
        else:
            print("Please Choose number of Opration from 1 to 7")
            return calculator()
    else:
        print("Wrong answer Try again")
        return calculator()



result = calculator()
print(result)















































































