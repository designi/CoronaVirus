from datetime import datetime
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import path
from urllib.error import HTTPError
import sys

logging.getLogger().setLevel(logging.INFO)
dt = datetime.today().strftime('%Y-%m-%d')
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{0}.xlsx'.format(dt)
fileLocation = '/Users/nikolasgarcia/PycharmProjects/CoronaVirus/DailyDownload/'
if path.exists(fileLocation) is False:
    logging.error('File directory does not exist.')
    sys.exit(1)
fileName = url[url.find('COVID'):len(url)]

if path.isfile(fileLocation+fileName):
    logging.info('\nFile already exists at {0} \nLoading file from that directory.\n'.format(fileLocation))
    df = pd.read_excel(fileLocation+fileName)
    df['DateRep'] = pd.to_datetime(df['DateRep'], format='%Y-%m-%d')
    print(df.head())
else:
    try:
        df = pd.read_excel(url)
        df['DateRep'] = pd.to_datetime(df['DateRep'], format='%Y-%m-%d')
        logging.info('\nSuccessfully pulled down file containing {0} records.'.format(len(df)))
        logging.info('\nMoving {0} to \n'.format(fileName) + fileLocation)
        df.to_excel(fileLocation + '{0}'.format(fileName), sheet_name='Data', index=True)
    except HTTPError as e:
        logging.error('\nEncountered {0} error. Web Link {1}.'.format(e.code, e.reason))
    except FileNotFoundError as e:
        logging.error('\nEncountered {0} while trying to download. \nCheck URL.'.format(e))
