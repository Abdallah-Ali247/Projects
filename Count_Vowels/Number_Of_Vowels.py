

########### function using substring Regular Expressions  ##########

def regular_ex_vowels(line):
    import re

    new_line = re.sub('[a,e,i,o,u,y]','x',line.lower())
    #print(new_line)    # print the new line after replacement with 'x'
    return new_line.count('x')


########### manual function ##############

def manual_vowels(line):
    vowels = ['a','e','i','o','u','y']
    num=0
    for letter in line.lower():
        if letter in vowels:
            num += 1
    return num


######################################################
#line = input("Enter your String : ")      # if you want to take input from user
######################################################

line = "I Love python Too Mutch And Using it In AI Doploma"

print(f"\n{'*'*50}")

num_ex = regular_ex_vowels(line)
print(f'Number Of Vowels From regular_ex_vowels is : {num_ex}')

print('*'*50)

num_m = manual_vowels(line)
print(f'Number Of Vowels From manual_vowels is : {num_m}')
print('*'*50)


