email = input("Enter your email: ").lower()

username = email[: email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your Username: {username}")
print(f"Your domain: {domain}")