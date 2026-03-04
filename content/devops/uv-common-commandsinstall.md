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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSD5XMCT%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7qyVmxNePRKeRZVbuk93TItogCzoDxciVXYEuKtnuLAiAGJ1v0%2FB%2Fctp0EWkbRdguYVAsvBP9SEkF%2BXXqTm%2F0KTCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjiwI%2Bm%2B1onQxyQT8KtwDWB%2FNGWitwMEaX69mxNIRyeq13Epq%2FcpPCtcMbTP8iUxg9lpLB2X3uuemiXIX4xfZpbnDrXfdnCkQhclaxxeTeijKKc8Kj9Tok7tyvdplTiX9eqqK9kGjhfuIujcIqgPz7Wg%2FKyXqb8VeR11lEcvaL6ZC3yY2b0P6PCDLTtGsZf1aapp2hzv3VS5O%2BdcRBOP8P8LNfnRRxArLKc%2BfzVKaebA8RavRNR3canA5VXh%2FFxLiDcxUKGdXNee03KBe9CUiXjiOG2NXXYzu3MkNBKKnxU4B6vN0tQkBt1LHdLCjxv8Dg2AuyZCfkpr%2FaRmRXIh7h1xvvfdKnajD%2FJyTKgRHdapak68u%2F0HHgFdLYkRuwaBo6BbyocslPJRoboRIreP8OveuwPA49NlsYoZsK%2BNnA2aH83y6Cxl53Bl5bAwqfBMXuVmkZrX8rRtvSxsQYGNaWCp0HeUxMejjJpT%2FvLZgIPfGYNghfdT4gySZZAr8k6eEkjbUDVHY8Qnsk5plJId8kPmODg71x130ZcglkDz32JNOD%2B8rQcIG5aZgZKassVwF626AWTHpJ7PZnoko167Jvr9lW39OUV%2Bw3zerZy17LIu3cSfp3urc0LVjhpemZTkkH776cMNta0xYsJMw6ZmezQY6pgEnJ6t8HoA3400C6Q0H4EvJE9eeo7wVu%2BHhD423dEiVscC%2BM0QiJSZb3HD8p%2Fs5X6%2FmagLJBz%2FbfRQlYrP0cFD2wYlmjjxUnTBISppZK09Lw%2BB42jw2DGCpKrNYYxJdhODxYcDX55Zue3r7J9TZ027uDjZVvghJy%2BwQHhfeaYOxy2Ztki4PSYeSSMmcgkekCbMauXmE4TaF3F4q0xRWVTd5SXmKeBVa&X-Amz-Signature=f78c46dfe35f0c23a0980b3070979f186488409b5c66368b0b30b31b03717e01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSD5XMCT%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7qyVmxNePRKeRZVbuk93TItogCzoDxciVXYEuKtnuLAiAGJ1v0%2FB%2Fctp0EWkbRdguYVAsvBP9SEkF%2BXXqTm%2F0KTCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjiwI%2Bm%2B1onQxyQT8KtwDWB%2FNGWitwMEaX69mxNIRyeq13Epq%2FcpPCtcMbTP8iUxg9lpLB2X3uuemiXIX4xfZpbnDrXfdnCkQhclaxxeTeijKKc8Kj9Tok7tyvdplTiX9eqqK9kGjhfuIujcIqgPz7Wg%2FKyXqb8VeR11lEcvaL6ZC3yY2b0P6PCDLTtGsZf1aapp2hzv3VS5O%2BdcRBOP8P8LNfnRRxArLKc%2BfzVKaebA8RavRNR3canA5VXh%2FFxLiDcxUKGdXNee03KBe9CUiXjiOG2NXXYzu3MkNBKKnxU4B6vN0tQkBt1LHdLCjxv8Dg2AuyZCfkpr%2FaRmRXIh7h1xvvfdKnajD%2FJyTKgRHdapak68u%2F0HHgFdLYkRuwaBo6BbyocslPJRoboRIreP8OveuwPA49NlsYoZsK%2BNnA2aH83y6Cxl53Bl5bAwqfBMXuVmkZrX8rRtvSxsQYGNaWCp0HeUxMejjJpT%2FvLZgIPfGYNghfdT4gySZZAr8k6eEkjbUDVHY8Qnsk5plJId8kPmODg71x130ZcglkDz32JNOD%2B8rQcIG5aZgZKassVwF626AWTHpJ7PZnoko167Jvr9lW39OUV%2Bw3zerZy17LIu3cSfp3urc0LVjhpemZTkkH776cMNta0xYsJMw6ZmezQY6pgEnJ6t8HoA3400C6Q0H4EvJE9eeo7wVu%2BHhD423dEiVscC%2BM0QiJSZb3HD8p%2Fs5X6%2FmagLJBz%2FbfRQlYrP0cFD2wYlmjjxUnTBISppZK09Lw%2BB42jw2DGCpKrNYYxJdhODxYcDX55Zue3r7J9TZ027uDjZVvghJy%2BwQHhfeaYOxy2Ztki4PSYeSSMmcgkekCbMauXmE4TaF3F4q0xRWVTd5SXmKeBVa&X-Amz-Signature=a2ab648f1afbc8aa66870270a34094669f718bcd847ba3ca130c43a9257785ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSD5XMCT%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7qyVmxNePRKeRZVbuk93TItogCzoDxciVXYEuKtnuLAiAGJ1v0%2FB%2Fctp0EWkbRdguYVAsvBP9SEkF%2BXXqTm%2F0KTCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjiwI%2Bm%2B1onQxyQT8KtwDWB%2FNGWitwMEaX69mxNIRyeq13Epq%2FcpPCtcMbTP8iUxg9lpLB2X3uuemiXIX4xfZpbnDrXfdnCkQhclaxxeTeijKKc8Kj9Tok7tyvdplTiX9eqqK9kGjhfuIujcIqgPz7Wg%2FKyXqb8VeR11lEcvaL6ZC3yY2b0P6PCDLTtGsZf1aapp2hzv3VS5O%2BdcRBOP8P8LNfnRRxArLKc%2BfzVKaebA8RavRNR3canA5VXh%2FFxLiDcxUKGdXNee03KBe9CUiXjiOG2NXXYzu3MkNBKKnxU4B6vN0tQkBt1LHdLCjxv8Dg2AuyZCfkpr%2FaRmRXIh7h1xvvfdKnajD%2FJyTKgRHdapak68u%2F0HHgFdLYkRuwaBo6BbyocslPJRoboRIreP8OveuwPA49NlsYoZsK%2BNnA2aH83y6Cxl53Bl5bAwqfBMXuVmkZrX8rRtvSxsQYGNaWCp0HeUxMejjJpT%2FvLZgIPfGYNghfdT4gySZZAr8k6eEkjbUDVHY8Qnsk5plJId8kPmODg71x130ZcglkDz32JNOD%2B8rQcIG5aZgZKassVwF626AWTHpJ7PZnoko167Jvr9lW39OUV%2Bw3zerZy17LIu3cSfp3urc0LVjhpemZTkkH776cMNta0xYsJMw6ZmezQY6pgEnJ6t8HoA3400C6Q0H4EvJE9eeo7wVu%2BHhD423dEiVscC%2BM0QiJSZb3HD8p%2Fs5X6%2FmagLJBz%2FbfRQlYrP0cFD2wYlmjjxUnTBISppZK09Lw%2BB42jw2DGCpKrNYYxJdhODxYcDX55Zue3r7J9TZ027uDjZVvghJy%2BwQHhfeaYOxy2Ztki4PSYeSSMmcgkekCbMauXmE4TaF3F4q0xRWVTd5SXmKeBVa&X-Amz-Signature=9ed8f4c688ccec0c46880618df088fac2492e40a9c45ed4d9fc346bedd3fcd0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

