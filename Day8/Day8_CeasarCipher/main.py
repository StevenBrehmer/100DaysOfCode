alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    #blank var for output message
    encrypted_msg = ""
    for i in range(0,len(text)):
        original_position = alphabet.index(text[i])
        shiftIndex = int(original_position) + int(shift)
        if shiftIndex >25:
            shiftIndex = shiftIndex % 26
        encrypted_msg = encrypted_msg + alphabet[shiftIndex]
    print("encrypted msg: " + encrypted_msg)
    return encrypted_msg

def decrypt(text,shift):
    decrypted_msg = ""
    for i in range(0,len(text)):
        original_position = alphabet.index(text[i])
        shiftIndex = int(original_position) - int(shift)
        if shiftIndex >25:
            shiftIndex = shiftIndex%26
        decrypted_msg = decrypted_msg + alphabet[shiftIndex]
    print("decrypted msg: " + decrypted_msg)
    return decrypted_msg

stop = False
while stop == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode": 
        decrypt(text,shift)
    else:
        print("invalid request... try again")
        






#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 