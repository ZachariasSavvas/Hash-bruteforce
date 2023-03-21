import hashlib


def hashdetect(x): # detecting the alg of the hash via numbers
    y=len(x)
    if y== 32 :
        alg= hashlib.md5()
       
    elif y== 40 :
        alg= hashlib.sha1()
        
    elif y==56 :
        alg= hashlib.sha224()
        
    elif y== 64:
        alg= hashlib.sha256()
        
    elif y== 96:
        alg= hashlib.sha384()
        
    elif y == 128:
        alg= hashlib.sha512()
        
    else:
        alg="error"

    return alg


hashed_import = input("dwse to hashed value :")
hashed_import_enc = hashed_import.encode()


wordlist = "wordlist.txt" # importing wordlist
wordfound= False
with open(wordlist) as file:
    while (line := file.readline() ) and (wordfound == False):
        
        alg = hashdetect(hashed_import)

        if (alg!="error"):

            

            key = line.rstrip()
            key_enc = key.encode()

            alg.update(key_enc)

            hashedword = alg.hexdigest()


            if  hashedword == hashed_import :
                print("correct word found: ",key," ",hashedword)
                wordfound=True
            
            

            else:
                print("Word not correct: ",key," ",hashedword)
        else:
            print("Wrong hash value was given")
            break
    


