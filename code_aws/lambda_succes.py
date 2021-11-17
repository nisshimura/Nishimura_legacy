import csv
import re
import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import math
import datetime

class lambdajobcan():
    name_dic = {'西村 喬行':'NishimuraTakayuki', '坂井 伸弥':'SakaiShinnya', '木村 康之':'KimuraYasuyuki', '荻野 潤':'OginoJun', '多田 裕介':'TadaYusuke', '髙橋 新太郎':'TakahashiShintaro', '井上 恵介':'InoueKeisuke',
    '渡邉 聰':'WatanabeSatoshi', '有藤 雅子':'AritoMasako', '細江 康':'HosoeYasushi', '福冨 彩花':'FukutomiSayaka', '鴇田 和士':'TokitaKazushi', '迫田 岳志':'SakodaGakushi', '白井 東州男':'ShiraiToshio'}
    row_name = ['日時', 'スタッフコード', '姓名', '所属グループ名', 'スタッフ種別', '総労働時間', 'プロジェクトコード','プロジェクト名', 'タスクコード', 'タスク名', '工数']
    
    name = '西村 喬行'
    bucket_name = 'sophia-jobcan'
    csv_name = 'manhour_20200820.csv'
    
    name_count = 0
    all_count = 0

    body = None
    value_dictlist = []
    
    def initial(self):
        name = self.name
        all_count = self.all_count
        name_dic = self.name_dic

        if name == 'ALL':
            name = list(name_dic.keys())[all_count]
            all_count += 1
        else:
            pass

            
        dynamoDB = boto3.resource('dynamodb')
        table= dynamoDB.Table('jobcan')
        s3 = boto3.client('s3')
        s3_res =boto3.resource('s3')
        return dynamoDB, table, s3, s3_res
    
    def get_csv(self, s3):
        response = s3.get_object(Bucket=self.bucket_name, Key=self.csv_name)
        self.body = response['Body'].read().decode().splitlines()
        
    def dynamo_put(self, dynamoDB, table):
        body = self.body
        for i, b in enumerate(body): 
            row_name = self.row_name
            value = re.sub('"', '', b).split(',')
            
            if i == 0:
                pass
            elif value[2] == self.name:
                table.put_item(Item = {'NO' : i, row_name[2] : value[2], row_name[0] : value[0], row_name[1] : value[1], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
                self.name_count += 1
            else:
                table.put_item(Item = {'NO' : i, row_name[2] : value[2], row_name[0] : value[0], row_name[1] : value[1], row_name[3] : value[3], row_name[4] : value[4], row_name[5] : value[5], row_name[6] : value[6], row_name[7] : value[7], row_name[8] : value[8], row_name[9] : value[9], row_name[10] : value[10]})
    
    def lambda_serch(self, table):
        name_count = 40
        name = self.name
        value_dictlist = self.value_dictlist
        
        time_list = []
        temp_dict = {}
        
        response = table.query(IndexName='name-index', KeyConditionExpression=Key('姓名').eq(name))
        
        for i in range(name_count):
            time_list.append(datetime.datetime.strptime(response['Items'][i]['総労働時間'], '%H:%M'))
            value_dictlist.append(response['Items'][i])
    
        hour, minute = self.calc(time_list)
        
        temp_dict['計'] = str(name_count) + '回'
        temp_dict['合計'] = str(hour) + ':' + str(minute)
        
        value_dictlist.append(temp_dict)
    
    def upload_s3(self, s3):
        value_dictlist = self.value_dictlist
        name = self.name
        name_dic = self.name_dic
        
        bucket = 'sophia-jobcan-output'    
        key = 'lambdajobcan_' + name_dic[name] + '.json'
        
        obj = s3.Bucket(bucket).Object(key)
        obj.put(Body=json.dumps(value_dictlist, indent=2, ensure_ascii=False, default=self.default_decimal_proc))
        return json.dumps(value_dictlist, indent=2, ensure_ascii=False, default=self.default_decimal_proc)
        
    def calc(self, time_list):
        hour = 0
        minute = 0
        for i in time_list:
            hour += i.hour
            minute += i.minute
            
        if minute >= 60:
            hour += math.floor(minute/60)
            minute = minute % 60
            
        return hour, minute
        
    def default_decimal_proc(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
        
def lambda_handler(event, context):
    work = lambdajobcan()
    dynamoDB, table, s3, s3_res= work.initial()
    work.get_csv(s3)
    work.dynamo_put(dynamoDB, table)
    work.lambda_serch(table)
    result = work.upload_s3(s3_res)
    return result