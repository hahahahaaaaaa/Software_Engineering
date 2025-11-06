
import paho.mqtt.client as mqtt

from ..config.config import HOST, PORT,publish_topic
from queue import Queue
import datetime
import threading
from threading import Thread, Event
import threading
from queue import Queue
import paho.mqtt.client as mqtt
import time
from abc import abstractmethod


class Client:#基类
    def __init__(self, userName=None,userPwd=None):
        self.userName = userName
        self.userPwd = userPwd
        self.lock = threading.Lock()

        self.loopNum = 0
        self.start_evt = None  # 这是一个Event对象，用来查看是否验证成功
        # 自动在初始化的时候进行链接
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(HOST, PORT, 60)


    def start_loop(self):
        # 用线程锁来控制同时仅能一个loop_forever
        if self.loopNum == 0:
            self.lock.acquire()
            print('进程锁加载')
            self.loopNum = 1
            self.client._thread_terminate = False
            self.client.loop_forever()

    def stop_loop(self):
        # 停止这个线程
        if self.loopNum == 1:
            self.lock.release()
            print('进程锁结束!!')
            self.client._thread_terminate = True
            self.loopNum = 0

    @abstractmethod
    def on_connect(self, client, userdata, flags, rc):
        pass

    @abstractmethod
    def on_message(self, client, userdata,  msg):
        pass
    def clientStart(self):#启动进程，使用threading（python自带进程管理库）进行管理
        loopThread = threading.Thread(target=self.start_loop)
        loopThread.start()
        return loopThread



class Register(Client):
    def __init__(self,userName,userPwd):
        super().__init__(userName,userPwd)
        self.flag=False #标志注册是否成功
        self.clientStart()
        self.publishRegister()


    def on_connect(self, client, userdata, flags, rc):#链接
        if rc == 0:
            print("Connected successfully")
            returnRegister=self.userName+"register"
            client.subscribe(returnRegister) # 订阅 return 主题
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self,client, userdata,  msg):#接受数据
        # 规定传入数据均为dict的形式

        data = eval(msg.payload.decode('utf-8'))
        #读取数据
        code=data.get('code')
        message=data.get('message')
        if code==0:
            print(message)
        if code==1:
            self.flag=True #成功了更新
            print(message)
        return data

    def publishRegister(self):
        returnTopic=self.userName+"register"
        #数据发送特定格式
        data = {'userName': self.userName, 'userPwd': self.userPwd, 'returnTopic': returnTopic}
        # qos1
        self.client.publish(publish_topic["register_topic"], str(data).encode(), 1)
        # client.loop()
        print('发布信息 ', publish_topic['register_topic'], ' 成功')

class Login(Client):
    def __init__(self,userName,userPwd):
        super().__init__(userName,userPwd)
        self.flag=False
        self.clientStart()
        self.publishLogin()

    def on_connect(self, client, userdata, flags, rc):#链接
        if rc == 0:
            print("Connected successfully")
            returnLogin=self.userName+"login"
            client.subscribe(returnLogin) # 订阅 return 主题
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self,client, userdata,  msg):#接受数据
        # 规定传入数据均为dict的形式

        data = eval(msg.payload.decode('utf-8'))
        #读取数据
        code=data.get('code')
        message=data.get('message')
        if code==0:  #表示登入失败
            print(message)
        if code==1:  #表示登入成功
            self.flag=True
            print(message)
        return data

    def publishLogin(self):
        returnTopic=self.userName+"login"
        #数据发送特定格式
        data = {'userName': self.userName, 'userPwd': self.userPwd, 'returnTopic': returnTopic}
        # qos1
        self.client.publish(publish_topic["login_topic"], str(data).encode(), 1)
        # client.loop()
        print('发布信息 ', publish_topic['login_topic'], ' 成功')

class GetMessage(Client):
    def __init__(self, userName):
        super().__init__(userName=userName)
        self.messages=[]
        self.clientStart()
        self.publishGetAllMessage()

    def on_connect(self, client, userdata, flags, rc):  # 链接
        if rc == 0:
            print("Connected successfully")
            returnLogin = self.userName + "chatall"
            client.subscribe(returnLogin)  # 订阅 chatall 主题
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):  # 接受数据
        # 规定传入数据均为dict的形式

        messages = eval(msg.payload.decode('utf-8'))
        # 读取数据
        self.messages=messages #返回一个字典的列表，['id':id,'senderID':senderID,'message':message]存到类中
        print(messages)


    def publishGetAllMessage(self):
        returnTopic = self.userName + "chatall"
        # 数据发送特定格式
        data = {'userName': self.userName, 'returnTopic': returnTopic}
        # qos1
        self.client.publish("chatall", str(data).encode(), 1)
        # client.loop()
        print('发布信息 ', "chatall", ' 成功')

