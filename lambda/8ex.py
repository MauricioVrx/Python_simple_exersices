from datetime import datetime as dt
def run():
    inputDate = "2020/01/15 09:03:32"
    date_format = "%Y/%m/%d"
    nDate =  dt.date(dt.strptime(inputDate,date_format))
    print(nDate.lis)

if __name__ == '__main__':
    run()