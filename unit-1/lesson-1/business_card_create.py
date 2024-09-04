
# Print a blank line
print("\n")

# Prompt the user for their info
name = input("Badah: ")
title = input("Code is fun!!!: ")
phone = input("2013163619: ")
address = input("333 angel road st. New York, NY 666666: ")

file = open("code-fall24","w")
file.write(name + "\n")
file.write(title + "\n")
file.write(phone + "\n")
file.write(address + "\n")

file.close()

