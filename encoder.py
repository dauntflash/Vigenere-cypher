
def encryption_key_checker():
    encryption_key=input("Enter your encryption key: ")
    encryption_key=encryption_key.replace(" ","")
    while True:
        if len(encryption_key) < 2 or not encryption_key.isalpha():
            encryption_key= input("Invalid input. Enter your encryption key(must be atleast 2 characters and only alphabets): ")
        else:
            break
    return encryption_key


def encoder(message,encryption_key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    new_word=""
    my_array=[]
    upper_case_index=[]
    key_index=0

    for j in encryption_key.lower():
        encryption_index=alphabet.find(j)
        my_array.append(encryption_index)


    for i in range(len(message)):
        if message[i].isupper():
            upper_case_index.append(i)

    for x in message:
        x=x.lower()
        if x.isalpha():
            letter_index=alphabet.find(x)
            new_index= letter_index + my_array[key_index % len(my_array)]
            new_letter=alphabet[new_index % 26]
            key_index+=1
        else:
            new_letter=x

        new_word+=new_letter


    def changer():
        choice=input("Do you want to retain capital letters? (y/n): ").lower()
        while True:
            if choice not in ('y','n'):
                print("Invalid entry. Please try again.")
                choice=input("Do you want to retain capital letters? (y/n): ").lower()=='y'
            else:
                break
        if choice=='y':
            final_word=''
            for i in range(len(new_word)):
                if i in upper_case_index:
                    final_word+=new_word[i].capitalize()
                else:
                    final_word+=new_word[i]
            
            return final_word
        else:
            return new_word

    if len(upper_case_index) > 0:
        return changer()
    else:
        return new_word

if __name__=="__main__":
    message=input("Enter message to encrypt: ")
    encryption_key=encryption_key_checker()
    encrypted_message=encoder(message,encryption_key)
    print(f"\nEncrypted message is: {encrypted_message}")
