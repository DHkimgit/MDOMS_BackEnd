from typing import List

# [0600, 0800, 1000, 1200, 1400 ]
# 근무 시간 배열, 근무 순서 배열, 오늘 날짜
# def MakeDailySchedule(array_time : List[int], array_roster = List[str], todaydate) -> List:
#     result = []
#     for i in range(len(array_time) - 1):
#         result.append([f'{array_time[i]} - {array_time[i + 1]}'])
#     return result

def MakeDailySchedule_time(array_time : List[int]) -> List:
    result = []
    for i in range(len(array_time) - 1):
        start_time = str(array_time[i])
        end_time = str(array_time[i + 1])
        if len(start_time) != 4:
            start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        result.append([f'{start_time} - {end_time}'])
    return result

roster_0830 = MakeDailySchedule_time([600, 800, 1000, 1200, 1400])

print(roster_0830)
