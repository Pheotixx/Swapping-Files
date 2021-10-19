#Mam I am not able to understand how to switch the data even after researching on google. Apologies on my end for not being able to complete the project. 

import os
import shutil


source = input("enter source folder name:- ")
destination = input('enter destination folder name:- ')

source = source + '/'
destination = destination + '/'


list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination)
