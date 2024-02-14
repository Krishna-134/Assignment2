str=input("enter a word:")
str=str.casefold()
reverse=reversed(str)
if list(str)==list(reverse):
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")