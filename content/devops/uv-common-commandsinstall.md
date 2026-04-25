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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJPU2SG3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZEPCUYjF93W%2BqQySI6RBc5VD%2BowuALOifzKI91y%2BuKAiEA2VRkqkjuK3aCx%2FipzL%2Ba%2BbLE9YBr%2Bvf8MqipJ5aPTL8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAoJv6sjbLiDpdpJdircAyweArUWFa5xh8MKAuzfQx2B8OJnqMB4%2FbcOsA7erDQGRRxijgggDgwT5sDlI%2FwqmDeHKkCQv9hInYdwPQEU7lm5o9lqXjt4J4%2B%2BG1654d9iGUvHmyH79LkdtIGaW4oP%2FkW2AhJzHqPpo7YzMi%2FWcahxo2yX2Fr4ulAk1baW3gyhYD24vh6bqyEmpVXYTNgQ9TXZDmbPr%2BJhyQt%2FYzJ%2BelbTmnm8aLAESNFGmStwETrNRy3Sepqu0IT26wmf7vgmuo%2FtboKUVALra8rS3RTtV2SbtUIz4HssU221NOu4%2FDborOj1d5h5w8qrU%2BsI0wxGbLNJgFzuVy%2FYQgPNaqL0%2B96sM52kCpzom1aBeu2rwzsM5CGlCOWpQl8ZJ1WDxB3q%2FqiGM9lvmwsAN4y6VSSUlPdF9GxWfJhEpw9bvDK55kOBrM7OUltpgy4LX55i3Kpz93LDN7lr052JXVMBg7qBmxGgceho3jD4cLIIMb%2B8a5vhMRZKvYR%2BeoMpVv2UL5TLhdQj7hdlLbO1463%2BMl4tpvYYmEjzhNegauZwFS4M9U7LPem7O2scZRDGOorWGFiI%2FfmkNtmnFcGaVlY4c%2BxKsKUlQNax%2BHkxzAufTAiErkoqR%2FhvSrgBm9QS6w4TMO7wsM8GOqUBYXlhoQd7Bsu4SKkCDnSoxeEcM5piH%2Fnjs17ugbzmpxNCBGSQiIrKFMaVfZ4C5WuZV2MZ%2F5URXRlA42axMg%2FvPF7hpzT81Bi4V7xp4SV8nHUtAl1BQ7qUXcxKtgmF%2B4AAuTxAb9QX97eCX73OZQSjNIhwQpcHPv%2BYC9Lw48bJcJnD79lE92CxYJwzQQuAcVeWGHGaZSIcxZdyq1keKXHP62baMUGA&X-Amz-Signature=83fac0c44c1a4a1c2f1366a08bbef505678144a68c3503315297309641886f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJPU2SG3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZEPCUYjF93W%2BqQySI6RBc5VD%2BowuALOifzKI91y%2BuKAiEA2VRkqkjuK3aCx%2FipzL%2Ba%2BbLE9YBr%2Bvf8MqipJ5aPTL8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAoJv6sjbLiDpdpJdircAyweArUWFa5xh8MKAuzfQx2B8OJnqMB4%2FbcOsA7erDQGRRxijgggDgwT5sDlI%2FwqmDeHKkCQv9hInYdwPQEU7lm5o9lqXjt4J4%2B%2BG1654d9iGUvHmyH79LkdtIGaW4oP%2FkW2AhJzHqPpo7YzMi%2FWcahxo2yX2Fr4ulAk1baW3gyhYD24vh6bqyEmpVXYTNgQ9TXZDmbPr%2BJhyQt%2FYzJ%2BelbTmnm8aLAESNFGmStwETrNRy3Sepqu0IT26wmf7vgmuo%2FtboKUVALra8rS3RTtV2SbtUIz4HssU221NOu4%2FDborOj1d5h5w8qrU%2BsI0wxGbLNJgFzuVy%2FYQgPNaqL0%2B96sM52kCpzom1aBeu2rwzsM5CGlCOWpQl8ZJ1WDxB3q%2FqiGM9lvmwsAN4y6VSSUlPdF9GxWfJhEpw9bvDK55kOBrM7OUltpgy4LX55i3Kpz93LDN7lr052JXVMBg7qBmxGgceho3jD4cLIIMb%2B8a5vhMRZKvYR%2BeoMpVv2UL5TLhdQj7hdlLbO1463%2BMl4tpvYYmEjzhNegauZwFS4M9U7LPem7O2scZRDGOorWGFiI%2FfmkNtmnFcGaVlY4c%2BxKsKUlQNax%2BHkxzAufTAiErkoqR%2FhvSrgBm9QS6w4TMO7wsM8GOqUBYXlhoQd7Bsu4SKkCDnSoxeEcM5piH%2Fnjs17ugbzmpxNCBGSQiIrKFMaVfZ4C5WuZV2MZ%2F5URXRlA42axMg%2FvPF7hpzT81Bi4V7xp4SV8nHUtAl1BQ7qUXcxKtgmF%2B4AAuTxAb9QX97eCX73OZQSjNIhwQpcHPv%2BYC9Lw48bJcJnD79lE92CxYJwzQQuAcVeWGHGaZSIcxZdyq1keKXHP62baMUGA&X-Amz-Signature=75c1ed512db3922425c64296ff8c51b942f166c3bf25101182b7ecf9d938d1c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJPU2SG3%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZEPCUYjF93W%2BqQySI6RBc5VD%2BowuALOifzKI91y%2BuKAiEA2VRkqkjuK3aCx%2FipzL%2Ba%2BbLE9YBr%2Bvf8MqipJ5aPTL8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAoJv6sjbLiDpdpJdircAyweArUWFa5xh8MKAuzfQx2B8OJnqMB4%2FbcOsA7erDQGRRxijgggDgwT5sDlI%2FwqmDeHKkCQv9hInYdwPQEU7lm5o9lqXjt4J4%2B%2BG1654d9iGUvHmyH79LkdtIGaW4oP%2FkW2AhJzHqPpo7YzMi%2FWcahxo2yX2Fr4ulAk1baW3gyhYD24vh6bqyEmpVXYTNgQ9TXZDmbPr%2BJhyQt%2FYzJ%2BelbTmnm8aLAESNFGmStwETrNRy3Sepqu0IT26wmf7vgmuo%2FtboKUVALra8rS3RTtV2SbtUIz4HssU221NOu4%2FDborOj1d5h5w8qrU%2BsI0wxGbLNJgFzuVy%2FYQgPNaqL0%2B96sM52kCpzom1aBeu2rwzsM5CGlCOWpQl8ZJ1WDxB3q%2FqiGM9lvmwsAN4y6VSSUlPdF9GxWfJhEpw9bvDK55kOBrM7OUltpgy4LX55i3Kpz93LDN7lr052JXVMBg7qBmxGgceho3jD4cLIIMb%2B8a5vhMRZKvYR%2BeoMpVv2UL5TLhdQj7hdlLbO1463%2BMl4tpvYYmEjzhNegauZwFS4M9U7LPem7O2scZRDGOorWGFiI%2FfmkNtmnFcGaVlY4c%2BxKsKUlQNax%2BHkxzAufTAiErkoqR%2FhvSrgBm9QS6w4TMO7wsM8GOqUBYXlhoQd7Bsu4SKkCDnSoxeEcM5piH%2Fnjs17ugbzmpxNCBGSQiIrKFMaVfZ4C5WuZV2MZ%2F5URXRlA42axMg%2FvPF7hpzT81Bi4V7xp4SV8nHUtAl1BQ7qUXcxKtgmF%2B4AAuTxAb9QX97eCX73OZQSjNIhwQpcHPv%2BYC9Lw48bJcJnD79lE92CxYJwzQQuAcVeWGHGaZSIcxZdyq1keKXHP62baMUGA&X-Amz-Signature=ec4aaa14c80f1c126c274a70612fd1476f45595ee19ed580142256c6ab4a22c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

