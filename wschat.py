# coding=utf-8
import HuobiService
import sys
from flask import Flask
import itchat
from receiveOld import getEmails

app = Flask(__name__)
reload(sys)
sys.setdefaultencoding('utf-8')
@app.route('/')
def hello_world():
    #code = getEmails();
    #print("您转让点卡的验证码为："+code);
    HuobiService.login();
    #print(HuobiService.send_ponter_transfer_order(123456,'usdt', '18525424152', "123", "123", 10))
    return "hello"
if __name__ == '__main__':
     app.run()





# list = [];
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     list.append(msg.fromUserName)
#     print(HuobiService.get_depth('btcusdt', 'step0'))
#     print(list)
#     return '请输入购买数量.最小需要大于10。\n'\
#           + '当前可交易数量:32049, 价格:0.231。\n' \
#           +'(不懂点卡的朋友请看下我的朋友圈有详细介绍,如需大量请联系微信hust868）\n'\
#           +'如需终止请输入:ZZ\n' \
#           +'当前点卡收购单价:0.229,最高收购量:9250.\n' \
#           +'点UID:33875833账号:a472706330@163.com\n' \
#           +'出售点卡的朋友请直接发起交易，我们会在您发起交易后1分钟内接受您的订单(需要购买或者出售0~K点卡的请加微信hust868)';
#
# itchat.auto_login()
#
# itchat.run()
