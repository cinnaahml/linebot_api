from linebot import LineBotApi
from linebot.models import TextSendMessage
import netifaces as ni



import netifaces as ni
ni.ifaddresses('enp0s3')
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
print(ip)

CHANNEL_ACCESS_TOKEN = "u8IINXf77/Wtv+HwVO4n141TRW99ftv6fVCeqOtHEQ0t+ufEAP1nOo5smlJAOFz5d3w0cvSQqvFXZHkPFPVGMp6tknHXYOMCKMtJvd76cfrvHhDKN2UU9RvGsjptmK+H7tJ5/ZCtH+4HyKCY9PVxIgdB04t89/1O/w1cDnyilFU="

result01 = ("ip: "+ ip +",網路品質良好!")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(result01))