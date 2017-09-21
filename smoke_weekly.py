import os, glob
import matplotlib
#basic input
start = 444437
#input("Please input the first Changelist to be processed. ")
end = 454777
#input("Please input the last Changelist to be processed. ")
directory = r"C:/Area/**/"
path =  directory + 'Smoke Report General - AOI 200.xlsx'
for file in glob.glob(path):
    dirname = os.fsdecode(directory)
    print(file)
    print(file[8:14:])
    #nie wyświetla niczego 
    """if (int(file[8:14:]) >= start and int(file[8:14:]) <= end):
        print(directory)"""