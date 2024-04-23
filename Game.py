import pyfiglet as fig
from colorama import Fore
import random

txt1 = fig.figlet_format("Number", font='slant')
txt2 = fig.figlet_format("Guessing", font='slant')
txt3 = fig.figlet_format("Game", font='slant')

print(txt1)
print(txt2)
print(txt3) 

print("🕹Let's play🕹")
print("You have 200 points by default")

choose = 0 

total_score = [200]

score_easy = 50
score_normal = 100
score_hard = 150

while choose < 3:
    print(Fore.GREEN,"\nEasy (1,50)",Fore.RESET)
    print(Fore.BLUE,"\nNormal (1,100)",Fore.RESET)
    print(Fore.RED,"\nHard (1,200)",Fore.RESET)
    level = input(f"\nSelect the game level : ")

    if level in ["easy", "Easy"]:
        print(Fore.GREEN,f"\nYou selected the {level} level",Fore.RESET)

        easy_q = 0
        sec_num_easy = random.randint(1, 50)  

        while easy_q < 6:
            user_guess = int(input("\nNow guess what is the number in this hat 🎩 ? "))

            if user_guess > 50:
                print("Out of range") 
            elif user_guess < sec_num_easy:
                print("The number is higher")
            elif user_guess > sec_num_easy:
                print("The number is lower")
            else:
                total_score.append(50)
                print(Fore.GREEN, f"You win. The number in the hat 🎩 was  {sec_num_easy}", Fore.RESET)
                print("You got 50 points.")
                
                break  
                 
            easy_q += 1

            if easy_q == 6:
                total_score.append(-50)
                print(Fore.RED, f"⚠ You lose. The number in the hat 🎩 was ({sec_num_easy}) ⚠", Fore.RESET)
                print(Fore.RED,"You lost 50 points.",Fore.RESET)


        
        play_again = input("\nDo you want to play again (yes/no) : ")
        if play_again.lower() == 'yes':
            total_sum = sum(total_score)
            print(f"your score : {total_sum}")
            continue
        elif play_again.lower() == 'no':
            print(f"Your final score : {total_sum}")

            print("Goodbye!")
            exit()
           
        else:
            print(Fore.RED, "Please just enter yes or no", Fore.RESET)

    elif level in ["normal", "Normal"]:
        print(Fore.BLUE,f"\nYou selected the {level} level",Fore.RESET)

        normal_q = 0
        sec_num_normal = random.randint(1, 100) 

        while normal_q < 6:
            user_guess = int(input("\nNow guess what is the number in this hat 🎩 ? "))

            if user_guess > 100:
                print("Out of range") 
            elif user_guess < sec_num_normal:
                print("The number is higher")
            elif user_guess > sec_num_normal:
                print("The number is lower")
            else:
                total_score.append(100)
                print(Fore.GREEN, f"You win. The number in the hat 🎩 was  {sec_num_normal}", Fore.RESET)
                print("You got 100 points.")
                break  
                 
            normal_q += 1

            if normal_q == 6:
                total_score.append(-100)
                print(Fore.RED, f"⚠ You lose. The number in the hat 🎩 was ({sec_num_normal}) ⚠", Fore.RESET)
                print(Fore.RED,"You lost 100 points.", Fore.RESET)



        
        play_again = input("\nDo you want to play again (yes/no) : ")
        if play_again.lower() == 'yes':
            total_sum = sum(total_score)
            print(f"your score : {total_sum}")
            continue
        elif play_again.lower() == 'no':
            print(f"Your final score : {total_sum}")

            print("Goodbye!")
            exit()
         
        else:
            print(Fore.RED, "Please just enter yes or no", Fore.RESET)

  
    elif level in ["hard", "Hard"]:
        print(Fore.RED, f"\nYou selected the {level} level", Fore.RESET)

        hard_q = 0
        sec_num_hard = random.randint(1, 200)
        
        while hard_q < 6:
            user_guess = int(input("\nNow guess what is the number in this hat 🎩 ? "))

            if user_guess > 200:
                print("Out of range") 
            elif user_guess < sec_num_hard:
                print("The number is higher")
            elif user_guess > sec_num_hard:
                print("The number is lower")
            else:
                total_score.append(150)
                print(Fore.GREEN, f"You win. The number in the hat 🎩 was  {sec_num_hard}", Fore.RESET)  
                print("You got 150 points.")
                break  

            hard_q += 1

            if hard_q == 6:
                total_score.append(-150)
                print(Fore.RED, f"⚠ You lose. The number in the hat 🎩 was ({sec_num_hard}) ⚠", Fore.RESET)
                print(Fore.RED, "You lost 150 points.", Fore.RESET)

        play_again = input("\nDo you want to play again (yes/no) : ")
        if play_again == 'yes':
            total_sum = sum(total_score)
            print(f"your score : {total_sum}")
            continue
        elif play_again == 'no':
            print(f"Your final score : {total_sum}")
            print("Goodbye!")
            exit()
           
        else:
            print(Fore.RED, "Please just enter yes or no", Fore.RESET)

            

    else:
        choose += 1
        if choose == 3:
            print(Fore.RED, "\n⚠ Failed to choose the game level ⚠", Fore.RESET)
            break
