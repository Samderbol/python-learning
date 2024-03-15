import json
import socket
import time
from io import BytesIO
from selectors import DefaultSelector
from selectors import EVENT_READ
from selectors import EVENT_WRITE
from urllib.parse import urlparse


class IOResponse:
    def __init__(self, recv):
        self.__headers__ = recv.split(b'\r\n\r\n')[0].decode('utf-8').split('\r\n')
        self.__body__ = recv.split(b'\r\n\r\n')[1]

    @property
    def http_version(self):
        return float(self.__headers__[0].split(' ', 2)[0].split('/')[-1])

    @property
    def status_code(self):
        return int(self.__headers__[0].split(' ', 2)[1])

    @property
    def reason_phrase(self):
        return self.__headers__[0].split(' ', 2)[-1]

    @property
    def headers(self):
        _headers = {}
        for _item in self.__headers__[1:]:
            _key, _value = _item.split(': ')
            _headers[_key] = _value
        return _headers

    @property
    def content(self):
        return self.__body__

    @property
    def text(self):
        return self.__body__.decode('utf-8')

    @property
    def json(self):
        return json.loads(self.text)


class IORequests:
    selector = DefaultSelector()

    tasks = {
        "unfinished": 0
    }

    def __init__(self, url, callback=None):
        self.tasks["unfinished"] += 1

        self.callback = callback if callable(callback) else None

        url = urlparse(url)

        self.netloc = url.netloc
        self.path = url.path or "/"
        self.client = socket.socket()
        self.client.setblocking(False)
        self.buffer = BytesIO()

    def connect(self):
        if ":" not in self.netloc:
            host, port = self.netloc, 80
        else:
            host, port = self.netloc.split(':')
        try:
            self.client.connect((host, int(port)))
        except BlockingIOError:
            pass

    def get(self):
        self.connect()

        self.selector.register(self.client.fileno(), EVENT_WRITE, self.send_get)

    def post(self):
        self.connect()

        self.selector.register(self.client.fileno(), EVENT_WRITE, self.send_post)

    def send_get(self, key):
        payload = (f"GET {self.path} HTTP/1.1\r\n"
                   f"Host: {self.netloc}\r\n"
                   "Connection: close\r\n\r\n")
        self.selector.unregister(key.fd)
        self.client.send(payload.encode("utf-8"))

        self.selector.register(self.client.fileno(), EVENT_READ, self.recv)

    def send_post(self, key):
        payload = (f"POST {self.path} HTTP/1.1\r\n"
                   f"Host: {self.netloc}\r\n"
                   "Connection: close\r\n\r\n")
        self.selector.unregister(key.fd)
        self.client.send(payload.encode("utf-8"))

        self.selector.register(self.client.fileno(), EVENT_READ, self.recv)

    def recv(self, key):
        data = self.client.recv(2048)
        if data:
            self.buffer.write(data)
        else:
            self.selector.unregister(key.fd)
            self.client.close()
            all_data = self.buffer.getvalue()
            response = IOResponse(all_data)
            if self.callback:
                self.callback(response)
            self.tasks["unfinished"] -= 1

    @classmethod
    def run_until_complete(cls):
        while cls.tasks["unfinished"]:
            selector = cls.selector.select()
            for key, mask in selector:
                _callback = key.data
                _callback(key)


if __name__ == "__main__":
    class CallBack:
        def __init__(self):
            self.count = 0

        def handle(self, response: IOResponse):
            if response.status_code == 200:
                self.count += 1
                print(f"第 {self.count} 次请求: {response.status_code}")


    handle = CallBack()

    start = time.perf_counter()
    for _ in range(500):
        IORequests(url="http://zyyo.net/", callback=handle.handle).get()
    IORequests.run_until_complete()
    end = time.perf_counter()
    print(f"耗时: {end - start}")

