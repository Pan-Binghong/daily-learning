---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RSWUF5Z%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBx0P2VToZ%2Bph89YpkTgyEJOm%2FS4EUZMuWwfmvCbidKeAiBtD%2BLSKcw8fDg9vIhs6y5kbuwEepDclJtZnGmC1N7eiyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGixQ%2Bx0%2F1irN7JvGKtwDKjBusSfkpMTQRNJlUzC5Jag2%2BFbX5g04DLttpYHktvLOlYxLEFAjm4thNfySR4W%2FlQ8vCrQSJyNhb%2FCCmYLEiA0UYBx66O35eSsMgVaAs40GeSXzXA%2BkCQcRbK1rDOT1rX0ImEaBnOsB%2BS8SJbTAXnwv6ySt4GVuC1qLKmYwAcQyT7MeyH3lAoQpEWyqJxdhDe7slssBh%2BC4L84qN%2BUH3ezC1GhL6JJ3fgCpJNYxhYx5UItNPU%2BAO6cPETJXwRv62Qk92qL63ePJ07uamMXB0QK24pysV9ozyBPZdkccXWDYFdX0Emoo%2BUs%2FqqIyztMe7PnAqxUz4YUv7fjTtQHamAxb0eeTeu7Hs5HwjvfKdpODz2oObROBUBloMczKOxxhNrh9blEdLdKTvcH2SBEdAzv0ncpvCnbtfY7cPO7K32%2F7u9JYGYc5jIo9ZqhH6MocZkb9G8vohzehkc0WLQDw7okY7a9OG0KU4Nup7xDnkJ0N62DiN5mVmShsB7NkQQgdxsBH4u4X%2BXS0w%2BGzKNxB69%2B53qB6B2vwbgCP%2FfzlguQX1xwQxMOgTTdSxRvGU8Nln7kET0VFGdaZiph%2FbkKNTm%2FdVhfAPO6UVoxhxWbrLW5FnrFdAScMIJL0PRswkfOvyAY6pgE14GUHmDK2VWnig%2FBe%2FtrHTocsK%2F7NqY%2Bao4A9XYDL80xkt0WLFjRIUZdQ0heuvb6jcazqC%2FPSiIundXBEJkQ%2B1c0eKpguyG5EzIMr9fhjP5qIx1sGJAXsEMypc3ikbeXJIkFN5XYuRQKUEy%2BA%2BIHNMOstZgHbpsglMa%2FIu1g064Ue8BTh%2B%2FAraMMFvlLVruYcYx1PBB5OIgTw9AFbe5kEY1K7rcUX&X-Amz-Signature=c9411a2c3e34b9fcf8bd68caf3c8904d9c77bd818a33e2d6a7d8c6a2f4f61c73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RSWUF5Z%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBx0P2VToZ%2Bph89YpkTgyEJOm%2FS4EUZMuWwfmvCbidKeAiBtD%2BLSKcw8fDg9vIhs6y5kbuwEepDclJtZnGmC1N7eiyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGixQ%2Bx0%2F1irN7JvGKtwDKjBusSfkpMTQRNJlUzC5Jag2%2BFbX5g04DLttpYHktvLOlYxLEFAjm4thNfySR4W%2FlQ8vCrQSJyNhb%2FCCmYLEiA0UYBx66O35eSsMgVaAs40GeSXzXA%2BkCQcRbK1rDOT1rX0ImEaBnOsB%2BS8SJbTAXnwv6ySt4GVuC1qLKmYwAcQyT7MeyH3lAoQpEWyqJxdhDe7slssBh%2BC4L84qN%2BUH3ezC1GhL6JJ3fgCpJNYxhYx5UItNPU%2BAO6cPETJXwRv62Qk92qL63ePJ07uamMXB0QK24pysV9ozyBPZdkccXWDYFdX0Emoo%2BUs%2FqqIyztMe7PnAqxUz4YUv7fjTtQHamAxb0eeTeu7Hs5HwjvfKdpODz2oObROBUBloMczKOxxhNrh9blEdLdKTvcH2SBEdAzv0ncpvCnbtfY7cPO7K32%2F7u9JYGYc5jIo9ZqhH6MocZkb9G8vohzehkc0WLQDw7okY7a9OG0KU4Nup7xDnkJ0N62DiN5mVmShsB7NkQQgdxsBH4u4X%2BXS0w%2BGzKNxB69%2B53qB6B2vwbgCP%2FfzlguQX1xwQxMOgTTdSxRvGU8Nln7kET0VFGdaZiph%2FbkKNTm%2FdVhfAPO6UVoxhxWbrLW5FnrFdAScMIJL0PRswkfOvyAY6pgE14GUHmDK2VWnig%2FBe%2FtrHTocsK%2F7NqY%2Bao4A9XYDL80xkt0WLFjRIUZdQ0heuvb6jcazqC%2FPSiIundXBEJkQ%2B1c0eKpguyG5EzIMr9fhjP5qIx1sGJAXsEMypc3ikbeXJIkFN5XYuRQKUEy%2BA%2BIHNMOstZgHbpsglMa%2FIu1g064Ue8BTh%2B%2FAraMMFvlLVruYcYx1PBB5OIgTw9AFbe5kEY1K7rcUX&X-Amz-Signature=84c8f042ca4d5140a642b931cdbb9bb27f4726cf07b6c76792e3bdadf94fba80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









