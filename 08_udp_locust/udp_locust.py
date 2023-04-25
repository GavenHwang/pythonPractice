# -*- coding:utf-8 -*-
import socket
import time
from locust import User, task, events
from locust.env import Environment


class UDPClient(object):

    def __init__(self, host):
        self.host = host
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self, host):
        self.conn = None
        host, port = host.split(":")
        try:
            self.conn = self.client.connect((host, int(port)))
            self.client.settimeout(3)
        except Exception as e:
            print(e.__str__)
        return self.conn

    def send(self, msg):
        start_time = time.time()
        try:
            self.client.send(msg.encode("utf-8"))
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="udp", name='udp send failed', response_time=total_time,
                                        exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="udp", name='udp send succeded', response_time=total_time,
                                        response_length=0)

    def request(self, msg, b=1024):
        start_time = time.time()
        response = None
        try:
            self.client.send(msg.encode("utf-8"))
            response = self.client.recv(b).decode('utf-8')
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="udp", name='udp request', response_time=total_time,
                                        exception=e, response_length=0)
        else:
            if response != 'hi':
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="udp", name='udp request', response_time=total_time,
                                            exception=None, response_length=0)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="udp", name='udp request', response_time=total_time,
                                            exception=None, response_length=0)
        return response

    def close(self):
        self.client.close()


class UDPLocust(User):
    host = '127.0.0.1:6000'

    def __init__(self, environment):
        super(UDPLocust, self).__init__(environment)
        self.client = UDPClient(self.host)

    def on_start(self):
        self.client.connect(self.host)

    def on_stop(self):
        self.client.close()

    @task
    def udp_request(self):
        if not self.client.conn:
            self.client.connect(self.host)
        self.client.request('hello', b=1024)


if __name__ == "__main__":
    environment = Environment(locustfile="./udp_locust.py")
    udp_send = UDPLocust(environment)
    udp_send.run()
