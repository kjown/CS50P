month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        #split date by /
        month, date, year = date.split("/")
        #check if month between 1-12 and date between 1-31
        if int(month) >= 1 and int(month) <= 12 and int(date) >= 1 and int(date) <= 31:
            break
    except:
        try:
            #split the date by space
            old_month, old_date, old_year = date.split(" ")
            #find the number of month
            for i in range (len(month)):
                if old_month == month[i]:
                    month = i + 1
            #remove coma from day variable
            date = old_date.replace(",", "")
            #check if month between 1-12 and date between 1-31
            if int(month) >= 1 and int(month) <= 12 and int(date) >= 1 and int(date) <= 31:
                print(year + "-" + f"{month:02}" + "-" + f"{date:02}" )
                break
        except:
            pass



