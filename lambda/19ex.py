def run():
    word = "cabd"
    list1 = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']

    wordsInList = lambda li, wd : list(filter( lambda x :"".join(sorted(x)) == "".join(sorted(wd)) ,li))

    print(wordsInList(list1,word))

if __name__ == '__main__':
    run()