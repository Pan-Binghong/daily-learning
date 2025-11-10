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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DCOE4AN%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQC5cPEgBFQR2nuFe29DK7QqLBCM5g6qgAFihl8NhzY8fwIhAPdno7pVjOy6nsOu%2B0sgS0Moenlmq2hKj7deAo07vvupKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ66vDsw4cnC%2FgFOgq3APClwq50xLWFF9ZfInkzuJ3qdevhIq1phfzjk7Re5EBWI5oqy1loBYVp6oJmrAxEx892iZN1Ux2bJBXRwdDEc6Nq0MVpm6K0BzxPQO77wDrSuw20SuKOm7aFNRfqXS9gmLPVuJry6kueX2JPNaW6dCaQKXVYQLvhzeaKt%2FbTdg6u9lOlAUg2VQUIl8yiJEE9QWk0Mfiz1dUCxhxUScvAiWBYG1OJUTYRz8ZteH6xD82G3U0ncllQQYod624NEVcOcNpMOMlNlydrWQE29IpQEYajHMqAlRcf7xhw%2FdhP8Px8SbLGjBHCIffxSXa%2FfudgqfW8LS%2B49dJ93H5QHYPBuvRY0zxHJl6Y7D5hJseniTCok8XBmQL7IIXyXsD6ppIAg5r3Rd1wcYyhU6U%2BjVNHeIUF9OgUkl8XUDQXw%2FfdY5FGs%2BwuUylYMSZ6JIZAQMsAq5HB1MiEKSdIhpzV%2FnLT1Gjpo0vss53SXIqRPxE3wDa%2FcenYdOIyha3B27%2FYSC7L1SxwmN4hHumQQQkwZJhZ%2Be%2BPb7Odp3HZUxKWKVumSEba0Rl41Lb97feQM6TAJpUTdkDXS%2Bp3UZ30QeBOBuZCBKZ9AuzkmsXMdaGwSwPpOYbpKdWBZx94NVQB%2FcbnTDNusTIBjqkAcRVV2wuxGNkC4WXn5wPF6JoJHW3jB4iYXHcMcfj90%2B15fr8alvsS1QLqhjygEA2pGtPs1nhRMTnp%2Bb3VgKRMXrgqqCOYKyS7AqQ69xx6Ro8j2wRE%2BQYXu8Y6OKpW%2BDmLz%2Fr3eafLhTSOfx845f51A%2FfK8l9%2F0ST1ZaEDRi7ickgyvdeZjBYdVrGOoew0okCgrj5%2FY8B%2BuvaKnQ4aMgGDoUrMGuJ&X-Amz-Signature=e90b57cb624b616915d9f2cc076889aef6f40f5793b55832ba4dc913d318d831&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DCOE4AN%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQC5cPEgBFQR2nuFe29DK7QqLBCM5g6qgAFihl8NhzY8fwIhAPdno7pVjOy6nsOu%2B0sgS0Moenlmq2hKj7deAo07vvupKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ66vDsw4cnC%2FgFOgq3APClwq50xLWFF9ZfInkzuJ3qdevhIq1phfzjk7Re5EBWI5oqy1loBYVp6oJmrAxEx892iZN1Ux2bJBXRwdDEc6Nq0MVpm6K0BzxPQO77wDrSuw20SuKOm7aFNRfqXS9gmLPVuJry6kueX2JPNaW6dCaQKXVYQLvhzeaKt%2FbTdg6u9lOlAUg2VQUIl8yiJEE9QWk0Mfiz1dUCxhxUScvAiWBYG1OJUTYRz8ZteH6xD82G3U0ncllQQYod624NEVcOcNpMOMlNlydrWQE29IpQEYajHMqAlRcf7xhw%2FdhP8Px8SbLGjBHCIffxSXa%2FfudgqfW8LS%2B49dJ93H5QHYPBuvRY0zxHJl6Y7D5hJseniTCok8XBmQL7IIXyXsD6ppIAg5r3Rd1wcYyhU6U%2BjVNHeIUF9OgUkl8XUDQXw%2FfdY5FGs%2BwuUylYMSZ6JIZAQMsAq5HB1MiEKSdIhpzV%2FnLT1Gjpo0vss53SXIqRPxE3wDa%2FcenYdOIyha3B27%2FYSC7L1SxwmN4hHumQQQkwZJhZ%2Be%2BPb7Odp3HZUxKWKVumSEba0Rl41Lb97feQM6TAJpUTdkDXS%2Bp3UZ30QeBOBuZCBKZ9AuzkmsXMdaGwSwPpOYbpKdWBZx94NVQB%2FcbnTDNusTIBjqkAcRVV2wuxGNkC4WXn5wPF6JoJHW3jB4iYXHcMcfj90%2B15fr8alvsS1QLqhjygEA2pGtPs1nhRMTnp%2Bb3VgKRMXrgqqCOYKyS7AqQ69xx6Ro8j2wRE%2BQYXu8Y6OKpW%2BDmLz%2Fr3eafLhTSOfx845f51A%2FfK8l9%2F0ST1ZaEDRi7ickgyvdeZjBYdVrGOoew0okCgrj5%2FY8B%2BuvaKnQ4aMgGDoUrMGuJ&X-Amz-Signature=70923c57ed68661963068d6022b396c8df9980c511a0b29aadd0d99579c79233&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DCOE4AN%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQC5cPEgBFQR2nuFe29DK7QqLBCM5g6qgAFihl8NhzY8fwIhAPdno7pVjOy6nsOu%2B0sgS0Moenlmq2hKj7deAo07vvupKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ66vDsw4cnC%2FgFOgq3APClwq50xLWFF9ZfInkzuJ3qdevhIq1phfzjk7Re5EBWI5oqy1loBYVp6oJmrAxEx892iZN1Ux2bJBXRwdDEc6Nq0MVpm6K0BzxPQO77wDrSuw20SuKOm7aFNRfqXS9gmLPVuJry6kueX2JPNaW6dCaQKXVYQLvhzeaKt%2FbTdg6u9lOlAUg2VQUIl8yiJEE9QWk0Mfiz1dUCxhxUScvAiWBYG1OJUTYRz8ZteH6xD82G3U0ncllQQYod624NEVcOcNpMOMlNlydrWQE29IpQEYajHMqAlRcf7xhw%2FdhP8Px8SbLGjBHCIffxSXa%2FfudgqfW8LS%2B49dJ93H5QHYPBuvRY0zxHJl6Y7D5hJseniTCok8XBmQL7IIXyXsD6ppIAg5r3Rd1wcYyhU6U%2BjVNHeIUF9OgUkl8XUDQXw%2FfdY5FGs%2BwuUylYMSZ6JIZAQMsAq5HB1MiEKSdIhpzV%2FnLT1Gjpo0vss53SXIqRPxE3wDa%2FcenYdOIyha3B27%2FYSC7L1SxwmN4hHumQQQkwZJhZ%2Be%2BPb7Odp3HZUxKWKVumSEba0Rl41Lb97feQM6TAJpUTdkDXS%2Bp3UZ30QeBOBuZCBKZ9AuzkmsXMdaGwSwPpOYbpKdWBZx94NVQB%2FcbnTDNusTIBjqkAcRVV2wuxGNkC4WXn5wPF6JoJHW3jB4iYXHcMcfj90%2B15fr8alvsS1QLqhjygEA2pGtPs1nhRMTnp%2Bb3VgKRMXrgqqCOYKyS7AqQ69xx6Ro8j2wRE%2BQYXu8Y6OKpW%2BDmLz%2Fr3eafLhTSOfx845f51A%2FfK8l9%2F0ST1ZaEDRi7ickgyvdeZjBYdVrGOoew0okCgrj5%2FY8B%2BuvaKnQ4aMgGDoUrMGuJ&X-Amz-Signature=fee363c81d93045194d30ab43d9507111bd36f63c394fe0a44806dcacaca2ecd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

