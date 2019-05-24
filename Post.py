# -*- coding: utf-8 -*-
"""
@author: Joe Thunyathep Santhanavanich (thunyathep.s@outlook.com)
"""
import requests
import csv
import time
import json

#Setting
STA_Endpoint = "<input your STA Observations URL here>" #Example: http://xxx/xxx/v1.0/Observations
#Code
datastream_id = {}
headers = {'content-type': 'application/json'}
with open('./csv_data/sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: #1-1
            # print(f'Column names are {", ".join(row)}')
            print('This is a header')
            column_count = 0
            for x in row:
                if column_count ==0:
                    print('---')
                else:
                    datastream_id[str(column_count)] = row[column_count]
                column_count += 1
        # elif line_count <= 3501: #3502-1
        else:
            Timestamp = row[0]
            column_count = 0
            for x in row:
                if column_count ==0:
                    print('-0-')
                else:
                    body = {"phenomenonTime": Timestamp,
                            "resultTime": Timestamp,
                            "result": row[column_count],
                            "Datastream": { "@iot.id": datastream_id[str(column_count)]}}
                    print("Posting body: ", body)
                    myResponse = requests.post(url = STA_Endpoint, data=json.dumps(body), headers=headers) 
                    if(myResponse.ok):
                        print(f'Posted Completed!')
                    else:
                        print('Posted Error')
                        print(myResponse.text)
                column_count += 1
        line_count += 1
    print(f'Processed {line_count} Data rows. Completed!')