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
import urllib2
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
versionurl = "https://raw.githubusercontent.com/Girthquake/Cards/master/inc/version"
version=0
updateurl = 0
updateversion=0
includefolder='inc/'

def internet_on():
    try:
        urllib2.urlopen('https://www.google.com/', timeout=2)
        return True
    except urllib2.URLError as err: 
        return False

if __name__ == 'Core':
    try:
        _create_unverified_https_context = ssl._create_unverified_context 
    except AttributeError: 
        pass 
    else: 
        ssl._create_default_https_context = _create_unverified_https_context
    if os.path.isfile(includefolder+'version'):
        with open(includefolder+'version', 'rb') as fp:
            version = pickle.load(fp)
            fp.close()
    if internet_on:
        version_check = requests.get(versionurl, verify=False) #Download version file
        with open('vers', 'wb') as f: #Save downloaded version file to a temp vers file.
            f.write(version_check.content)
            f.close
        with open('vers', 'r') as f: #reopen the file and pull vsriables
            new_version=f.readlines()
            updateurl=new_version[1].strip('\n') #get download file URL
            updatedversion=new_version[0].strip('\n') #put new version number into a variable
            updatecoreurl=new_version[3] #get url for core files.
            injesturl=new_version[4]
            f.close() #now that we have the variables saved lets do the work.
        if Decimal(updatedversion) <= Decimal(version):
            if Confirm.ask("Are there Images you would like to process?"):
                if os.path.isfile('ImageInjest.py'):
                    import importlib
                    import importlib.util
                    spec = importlib.util.spec_from_file_location('ImageInjest', 'ImageInjest.py')
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                else:
                    import ImageInjest
            else:
                if os.path.isfile('Main.py'):
                    import importlib
                    import importlib.util
                    spec = importlib.util.spec_from_file_location('Main', 'Main.py')
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                else:
                    print('Importing system main')
                    import Main
        else:
            ur.urlretrieve(updateurl, "Main.py")
            ur.urlretrieve(updatecoreurl, "Core.py")
            ur.urlretrieve(injesturl,"ImageInjest.py")
            version = updatedversion
            with open(includefolder+'version', 'wb') as fp:
                pickle.dump(version, fp)
            if Confirm.ask("Are there Images you would like to process?"):
                if os.path.isfile('ImageInjest.py'):
                    import importlib
                    import importlib.util
                    spec = importlib.util.spec_from_file_location('ImageInjest', 'ImageInjest.py')
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                else:
                    import ImageInjest
            else:
                if os.path.isfile('Main.py'):
                    import importlib
                    import importlib.util
                    spec = importlib.util.spec_from_file_location('Main', 'Main.py')
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                else:
                    print('Importing system main')
                    import Main
    else:
        print("no internet for updating..... \ntisk tisk...")
        if Confirm.ask("Are there Images you would like to process?"):
            if os.path.isfile('ImageInjest.py'):
                import importlib
                import importlib.util
                spec = importlib.util.spec_from_file_location('ImageInjest', 'ImageInjest.py')
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            else:
                import ImageInjest
        else:
            if os.path.isfile('Main.py'):
                import importlib
                import importlib.util
                spec = importlib.util.spec_from_file_location('Main', 'Main.py')
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            else:
                print('Importing system main')
                import Main