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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MISCOQZ%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDhKHAz%2FvUCSA6nHX6uRnVwvoD%2FbztMNare7Ncb9Cp2AwIhAODW2Ng%2B5ZQmZL3%2BB5%2F%2FgeKc8lR4cByP6gm%2FjyZ3rdaEKv8DCCsQABoMNjM3NDIzMTgzODA1IgwIu6LijoI9PWpYGl8q3AMb8vT6FBoru7ZMSN53pwhnpJuHItxinl7V%2F9837X6qDJ898y91BIJI85HK63NNuOL0uM5N%2BbEwDOnl9UB2ujWdr46gr7qVZArpnB%2BAlwxE4f7skQPWKc%2B47m4UJOhjXg28cFyV%2B0%2BH26OvXWvvxBbDEa%2FwwcvvcNWLzEhn4t1VB7iuZKfFEZfsKnt%2FxIgbaZ2jIlktl2Ix%2BZyhe9Rhymo150zwcrNQlRXC0NZNB05ui%2FDhbMRQ09edoL37Am185CubOQ5KDjmW92O7fUdcpsjfRTaD4FXDVHNelubIicVaqLH4p%2FYWTcg4%2FsTzScqakNFfn2uxv8r%2Fa6PpJg8QQzIObEY5lf5aJTwnSepJGEKN8Jc9%2BCgYnPycS%2Ftf4NQiOr5q76fTH43reR4dEpLbUK5FDDerYVxlFUMHrXXjEuP0T02muGV4pthYWOncJI4UieuFljNzzrL2uCjyqhlseRmQl5uNvssHwmyPv0uHlhb%2B5ZoB4hDMS0Ex1bEJxK64AxERihWHmQaWPHNHpQ%2F%2Fvo%2FMvL4lghWMkSpF2GRFhQ7NbX%2FMijvy3dTJ5GMmnxkQkmue%2B6YA%2BzP%2B4KNlpec0ah1Dly9k8eCP%2FBuaIWKDJZyyNLLghzAG5sY4DAhkMTCvmqHLBjqkASdAfFocfCN%2FscHWiHNGdnuAXmmjSmOQ0H%2B%2BAI2eO57TEoYNUuRrvPhpP%2BF5XvtJVw5jp04AOXHdRIcl9kZmOmNcSOjs4FTeo1yw4tlRfhKxmIeTVDwlXWt%2FN5QaGxciXIN6VSCON%2FZ9x24mHmP4wYnwtWt4fUiQLwQXaydUtrXRTu6BXRYeN5CzCGAhxMHBF3j6%2FsvmwcpCGddn0rZZAJlOIxKN&X-Amz-Signature=ff488783ce94e044f7c8cafb363bc16cee768c072fdca9e0f98fd1ae3367dc50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MISCOQZ%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDhKHAz%2FvUCSA6nHX6uRnVwvoD%2FbztMNare7Ncb9Cp2AwIhAODW2Ng%2B5ZQmZL3%2BB5%2F%2FgeKc8lR4cByP6gm%2FjyZ3rdaEKv8DCCsQABoMNjM3NDIzMTgzODA1IgwIu6LijoI9PWpYGl8q3AMb8vT6FBoru7ZMSN53pwhnpJuHItxinl7V%2F9837X6qDJ898y91BIJI85HK63NNuOL0uM5N%2BbEwDOnl9UB2ujWdr46gr7qVZArpnB%2BAlwxE4f7skQPWKc%2B47m4UJOhjXg28cFyV%2B0%2BH26OvXWvvxBbDEa%2FwwcvvcNWLzEhn4t1VB7iuZKfFEZfsKnt%2FxIgbaZ2jIlktl2Ix%2BZyhe9Rhymo150zwcrNQlRXC0NZNB05ui%2FDhbMRQ09edoL37Am185CubOQ5KDjmW92O7fUdcpsjfRTaD4FXDVHNelubIicVaqLH4p%2FYWTcg4%2FsTzScqakNFfn2uxv8r%2Fa6PpJg8QQzIObEY5lf5aJTwnSepJGEKN8Jc9%2BCgYnPycS%2Ftf4NQiOr5q76fTH43reR4dEpLbUK5FDDerYVxlFUMHrXXjEuP0T02muGV4pthYWOncJI4UieuFljNzzrL2uCjyqhlseRmQl5uNvssHwmyPv0uHlhb%2B5ZoB4hDMS0Ex1bEJxK64AxERihWHmQaWPHNHpQ%2F%2Fvo%2FMvL4lghWMkSpF2GRFhQ7NbX%2FMijvy3dTJ5GMmnxkQkmue%2B6YA%2BzP%2B4KNlpec0ah1Dly9k8eCP%2FBuaIWKDJZyyNLLghzAG5sY4DAhkMTCvmqHLBjqkASdAfFocfCN%2FscHWiHNGdnuAXmmjSmOQ0H%2B%2BAI2eO57TEoYNUuRrvPhpP%2BF5XvtJVw5jp04AOXHdRIcl9kZmOmNcSOjs4FTeo1yw4tlRfhKxmIeTVDwlXWt%2FN5QaGxciXIN6VSCON%2FZ9x24mHmP4wYnwtWt4fUiQLwQXaydUtrXRTu6BXRYeN5CzCGAhxMHBF3j6%2FsvmwcpCGddn0rZZAJlOIxKN&X-Amz-Signature=49a7ad16d13335b1646e80cb94e55390038f2da4b20fa5d43f2f08777126ea26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









