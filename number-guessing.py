import random

algo = """ Today is number guessing day, So the computer will automatically generate 
number between 1 to 99 and the user has to guess it correctly within the stipulated 
number of turns he has. The clues for guessing would be first even or odd, then prime
or not a prime, then single digit or a double digit number, the problem still has lot of 
chances to get any number and finding the right number is hard, so as the last clue and 
for the last second chance we will give a clue that that will tell in which range the 
number really lies for example if the number is 25, the last second clue will be 
'The number lies in the range of 21-29', and after all this, its solely the luck factor
Funzzzzzzzz expected ! """

def random_num():
    num = random.randint(1,100)
    return num

def even_or_odd(num):
    if(num%2 == 0):
        return 'even'
    else:
        return 'Odd'


def prime_or_not(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                return 'Not a prime'
                break
        else:
            return 'Prime'
    else:
        return 'Not a prime'


def single_or_doub(num):
    if num<=9:
        return ' single digit '
    if num>9 and num<=99:
        return ' double digit '


def num_range(num):
    if num<=9:
        return 'The number is between 1 to 9'
    else:
        str_num = str(num)
        str_num1 = str_num[0]
        str_print = 'The number is between' + str_num1 + '1 to ' + str_num1 + '9'
        return str_print

def take_ans(num):
    take_ans = int(input("Enter your guess for the computer generated number "))
    if take_ans == num:
        return (" Yayyyyy, U got it right ! Congrats. ", exit())
    else:
        return " Naahh, go for another clue and guess... "
    
   
def start_game():
    num = random_num()
    print(take_ans(num))
    print(single_or_doub(num))
    print(take_ans(num))
    print(even_or_odd(num))
    print(take_ans(num))
    print(prime_or_not(num))
    print(take_ans(num))
    print(num_range(num))
    final_turn = take_ans(num)
    if final_turn == " Naahh, go for another clue and guess... ":
        print(f'Sorry game over, The number is {num}')
    else:
        print(" Yayy, u got the right number ")


print(algo)
ans = input("Do u want to start the game ? Ans: Yes or No ")

if ans.lower() == 'yes':
    start_game()
else:
    print(" You're missing such a wonderful chance to play an amazing game")




    





