---
title: Python_asyncio
date: '2025-03-18T05:33:00.000Z'
lastmod: '2025-03-20T06:47:00.000Z'
draft: false
tags:
- Python
categories:
- 后端
---

> 💡 最近读代码的时候，发现出现很多async异步编程的用法，打算学习一下。

---

# 1. Understanding Asyncio

asyncio模块提供了使用协程构建并发应用的工具。它使用一种单线程单进程的的方式实现并发，应用的各个部分彼此合作, 可以显示的切换任务，一般会在程序阻塞I/O操作的时候发生上下文切换如等待读写文件,或者请求网络。同时asyncio也支持调度代码在将来的某个特定事件运行，从而支持一个协程等待另一个协程完成，以处理系统信号和识别其他一些事件。

---

- Event Loop事件循环：中央执行设备由asyncio，它管理和分配不同任务的执行。负责处理事件和调度异步例程。
- Coroutines协程：用async def 声明的异步函数。这些函数可以在await点暂停和恢复，从而允许I/O操作在后台运行。
- Futures：表示尚未完成的工作结果的对象。它们是由事件循环调度的任务返回的。
- Tasks：由事件循环包装到Future对象中的计划协程，从而允许其执行。
---

# 2. 同步服务器

需要熟记以下内容，本次学习基本都依赖于此代码。

```python
"""
Author: Pan Binghong
Date: 2023-03-18
Description: socket base code
"""
import socket

def run_server(host='127.0.0.1',port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    print(f"服务器启动成功，正在监听 {host}:{port}")
    while 1:
        client_sock, addr = sock.accept()
        print("连接来自", addr)
        handle_client(client_sock)


def handle_client(sock):
    while 1:
        received_data = sock.recv(4096)
        if not received_data:
            break
        sock.sendall(received_data)
        
    print("客户端断开连接", sock.getpeername())
    sock.close()
    
if __name__ == '__main__':
    run_server()
```

## 原作者提供的测试代码

运行后输出内容如下：

```python
[17.015000] 客户端 0 正在尝试连接。
        [17.015000] 客户端 1 正在尝试连接。
                [17.015000] 客户端 2 正在尝试连接。
[17.015000] 客户端 0 已连接。
[17.515000] 客户端 0 发送消息 "你好"。
[17.515000] 客户端 0 收到响应 "你好"。
[18.031000] 客户端 0 发送消息 "世界！"。
[18.031000] 客户端 0 收到响应 "世界！"。
[18.031000] 客户端 0 断开连接。
        [18.031000] 客户端 1 已连接。
        [18.546000] 客户端 1 发送消息 "你好"。
        [18.546000] 客户端 1 收到响应 "你好"。
        [19.062000] 客户端 1 发送消息 "世界！"。
        [19.062000] 客户端 1 收到响应 "世界！"。
        [19.062000] 客户端 1 断开连接。
                [19.062000] 客户端 2 已连接。
                [19.562000] 客户端 2 发送消息 "你好"。
                [19.562000] 客户端 2 收到响应 "你好"。
                [20.078000] 客户端 2 发送消息 "世界！"。
                [20.078000] 客户端 2 收到响应 "世界！"。
                [20.078000] 客户端 2 断开连接。
```

可以发现处理三个客户端的请求，一共用时约3秒。

---

# 3. OS threads  操作系统线程

引入并发最简单的方法是使用OS线程。只需要在单独的线程中运行handle_client函数即可。

```python
import socket
import threading

def run_server(host="127.0.0.1", port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host,port))
    sock.listen()
    while 1:
        client_sock, addr = sock.accept()
        thread = threading.Thread(target=handle_client,args=[client_sock])
        thread.start()

def handle_client(sock):
    while 1:
        received_data = sock.recv(4096)
        if not received_data:
            break
        sock.sendall(received_data)
        
    print("客户端断开连接", sock.getpeername())
    sock.close()
        
if __name__ == '__main__':
    run_server()
```

运行测试程序后：

```python
[0.000000] 客户端 0 正在尝试连接。
        [0.000977] 客户端 1 正在尝试连接。
                [0.000977] 客户端 2 正在尝试连接。
[0.001977] 客户端 0 已连接。
        [0.001977] 客户端 1 已连接。
                [0.001977] 客户端 2 已连接。
[0.515324] 客户端 0 发送消息 "你好"。
        [0.517047] 客户端 1 发送消息 "你好"。
                [0.517047] 客户端 2 发送消息 "你好"。
[0.517047] 客户端 0 收到响应 "你好"。
        [0.517047] 客户端 1 收到响应 "你好"。
                [0.517047] 客户端 2 收到响应 "你好"。
[1.018273] 客户端 0 发送消息 "世界！"。
        [1.018686] 客户端 1 发送消息 "世界！"。
                [1.018686] 客户端 2 发送消息 "世界！"。
[1.019693] 客户端 0 收到响应 "世界！"。
[1.019693] 客户端 0 断开连接。
        [1.019693] 客户端 1 收到响应 "世界！"。
        [1.019693] 客户端 1 断开连接。
                [1.019693] 客户端 2 收到响应 "世界！"。
                [1.019693] 客户端 2 断开连接。
```

