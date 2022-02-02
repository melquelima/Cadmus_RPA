from RPA.Libs.Logs import LogCsv
import os

#=============DEFAULT=======
DEFAULT_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
CURRENT_FOLDER = os.path.dirname(__file__)

#========CHROME DRIVER======
CHROME_DRIVER = CURRENT_FOLDER + '/chromedriver.exe'
#========SMT CONFIG==========
FROM    = ''
SERVER  = 'smtp.gmail.com'
PORT    = 587
USER    = 'my_email@gmail.com'
PWD     = 'my_password'
TO      = "emailWilreceive@gmail.com"
SUBJECT = "Report Oportunities CADMUS"
#=======LOG FILE=============
LOG_FILE = DEFAULT_FOLDER + '/Logs/log.csv'
if os.path.exists(LOG_FILE): os.remove(LOG_FILE)
LOG     = LogCsv(LOG_FILE)
#=======OUTPUT FILE==========
OUTPUT_FILE = DEFAULT_FOLDER + "/Output/Oportunities.xlsx"
