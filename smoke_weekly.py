import os, glob
import matplotlib
#basic input
start = input("Please input the first Changelist to be processed. ")
end = input("Please input the last Changelist to be processed. ")
directory = r"C:/Area/**/"
path =  directory + 'Smoke Report General - AOI 200.xlsx'
for file in glob.glob(path):
    dirname = os.fsdecode(directory)
    if (int(file[8:14:]) >= int(start) and int(file[8:14:]) <= int(end)):
        print(file)
        print(file[8:14:])
    #nie wyświetla niczego 
    