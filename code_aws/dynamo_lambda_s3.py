import csv
import re
import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import math
import datetime

name_dic = {'西村 喬行':'NishimuraTakayuki', '坂井 伸弥':'SakaiShinnya', '木村 康之':'KimuraYasuyuki', '荻野 潤':'OginoJun', '多田 裕介':'TadaYusuke', '髙橋 新太郎':'TakahashiShintaro', '井上 恵介':'InoueKeisuke',
'渡邉 聰':'WatanabeSatoshi', '有藤 雅子':'AritoMasako', '細江 康':'HosoeYasushi', '福冨 彩花':'FukutomiSayaka', '鴇田 和士':'TokitaKazushi', '迫田 岳志':'SakodaGakushi', '白井 東州男':'ShiraiToshio'}
row_name = ['日時', 'スタッフコード', '姓名', '所属グループ名', 'スタッフ種別', '総労働時間', 'プロジェクトコード','プロジェクト名', 'タスクコード', 'タスク名', '工数']

name = '西村 喬行'
csv_name = 'manhour_20200820.csv'

value_dictlist = []

def __init__():
    dynamoDB = boto3.resource('dynamodb')
    table= dynamoDB.Table('jobcan')
    s3 = boto3.client('s3')
    s3_res =boto3.resource('s3')
    return dynamoDB, table, s3, s3_res
    
def return_name():
    return name, name_dic
    
def change_name(person):
    name = person
    return name
    
def get_csv(s3):
    bucket_name = 'sophia-jobcan'
    response = s3.get_object(Bucket=bucket_name, Key=csv_name)
    body = response['Body'].read().decode().splitlines()
    return body
    
def dynamo_put(dynamoDB, table, body):
    name_count = 0
    
    for i, b in enumerate(body): 
        value = re.sub('"', '', b).split(',')
        
        if i == 0:
            pass
        elif value[2] == name:
            table.put_item(Item = {'No' : 1000000 + name_count, '姓名' : value[2], row_name[0] : value[0], row_name[1] : value[1], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
            name_count += 1
        else:
            table.put_item(Item = {'No' : i, '姓名' : value[2], row_name[0] : value[0], row_name[1] : value[1], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
            
    return name_count

def lambda_serch(table, name_count):
    time_list = []
    temp_dict = {}
    
    for i in range(name_count):
        response = table.query(KeyConditionExpression=Key('No').eq(int(1000000 + i)))
        time_list.append(datetime.datetime.strptime(response['Items'][0]['総労働時間'], '%H:%M'))
        value_dictlist.append(response['Items'][0])
  
    hour, minute = calc(time_list)
    
    temp_dict['計'] = str(name_count) + '回'
    temp_dict['合計'] = str(hour) + ':' + str(minute)
    
    value_dictlist.append(temp_dict)

def upload_s3(s3):
    bucket = 'sophia-jobcan-output'    
    key = 'lambdajobcan_' + name_dic[name] + '.json'
    
    obj = s3.Bucket(bucket).Object(key)
    obj.put(Body=json.dumps(value_dictlist, indent=2, ensure_ascii=False, default=default_decimal_proc))
    
def calc(time_list):
    hour = 0
    minute = 0
    for i in time_list:
        hour += i.hour
        minute += i.minute
        
    if minute >= 60:
        hour += hour + math.floor(minute/60)
        minute = minute % 60
        
    return hour, minute
    
def default_decimal_proc(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
    
    return count, name_count
    
def lambda_handler(event, context):
    

    if name == 'ALL':
        for value in name_dic.keys():
            change_name(value)
            dynamoDB, table, s3, s3_res= __init__()
            body = get_csv(s3)
            name_count = dynamo_put(dynamoDB, table, body)
            lambda_serch(table, name_count)
            upload_s3(s3_res) 
    else:
        dynamoDB, table, s3, s3_res= __init__()
        body = get_csv(s3)
        name_count = dynamo_put(dynamoDB, table, body)
        lambda_serch(table, name_count)
        upload_s3(s3_res)      