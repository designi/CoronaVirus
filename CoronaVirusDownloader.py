from datetime import datetime
import logging
import numpy as np
import pandas as pd
from os import path
from urllib.error import HTTPError

# COVID-19 cases worldwide
dt = datetime.today().strftime('%Y-%m-%d')
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{0}.xlsx'.format(dt)
fileLocation = '/Users/nikolasgarcia/PycharmProjects/CoronaVirus/DailyDownload/'

try:
    df = pd.read_excel(url)
    logging.info('Successfully pulled down file')
    print(df.head())
    if path.exists(fileLocation.format(url[url.find('COVID'):len(url)])):
        logging.info('Moving {0} file to \n'+fileLocation.format(url[url.find('COVID'):len(url)]))
        df.to_excel(fileLocation+'{0}'.format(url[url.find('COVID'):len(url)]))
    else:
        logging.info('File already exists at {0}'.format(fileLocation))
except FileNotFoundError as e:
    logging.error('Encountered {0} while trying to download. \nCheck URL.'.format(e))
except HTTPError as e:
    logging.error('Encountered {0} error. Web Link {1}.'.format(e.code, e.reason))


