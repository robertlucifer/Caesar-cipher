from logo import logo
def caesar(text,shift,direction):
  msg=''
  if direction =='decode':
    shift*=-1
  for x in text:
    if x in alphabet:
      current_position=alphabet.index(x)
      position=current_position+shift
      msg+=alphabet[position]
    else:
      msg+=x
  print(f"The {direction}d text is {msg}.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
should_run=True
while should_run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(text,shift,direction)
  result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result=='no':
    should_run=False
    print("Good Bye!")
  
  



