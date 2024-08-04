"""
Write a program to find user input letter is vowel or not
"""
letter = input("Enter a letter:")
letter=letter.upper()
if letter in ['A','E','I','O','U']:
    print(f"Letter({letter}) is Vowel")
else:
    print(f"Letter({letter}) is not Vowel")