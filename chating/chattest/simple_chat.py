#!coding=utf-8
from asynchat import async_chat
from asyncore import dispatcher
import socket,asyncore

PORT = 5005
NAME = 'TestChat'

class ChatSession(async_chat):
    '''
    处理一个服务器和一个用户之间连接的类
    '''
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.sever = server
        self.set_terminator("\r\n")
        self.data = []
        self.push('Welcome to %s \r\n'%self.sever.name)
    def collect_incoming_data(self, data):
        self.data.append(data)
    def found_terminator(self):
        '''
        如果发现了一个终止对象，也就意味着读入了一个完整的行，将其广播给每个人
        '''
        line = ''.join(self.data)
        data = []
        self.sever.broadcast(line)
    def handle_close(self):
        async_chat.handle_close(self)
        self.sever.disconnect(self)

class ChatServer(dispatcher):
    '''
    接受连接并且产生单个会话的类。它还会处理到其它会话的广播。
    '''
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('localhost',port))
        self.listen(5)
        self.name = name
        self.sessions = []
    def disconnect(self, session):
        self.sessions.remove(session)
    def broadcast(self,line):
        for session in self.sessions:
            session.push(line + '\r\n')
    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self,conn))
if __name__ =="__main__":
    s = ChatServer(PORT,NAME)
    try:asyncore.loop()
    except KeyboardInterrupt:print