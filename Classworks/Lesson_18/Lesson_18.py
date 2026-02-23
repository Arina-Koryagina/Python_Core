# def getText(name, merge):
#     merge.append(name)
#     f = open(name, "r")
#     merge.append(f.read()+"\n")
#     f.close()
#     return merge
#
# merged = []
# for i in range(1, 4):
#     getText(f"file{i}.txt", merged)
#
# f = open("merged.txt", "w")
# f.write('\n'.join(merged))
# f.close()
# print("Done.")
import datetime

# file_list = ["file1.txt", "file2.txt", "file3.txt"]
#
# for file_name in file_list:
#     f = open(file_name, "r")
#     info = f.read()
#     f.close()
#     merged = open("merged.txt", "a")
#     merged.write(file_name + '\n')
#     merged.write(info + '\n')
#     merged.close()
#
# print("Done.")

# import random
#
# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# f = open("log.txt", "w")
# for i in range(10000):
#     f.write("192.168.0." + str(random.randint(100, 255)) + " " + week[random.randint(0,6)] + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + "\n")

# 192.168.0.160 Fr 07.27 13.39

f = open("log.txt", 'r')
# lines_list = f.readlines()
# f.close()
#
# IPs = []
# for data in lines_list:
#     IPs.append(data.split()[0])
logList = [[l for l in line.replace('\n', '').split()] for line in f.readlines()]
f.close()

# IPs = [el[0] for el in logList]
# times = []
# IPs_unique = []
# for user_IP in IPs:
#     times.append(IPs.count(user_IP))
# for i in range(len(IPs)):
#     if [IPs[i], times[i]] not in IPs_unique:
#         IPs_unique.append([IPs[i], times[i]])
#
# the_IP = IPs_unique[0][0]
# most_common = IPs_unique[0][1]
# for i in range(len(IPs_unique)):
#     if IPs_unique[i][1] > most_common:
#         most_common = IPs_unique[i][1]
#         the_IP = IPs_unique[i][0]
#
# print(f"The winner is {the_IP} with total of {most_common} entries.")
# # The winner is 192.168.0.139 with total of 88 entries.

# days = [el[1] for el in logList]
# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# times = []
# for day in week:
#     times.append(days.count(day))
#
# the_day = week[0]
# most_common = times[0]
# for i in range(len(week)):
#     if times[i] > most_common:
#         most_common = times[i]
#         the_day = week[i]
#
# print(f"The day is {the_day} with total of {most_common} entries.")
# # The day is Fr with total of 1480 entries.

IPs = [el[0] for el in logList]
start = [el[2] for el in logList]
end = [el[3] for el in logList]

def getTime(st, en):
    h1, m1 = map(int, st.split('.'))
    h2, m2 = map(int, en.split('.'))
    h = h2 - h1
    m = m2 - m1
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h += 24
    return m + (60 * h)

total_list = []
for i in range(len(IPs)):
    total_list.append([IPs[i], getTime(start[i], end[i])])

unique_IPs = []
for i in range(len(IPs)):
    if IPs[i] not in unique_IPs:
        unique_IPs.append(IPs[i])

the_list = []

# for i in range(len(unique_IPs)):
#     # the_list.append([total_list[i]])
#     for IP in unique_IPs:
#         # порахувати загальну кіл-ть годин за весь час для кожного IP

the_IP = the_list[0][0]
longest = the_list[0][1]
for i in range(len(unique_IPs)):
    if the_list[i][1] > longest:
        longest = the_list[i][1]
        the_IP = the_list[i][0]

lon_h = round(longest / 60)
lon_m = longest - lon_h * 60
if lon_m < 60:
    lon_h -= 1
    lon_m += 60

print(f"The IP is {the_IP} with total of {lon_h}h {lon_m}m.")
# The IP is 192.168.0.110 with total of 23h 39m. (1419 minutes)

# def deltatime(t1, t2):
#     h1, m1 = map(int, t1.split('.'))
#     h2, m2 = map(int, t2.split('.'))
#     dt1 = datetime.timedelta(hours=h1, minutes=m1)
#     dt2 = datetime.timedelta(hours=h2, minutes=m2)
#     # dt = str(dt2-dt1).split()
#     # dt = dt[-1].split(":")
#     # print(f"{dt[0]}h {dt[1]}m")
#     if dt1 < dt2:
#         return dt2 - dt1
#     return datetime.timedelta(hours=24) - (dt1 - dt2)

# print(getTime('10.32', '8.54'))
# print(deltatime('07.27', '13.39'))
# print(deltatime('12.04', '06.47'))
# print(deltatime('17.00', '03.54'))
