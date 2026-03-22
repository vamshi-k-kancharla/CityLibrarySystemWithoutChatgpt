import bcrypt

password = "12345".encode('utf-8')
salt = bcrypt.gensalt()
hashedPassword = bcrypt.hashpw(password, salt)

print(hashedPassword)