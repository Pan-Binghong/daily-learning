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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PGYF4SL%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICorf6ts3WyuRd0qBi4a22S202rLZLXvKw2wxojvLVVVAiBEFttiWNTCUQdDS7RS4f1yACnMaJ07JqckQbRw%2Fe6%2BlCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMW%2FAEAoo6TiTcSc9JKtwDuiH64jJ%2BgfRueSs8zw2Q1NuGe0GaHj9c2IsCf9tFLbqUDD1FDOXzzHqIK6poYGlxou0uxMO53AqP%2BVvIXiKoc5IeTnqQYNwwI%2BA%2BI7MjdugIVRxjV9MpsUD2ljZaux29xeIc6lvgVDK01K%2FumVV1jT8aCQWiAheNvarPxRbo%2B214ixTj%2BahsPbjq7fwYRWsNJAfenmphYVqLmdYCk5e1PnmxJRpTs8WC6yDhm%2FEd9s6k%2FimLyFT2PAxkw5mSwazu3QgNNIan1ty%2FOmbO%2FlNwU6%2B7DkUGJ%2BlM0EQmHwqjmvgKlJAjTyHml8hFBtGxPF8DcpZL9LEKEcNgJm4XKJT9AxZcKrFtO91GEiD8G%2FXCNmX23M7qyDAOkqygu9SlcK1gySHKXyYGM4rirN9liRwtsXee2CSLNSa531lZUiLdoSS31ijJDTwSnnWX4j7QLStXqXPIx3Q6OCdPGBK%2FrvdaaL7zdi84jXJxU%2Fv23TodfxwLlRI6SVzbx%2FdXRnFWTWjexUImVDhX%2FoGHImp8eOMBIPWO%2BHVr%2F6m6hNtGn9Tkov7Upw%2FnOpWIHwYaKKqQsWuh7TGC8WO6MtJE1RoSbFPWbGePnHk0lfawQxCP9pyOHMQWEUe9KCWHV09stCAwrfHUyAY6pgHIeJ59%2BjXM540trxsB7ArdodJo6tlCcUyDNItHrF901Sayn1ww90fpMSYF1Q78FEz09PUykk%2BKU9EGucXNgPPW4%2Bc%2BpZ3Kb1c2fd7v4u4kZsi6cfBhUzvwaePEuDC2bE2zRpMq0bSIhYvGZIawfbRWbrBAaKWeLVktC%2FnHbh%2BReI5Vqik4xj5mSrc2b2bwIwZ2Tacl4RyR7UgJRPbHUQaB0Iytg4u%2F&X-Amz-Signature=119945afad9e70a9abd0c8b53cc2af46a027924d74c0b9baa2a1114f998715bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PGYF4SL%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICorf6ts3WyuRd0qBi4a22S202rLZLXvKw2wxojvLVVVAiBEFttiWNTCUQdDS7RS4f1yACnMaJ07JqckQbRw%2Fe6%2BlCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMW%2FAEAoo6TiTcSc9JKtwDuiH64jJ%2BgfRueSs8zw2Q1NuGe0GaHj9c2IsCf9tFLbqUDD1FDOXzzHqIK6poYGlxou0uxMO53AqP%2BVvIXiKoc5IeTnqQYNwwI%2BA%2BI7MjdugIVRxjV9MpsUD2ljZaux29xeIc6lvgVDK01K%2FumVV1jT8aCQWiAheNvarPxRbo%2B214ixTj%2BahsPbjq7fwYRWsNJAfenmphYVqLmdYCk5e1PnmxJRpTs8WC6yDhm%2FEd9s6k%2FimLyFT2PAxkw5mSwazu3QgNNIan1ty%2FOmbO%2FlNwU6%2B7DkUGJ%2BlM0EQmHwqjmvgKlJAjTyHml8hFBtGxPF8DcpZL9LEKEcNgJm4XKJT9AxZcKrFtO91GEiD8G%2FXCNmX23M7qyDAOkqygu9SlcK1gySHKXyYGM4rirN9liRwtsXee2CSLNSa531lZUiLdoSS31ijJDTwSnnWX4j7QLStXqXPIx3Q6OCdPGBK%2FrvdaaL7zdi84jXJxU%2Fv23TodfxwLlRI6SVzbx%2FdXRnFWTWjexUImVDhX%2FoGHImp8eOMBIPWO%2BHVr%2F6m6hNtGn9Tkov7Upw%2FnOpWIHwYaKKqQsWuh7TGC8WO6MtJE1RoSbFPWbGePnHk0lfawQxCP9pyOHMQWEUe9KCWHV09stCAwrfHUyAY6pgHIeJ59%2BjXM540trxsB7ArdodJo6tlCcUyDNItHrF901Sayn1ww90fpMSYF1Q78FEz09PUykk%2BKU9EGucXNgPPW4%2Bc%2BpZ3Kb1c2fd7v4u4kZsi6cfBhUzvwaePEuDC2bE2zRpMq0bSIhYvGZIawfbRWbrBAaKWeLVktC%2FnHbh%2BReI5Vqik4xj5mSrc2b2bwIwZ2Tacl4RyR7UgJRPbHUQaB0Iytg4u%2F&X-Amz-Signature=cf45d0485990f6a64722115185b3f98ce89ab871448ae66d0a69b8f313bd94e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PGYF4SL%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICorf6ts3WyuRd0qBi4a22S202rLZLXvKw2wxojvLVVVAiBEFttiWNTCUQdDS7RS4f1yACnMaJ07JqckQbRw%2Fe6%2BlCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMW%2FAEAoo6TiTcSc9JKtwDuiH64jJ%2BgfRueSs8zw2Q1NuGe0GaHj9c2IsCf9tFLbqUDD1FDOXzzHqIK6poYGlxou0uxMO53AqP%2BVvIXiKoc5IeTnqQYNwwI%2BA%2BI7MjdugIVRxjV9MpsUD2ljZaux29xeIc6lvgVDK01K%2FumVV1jT8aCQWiAheNvarPxRbo%2B214ixTj%2BahsPbjq7fwYRWsNJAfenmphYVqLmdYCk5e1PnmxJRpTs8WC6yDhm%2FEd9s6k%2FimLyFT2PAxkw5mSwazu3QgNNIan1ty%2FOmbO%2FlNwU6%2B7DkUGJ%2BlM0EQmHwqjmvgKlJAjTyHml8hFBtGxPF8DcpZL9LEKEcNgJm4XKJT9AxZcKrFtO91GEiD8G%2FXCNmX23M7qyDAOkqygu9SlcK1gySHKXyYGM4rirN9liRwtsXee2CSLNSa531lZUiLdoSS31ijJDTwSnnWX4j7QLStXqXPIx3Q6OCdPGBK%2FrvdaaL7zdi84jXJxU%2Fv23TodfxwLlRI6SVzbx%2FdXRnFWTWjexUImVDhX%2FoGHImp8eOMBIPWO%2BHVr%2F6m6hNtGn9Tkov7Upw%2FnOpWIHwYaKKqQsWuh7TGC8WO6MtJE1RoSbFPWbGePnHk0lfawQxCP9pyOHMQWEUe9KCWHV09stCAwrfHUyAY6pgHIeJ59%2BjXM540trxsB7ArdodJo6tlCcUyDNItHrF901Sayn1ww90fpMSYF1Q78FEz09PUykk%2BKU9EGucXNgPPW4%2Bc%2BpZ3Kb1c2fd7v4u4kZsi6cfBhUzvwaePEuDC2bE2zRpMq0bSIhYvGZIawfbRWbrBAaKWeLVktC%2FnHbh%2BReI5Vqik4xj5mSrc2b2bwIwZ2Tacl4RyR7UgJRPbHUQaB0Iytg4u%2F&X-Amz-Signature=b134073a9e8015035e9794243602948c553e2ee04094e4cee17a59e7872c6bc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

