import os, glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#basic input
"""
start = input("Please input the first Changelist to be processed. ")
end = input("Please input the last Changelist to be processed. ")"""
start = 1
end = 9999999999999
directory = r"C:/Area/**/"
path =  directory + 'Javelin Smoke Report General - AOI 200.xlsx'
cl = []
directories = []

Pass = []
Fail = []
Issues = []
Blocked = []

def resultSearch():
    for file in glob.glob(path):
        if (int(file[8:14:]) >= int(start) and int(file[8:14:]) <= int(end)):
            directories.append(file)
            cl.append(int(file[8:14:]))
            df = pd.read_excel(open(file, 'rb'), sheetname=0)
            Pass.append(df.iloc[3, 7])
            Fail.append(df.iloc[4, 7])
            Issues.append(df.iloc[5, 7])
            Blocked.append(df.iloc[6, 7])
            


def resPlotter():
    global Pass
    global Fail
    global Issues
    global Blocked
    Pass = np.array(Pass)
    Fail = np.array(Fail)
    Issues = np.array(Issues)
    Blocked = np.array(Blocked)
    N = len(cl)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence
    
    p1 = plt.bar(ind, Pass, width, color='olivedrab')
    p3 = plt.bar(ind, Issues, width, color='gold', bottom=Pass)
    p2 = plt.bar(ind, Fail, width, color='firebrick', bottom = Pass + Issues)
    p4 = plt.bar(ind, Blocked, width, color='black', bottom=Pass + Issues + Fail)
    

    
    plt.ylabel('Results')
    plt.title('Weekly Smoke Report')
    plt.xticks(ind, (cl))
    plt.yticks(np.arange(0, 10, 1))
    plt.legend((p1[0], p3[0], p2[0], p4[0]), ('Pass', 'Issues', 'Fail', 'Blocked'), loc= 'lower center',
    bbox_to_anchor=(0.5, 0.01), ncol=4, fancybox=True, shadow=True)
    
    plt.show()
    
    
resultSearch()
resPlotter()



