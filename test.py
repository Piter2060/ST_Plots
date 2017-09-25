"""import os, glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

start = 1
end = 9999999999999
directory = r"C:/Area/**/"
path =  directory + 'Smoke Report General - AOI 200.xlsx'
cl = []
directories = []

Pass = []
Fail = []
Issues = []
Blocked = []


for file in glob.glob(path):
    dirname = os.fsdecode(directory)
    if (int(file[8:14:]) >= int(start) and int(file[8:14:]) <= int(end)):
        directories.append(file)
        cl.append(int(file[8:14:]))
        df = pd.read_excel(open(file, 'rb'), sheetname=0)
        print(df.iloc[5, 2])
        print(df.iloc[6, 2])
        print(df.iloc[7, 2])
        print(df.iloc[8, 2])
        print(df.iloc[9, 2])
"""


import os, glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame as DataFrame
#basic input
"""
start = input("Please input the first Changelist to be processed. ")
end = input("Please input the last Changelist to be processed. ")
"""
start = 1
end = 9999999999999
directory = r"C:/Area/**/"
path =  directory + 'Smoke Report General - AOI 200.xlsx'
cl = []
directories = []

Pass = []
Fail = []
Issues = []
Blocked = []
avg_AMD = []
avg_Intel = []
avg_Geforce = []
avg_Radeon = []
avg_Ram = []
avg_uptime = []

def resultSearch():
    for file in glob.glob(path):
        dirname = os.fsdecode(directory)
        if (int(file[8:14:]) >= int(start) and int(file[8:14:]) <= int(end)):
            directories.append(file)
            cl.append(int(file[8:14:]))
            df = pd.read_excel(open(file, 'rb'), sheetname=0)
            Pass.append(df.iloc[3, 7])
            Fail.append(df.iloc[4, 7])
            Issues.append(df.iloc[5, 7])
            Blocked.append(df.iloc[6, 7])
            avg_AMD.append(float(df.iloc[5, 2]) * 100)
            avg_Intel.append(float(df.iloc[6, 2]) * 100)
            avg_Geforce.append(df.iloc[7, 2])
            avg_Radeon.append(df.iloc[8, 2])
            avg_Ram.append(df.iloc[9, 2])
            avg_uptime.append(df.iloc[10, 2])
            print(avg_AMD)
            print("AMD")
            print(avg_Intel)
            print("Intel")

def resPlotter():
    global Pass
    global Fail
    global Issues
    global Blocked
    Pass = np.array(Pass)
    Fail = np.array(Fail)
    Issues = np.array(Issues)
    Blocked = np.array(Blocked)
    AMD = np.array(avg_AMD)
    Intel = np.array(avg_Intel)
    Geforce = np.array(avg_Geforce)
    Radeon = np.array(avg_Radeon)
    Ram = np.array(avg_Ram)
    N = len(cl)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    fig1 = plt.figure()
    p1 = plt.bar(ind, Pass, width, color='green')
    p2 = plt.bar(ind, Fail, width, color='red', bottom=Pass)
    p3 = plt.bar(ind, Issues, width, color='yellow', bottom=Pass + Fail)
    p4 = plt.bar(ind, Blocked, width, color='black', bottom=Pass + Fail + Issues)
    
    plt.ylabel('Results')
    plt.title('Weekly Smoke Report')
    plt.xticks(ind, (cl))
    plt.yticks(np.arange(0, 10, 1))
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Pass', 'Fail', 'Issues', 'Blocked'))
    plt.show()


    bar_width = 0.4
    plt.ylabel('Results')
    plt.title('Performance Smoke: average CPU usage (in %)')
    bar_locations = np.arange(len(cl))
    plt.xticks(ind, (cl))
    p1 = plt.bar(bar_locations, AMD, bar_width, color = "tomato")
    p2 = plt.bar(bar_locations - bar_width, Intel, bar_width, color="c")
    plt.legend((p1[0], p2[0]), ("CPU AMD", "CPU Intel"))
    plt.show()

    plt.ylabel('Results')
    plt.title('Performance Smoke: average GPU frames')
    bar_locations = np.arange(len(cl))
    plt.xticks(ind, (cl))
    p1 = plt.bar(bar_locations, Radeon, bar_width, color="tomato")
    p2 = plt.bar(bar_locations - bar_width, Geforce, bar_width, color="c")
    plt.legend((p1[0], p2[0]), ("CPU Radeon", "CPU Geforce"))
    plt.show()

    plt.ylabel('Results')
    plt.title('Performance Smoke: average RAM usage')
    bar_locations = np.arange(len(cl))
    plt.xticks(ind, (cl))
    p1 = plt.bar(bar_locations, Ram, bar_width, color="tomato")
    plt.show()


resultSearch()
resPlotter()
print(avg_AMD)
print(cl)

