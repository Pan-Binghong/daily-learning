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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXACOT5O%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCj66%2FnN49gUqp8fzsFMULLKUisKdch1GgFlSwMi4UtugIgDDZxLW4fX87FFOY6xN4oM3XW7TVwZidiCbkf2D4BqloqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJvl2PntOAqG4L4LqyrcA8roIxTckXOwrdY1AJLVAHFE6U3v3CLAzdFXpfO05PfFY3Wh6yHQyUA%2FcWBVeAKArp0L9HzhSnniCKZJdqeWsyh2eJErto3p6LnftisS9UbKF%2BJ1vAQapMBr%2FMEdiws8hLRUXczwsolvRu%2FjXbY7%2Bbb9FDnPCpPQuZoLGFrCNdK8K7TxWRAEfZyuk9wQtFjIUjuA0%2BZEUR9OdJVl6B%2FJu999RbulmMtK2ntZMY9zEi7RVJQLkbAAHAkDWO2REwMdkMRL%2FHwpX0WWYz3nNtJ5FqATP38Zo98eMBLbwsbBBE%2FtB%2BQYS6BTVBbVoWAPt%2FPjz%2Ba5BSYFDuRg15zEZiToigzseyAEcYFN9iQOHpq6Y3bfmysBpQ9pv9Iw8yLmy%2FFcH50GNlOq7WU9iig5mqL8mXQYgsU7f1RfkbloXfzsNgReE1Nd2hbyWJlAKvWchbQvdpllLGpP9jzp3gqIFKTrR4i%2BG0gIoMpef1t3ShHcZACTFkqore2MW5%2B2i5GFoi8NrrPmJiKh0Yij5UDceWxbLsYtbY7NP37mojokfqViowOVcqjK807lvss%2B16zocRPFudlFWEPyloXKoVxrZyLctn2tb3ztxfh4McnTn8pR3FYIBSFtGQxPOwHoKgt%2BMJWQts8GOqUBL4YMXDRM1gPuPb5Nc5jWXPlDPzpFJjXAzcxV053VUGskAoYo6Nj4UN%2BSW9oZ9n0hGZLu%2F4YulrmFkUJZutu7LiEAJOfoukC98yapo%2FOmU%2FE3v%2FQ5zm3%2FmHbN5s0IxfReGJuC1q%2F0xhB71Jlw2KtKUxQw9BBKs%2BZz9Cc9zKnPZdLqDOUURHBBXMvcqMMzDuFUINlkz6%2BTQaYXFFD2yAlRlMDXZTmb&X-Amz-Signature=b5241281bd0932496634270fbd93d8f429424c37d5bf2204b9b9d88098196e91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXACOT5O%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCj66%2FnN49gUqp8fzsFMULLKUisKdch1GgFlSwMi4UtugIgDDZxLW4fX87FFOY6xN4oM3XW7TVwZidiCbkf2D4BqloqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJvl2PntOAqG4L4LqyrcA8roIxTckXOwrdY1AJLVAHFE6U3v3CLAzdFXpfO05PfFY3Wh6yHQyUA%2FcWBVeAKArp0L9HzhSnniCKZJdqeWsyh2eJErto3p6LnftisS9UbKF%2BJ1vAQapMBr%2FMEdiws8hLRUXczwsolvRu%2FjXbY7%2Bbb9FDnPCpPQuZoLGFrCNdK8K7TxWRAEfZyuk9wQtFjIUjuA0%2BZEUR9OdJVl6B%2FJu999RbulmMtK2ntZMY9zEi7RVJQLkbAAHAkDWO2REwMdkMRL%2FHwpX0WWYz3nNtJ5FqATP38Zo98eMBLbwsbBBE%2FtB%2BQYS6BTVBbVoWAPt%2FPjz%2Ba5BSYFDuRg15zEZiToigzseyAEcYFN9iQOHpq6Y3bfmysBpQ9pv9Iw8yLmy%2FFcH50GNlOq7WU9iig5mqL8mXQYgsU7f1RfkbloXfzsNgReE1Nd2hbyWJlAKvWchbQvdpllLGpP9jzp3gqIFKTrR4i%2BG0gIoMpef1t3ShHcZACTFkqore2MW5%2B2i5GFoi8NrrPmJiKh0Yij5UDceWxbLsYtbY7NP37mojokfqViowOVcqjK807lvss%2B16zocRPFudlFWEPyloXKoVxrZyLctn2tb3ztxfh4McnTn8pR3FYIBSFtGQxPOwHoKgt%2BMJWQts8GOqUBL4YMXDRM1gPuPb5Nc5jWXPlDPzpFJjXAzcxV053VUGskAoYo6Nj4UN%2BSW9oZ9n0hGZLu%2F4YulrmFkUJZutu7LiEAJOfoukC98yapo%2FOmU%2FE3v%2FQ5zm3%2FmHbN5s0IxfReGJuC1q%2F0xhB71Jlw2KtKUxQw9BBKs%2BZz9Cc9zKnPZdLqDOUURHBBXMvcqMMzDuFUINlkz6%2BTQaYXFFD2yAlRlMDXZTmb&X-Amz-Signature=45991e806697365e90b168601c38c720a6d33d3b58c93981ca39415233dce50a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXACOT5O%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCj66%2FnN49gUqp8fzsFMULLKUisKdch1GgFlSwMi4UtugIgDDZxLW4fX87FFOY6xN4oM3XW7TVwZidiCbkf2D4BqloqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJvl2PntOAqG4L4LqyrcA8roIxTckXOwrdY1AJLVAHFE6U3v3CLAzdFXpfO05PfFY3Wh6yHQyUA%2FcWBVeAKArp0L9HzhSnniCKZJdqeWsyh2eJErto3p6LnftisS9UbKF%2BJ1vAQapMBr%2FMEdiws8hLRUXczwsolvRu%2FjXbY7%2Bbb9FDnPCpPQuZoLGFrCNdK8K7TxWRAEfZyuk9wQtFjIUjuA0%2BZEUR9OdJVl6B%2FJu999RbulmMtK2ntZMY9zEi7RVJQLkbAAHAkDWO2REwMdkMRL%2FHwpX0WWYz3nNtJ5FqATP38Zo98eMBLbwsbBBE%2FtB%2BQYS6BTVBbVoWAPt%2FPjz%2Ba5BSYFDuRg15zEZiToigzseyAEcYFN9iQOHpq6Y3bfmysBpQ9pv9Iw8yLmy%2FFcH50GNlOq7WU9iig5mqL8mXQYgsU7f1RfkbloXfzsNgReE1Nd2hbyWJlAKvWchbQvdpllLGpP9jzp3gqIFKTrR4i%2BG0gIoMpef1t3ShHcZACTFkqore2MW5%2B2i5GFoi8NrrPmJiKh0Yij5UDceWxbLsYtbY7NP37mojokfqViowOVcqjK807lvss%2B16zocRPFudlFWEPyloXKoVxrZyLctn2tb3ztxfh4McnTn8pR3FYIBSFtGQxPOwHoKgt%2BMJWQts8GOqUBL4YMXDRM1gPuPb5Nc5jWXPlDPzpFJjXAzcxV053VUGskAoYo6Nj4UN%2BSW9oZ9n0hGZLu%2F4YulrmFkUJZutu7LiEAJOfoukC98yapo%2FOmU%2FE3v%2FQ5zm3%2FmHbN5s0IxfReGJuC1q%2F0xhB71Jlw2KtKUxQw9BBKs%2BZz9Cc9zKnPZdLqDOUURHBBXMvcqMMzDuFUINlkz6%2BTQaYXFFD2yAlRlMDXZTmb&X-Amz-Signature=aa14ab4cc4f234a338c39b55b879d0bc6f79094d6ce6986200656220b58c023c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

