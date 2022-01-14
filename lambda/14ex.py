def run():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    lam  = lambda l1 : list(filter(lambda x: len(x)==6, l1)) #Dinamic
    lam2 = list(filter(lambda x: len(x)==6, week)) #static

    print(lam(week))

if __name__ == "__main__":
    run()