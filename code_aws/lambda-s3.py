import boto3
import csv
import re

   
def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    
    bucket_name = 'sophia-jobcan'
    file_name = 'manhour_20200820.csv'
    
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    body = response['Body'].read().decode().splitlines()
    #reader = csv.DictReader(body, csv_header, dialect='excel-tab', quoting=csv.QUOTE_ALL, )
    #datas = [row for row in reader]
    #body = body.split(',')
    #print(body)
    myfunc01_handler(body, '西村 喬行')
    

def myfunc01_handler(body, name):
    dynamoDB = boto3.resource('dynamodb')
    table= dynamoDB.Table('jobcan')
    
    row_name = ['日時', 'スタッフコード', '姓名', '所属グループ名', 'スタッフ種別', '総労働時間', 'プロジェクトコード','プロジェクト名', 'タスクコード', 'タスク名', '工数']
    count = 0
    name_count = 0
    
    for i, b in enumerate(body): 
        value = re.sub('"', '', b).split(',')
        print(value)
        
        if i == 0:
            pass
        else:
            table.put_item(Item = {'No' : i, row_name[0] : value[0], row_name[1] : value[1], row_name[2] : value[2], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
        
        if value[2] == name:
            table.put_item(Item = {'No' : 1000000 + name_count, row_name[0] : value[0], row_name[1] : value[1], row_name[2] : value[2], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
            name_count += 1
        else:
            pass
        count += 1
        
    print(count)
    print(name_count)
    
    return count, name_count 