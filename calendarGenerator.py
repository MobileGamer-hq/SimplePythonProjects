days_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
month = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}


def generate_calendar(m = 'jan', d = 1):

    stop_month = 'dec'
    stop_day = ''

    year = {}
    _week = []
    for i in month:
        year[i] = []
        for j in range(1, month[i]+ 1):
            _week.append(j)
            if len(_week) == 7:
                year[i].append(_week)
                _week = []
        if len(_week) > 0:
            year[i].append(_week)
            temp = []
            for _ in range(len(_week)):
                temp.append(0)
            _week = temp
    
    cut = year[m]
    
    for i in cut:
        for j in i:
            if j == d:
                _index = i.index(j)
                print(days_of_week[_index])

    #display calendar
    for _month in year:
        print(_month)
        for week in year[_month]:
            print(week)
        


# def generate_calendar2(m = 'jan', d = 1):

#     year = []
#     _week = []
#     for i in month:
#         for j in range(1, month[i]+ 1):
#             _week.append(j)
#             if len(_week) == 7:
#                 year.append(_week)
#                 _week = []

    


generate_calendar(m = 'dec', d=  21)