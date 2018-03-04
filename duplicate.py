from FOStocks import  FOStocks
entries = []
duplicate_entries = []
fostocks = FOStocks()
todaypath = fostocks.getbsetodaypath()
with open(todaypath, 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[1] not in entries:
            entries.append(columns[1])
        else:
            duplicate_entries.append(columns[1])
print(duplicate_entries)