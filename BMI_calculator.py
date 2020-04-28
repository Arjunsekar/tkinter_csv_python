import csv
from random import seed
from random import choice
# import tkinter
# from tkinter import filedialog
dummy=[]
Random = []
output =[]
Dum=[]            

# Can be used to get user input
# tkinter.Tk().withdraw()
# print('Select ur file')
# File = filedialog.askopenfilename(filetypes = (("All files","*.*"),("Text File","*.csv")),title="Select input file")

# with open(File,'r') as file1:
#     reader =  csv.reader(File)
#     label = list(reader)
#     for row in label:
#         Dum.appened(row) 
        
with open("customer_list.csv",'r') as File:
    reader = csv.reader(File)
    label = list(reader)

for i in label:
    dummy.append(i[0])
# seed random number generator
seed(1)
# generate some random numbers to select for customers
print('The dummy random variables are')
for k in range(20):
    selection = choice(dummy)
    print(selection)
    Random.append(selection)

d ={}
for a in Random:
    for e in label:
        if a == e[0]:
            if (float(e[12])<18.5) or float(e[12])>24.9:
                d={'RowNumber':e[0],'Gender':e[1],'Name':e[2],'Surname':e[3],'Weight':e[10],'Height':e[11],'BodyMassIndex':e[12],'Mobile Number':e[4]}
                output.append(d)
                print("Abnormal Body mass index %f found in the random customer number %d:",e[12],e[0])

key = output[0].keys()
with open('Abnormal_BMI.csv','w') as OPFile:
    writer = csv.DictWriter(OPFile, key)
    writer.writeheader()
    writer.writerows(output)


        
        
