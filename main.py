import time
import sys
print("Welcome to the customer support chatbot!")

for i in range(3):
    print(".", end="")
    time.sleep(1)
print("\n")

name = input("Please enter your name.\n")


time.sleep(1)

print(name, end="")
for i in range(4):
    print(".", end="")
    time.sleep(0.5)
print(" That's a great name!")

time.sleep(1)

age = int(input("And what's your age?\n"))

time.sleep(1)

if age >= 100:
    print("You're very old!")
    time.sleep(1)

print("\nOkay. Now, " + name + ", choose an option:")
print("1. Placeholder")
print("2. Placeholder")
print("3. Placeholder")
print("4. Exit the conversation")
print("Awating your response...")

choice = int(input())

if choice == 4:
    print("Goodbye, " + name + "! Thanks for chatting with me.")
    sys.exit()