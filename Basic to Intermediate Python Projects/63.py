#Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.
import time

# i = 0
# while True:
#     print("Hello")
#     i = i + 1
#     if i > 3:
#         print("End of loop")
#         break
#     time.sleep(i)

i = 0
game_is_on = True

while game_is_on:
    print("Hello")
    i += 1

    if i > 3:
        print("End of Loop")
        game_is_on = False
    time.sleep(i)