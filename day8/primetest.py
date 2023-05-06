#Write your code below this line 👇

from termcolor import colored, cprint

def prime_checker(number):
    prime_status = True
    if number == 1:
        prime_status = False
    for divisor in 2, 3, 5, 7:
        if number % divisor == 0 and number != divisor:
            prime_status = False
    if prime_status == True:
        colored_output = colored(f"{number} is a prime number.", 'yellow')
        cprint(colored_output)
    else:
        print(f"{number} is not a prime number.")        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
for n in range(1,101):  
    prime_checker(number=n)
