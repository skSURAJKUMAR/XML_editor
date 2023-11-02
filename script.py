from bs4 import BeautifulSoup
def XML_Modify(filename):
    with open(inpath+"\\"+filename, 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    data=str(Bs_data).replace("Owner","Clt")
    # print(Bs_data)

    file1 = open(outpath+'\\'+filename, 'w')
    file1.write(str(data))
    file1.close()


import os
inpath=r"C:\Users\32020\Desktop\XML EDITOR\Input"
outpath=r"C:\Users\32020\Desktop\XML EDITOR\Output"
listdir=[]
for file in os.listdir(inpath):
	XML_Modify(file)
