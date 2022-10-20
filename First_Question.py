import collections
import os
File_Name = 'sample.csv' #File_Name please use full path
Delimeter = ',' #Delimeter
File_is_There = os.path.exists(File_Name)
if not File_is_There : # File is not there
        print('_'*80)
        print("ERROR : FILE NOT FOUND")
        print('_'*80)
        exit()
File_Desc=open(File_Name) #Open File
File_Data = File_Desc.readlines()#Read File
Column_Repeations = {} 
Duplicates = [] 
File_Length = 0 
File_Size = os.path.getsize(File_Name) #get file size
if len(File_Data) and File_Size: #file have valid size
        for line in File_Data:
                File_Length += 1
                line = line.strip().split(Delimeter) #stored file data as line by line splited
                if len(line) == 1: # File have empty data
                        print('_'*80)
                        print(f'ERROR : Delimeter is not Found,For this {File_Length} line in File Data')
                        print('_'*80)
                        continue
                Eater_Id = line[0]
                if len(Eater_Id) == 0 and (Eater_Id == ''): #Eater id is empty
                        print('_'*80)
                        print(f'ERROR : Eater_ID is not Found, for this {File_Length} line in File')
                        print('_'*80)
                        continue
                Food_Id =line[1:]
                if len(Food_Id) == 1 and (Food_Id[0] == ''): #Food_ID is empty
                        print('_'*80)
                        print(f'ERROR : Food_Id is not Found, for this {File_Length} line in File')
                        print('_'*80)
                        continue 
                Duplicates += ([(item,Eater_Id) for item,count in collections.Counter(Food_Id).items() if count > 1]) #store value count more than 1 time
                for _ in Food_Id:
                        if _ in Column_Repeations:
                                Column_Repeations[_] += 1 #increase count if the item occurs again
                        else:
                                Column_Repeations[_] = 1 #insert value one
        Sorted_Dict_Top_Three = {Food:count for Food,count in sorted(Column_Repeations.items(),key = lambda item : item[1],reverse = True)} #Sorted Top items by count(dict) value
        Top_Three = {_:Column_Repeations[_] for _ in list(Sorted_Dict_Top_Three)[:3]} # top 3 items 
        print('_'*50)
        print(f'TOP ITEMS')
        print('_'*50)
        for Food_ID,Count in Top_Three.items():
                print(f'Item {Food_ID} consumed {Count} times')
        else:
                print('_'*50)
        
        if len(Duplicates):
                print('_'*50)
                print('ERRORS : REPEATION EATER_ID')
                print('_'*50)
                for Items in Duplicates:
                        print(f'This Eater_Id {Items[1]} has Repeations of {Items[0]}')
else:
        print('_'*80)
        print('ERROR : INPUT FILE IS NOT A VALID FILE SIZE OR EMPTY DATA,PLEASE UPLOAD VALID FILE')
        print('_'*80)
                                                                                                                                                                                                                                                                                         
