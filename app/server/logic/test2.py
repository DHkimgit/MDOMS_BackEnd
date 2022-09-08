from typing import List
[
    {
        "time" : '06:00 - 08:00',
        "Monday" : '',
        "Tuesday" : '',
        "wednesday" : '',
        "Thursday" : '',
        "Friday" : '',
        "Saturday" : '',
        "Sunday" : ''
    },
]
# [[600, 800], [800, 1000, 1200, 1400, 1600, 1800], [1800, 2000], [2000, 2200]]


# 시간 리스트 -> database dict 추가
# input : [[600, 800], [800, 1000, 1200, 1400, 1600, 1800], [1800, 2000], [2000, 2200]]
# output : [{'time': '06:00 - 08:00'}, {'time': '08:00 - 10:00'}, {'time': '10:00 - 12:00'}, {'time': '12:00 - 14:00'}, {'time': '14:00 - 16:00'}, {'time': '16:00 - 18:00'}, {'time': '18:00 - 20:00'}, {'time': '20:00 - 22:00'}]
def create_schedule_form_with_time(time_list: List[int]) -> List:
    result = []
    for i in range(len(time_list)):
        for j in range(len(time_list[i]) - 1):
            start_time = str(time_list[i][j])
            end_time = str(time_list[i][j + 1])
            if len(start_time) != 4:
                start_time = start_time.zfill(4)
            if len(end_time) != 4:
                end_time = end_time.zfill(4)
            result.append({"time": f"{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}"})

    return result
# [600, 800], [800, 1000, 1200, 1400, 1600, 1800]
def test2(schedule_form_with_time: List[dict], time_list: List[int], array_roster: List[str], start_index: int, interval: int) -> List:
    index_array = []
    for i in range(len(time_list) - 1):
        start_time = str(time_list[i])
        end_time = str(time_list[i+1])
        if len(start_time) != 4:
                start_time = start_time.zfill(4)
        if len(end_time) != 4:
            end_time = end_time.zfill(4)
        for j in range(len(schedule_form_with_time)):
            if schedule_form_with_time[j]['time'] == f'{start_time[0]}{start_time[1]}:{start_time[2]}{start_time[3]} - {end_time[0]}{end_time[1]}:{end_time[2]}{end_time[3]}':
                schedule_form_with_time[j]['Monday'] = array_roster[start_index]
                next_index = start_index + interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Tuesday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Wednesday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Thursday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Friday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Saturday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                schedule_form_with_time[j]['Sunday'] = array_roster[next_index]
                next_index += interval
                if next_index >= len(array_roster):
                    next_index -= len(array_roster)
                start_index += 1
        index_array.append(next_index)
    return schedule_form_with_time
           
# 근무 시간을 나누는 함수
# input: [[600, 800], [800, 1000, 1200, 1400, 1600, 1800], [1800, 2000], [2000, 2200]]
# Output: [1, 5, 1, 1]
def schedule_time_interval(time_list: List[int]) -> List:
    result = []
    for i in range(len(time_list)):
        result.append(len(time_list[i]) - 1)
    return result

