#Importing the user defined modules
import encrypt as cipher
import decrypt as decipher                           

print("\t\t\t\t***********************")
print("\t\t\t\t MORSE CODE TRANSLATOR ")
print("\t\t\t\t***********************")
print("\n")

ch= input("Press 'E' to encrypt and 'D' to decrypt: ")
print("\n")

if (ch=='E' or ch== 'e'):
    plain_Text= input("Enter Text to encrypt: ").upper()
    print("\n")
    
    #Calling encryption function
    cipher.encryptor(plain_Text)

elif (ch=='D' or ch== 'd'):
    morse_code= input("Enter morse code to decrypt: ")
    print("\n")
    
    #Calling decryption function
    decipher.decryptor(morse_code)

else:
    print("Invalid input!!!")        