def is_alphabet(char):
    if char.isalpha():
        return f"{char} is an alphabet letter."
    else:
        return f"{char} is not an alphabet letter."
char = input("Enter a character: ")
print(is_alphabet(char))
while True:
    char = input("Enter a character: ")
    print(is_alphabet(char))