可以发现该服务可以同时处理不同客户端。但是使用该方式无法支持高并发。因为系统线程会消耗大量内存，能同时运行的数量有限。并且服务器使用该方法很容易遭受DoS攻击。

### ThreadPool 线程池

增加了限制，不会崩溃。线程池版本的服务器既简单又实用，但要防止单个客户端长时间占用某个线程。

```python
"""
Author: Pan Binghong
Date: 2023-03-18
Description: socket base code
"""
import socket
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=10)

def run_server(host='127.0.0.1',port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 这里是SOL_SOCKET而不是S0L_SOCKET(数字0)
    sock.bind((host, port))
    sock.listen()
    print(f"服务器启动成功，正在监听 {host}:{port}")
    while 1:
        client_sock, addr = sock.accept()
        print("连接来自", addr)
        handle_client(client_sock)


def handle_client(sock):
    while 1:
        received_data = sock.recv(4096)
        if not received_data:
            break
        sock.sendall(received_data)
        
    print("客户端断开连接", sock.getpeername())
    sock.close()
    
```

---

# 4. I/O多路复用于事件循环

我们再来看一下顺序服务器，会发现它总是在等待某个事件发生，没有连接时，它等待新的客户端连接，有连接后，又等待客户端发送数据。为了实现并发，应该让服务器有能力处理不同事件，如果当前连接的客户端没有发送数据，就可以处理新的连接请求，这样就能同时保持多个连接，回复任意连接发送的数据。

怎么让服务器知道下一个要处理的是什么事件呢？默认情况下，socket 的 accept()、recv()、sendall() 等方法都是阻塞的，调用 accept() 时，会保持阻塞状态，直到新的客户端接入，并不能同时调用其它客户端 socket 的 recv() 方法。不过，我们可以对阻塞方法设置超时，sock.settimeout(timeout)，或将 socket 设置为非阻塞模式，sock.setblocking(False)，然后同时保持多个 socket 连接，并在一个无限循环中调用每个 socket 对应的事件方法。对于还在监听新连接的 socket，就调用 accept()，对于等待客户端数据的 socket，就调用 recv()。

这个方法的问题在于，轮询时间很难准确配置。如果所有 socket 都设置为非阻塞模式，或超时时间设置得太短，服务器就会一直执行调用，消耗大量 CPU，如果超时时间设置得太长，又会导致响应很慢。

一个更好的选择是询问操作系统哪个 socket 已经就绪。显然，操作系统是掌握这个信息的，新数据包到达网络接口后，会通知操作系统，操作系统随即将其解码并唤醒正在等待读取该 socket 的进程。对于处理进程来说，除了等待读取该 socket，还可以通过 I/O 多路复用机制告诉操作系统，它准备读或写哪些 socket，如 select()、poll() 或 epoll() 等，当某个 socket 可读或可写时，操作系统也会唤醒该进程。

Python selectors 标准库封装了不同的 I/O 多路复用机制，暴露的高层接口称为选择器（selector）。其中，SelectSelector 对应 select() 机制，EpollSelector 对应 epoll() 机制，而 DefaultSelector 对应当前操作系统支持的效率最高的机制。

```python
import socket
import selectors

sel = selectors.DefaultSelector()

def setup_listening_socket(host="127.0.0.1", port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    sel.register(sock, selectors.EVENT_READ, accept)
    
def accept(sock):
    client_sock, addr = sock.accept()
    sel.register(client_sock, selectors.EVENT_READ, recv_and_send)
    
def recv_and_send(sock):
    recvied_data = sock.recv(4096)
    if recvied_data:
        sock.sendall(recvied_data)
    else:
        print('Client disconnected', sock.getpeername())
        sel.unregister(sock)
        sock.close()

def run_event_loop():
    while True:
        for key, _ in sel.select():
            callback = key.data
            sock = key.fileobj
            callback(sock)
            
if __name__ == '__main__':
    setup_listening_socket()
    run_event_loop()
```

