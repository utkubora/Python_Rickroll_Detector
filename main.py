import RickRollDetector
from RickRollDetector import Rick
import sys
import os

if os.name == 'nt':
    char1 = '\\'
else:
    char1 = '/'
fileway = os.getcwd()+char1+'Rick'
temp_file_way = os.getcwd()+char1+'temp'

rick = Rick(sys.argv[1],file_way=fileway,temp_file_way=temp_file_way,char1=char1)
rick.RickRollChecker()
