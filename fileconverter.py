##file convert run this as root sudo dosent work really weird 
import os
import subprocess
import sys 

path=sys.argv[1]
os.chdir(path)
num=0
for dirName, subdirList, fileList in os.walk(path):
        os.chdir(dirName)
        print(os.getcwd())
        for fname in fileList:
                print(fname)
                subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf:writer_pdf_Export', fname])
                
                num+=1
        
               
print(num,'Files Converted')


