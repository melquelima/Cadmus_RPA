import csv
import traceback
from datetime import datetime as dt
import os.path

class LogCsv:
    def __init__(self,addrs,dtFormat="%d/%m/%Y %H:%M:%S"):
        self.addrs      = addrs
        self.csvFile    = None
        self.spamwriter = None
        self.columns    = ["Datetime","Status","Step","Obs","Traceback"]
        self.headers(self.columns)
        self.format = dtFormat

    def headers(self,columns):
        if not os.path.isfile(self.addrs):
            self.writeRow(self.columns)

    def openLog(self):
        self.csvFile = open(self.addrs, 'a', newline='')
        self.spamwriter = csv.writer(self.csvFile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def closeLog(self):
        self.csvFile.close()

    def writeRow(self,columns):
        self.openLog()
        self.spamwriter.writerow(columns)
        self.closeLog()

    def writeLogSuccess(self,step,Obs):
        date = dt.now().strftime(self.format)
        rows = [date,"SUCCESS",step,Obs]
        self.writeRow(rows)

    def writeLogWarning(self,step,Obs):
        date = dt.now().strftime(self.format)
        rows = [date,"WARNING",step,Obs]
        self.writeRow(rows)

    def writeLogFailed(self,step,Obs):
        date = dt.now().strftime(self.format)
        rows = [date,"FAILED",step,Obs]
        self.writeRow(rows)

    def writeLogException(self,step,Obs):
        date = dt.now().strftime(self.format)
        rows = [date,"EXCEPTION",step,Obs,traceback.format_exc().replace(";","").replace("\n"," /n ")]
        self.writeRow(rows)



def deco_log(log:LogCsv,step): 
  
    def Inner(func): 
        def wrapper(*args, **kwargs):
            log.writeLogSuccess(step,"START")
            value = None
            try:
                value = func(*args, **kwargs)
                log.writeLogSuccess(step,"END")
            except:
                log.writeLogException(step,"STEP FAILED")
            return value
              
        return wrapper 
    return Inner 

    #traceback.format_exc()
