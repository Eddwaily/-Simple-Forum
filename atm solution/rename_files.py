import os

file_list = os.listdir(r"e:/myPrank")
saved_path = os.getcwd()
os.chdir(r"e:/myPrank")
for file_name in file_list :
    os.rename( file_name, file_name.translate( None, "0123456789"))
os.chdir(saved_path)
print file_list
