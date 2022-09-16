from datetime import datetime, date
dates= '2022-09-15'
class date_parser:
    def year(date):
        return date[0]+date[1]+date[2]+date[3]

    def month(date):
        return date[5]+date[6]

    def date(date):
        return date[8]+date[9]

    def is_weekend(date):
        today = datetime(int(date_parser.year(date)), int(date_parser.month(date)), int(date_parser.date(date))).weekday()
        if today==5 or today == 6:
            return True
        else:
            return False

    def day(date):
        today = datetime(int(date_parser.year(date)), int(date_parser.month(date)), int(date_parser.date(date))).weekday()
        if today == 0:
            return "월요일"
        elif today == 1:
            return "화요일"
        elif today == 2:
            return "수요일"
        elif today == 3:
            return "목요일"
        elif today == 4:
            return "금요일"
        elif today == 5:
            return "토요일"
        else:
            return "일요일"

print(date_parser.is_weekend(dates))
print(date_parser.day(dates))

i = 1
j = 5

time_data = [
    "06:00 - 08:00",
    "08:00 - 10:00",
    "10:00 - 12:00",
    "12:00 - 14:00",
    "14:00 - 16:00",
    "18:00 - 18:00"
]
test = time_data[i][0] + time_data[i][1] + ':' +  time_data[i][3] + time_data[i][4] + ' ' + '-' + ' ' + time_data[i + j - 1][8] + time_data[i + j - 1][9] + ':' + time_data[i + j - 1][11] + time_data[i + j - 1][12]
print(test)



