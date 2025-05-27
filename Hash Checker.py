#This is a hash checker that compaares files to known bad hashes

import hashlib

#ask for the file path
file_path = input("Please enter the file you wish to check: ")

#choose the hash type, md5 or sha256
hash_type = input("Choose your hash type, md5 or sha256").lower()

#checking if input was valid
if hash_type not in ["md5", "sha256"]:
    print("Invalid input! Decide from either 'md5' or 'sha256'.")
    exit()

