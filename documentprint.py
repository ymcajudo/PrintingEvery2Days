import os, psutil
import datetime as dt
from time import sleep

def pdfprint():
    os.startfile("test.pdf", "print")       #print test.pdf
    sleep(5)
    for p in psutil.process_iter(): #Close Acrobat after printing the PDF
        if 'AcroRd' in str(p):
            p.kill()

def dateoftoday():
    x = dt.datetime.today()         # x is today
    y = x.strftime("%Y%m%d")        # transform x to the year, month and day(ex:20221231)
    return int(y)                   # convert string to integer

def lastprint():
    f = open("printhistory.txt", 'r')
    line = int(f.readline())
    f.close()
    return line

def recordprint():
    f = open("printhistory.txt", 'w')
    f.write(str(dateoftoday()))
    f.close()

if __name__ == "__main__":
    if dateoftoday()-lastprint() > 1:
        pdfprint()                      #The test file is printed at least two days later since last printing
        recordprint()                   #write the printing date to printhistory.txt
    else:
        print("Do not need to print the test file yet.")

