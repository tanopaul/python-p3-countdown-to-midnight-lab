# your code goes here!
import time

def countdown(num):
    counter = num

    while counter > -1 :
        if counter == 0:
            print('HAPPY NEW YEAR!')
        else:
            print(f"{counter} SECOND(S)!")
        counter-=1

def countdown_with_sleep(num):
    counter = num

    while counter > -1 :
        if counter == 0:
            print('HAPPY NEW YEAR!')
        else:
            print(f"{counter} SECOND(S)!")
        counter-=1
        time.sleep(1)



countdown_with_sleep(10)



