
import random

def binary_search():

    list1 = [i for i in range(101)]

    list1.sort()

    low = 0
    high = list1.index(list1[-1]) # or = len(list1)-1
    #mid = 0        # basic binary search mid

    game = input("Enter 'y' to play 'n' to exite :")

    if game.lower() == 'y':

        print("please think in a number between 0 and 100 : ")

        while low <= high:

            #mid = (high + low) // 2       # calc mid for basic binary search

            num = random.randrange(low,high+1)

            #print(f"\nlow: {low} , mid: {mid}  , high: {high} , num: {num}")   # show every repetition changes in variables

            print(f"\nI guess you think in : {num}")

            ans = input("Enter 't' if number is True // 'h' if it high // 'l' if it lower : ")

            if ans.lower() == 't':
                return f"\n\n THE NUMBER IS : {num}"

            elif ans.lower() == 'h':
                #low = mid + 1               # basic binary search new low
                low = list1.index(num) + 1

            elif ans.lower() == 'l':
                #high = mid - 1             # basic binary search new high
                high = list1.index(num) - 1

            else:
                print("\n\nplease enter correct answer ['t' or 'h' or 'l']")
                return binary_search()

            ms1 = ' your number is not found in range 0  to 100 '
            ms2 = ' G  A  M  E   $  O  V  E   R '

        return f"\n\n{'*'*100}\n{'*'*27}{ms1}{'*'*28}\n{'*'*27}{' '*8}{ms2}{' '*8}{'*'*28}\n{'*'*100} "

    elif game.lower() == 'n':
        return f"\n\n{'*'*100}\n{'*'*43} E  X  I  T  {'*'*44}\n{'*'*100}"
    else:
        print("\nwrong choice try agin :")
        return binary_search()

result = binary_search()
print(result)

