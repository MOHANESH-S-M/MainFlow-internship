""" ===============1. Custom Encryption-Decryption System==========================================================
 ● Description  : Develop a program that encrypts and decrypts messages using custom
                encryption algorithms like substitution ciphers or matrix transformations.
 ● Challenges   :
                 ○ Create a robust algorithm for encryption and decryption.
                 ○ Handle edge cases (e.g., special characters, spaces).
                 ○ Optionally, implement multi-layer encryption.
 ● Skills       : Algorithm design, string manipulation, and logical reasoning.
 ● Restriction  : ## No use of built-in encryption libraries like cryptography or hashlib.##
 ● Reason       : The goal of this project is for students to build an understanding of how
                 encryption works at a low level. By manually implementing encryption and decryption
                 algorithms (such as a Caesar cipher, Vigenère cipher, or even a simple substitution
                 cipher), students gain deeper insight into data security principles, such as the
                 importance of keys and encryption algorithms. Using pre-built libraries would only teach
                 them how to apply the algorithm, not how it works.
 ● Learning Outcome  : Students will learn about algorithm design, data transformation,
                        and security principles without relying on ready-made solut
                        ions."""
import random
import string

#printable character list generation
character_list =[' ']+ list(string.printable.strip())

#to create the shuffled randomversion
def shuffle_the_list(list1):
    """Shuffle the given list of characters"""
    list2 = list(list1)
    random.shuffle(list2)
    return list2

def mapping_the_characters(const_list):
    """Maps the shuffled characters into mapped list returns mapped dictinary"""
    shuffled_list = shuffle_the_list(const_list)
    dictionary_mapped ={}
    for i in range(len(const_list)):
        dictionary_mapped[const_list[i]] = shuffled_list[i]
    return dictionary_mapped

def do_encrypt(message,en_code):
    """the function encrypts the message with the encode and returns the encryped message"""
    encrypted_message =""
    for i in message:
        a = en_code[i]
        encrypted_message += a
    return encrypted_message

def do_decrypt(message,key_code):
    """The function decryts the message with the given encode"""
    decrypted_message =""
    for i in message:
        for key,val in key_code.items():
            if i in str(val):
                decrypted_message += key
    return decrypted_message

def main():

    #map the code with the actualcharacter set
    code = mapping_the_characters(character_list)

    #get the input message
    message = str(input("enter the message you want to encrypt"))

    #print the encrypt the message
    print("the encrypted message is ",do_encrypt(message,code))

    #print the decrypted message
    print("the decrypted message is ",do_decrypt(do_encrypt(message,code),code))

if __name__ == "__main__":
    main()




