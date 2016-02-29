delayqueue
==
Synchronized delay queue class.

The sole content of this package is a thread-safe 
`DelayQueue` class, which is designed to be as lightweight
as possible. Only the core functionality of the delay queue
itself is included so that custom functionality can be
built around it.

The design closely resembles the built-in Python 
[Queue](https://docs.python.org/2.7/library/queue.html) 
([queue](https://docs.python.org/3.5/library/queue.html) in Python 3)
without some non-critical features that can be added if needed
in client code and features marked as likely to be deprecated.

Usage
--
    from delayqueue import DelayQueue
    import time

    queue = DelayQueue()
    queue.put('eggs', delay=30)
    print(queue.ask())
    # 29.999
    try:
        item = queue.get()
    except NotReady:
        print('not ready')
        # 'not ready'
        time.sleep(30)
    except Empty:
        print('empty')
        # no output: queue is not empty, so  this isn't executed
    else:
        print(item)
        # no output: never made it to this block
    # try again after sleeping
    try:
        item = queue.get()
    except NotReady:
        print('not ready')
        # no output: queue is now ready after sleeping
        time.sleep(30)
    except Empty:
        print('empty')
        # no output: queue is not empty, so  this isn't executed
    else:
        print(item)
        # 'eggs'
