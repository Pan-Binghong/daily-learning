---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UADYXO2I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICE0vZGN0vd1NtXto8kkh%2BSUfPPuO1IE5XEOIMVRc7pQAiA9a3WbaXHUBVbRMwcTdBXZaxdJAjJJMXDJtYy67kDPCCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd8ahC%2BAIuf6DE%2BvsKtwD80xipWsn%2BUfNI4tDk5a8AwUHSIkzIC72hc4L3zobL7Cukfj%2FEx%2FxzSzR9OMSh0PMaQdP2OOcBEIUphDeM3%2B%2FamgBd9Pi7nBFK3dNe3CqQGF9tBOEBU%2B4MkbQnTkaahW%2BvUZxAbueT6H%2F5cGmrwOicgGFNx%2FfuVWNRqfy9tnRP6QyRYgixyvGbKtldKgWg4AYbWkRV5f6YxF%2BxxgV3DN50TROTUymIOBN71JI65Hrz4ZMFqmx3kAzu%2BgIShtnTlB5GLnW0%2BaRzhONiitgvw%2Fwd3EaA0%2BW0P9Ug0VUJVqgFsZRZGxuOeqCUY3kR59DG20ocvV1dK4rtsA%2FKMECkDrDp%2BA5BCv24D0X%2Bk78pK%2Fc%2F5yN3qU0uI5WrAbICzZ6LJPwI3CYy745pnMoS5ntTPKliM0%2BUrrHitXmTLjSs7Q2uJMIYmWXxvCu9ZM8fzPXL1nPOuE7xqmUFVvspPvAtgoNFQT1QY6T3K69%2BdY0pFyi17Wxt%2BxgMv%2F3r1kwO%2BhrNsrzl%2Bv69Js2Tq3OkHcEWy95QBOk%2B4bO3B7F2QSgMTjjhnbcWxUUNObmZ%2Fna8kMDXy%2F1RG6qbHaHpZI%2Byc0Rnsy9FYNnb4IH%2B98FcD3TWcRAZB5bGTDtH%2BYKnRN%2BasYwifKvyAY6pgGxDsCxQkhQNbIQXb%2BCTCRyd8igA%2FcFWO2ZvXx1Vr%2FyxGSps6fR0KF0hZm5PtZishPM73naBWknILRX%2BFgsKUaSqIwoajUZ2abqiPEmPu2rmWciLaZmQBgSVJZ8mU%2FOP07nMP9CFKxiO5Sdf1xU7A%2BSf%2BcIh4mB67P4nUNX69I0hA3Rb2XBuwHZz5ufQOZL%2FGtU4G0Buwom3C5npxmPMPJ%2F0MWUEdyN&X-Amz-Signature=1e792408a1c80e35b064a9760dfa5b6a9651bcb518eba7308c1e48f3d1df234d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UADYXO2I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICE0vZGN0vd1NtXto8kkh%2BSUfPPuO1IE5XEOIMVRc7pQAiA9a3WbaXHUBVbRMwcTdBXZaxdJAjJJMXDJtYy67kDPCCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd8ahC%2BAIuf6DE%2BvsKtwD80xipWsn%2BUfNI4tDk5a8AwUHSIkzIC72hc4L3zobL7Cukfj%2FEx%2FxzSzR9OMSh0PMaQdP2OOcBEIUphDeM3%2B%2FamgBd9Pi7nBFK3dNe3CqQGF9tBOEBU%2B4MkbQnTkaahW%2BvUZxAbueT6H%2F5cGmrwOicgGFNx%2FfuVWNRqfy9tnRP6QyRYgixyvGbKtldKgWg4AYbWkRV5f6YxF%2BxxgV3DN50TROTUymIOBN71JI65Hrz4ZMFqmx3kAzu%2BgIShtnTlB5GLnW0%2BaRzhONiitgvw%2Fwd3EaA0%2BW0P9Ug0VUJVqgFsZRZGxuOeqCUY3kR59DG20ocvV1dK4rtsA%2FKMECkDrDp%2BA5BCv24D0X%2Bk78pK%2Fc%2F5yN3qU0uI5WrAbICzZ6LJPwI3CYy745pnMoS5ntTPKliM0%2BUrrHitXmTLjSs7Q2uJMIYmWXxvCu9ZM8fzPXL1nPOuE7xqmUFVvspPvAtgoNFQT1QY6T3K69%2BdY0pFyi17Wxt%2BxgMv%2F3r1kwO%2BhrNsrzl%2Bv69Js2Tq3OkHcEWy95QBOk%2B4bO3B7F2QSgMTjjhnbcWxUUNObmZ%2Fna8kMDXy%2F1RG6qbHaHpZI%2Byc0Rnsy9FYNnb4IH%2B98FcD3TWcRAZB5bGTDtH%2BYKnRN%2BasYwifKvyAY6pgGxDsCxQkhQNbIQXb%2BCTCRyd8igA%2FcFWO2ZvXx1Vr%2FyxGSps6fR0KF0hZm5PtZishPM73naBWknILRX%2BFgsKUaSqIwoajUZ2abqiPEmPu2rmWciLaZmQBgSVJZ8mU%2FOP07nMP9CFKxiO5Sdf1xU7A%2BSf%2BcIh4mB67P4nUNX69I0hA3Rb2XBuwHZz5ufQOZL%2FGtU4G0Buwom3C5npxmPMPJ%2F0MWUEdyN&X-Amz-Signature=cc35aa059b2f0ee92ab31afd6fca545189a197741020a7cbb852c405910c686f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UADYXO2I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICE0vZGN0vd1NtXto8kkh%2BSUfPPuO1IE5XEOIMVRc7pQAiA9a3WbaXHUBVbRMwcTdBXZaxdJAjJJMXDJtYy67kDPCCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd8ahC%2BAIuf6DE%2BvsKtwD80xipWsn%2BUfNI4tDk5a8AwUHSIkzIC72hc4L3zobL7Cukfj%2FEx%2FxzSzR9OMSh0PMaQdP2OOcBEIUphDeM3%2B%2FamgBd9Pi7nBFK3dNe3CqQGF9tBOEBU%2B4MkbQnTkaahW%2BvUZxAbueT6H%2F5cGmrwOicgGFNx%2FfuVWNRqfy9tnRP6QyRYgixyvGbKtldKgWg4AYbWkRV5f6YxF%2BxxgV3DN50TROTUymIOBN71JI65Hrz4ZMFqmx3kAzu%2BgIShtnTlB5GLnW0%2BaRzhONiitgvw%2Fwd3EaA0%2BW0P9Ug0VUJVqgFsZRZGxuOeqCUY3kR59DG20ocvV1dK4rtsA%2FKMECkDrDp%2BA5BCv24D0X%2Bk78pK%2Fc%2F5yN3qU0uI5WrAbICzZ6LJPwI3CYy745pnMoS5ntTPKliM0%2BUrrHitXmTLjSs7Q2uJMIYmWXxvCu9ZM8fzPXL1nPOuE7xqmUFVvspPvAtgoNFQT1QY6T3K69%2BdY0pFyi17Wxt%2BxgMv%2F3r1kwO%2BhrNsrzl%2Bv69Js2Tq3OkHcEWy95QBOk%2B4bO3B7F2QSgMTjjhnbcWxUUNObmZ%2Fna8kMDXy%2F1RG6qbHaHpZI%2Byc0Rnsy9FYNnb4IH%2B98FcD3TWcRAZB5bGTDtH%2BYKnRN%2BasYwifKvyAY6pgGxDsCxQkhQNbIQXb%2BCTCRyd8igA%2FcFWO2ZvXx1Vr%2FyxGSps6fR0KF0hZm5PtZishPM73naBWknILRX%2BFgsKUaSqIwoajUZ2abqiPEmPu2rmWciLaZmQBgSVJZ8mU%2FOP07nMP9CFKxiO5Sdf1xU7A%2BSf%2BcIh4mB67P4nUNX69I0hA3Rb2XBuwHZz5ufQOZL%2FGtU4G0Buwom3C5npxmPMPJ%2F0MWUEdyN&X-Amz-Signature=ec853aa1379ce6c2300bb8239c5cbd70a984cd483c499721f75425bbe2df470a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

