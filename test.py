import main
import string
from hashlib import sha256
from random import randint, choice

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
            return ''.join(choice(chars) for _ in range(length))  

while True:
      u = password_gen()
      r = randint(1, 1024)
      test = u * r
      a = main.SHA256()
      a.message_to_blocks(test)

      print("Testing: " + u + ' - ' + str(r))
      if sha256(bytes(test, 'ascii')).hexdigest() == a.compress():
            print("Success")
      else:
            print("\nFailed\n")
            break