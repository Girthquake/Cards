from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import PieChart, Reference, Series
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from datetime import date
from rich.console import Console
from rich.text import Text
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
from rich.prompt import Confirm
from rich.theme import Theme
import openpyxl
import glob
import random
import time
import shutil
import pickle
import binascii
import requests
from decimal import *
import os, sys
import urllib.request as ur
requests.packages.urllib3.disable_warnings() 
import ssl
import os.path
from concurrent.futures import as_completed, ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
updateurl = "https://raw.githubusercontent.com/Girthquake/CardBuilder/master/main.py"
versionurl = "https://raw.githubusercontent.com/Girthquake/CardBuilder/master/Updater/version"
version=0
updateversion=0
style="old"
if __name__ == '__main__':
    try:
        _create_unverified_https_context = ssl._create_unverified_context 
    except AttributeError: 
        pass 
    else: 
        ssl._create_default_https_context = _create_unverified_https_context
    if os.path.isfile('version'):
        with open('version', 'rb') as fp:
            version = pickle.load(fp)
            fp.close()
    version_check = requests.get(versionurl, verify=False)
    #print(version)
    with open('vers', 'wb') as f:
        f.write(version_check.content)
        f.close
    with open('vers', 'r') as f:
        new_version=f.readlines()
        updateurl=new_version[1].strip('\n')
        updatedversion=new_version[0].strip('\n')
        f.close()
        #os.remove('vers')
    #print(new_version)
    if Decimal(updatedversion) <= Decimal(version):
        if os.path.isfile('main.py'):
            #print('Importing local main')
            import importlib
            import importlib.util
            spec = importlib.util.spec_from_file_location('main', 'main.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            print('Importing system main')
            import main
    else:
        ur.urlretrieve(updateurl, "main.py")
        version = updatedversion
        with open('version', 'wb') as fp:
            pickle.dump(version, fp)
        if os.path.isfile('main.py'):
            #print('Importing local main')
            import importlib
            import importlib.util
            spec = importlib.util.spec_from_file_location('main', 'main.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            print('Importing system main')
            import main
