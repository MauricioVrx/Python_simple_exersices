#is palindrome?

strO = "Ana aNa"
strN = strO
strN =strN.replace(" ", "").lower()


if strN == strN[::-1]:
    print(f'"{strO}" es un palindromo')
else:
    print(f'"{strO}" NO es un palindromo')