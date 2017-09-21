import os, glob
import pandas as pd
import matplotlib
#basic input
"""
start = input("Please input the first Changelist to be processed. ")
end = input("Please input the last Changelist to be processed. ")"""
start = 1
end = 9999999999999
directory = r"C:/Area/**/"
path =  directory + 'Smoke Report General - AOI 200.xlsx'
cl = []
directories = []
for file in glob.glob(path):
    dirname = os.fsdecode(directory)
    if (int(file[8:14:]) >= int(start) and int(file[8:14:]) <= int(end)):
        #print(file)
        directories.append(file)
        #print(file[8:14:])
        cl.append(int(file[8:14:]))
        df = pd.read_excel(open(file, 'rb'), sheetname=0)
        print(df.iloc[9,6])

#Dasd

print(directories)
print(cl)