import os
import matplotlib
#basic input
start = 444437
#input("Please input the first Changelist to be processed. ")
end = 454777
#input("Please input the last Changelist to be processed. ")

direct = "C:/Area/"

for directory in os.listdir(direct):
    dirname = os.fsdecode(directory)
    if os.path.isdir(int(dirname) >= start and int(dirname) <= end):
        print(directory)
