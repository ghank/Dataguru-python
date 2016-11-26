from pymongo import MongoClient
from time import sleep
from datetime import datetime

conn = MongoClient('localhost')
db = conn.rxie
ips = db.app1.ips
ips.remove(None)

f = open('2014ips.txt')

index = 1
transformed = 0

#start timing
start_time = datetime.now()
print('Start Time: ', start_time)

final_list = []

#skip the first two empty lines

f.readline()
f.readline()

for line in f:
    # get each non blank line
    if line == '\n':
        continue
    ip_record = line.split()

    if len(ip_record) == 4:
        row = {'_id': index, 'srcIP': ip_record[0], \
               'destIP': ip_record[1], 'country': ip_record[2], 'carrier': ip_record[3]}
    else:
        #there are lots of records with Carrier contains multiple words, so simply split will not produce the right Carrier
        carrier = ip_record[3:]

        #get the correct carrier name by concatenating the 4th items and after
        actual_acrrier =  ''.join(carrier)
        row = {'_id': index, 'srcIP': ip_record[0], \
               'destIP': ip_record[1], 'country': ip_record[2], 'carrier': actual_acrrier}
        #print actual_acrrier
        transformed = transformed + 1

    final_list.append(row)
    index = index + 1

f.close()

#write the final_list to the database
for item in final_list:
    ips.insert_one(item)

stop_time = datetime.now()
print('Completed Time: ', stop_time)

elapsed_time = stop_time - start_time

print  " %s records transformed"%str(transformed) + '\n'
print "Total records: %s" % str(index) + '\n'
print('Total time: ', elapsed_time)
