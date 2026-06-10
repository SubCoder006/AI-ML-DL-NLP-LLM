
# even = lambda num : num % 2 == 0
# print(even(2))
# print(even(3))

# add = lambda x,y,z : x+y+z
# # print(add(5,7,4))

# nums = [1,2,3,4,5,6]
# print(list(map(lambda x:x*x, nums)))

# details = [{'name':"John", 'age':25}, {'name':"Jane", 'age':30}, {'name':"Doe", 'age':22}]
# print(list(map(lambda p: p['name'],details)))

# lst = [1,2,4,7,8,9,11,12,14,16,17,21,26]
# print(list(filter(lambda x: x%2 == 0,lst)))

# people = [{'name':"John", 'age':25}, {'name':"Jane", 'age':30}, {'name':"Doe", 'age':22}]
# print(list(filter(lambda p:p['age'] > 22,people )))

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# from package import Maths as M
# print(M.add(1,2,3,4))

# import array
# arr = array.array('i'  ,[1,2,3])
# print(arr)

# import csv
# with open('data.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name','Age','City'])
#     writer.writerow(['John',25,'New York'])
#     writer.writerow(['Rahul',20,'Kolkata'])
    
# with open ('data.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
        
# import datetime as dt
# now = dt.datetime.now()
# print(now)
# yesterday = now - dt.timedelta(days=1)
# print(yesterday)

# import time as t
# print(t.time())
# t.sleep(3)
# print(t.time())

# with open('Module/src.txt','r') as file:
#     for line in file:
#         print(line.strip())
        
with open('newbin.bin','wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')
        
with open('newbin.bin','rb') as file:
    data = file.read()
    print(data)

