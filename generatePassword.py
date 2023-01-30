
import random
import string

def generate_pw(pw_length=11):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(random.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 2):
           pw_strong = True

   return pwd


if __name__ == '__main__':
   print(generate_pw())