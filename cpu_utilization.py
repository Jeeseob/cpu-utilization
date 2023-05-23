import datetime
import psutil
import pandas as pd
import sys
import atexit

def handle_exit():
    print("program exit")
    CPU_utilizationDF = pd.DataFrame({key: pd.Series(value) for key, value in CPU_utilization.items()})
    CPU_utilizationDF.to_csv("./cpu_util_log.csv", sep=',', na_rep="NaN") # if you want, change filename

# check argument
if len(sys.argv) < 2:
    print("Need argument: Running time(min)")
    sys.exit(1)
else:
    runningTime = int(sys.argv[1])
  
# cpuCount = psutil.cpu_count(logical=False)
cpuCount = psutil.cpu_count()
CPU_utilization = {"Time": []}
for i in range(0, cpuCount):
    CPU_utilization["core" + str(i)] = []

endTime = datetime.datetime.now() + datetime.timedelta(minutes=runningTime)

# handle_exit() if program exit, handle_exit run
atexit.register(handle_exit)  

while datetime.datetime.now() <= endTime:
    util_list = psutil.cpu_percent(interval=1, percpu=True)
    CPU_utilization["Time"].append(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

    for i in range(0, len(util_list)):
        CPU_utilization["core" + str(i)].append(util_list[i])
