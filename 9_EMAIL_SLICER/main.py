# email ='syntaxspheres@gmail.com'  # username = syntaxspheres , extension = gmail , domain = com
print("Welcome to the Email Address Slicer")
email = input("Enter a Valid Email Address: ")
if '@' in email:
    username,extension = email.split('@')
    extension,domain = extension.split('.')
    print(f"The Informations about the Email is:\nUsername: {username}\nExtension: {extension}\nDomain: {domain}")
else:
    print("Invalid Email Address")