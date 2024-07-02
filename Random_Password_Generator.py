import random
import string

pass_len = 12           # character length of the random password will be 12


#mixture of letters digits and puntuations that random password will consist
random_password = string.ascii_letters+string.digits+string.punctuation+string.ascii_uppercase+string.ascii_lowercase  


password = ""
print("Your random suggested password is: ",end="")
for i in range (pass_len):
    print(random.choice(random_password),end="")
    