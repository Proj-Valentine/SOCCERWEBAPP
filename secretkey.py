#this is just a code to generate secret key 
#didnt even use it
import secrets

# Generate a new SECRET_KEY
new_secret_key = secrets.token_hex(32)
print(new_secret_key)

