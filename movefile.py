import os
import shutil
fromdir= 'C:/Users/Saumya Narsang/Downloads'
todir= 'C:/Users/Saumya Narsang/Downloads/test'
listoffiles= os.listdir(fromdir)
#print(listoffiles)
for i in listoffiles:
    name , ext = os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.txt','.pdf', '.doc','.docx']:
        path1=fromdir+'/'+i
        path2=todir+'/'+'files'
        path3=todir+'/'+'files'+'/'+i
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving')
            shutil.move(path1,path3)

