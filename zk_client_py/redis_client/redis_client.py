#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import deque
import os
import random
import threading

import uuid
import redis
import time

SOCKET_TIMEOUT = 20  # sec
SOCKET_CONNECT_TIMEOUT = 20.0  # sec
MONITOR_STEP = 30  # sec
host = "127.0.0.1"
port = 6379


class RedisMemTest:

    @classmethod
    def create(cls):
        return cls()

    def __init__(self, host, port):
        self.__redis_client = redis.StrictRedis(host=host,
                                                port=port,
                                                socket_timeout=SOCKET_TIMEOUT,
                                                socket_connect_timeout=SOCKET_CONNECT_TIMEOUT,
                                                socket_keepalive=True)
        self.__host = host
        self.__port = port
        self.__stop = False

        self.__queue = deque()

    def run(self):
        t = self.spawn(self.delete_worker)
        while not self.__stop:
            key = str(uuid.uuid4())
            for i in xrange(0, 10):
                try:
                    val = self.random_str()
                    self.__redis_client.hset(key, i, val)
                    if i == 0:
                        self.__redis_client.expire(key, 360)
                except BaseException, e:
                    if len(e.args) > 0:
                        print "exception:" + e.args[0]
                    else:
                        self.__queue.append(key)
                        self.__stop = True
                        print "join"
                        t.join()
                        return

            self.__queue.append(key)

        t.join()

    @staticmethod
    def random_str():
        length = random.randint(1, 4194304)
        suffix = ""
        if length % 2 != 0:
            suffix = "="

        length /= 2
        return ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(length))) + suffix

    @staticmethod
    def spawn(func, *args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    def delete_worker(self):
        while True:
            time.sleep(1)
            try:
                key = self.__queue.popleft()
                self.__redis_client.delete(key)
            except IndexError:
                time.sleep(1)
                if self.__stop:
                    break

            '''
            while True:
                try:
                    key = self.__queue.popleft()
                    self.__redis_client.delete(key)
                except IndexError:
                    break
            '''

    def stop(self):
        self.__stop = True


if __name__ == "__main__":
    redisMem = RedisMemTest(host, port)
    redisMem.run()
