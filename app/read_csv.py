'''
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***' * 8)
      print(row)

if __name__ == '__main__':
  read_csv('./app/data.csv')
'''

'''
# creamos un array con el nombre de las columnas
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header)

if __name__ == '__main__':
  read_csv('./app/data.csv')
'''


'''


import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print('****' * 3)
  print(data[5])
'''

import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {Key:value for Key, value in iterable}
      data.append(country_dict)
    return data
     
  
if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])
  
