import os
import shutil
import inspect
import sqlite3 
import subprocess
import datetime
#import ctypes.wintypes

#Path of main progam

Myfilename = inspect.getframeinfo(inspect.currentframe()).filename
Mypath = os.path.dirname(os.path.abspath(Myfilename))

#Function for choose Solidworks Folder

def SldwrksFolderChoose():
    print("Specify the folder with installed SolidWorks (For example - C:\Program Files\SOLIDWORKS 2019\SOLIDWORKS)")
    global SLDWrksFold
    SLDWrksFold = input()
    SLDToolboxUpdFold = SLDWrksFold + '\sldtoolboxupdater.exe'
    if (os.path.exists (SLDToolboxUpdFold)):
        print("OK")
    else:
        print("The folder is invalid")
        return SldwrksFolderChoose()

#Function for choose Toolbox folder

def ToolboxFolderChoose():
    print("Specify the folder with installed Toolbox (For example - F:\Toolbox 2019)")
    global ToolboxFold
    global SwbrowserFold
    ToolboxFold = input()
    SwbrowserFold = ToolboxFold + '\lang\English\swbrowser.sldedb' 
    if (os.path.exists (SwbrowserFold)):
        print("OK")
    else:
        print("The folder is invalid")  
        return ToolboxFolderChoose()

def SQLScriptFolderChoose():
    FilenamesArray = []
    print("Specify the folder with SQLScript")
    global SQLScriptFold
    SQLScriptFold = input()
    
    for file in os.listdir(SQLScriptFold):
        FileSuffix = os.path.splitext(os.path.join(SQLScriptFold, file))[-1].lower()
        if FileSuffix == (".sql"):
            print(os.path.join(SQLScriptFold, file))
            FilenamesArray.append(1)
        else:
            FilenamesArray.append(0)
    if 1 in FilenamesArray:
        print ('OK')
    else:
        print ('No SQL scripts were found, select another folder')
        return SQLScriptFolderChoose()
    
def ToolboxUpdateFolderChoose():
    print("Specify the folder with Toolbox Update files")
    global ToolboxUpdFold
    ToolboxUpdFold = input()

def ToolboxPartsFolderChoose():
    FilenamesArray = []
    print("Specify the folder with new Toolbox parts")
    global ToolboxNewPartsFold
    ToolboxNewPartsFold = input()
    
    for file in os.listdir(ToolboxNewPartsFold):
        FileSuffix = os.path.splitext(os.path.join(ToolboxNewPartsFold, file))[-1].lower()
        if FileSuffix == (".sldprt"):
            print(os.path.join(ToolboxNewPartsFold, file))
            FilenamesArray.append(1)
        else:
            FilenamesArray.append(0)
    if 1 in FilenamesArray:
        print ('OK')
    else:
        print ('No new Toolbox parts were found, select another folder')
        return ToolboxPartsFolderChoose()
    
#Function execution

SldwrksFolderChoose()
ToolboxFolderChoose()
SQLScriptFolderChoose()
ToolboxUpdateFolderChoose()
ToolboxPartsFolderChoose()

#Change attributes of Toolbox folder

#FILE_ATTRIBUTE_NORMAL = 0x80
#ChngAttribToolboxfld = ctypes.windll.kernel32.SetFileAttributesW
#ChngAttribToolboxfld.argtypes = ctypes.wintypes.LPWSTR, ctypes.wintypes.DWORD
#ChngAttribToolboxfld.restype = ctypes.wintypes.BOOL

#RET=ChngAttribToolboxfld(ToolboxFold,FILE_ATTRIBUTE_NORMAL)

#if RET:
    #print('Attribute of Toolbox folder set to normal')
#else:
    #print('Attribute of Toolbox folder has been changed early')

#Make folder and copy Toolbox .sldprt file to new folder in Toolbox

if not os.path.exists(ToolboxFold+'\Browser\GOST\Bolt sets'):
    os.makedirs(ToolboxFold+'\Browser\GOST\Bolt sets')
    print("Folder for Bolts sets created")
else:
    print("Folder for Bolts sets already created")
if not os.path.exists(ToolboxFold+'\Browser\GOST\Bolt sets\BS_SET_32484_3.sldprt'):
    shutil.copy(ToolboxNewPartsFold+'\BS_SET_32484_3.sldprt',ToolboxFold+'\Browser\GOST\Bolt sets')
    print("BS_SET_32484_3 created")
else:
    print("BS_SET_32484_3 already created")

#Make backup of swbrowser.sldedb
TimeStampBackup = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
SwbrowserFoldNew = ToolboxFold + '\lang\English\oldswbrowser_'+TimeStampBackup+'.sldedb'
shutil.copy2(SwbrowserFold, SwbrowserFoldNew)
print("Backup of swbrowser is created")
#Delete updates folder, ToolboxFiles.index, ToolboxStandards.xml

if os.path.exists(ToolboxFold+r'\Updates'):
    shutil.rmtree(ToolboxFold+r'\Updates', ignore_errors=True)
    print("Update folder is deleted")
else:
    print("Update folder is already deleted")

if os.path.exists(ToolboxFold+'\ToolboxStandards.xml'):
    os.remove(ToolboxFold+'\ToolboxStandards.xml')
    print("ToolboxStandards.xml is deleted")
else:
    print("ToolboxStandards.xml is already deleted") 

if os.path.exists(ToolboxFold+'\Browser\ToolboxFiles.index'):
    os.remove(ToolboxFold+'\Browser\ToolboxFiles.index')
    print("ToolboxFiles.index is deleted")
else:
    print("ToolboxFiles.index is already deleted") 





#########################################################################################################################################################################
###############################################################SQLITE####################################################################################################
#########################################################################################################################################################################

print("Execute script in process")
SQLScriptTablesFileName = SQLScriptFold + '\\SQL CREATE TABLE 32484_3.sql'
SQLScriptRowsFileName =  SQLScriptFold + '\\SQL INSERT ROWS 32484_3.sql'
ToolboxBaseFolder = ToolboxFold + '\\lang\\English\\swbrowser.sldedb'

SQLScriptTables = open(SQLScriptTablesFileName, 'r').read()  #'r' - open for read this file
SQLScriptRows = open(SQLScriptRowsFileName, 'r').read()
ConnBase = sqlite3.connect(ToolboxBaseFolder)
CursorBase = ConnBase.cursor()
CursorBase.executescript(SQLScriptTables)
CursorBase.executescript(SQLScriptRows)
ConnBase.commit()
CursorBase.close()
ConnBase.close() 
print("Execute script = OK")  

#########################################################################################################################################################################
###############################################################SLDTOOLBOXUPDATER#########################################################################################
#########################################################################################################################################################################


print("Execute update in process")
SLDTLBUPDArg =SLDWrksFold + '\\sldtoolboxupdater.exe ' + '"' + ToolboxFold +'" ' + '"' + ToolboxUpdFold + '"'
result = subprocess.run(SLDTLBUPDArg,stdout=subprocess.PIPE)
print("Execute update = OK")

input('Press ENTER to exit')








