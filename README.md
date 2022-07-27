# linebot_api
### 環境
* Linux 系統
* Python3 可執行環境

* 基本要求:
日誌系統:
日誌 (log)
在 python 中實做日誌系統，例：
  2022-02-14 12:45 program started.
  2022-02-14 12:45 get IP address 192.168.43.95.
在 LINE BOT 中回報系統基本狀態
IP Address
  2022-02-14 12:45 program started.
  2022-02-14 12:45 get IP address 192.168.43.95.

1. LINE BOT 申請與安裝
新增一個 provider
聊天機器人分類為 Messaging API channel
Basic setting page (Basic Setting)
Basic setting page (Messaging API):
  Bot basic ID
  QR Code
產生一組 Channel access token


2. 在 Linux 安裝 LINE BOT 函式庫:
Install LINE Bot SDK:
pip3 install line-bot-sdk

3. 使用 LINE BOT 函式庫:
Broadcast :
from linebot import LineBotApi
from linebot.models import TextSendMessage
CHANNEL_ACCESS_TOKEN = ""
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text = "test"))

4. 使用 Python 抓取系統 IP Address
安裝套件:
pip3 install netifaces
程式範例:
import netifaces as ni
ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print(ip)


* LINE BOT 函式庫&抓取系統 IP Address

from linebot import LineBotApi  
from linebot.models import TextSendMessage  
import netifaces as ni  
ni.ifaddresses('enp0s3')  
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']  
print(ip)  

CHANNEL_ACCESS_TOKEN =   "u8IINXf77/Wtv+HwVO4n141TRW99ftv6fVCeqOtHEQ0t+ufEAP1nOo5smlJAOFz5d3w0cvSQqvFXZHkPFPVGMp6tknHXYOMCKMtJvd76cfrvHhDKN2UU9RvGsjptmK+H7tJ5/ZCtH+4HyKCY9PVxIgdB04t89/1O/w1cDnyilFU="  

result01 = ("ip: "+ ip +",網路品質良好!")  
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)  
line_bot_api.broadcast(TextSendMessage(result01))  
