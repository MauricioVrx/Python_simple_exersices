def simplePalindrome():
    strn = "Ana ana anA".lower().replace(" ","")
    isPal = lambda x: f"{x} - Es un palindromo" if x == x[::-1] else f"{x} - NO es un palindromo"
    print(isPal(strn))

def run():
    strn = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
    isPal = lambda li : list(filter(lambda x:x == x[::-1],li))
    print(isPal(strn))

if __name__ == "__main__":
    run()