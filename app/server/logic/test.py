from typing import List

# [0600, 0800, 1000, 1200, 1400 ]
# 근무 시간 배열, 근무 순서 배열, 오늘 날짜
def MakeDailySchedule(array_time : List[int], array_roster = List[str], todaydate = int) -> List:
    result = []
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}'])
    
    for i in range(len(result)):
        result[i].append(array_roster[i])

    return result

def MakeDailySchedule_time(array_time : List[int]) -> List:
    result = []
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}'])

    return result

def MakeWeekelySchedule():
    pass

roster_0830 = MakeDailySchedule_time([600, 800, 1000, 1200, 1400])
roster_0831 = MakeDailySchedule([630, 830, 1030, 1230, 1430], ['일병 김두현', '상병 이정현', '상병 박상하', '상병 이승만', '상병 윤보선', '일병 박정희', '일병 김영삼', '일병 노태우', '일병 박근혜', '일병 이명박', '병장 문재인', '병장 윤석열', '병장 김대중', '병장 노무현'])

print(roster_0831)

