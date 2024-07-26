def encryption_key_checker():
    encryption_key=input("Enter your encryption key: ")
    encryption_key=encryption_key.replace(" ","")
    while True:
        if len(encryption_key) < 2 or not encryption_key.isalpha():
            encryption_key= input("Invalid input. Enter your encryption key(must be atleast 2 characters and only alphabets): ")
        else:
            break
    return encryption_key


def decoder(message,encryption_key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    message_array=[]
    encryption_array=[]
    upper_case_index=[]
    final_word=""
    count=0

    for letter in message:
        letter=letter.lower()
        letter_index=alphabet.find(letter)
        message_array.append(letter_index)

    for i in range(len(message)):
        if message[i].isupper():
            upper_case_index.append(i)

    for i in encryption_key.lower():
        encryption_index=alphabet.find(i)
        encryption_array.append(encryption_index)

    for j in range(len(message_array)):
        if message_array[j] != -1:
            new_index=message_array[j]-encryption_array[count%len(encryption_array)]
            if new_index < 0:
                new_index+=len(alphabet)
            new_letter=alphabet[new_index]
            final_word+=new_letter
            count+=1
        else:
            final_word+=message[j]

    def retain_capitals():
        new_word=''
        choice=input("Do you want to retain capital letters? (y/n): ").lower()
        while True:
            if choice not in ('y','n'):
                print("Invalid entry. Please try again.")
                choice=input("Do you want to retain capital letters? (y/n): ").lower()
            else:
                break

        if choice=='y':
            for i in range(len(message)):
                if i in upper_case_index:
                    new_word+=final_word[i].upper()
                else:
                    new_word+=final_word[i]
            return new_word
        
        return final_word
    
    if len(upper_case_index) > 0:
        return retain_capitals()
    else:
        return final_word

if __name__=="__main__":
    message= input("Enter message to decrypt: ")
    encryption_key=encryption_key_checker()
    decrypted_message=decoder(message,encryption_key)
    print(f"\nDecrypted message is: {decrypted_message}")

