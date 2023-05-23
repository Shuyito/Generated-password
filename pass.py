import random
import string

print("contraseña:")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation
charts = lower + upper + number + symbols
temp = random.sample(charts, 25)

print("".join(temp))
