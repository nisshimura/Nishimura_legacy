from typing import OrderedDict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, messages,
)
import os
import csv
import re
import boto3
import json
import io
import pandas as pd



class VanillaAws():
    def __init__(self):
        self.list_bucket_name = ['vanilla2021']
        self.list_csv_name = ['2021FCvanilla_menbers.csv','vanilla_camp_2021102.csv','vanilla_uniform_2021.csv']

    def build(self,bucket_num=0):
        s3 = boto3.resource('s3',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='ap-northeast-1')
        self.bucket  = s3.Bucket(self.list_bucket_name[bucket_num])

    def get_csv(self,csv_name):
        body = self.bucket.Object(csv_name).get()['Body'].read().decode("utf-8-sig").replace('\r\n','\n')
        return body
    
    def get_command(self,json_name):
        body = self.bucket.Object(json_name).get()['Body'].read().decode("utf-8-sig")
        body_dic = json.loads(body)
        return body_dic
    
    def put_csv(self,key,df):
        try:
            df_csv = df.to_csv(header=False)
            self.bucket.Object(key).put(Body=df_csv.encode('utf-8-sig'))
            return True
        except:
            return False

    def edit_csv(self,csv_name,target):
        body = self.get_csv(csv_name)
        print(body)
        df = pd.read_csv(io.StringIO(body),lineterminator='\n',header=None).set_index(0)
        print(df)
        df.at[target,1] = 'ok'
        print(df)
        return df

        

class VanillaBot(VanillaAws):
    def __init__(self):
        super().__init__()
        self.command_dic = {}
        self.command_list = []
        self.teikei_list = ['\n以上の方の納入が確認できてません。不明点等ありましたら@西村喬行までご連絡ください。','対象者はいません。','変更が完了しました','変更できませんでした']

    def is_Command(self,message):
        command = [i for i in self.command_list if i in message]
        if len(command) == 0:
            return False,False
        return True,command[0]

    def get_text(self,message):
        output_text = ''
        
        if message=='!help':
            for i in self.command_list:
                if i == len(self.command_list):
                    output_text += i
                else:
                    output_text += i + ','
        else:
            body = self.get_csv(self.command_dic[message]).splitlines()
            body_list = [i.split(',') for i in body]
            crimer_list = [i[0] for i in body_list if not 'ok' in i]

            if len(crimer_list) == 0:
                output_text = self.teikei_list[1]
            else:
                for i in crimer_list:
                    output_text += '＠'+str(i)
                output_text += self.teikei_list[0]
         
        return output_text

    
app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "uKk92Nlb5RUocKteeyCFrtJzZAcrR8YxSkWae09O//Ha7ulSkgsAe/WePNMpp9REnpGpfyOSx7oc0uK9tYuwgVCnEAEgQtNNkcH0X2sgSukMscvw/wkZ5oGM9AmGcEMGmfaq/YKjBYeokq2WRsgC1wdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "4ac56d7b16290617d58a7f96c910a108"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

work = VanillaBot()
work.build()
command_dic = work.get_command("command.json")
work.command_list = command_dic.keys()
work.command_dic = command_dic

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = event.message.text
    iscommand,target = work.is_Command(reply)
    if iscommand:
        if reply in work.command_list:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=work.get_text(reply)))
        else:
            df = work.edit_csv(work.command_dic[target],reply.replace(target+'　',''))
            if work.put_csv(work.command_dic[target],df):
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=work.teikei_list[2]))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=work.teikei_list[3]))


    else:
        pass

    # group_id = event.source.groupId
    # member_ids_res = line_bot_api.get_group_member_ids(group_id)
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)