先给监听的 socket 注册一个 accept() 回调，接受新连接请求并对每个客户端 socket 注册一个 recv_and_send() 回调。程序的核心逻辑是一个事件循环——迭代处理就绪 socket，调用对应回调的无限循环。

事件循环版本的服务器可以正常处理多个客户端连接。与多线程版本相比，主要问题在于代码的组织方式比较奇怪，是围绕着回调实现的。上面的代码看着还好，是因为有些逻辑的处理并不严谨，比如，写 socket 的逻辑也可能在写队列满时被阻塞，我们现应该检查 socket 是否可写，然后再调用 sock.sendall() 方法，也就是说，recv_and_send() 函数需要一分为二，其中一个再次注册为回调。如果服务器逻辑复杂一些，而不是直接返回客户端数据的话，代码实现会更麻烦。

使用系统线程时，我们可以在非回调模式下实现并发。为什么呢？关键在于操作系统有挂起和恢复线程执行的能力。如果我们写的函数也可以像系统线程一样挂起和恢复，就可以实现单线程并发了。Python 是支持这类函数的。

```python
[0.000000] 客户端 0 正在尝试连接。
        [0.000000] 客户端 1 正在尝试连接。
                [0.000000] 客户端 2 正在尝试连接。
[0.000000] 客户端 0 已连接。
                [0.000000] 客户端 2 已连接。
        [0.000000] 客户端 1 已连接。
[0.505349] 客户端 0 发送消息 "你好"。
                [0.505349] 客户端 2 发送消息 "你好"。
        [0.506347] 客户端 1 发送消息 "你好"。
[0.506347] 客户端 0 收到响应 "你好"。
                [0.506347] 客户端 2 收到响应 "你好"。
        [0.506347] 客户端 1 收到响应 "你好"。
[1.019953] 客户端 0 发送消息 "世界！"。
                [1.021975] 客户端 2 发送消息 "世界！"。
        [1.022971] 客户端 1 发送消息 "世界！"。
[1.023989] 客户端 0 收到响应 "世界！"。
[1.023989] 客户端 0 断开连接。
                [1.024965] 客户端 2 收到响应 "世界！"。
                [1.024965] 客户端 2 断开连接。
        [1.024965] 客户端 1 收到响应 "世界！"。
        [1.024965] 客户端 1 断开连接。
```

# 5. 生成器函数与生成器

生成函数是指代码中有yield表达式的函数，例如：

```python
(base) PS C:\Users\24529> python -q
>>> def fx():
...     yield 1
...     yield 2
...
>>> a = fx()
>>> next(a)
1
>>> next(a)
2
```

Python引入生成器的最初目的是作为迭代器的代替。Python中，可以迭代处理（比如在for循环中）的对象称为可迭代对象，可迭代对象实现了__iter__()  特殊方法，返回一个迭代器。而迭代器实现__next__()  方法，每次调用时返回下一个值，用户可以通过next() 函数获得该value。

```python
>>> def fx():
...     yield 1
...     yield 2
...
>>> for i in fx():
...     i
...
1
2
>>>
```

# 6. 生成器作为协程

对多任务程序，可以在每个任务对应的函数中按需插入 yield 表达式，将其转为生成器，再轮流运行这些生成器：以固定顺序循环调用 next() 函数，直到生成器停止。

