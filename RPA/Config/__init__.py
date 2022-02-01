from RPA.Libs.Logs import LogCsv
import os

#=============DEFAULT=======
DEFAULT_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
CURRENT_FOLDER = os.path.dirname(__file__)

#========CHROME DRIVER======
CHROME_DRIVER = CURRENT_FOLDER + '/chromedriver.exe'
#========SMT CONFIG==========
FROM    = ''
SERVER  = ''
PORT    = ''
USER    = ''
PWD     = ''
TO      = "email_must_recieve@gmail.com"
SUBJECT = "Relatório de Vagas Disponíveis CadMus"
#=======LOG FILE=============
LOG_FILE = DEFAULT_FOLDER + '/Logs/log.csv'
if os.path.exists(LOG_FILE): os.remove(LOG_FILE)
LOG     = LogCsv(LOG_FILE)
#=======OUTPUT FILE==========
OUTPUT_FILE = DEFAULT_FOLDER + "/Output/Oportunities.xlsx"