class SendMessage(Client):
    def __init__(self, userName, msg):
        super().__init__(userName=userName)
        self.message=msg
        self.clientStart()
        self.publishSendMessage()

    def on_connect(self, client, userdata, flags, rc):  # 链接
        if rc == 0:
            print("Connected successfully")
            returnLogin = self.userName + "chatsend"
            client.subscribe(returnLogin)  # 订阅 chatall 主题
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):  # 接受数据
        # 规定传入数据均为dict的形式

        data = eval(msg.payload.decode('utf-8'))
        # 读取数据
        code = data.get('code')
        message = data.get('message')
        if code == 0:  # 表示发送消息失败
            print(message)
        if code == 1:  # 表示发送消息成功
            print(message)
        return data



    def publishSendMessage(self):
        returnTopic = self.userName + "chatsend"
        # 数据发送特定格式
        data = {'userName': self.userName,'message':self.message, 'returnTopic': returnTopic}
        # qos1
        self.client.publish("chatsend", str(data).encode(), 1)
        # client.loop()
        print('发布信息 ', "chatsend", ' 成功')

class Like(Client):
    def __init__(self,messageId):
        super().__init__()
        self.clientStart()
        self.publish_like(messageId)

    @abstractmethod
    def on_connect(self, client, userdata, flags, rc):
        pass

    @abstractmethod
    def on_message(self, client, userdata, msg):
        pass

    def publish_like(client, messageId):
        data = {'message_id': messageId}
        client.publish(publish_topic['like_topic'], str(data).encode(), 1)
        print(f'发布信息到 {publish_topic["like_topic"]} 成功')


class SecurityQuestion(Client):
    def __init__(self, userName, question=None, answer=None, new_password=None):
        super().__init__(userName)
        self.question = question
        self.answer = answer
        self.clientStart()
        self.rightQuestion=None
        self.request_security_question()
        time.sleep(1)
        self.flag=False
        if userName and question and answer and new_password:
            self.reset_password(answer,new_password)
        elif userName and question and answer:
            self.set_security_question()
        else:
            self.request_security_question()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("连接成功")
            returnTopic = self.userName + "security"
            client.subscribe(returnTopic)
        else:
            print("连接失败，返回码 %d\n", rc)

    def on_message(self, client, userdata, msg):
        data = eval(msg.payload.decode('utf-8'))
        print(data)
        if data.get('action') == 'set_question':
            print(data.get('code'))
        elif data.get('action') == 'request_question':
            self.rightQuestion=data.get('question')
            print(f"Security Question: {data.get('question')}")
        elif data.get('action') == 'verify_security_answer':
           if data.get('code')==1:
               self.flag=True
               print(f"密保验证成功,密码重制成功")
           else:
               print(f"密保验证失败")
        return data

    def set_security_question(self):
        returnTopic = self.userName + "security"
        data = {
            'action': 'set_question',
            'userName': self.userName,
            'question': self.question,
            'answer': self.answer,
            'returnTopic': returnTopic
        }
        self.client.publish('set_security_question', str(data).encode(), 1)
        print(f'发布信息到 set_security_question_response 成功')

    def request_security_question(self):
        returnTopic = self.userName + "security"
        data = {
            'action': 'request_question',
            'userName': self.userName,
            'returnTopic': returnTopic
        }
        self.client.publish('request_security_question', str(data).encode(), 1)
        print(f'发布信息到 request_security_question 成功')

    def reset_password(self, answer, new_password):
        if self.rightQuestion!=self.question:
            print("密保问题错误")
            return
        returnTopic = self.userName + "security"
        data = {
            'action': 'reset_password',
            'userName': self.userName,
            'answer': answer,
            'newPassword': new_password,
            'returnTopic': returnTopic
        }
        self.client.publish('verify_security_answer', str(data).encode(), 1)
        print(f'发布信息到 verify_security_answer 成功')


def main():
    pass



main()





