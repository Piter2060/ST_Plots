import os
import matplotlib
#basic input
start = input("Please input the first Changelist to be processed. ")
end = input("Please input the last Changelist to be processed. ")

directory = os.fsencode("C:/b/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        time = os.path.getctime(directory + file)
        print(time)
        print(filename)
        continue
    else:
        continue