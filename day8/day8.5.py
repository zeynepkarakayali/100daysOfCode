# Caesar's Cipher Part 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(plain_text, shift_amount, type):
    new_text = ""

    if(type == "encode"):
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
        print(f"The encoded text is {new_text}")
    elif(type == "decode"):
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_text += alphabet[new_position]
        print(f"The decoded text is {new_text}")
    else:
        print("You misspelled the encode or decode. Try again.")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)