```python
import socket
import selectors
from collections import deque

class EventLoopNoIO:
    """不带IO的事件循环实现"""
    def __init__(self) -> None:
        self.tasks_to_run = deque([])  # 存储待运行的任务队列
        
    def create_task(self, coro):
        """添加新任务到队列"""
        self.tasks_to_run.append(coro)
        
    def run(self):
        """运行事件循环"""
        while self.tasks_to_run:
            task = self.tasks_to_run.popleft()  # 从队列左侧取出任务
            try:
                next(task)  # 执行生成器的下一步
            except StopIteration:
                continue  # 如果生成器结束则继续下一个任务
            self.create_task(task)  # 将未完成的任务重新加入队列

class EventLoopIo:
    """带IO的事件循环实现"""
    def __init__(self):
        self.tasks_to_run = deque([])  # 存储待运行的任务队列
        self.sel = selectors.DefaultSelector()  # 创建默认的selector对象

    def create_task(self, coro):
        """添加新任务到队列"""
        self.tasks_to_run.append(coro)

    def run(self):
        """运行事件循环"""
        while True:
            if self.tasks_to_run:
                task = self.tasks_to_run.popleft()
                try:
                    op, arg = next(task)  # 执行生成器的下一步,获取操作类型和参数
                except TypeError:  # 处理生成器返回None的情况
                    self.create_task(task)
                    continue
                except StopIteration:
                    continue

                if op == 'wait_read':  # 注册读事件
                    self.sel.register(arg, selectors.EVENT_READ, task)
                elif op == 'wait_write':  # 注册写事件
                    self.sel.register(arg, selectors.EVENT_WRITE, task)
                else:
                    raise ValueError('Unknown event loop operation:', op)
            else:
                for key, _ in self.sel.select():  # 等待IO事件
                    task = key.data  # 获取关联的任务
                    sock = key.fileobj  # 获取关联的socket对象
                    self.sel.unregister(sock)  # 取消注册
                    self.create_task(task)  # 将任务重新加入队列

loop = EventLoopIo()  # 创建事件循环实例

def run_server(host='127.0.0.1', port=55555):
    """服务器主函数"""
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
        yield 'wait_read', sock  # 等待新的客户端连接
        client_sock, addr = sock.accept()
        print("连接自", addr)
        loop.create_task(handle_client(client_sock))  # 创建客户端处理任务
    
def handle_client(sock):
    """处理客户端连接"""
    try:
        while True:
            yield 'wait_read', sock  # 等待接收数据
            try:
                received_data = sock.recv(4096)
                if not received_data:  # 如果没有收到数据,说明客户端断开连接
                    break
                yield 'wait_write', sock  # 等待发送数据
                sock.sendall(received_data)  # 发送回显数据
            except socket.error as e:
                print(f"处理数据时发生错误: {e}")
                break
    except Exception as e:
        print(f"处理客户端连接时发生错误: {e}")
    finally:
        try:
            print('连接断开', sock.getpeername())
        except:
            print('连接断开')
        try:
            sock.close()
        except:
            pass


if __name__ == '__main__':
    loop.create_task(run_server())  # 创建服务器任务
    loop.run()  # 运行事件循环
```

```python
[0.000000] 客户端 0 正在尝试连接。
        [0.000983] 客户端 1 正在尝试连接。
                [0.000983] 客户端 2 正在尝试连接。
[0.000983] 客户端 0 已连接。
        [0.000983] 客户端 1 已连接。
                [0.002020] 客户端 2 已连接。
[0.502793] 客户端 0 发送消息 "你好"。
        [0.502793] 客户端 1 发送消息 "你好"。
                [0.502793] 客户端 2 发送消息 "你好"。
[0.502793] 客户端 0 收到响应 "你好"。
        [0.502793] 客户端 1 收到响应 "你好"。
                [0.502793] 客户端 2 收到响应 "你好"。
[1.003601] 客户端 0 发送消息 "世界！"。
        [1.004872] 客户端 1 发送消息 "世界！"。
                [1.004872] 客户端 2 发送消息 "世界！"。
[1.004872] 客户端 0 收到响应 "世界！"。
[1.005868] 客户端 0 断开连接。
        [1.005868] 客户端 1 收到响应 "世界！"。
        [1.005868] 客户端 1 断开连接。
                [1.005868] 客户端 2 收到响应 "世界！"。
                [1.005868] 客户端 2 断开连接。
```

以上内容为采用了生成器实现并发的结果，手动创建了事件循环代码，除此之外，在Python中，还可以使用asyncio。

> 在多任务中使用的生成器，称为协程。

---

# 7. 协程| asyncio 

一般异步方法被称之为协程(Coroutine)。asyncio事件循环可以通过多种不同的方法启动一个协程。一般对于入口函数，最简答的方法就是使用run_until_complete(),并将协程直接传入这个方法。

---

### 协程获取返回值

```python
import asyncio

async def foo():
    print("这是一个协程")
    return "返回值"

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coro = foo()
        print('进入事件循环')
        # 报错原因:
        # 1. 在Jupyter notebook中,每个cell都运行在同一个事件循环中
        # 2. 第一次运行时事件循环已经启动
        result = loop.run_until_complete(coro)
        print(f"协程返回值: {result}")
        print('事件循环结束')
    finally:
        loop.close()
```

```plain text
开始运行协程
进入事件循环
这是一个协程
协程返回值: 返回值
事件循环结束
```

run_until_complete()可以获取协程的返回值，如果没有设定返回值，则返回None。

---

### 协程调用协程

```python
import asyncio

async def main():
    print("这是主协程")
    print("等待result1协程运行")
    res1 = await result1()
    print("等待result2协程运行")
    res2 = await result2(res1)
    return res1, res2


async def result1():
    print("这是result1协程")
    return "result1"

async def result2(arg):
    print("这是result2协程")
    return f"result2 with {arg}"

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f"主协程返回值: {result}")
    finally:
        loop.close()
```

