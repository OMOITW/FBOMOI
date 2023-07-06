import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_username():
    return generate_random_string(8)

def generate_random_password():
    return generate_random_string(10)

def generate_random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com"]
    username = generate_random_username()
    return f"{username}@{random.choice(domain)}"

def create_account():
    username = generate_random_username()
    password = generate_random_password()
    email = generate_random_email()

    # Simulasikan proses pembuatan akun di sini
    # Misalnya, menyimpan akun yang dibuat ke database atau mencetak informasinya
    print("Akun berhasil dibuat:")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")

# Contoh penggunaan fungsi create_account untuk membuat 5 akun
for _ in range(5):
    create_account()
