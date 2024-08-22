print("Random Password Generator:")
import random
password = int(input("Enter the length of the password: "))
symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910!@#$%^&*()'?<>"
output = "".join(random.sample(symbol,password))
print("Your Random Password is:",output)
