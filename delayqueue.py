"""
.. Copyright (c) 2016 Marshall Farrier
   license http://opensource.org/licenses/MIT

Synchronized delay queue.

Notes
-----
`DelayQueue` dispenses with the block and timeout
features available in the `queue` library. Otherwise,
`DelayQueue` is built in a similar manner to `queue.PriorityQueue`.

The client can track retries by wrapping each item
with a parameter that counts retries:

    >>> queue.put([n_retries, item])
"""

import datetime as dt
from heapq import heappop, heappush 
import threading

class Empty(Exception):
    # raised by `get()` if queue is empty
    pass

class NotReady(Exception):
    # raised by `get()` if queue is not empty, but delay for head
    # of queue has not yet expired
    pass

class Full(Exception):
    # raised by `put()` if queue is full 
    pass

class DelayQueue(object):

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self.queue = []
        self.mutex = threading.Lock()
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)
        self.ready = threading.Condition(self.mutex)

    def ask(self):
        """
        Return the wait time in seconds required to retrieve the
        item currently at the head of the queue.
        
        Note that there is no guarantee that a call to `get()` will
        succeed even if `ask()` returns 0. By the time the calling
        thread reacts, other threads may have caused a different
        item to be at the head of the queue.
        """
        with self.mutex:
            if not len(self.queue): 
                raise Empty
            utcnow = dt.datetime.utcnow()
            if self.queue[0][0] <= utcnow:
                self.ready.notify()
                return 0
            return (self.queue[0][0] - utcnow).total_seconds()

    def put(self, item, delay=0):
        if delay < 0:
            raise ValueError("'delay' must be a non-negative number")
        with self.not_full:
            if len(self.queue) >= self.maxsize > 0:
                raise Full
            heappush(self.queue, (dt.datetime.utcnow() + dt.timedelta(seconds=delay), item))
            self.not_empty.notify()
            if not delay:
                self.ready.notify()

    def get(self):
        with self.ready:
            if not len(self.queue): 
                raise Empty
            utcnow = dt.datetime.utcnow()
            if utcnow < self.queue[0][0]:
                raise NotReady
            item = heappop(self.queue)[1]
            self.not_full.notify()
            return item

    def qsize(self):
        """
        Return the approximate size of the queue.

        The answer will not be reliable, as producers and consumers
        can change the queue size before the result can be used.
        """
        with self.mutex:
            return len(self.queue)

