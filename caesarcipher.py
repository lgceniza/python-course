alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt_or_decrypt(direction, text, shift):
  newtext = ""
  mode = 1 if direction == "encode" else -1
  for c in text:
    if c not in alphabet:
      newtext += c
      continue
    newtext += alphabet[(alphabet.index(c) + mode * shift) % 26]
  
  return newtext

def main():
  direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: ")
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift amount: "))

  print("Your ciphertext message is:")
  print(encrypt_or_decrypt(direction, text, shift))

loop = True
while loop:
  main()
  loop = True if input("Do you want to go again? Y or N: ") == "Y" else False