```python
这是主协程
等待result1协程运行
这是result1协程
等待result2协程运行
这是result2协程
主协程返回值: ('result1', 'result2 with result1')
```

---

### 协程中调用普通函数

- loop.call_soon()
---

- loop.call_later()
---

- call_at()
---

# 8. Future

Futures：表示尚未完成的工作结果的对象。它们是由事件循环调度的任务返回的。 

## Future的状态

---

---

```python
import asyncio

def foo(future : asyncio.Future, result :str):
    print("此时future的状态:{}".format(future))
    print("设置future的结果:{}".format(result))
    future.set_result(result)
    print("此时futuure的状态:{}".format(future))
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.call_soon(foo, all_done, "Future is done!")
        print("进入Event Loop")
        result = loop.run_until_complete(all_done)
        print("最终返回结果: {}".format(result))
    finally:
        loop.close()
    print("获取future的结果结束", all_done.result())
```

输出结果：

```python
进入Event Loop
此时future的状态:<Future pending cb=[_run_until_complete_cb() at E:\Anaconda\envs\llm-api\Lib\asyncio
\base_events.py:181]>
设置future的结果:Future is done!
此时futuure的状态:<Future finished result='Future is done!'>
最终返回结果: Future is done!
获取future的结果结束 Future is done!
```

调用future.set_result()的前后状态变化：pending → finished 。

---

## Future对象中使用await

future和协程一样可以使用await关键字获取其结果。

```python
import asyncio

def foo(future : asyncio.Future, result : str) -> None:
    print("此时future的状态:{}".format(future))
    future.set_result(result)
    
async def main(loop):
    all_done = asyncio.Future()
    print("调用函数获取future结果")
    loop.call_soon(foo, all_done, "the result")    
    
    result = await all_done
    print("最终返回结果: {}".format(result))
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
```

输出结果：

```python
调用函数获取future结果
此时future的状态:<Future pending cb=[Task.task_wakeup()]>
最终返回结果: the result
```

---

## Future调用回调函数

```python
import asyncio
import functools

def callback(future : asyncio.Future, n : str) -> None:
    """
    回调函数,当Future完成时会被调用
    Args:
        future: 已完成的Future对象
        n: 回调函数的标识符
    """
    print('{} : future is done : {}'.format(n, future.result()))


async def register_callbacks(all_done : asyncio.Future) -> None:
    """
    注册多个回调函数到Future对象
    使用functools.partial()固定回调函数的部分参数
    Args:
        all_done: 要注册回调的Future对象
    """
    print("注册callback到future对象")
    # 注册第一个回调,标识符为1
    all_done.add_done_callback(functools.partial(callback, n = 1))
    # 注册第二个回调,标识符为2
    all_done.add_done_callback(functools.partial(callback, n = 2))

async def main(all_done : asyncio.Future) -> None:
    """
    主协程函数
    Args:
        all_done: Future对象
    """
    # 等待注册回调完成
    await register_callbacks(all_done)
    print('设置future的结果')
    # 设置Future的结果,这将触发回调函数的执行
    all_done.set_result('the result')

if __name__ == '__main__':
    # 获取事件循环
    loop = asyncio.get_event_loop()
    try:
        # 创建Future对象
        all_done = asyncio.Future()
        # 运行主协程直到完成
        loop.run_until_complete(main(all_done))
    finally:
        # 关闭事件循环
        loop.close()
```

```python
注册callback到future对象
设置future的结果
1 : future is done : the result
2 : future is done : the result
```

通过add_done_callback方法给funtrue任务添加回调函数，当funture执行完成的时候,就会调用回调函数。并通过参数future获取协程执行的结果。

---

# 10. 任务| Task

任务（Task）是与事件循环交互的主要途径之一。任务可以包装协程，可以跟踪协程何时完成。任务是Future的子类，所以使用方法和future一样。协程可以等待任务，每个任务都有一个结果，在它完成之后可以获取这个结果。

因为协程是没有状态的，我们通过使用create_task方法可以将协程包装成有状态的任务。还可以在任务运行的过程中取消任务。

```python
import asyncio

async def child():
    print("进入子协程")
    return "the result"

async def main(loop):
    print("将child协程包装成任务")
    task = loop.create_task(child())
    print("通过cancel方法可以取消任务")
    # task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("取消任务抛出CancelledError异常")
    else:
        print("获取任务的结果".format(task.result()))    

if __name__ == '__main__':  
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
```

## 组合协程

对于多协程的场景，如果还使用await 方法调用，会出现一个协程等待多个协程的场面。此时需要引入wait或gather解决。

- wait 
- gather
- as_complete 
---

> Reference















