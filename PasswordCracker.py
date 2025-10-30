import itertools
import time

target=input("Enter a Target: ")
print(target)
possible_value="abcdefghijklmnopqrstuvwxyz123456789@#$%^&(){}[]+-/*"
max_length=len(target)
print(max_length)

def burte_force_password_cracker():
    attempts=0
    st=time.time()
    for i in range(1,max_length+1):
        for guess in itertools.product(possible_value,repeat=i):
            attempts+=1
            guess="".join(guess)
            print(guess)
            if guess==target:
                print("Password Cracked: ",guess)
                print("Attempts: ",attempts)
                print("Time: ",time.time()-st)
                return
burte_force_password_cracker()
