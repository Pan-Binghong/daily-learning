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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHZFSNSP%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyeIDALB%2BG0vtNMOVHot5LtwIAoboFWl3hG4AuOVppmgIhAMTwuU9Xh84P8NvMSsuyeUiW2%2F8m89wTo7Jku71lN1YuKv8DCEsQABoMNjM3NDIzMTgzODA1Igww7XWnBPATIH5o8rgq3AMp7pI9G2SArZl%2F%2BicG%2FrCfP6OtlMu8o%2BfApIDVHty9V7fhRxmRdFns6Y%2BIqj7w%2FtvPQ1ZOkP0hhs6yEy7MH1NoDM1yMQEjYhtPa%2BeLjpulZqQrdDfoCZCx1MY28zPzosciJRVfUKqUZgDtCAruKTQi97YWs5Om9llipw9aDSZIpKhRXo1Zno6%2FdMolwUlZDYvm0ITDAUcRT1LLQU9G5G3g2xGmmAPAbvjVsDEmhzX0LAoKvE4Sd96%2B20%2F%2FZqxQV4las7ZIJjHO3DPLbo520y%2FyNr7mMtHJBmvO2zthJdDFJSGDIqXGyoPwtHRxqexDR8vlqdCQAlAkQ74NmQBjNoedcDoFGhfhwQ7BH1jkOBNa2iJizNh8xGYSNsOKCpaf0kuuNdEveWXINF6ZDkK7nz9lC%2B%2F9YD6V5M1dhiVLNqKN7AnAB5wGeN%2BN19W5J9DBQGRP3W2%2BqyuMNSMGGUtJyrmDH3ahUE80XMo48Tlilvyf%2B1npj09yZ2KAKn%2FqoyHMi9yS2uLZitUUG2eZtfNJsitjxdt5CoO2gxD1Wh8hzbC6DH3d0cejdJyTnHUaym65XHNyJGA7nse7%2FEaxuhQgFCxZMAKTdZFf0HEFNK4cGApZ6lnLaIb1Iswr%2FNoIrTCP0LfKBjqkAe7uo4wzdiTbdWftFSWrFlb8BWB3XsntTRSPaoiVbhLroI02nqrk0ozOvo%2BYy9ngTLTxUXyeBnip5FlzILswVTkJvphQTkA6Rl9vwnBo20GR7J%2F3LE%2FvjNoRyRckg9SwB93Cd38s59oTRgwMeM%2BYL%2B%2FRLT0K07%2BcTBJH7w4YUpphNQHD1w0ScU%2BYLvnBW2N5EIWC93PIJocuQ%2BlPl19tgZmpYaro&X-Amz-Signature=d39ace08c5f959d665465673bbe8fe132372d0c9a578c4c8885f7e19d80c66ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHZFSNSP%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyeIDALB%2BG0vtNMOVHot5LtwIAoboFWl3hG4AuOVppmgIhAMTwuU9Xh84P8NvMSsuyeUiW2%2F8m89wTo7Jku71lN1YuKv8DCEsQABoMNjM3NDIzMTgzODA1Igww7XWnBPATIH5o8rgq3AMp7pI9G2SArZl%2F%2BicG%2FrCfP6OtlMu8o%2BfApIDVHty9V7fhRxmRdFns6Y%2BIqj7w%2FtvPQ1ZOkP0hhs6yEy7MH1NoDM1yMQEjYhtPa%2BeLjpulZqQrdDfoCZCx1MY28zPzosciJRVfUKqUZgDtCAruKTQi97YWs5Om9llipw9aDSZIpKhRXo1Zno6%2FdMolwUlZDYvm0ITDAUcRT1LLQU9G5G3g2xGmmAPAbvjVsDEmhzX0LAoKvE4Sd96%2B20%2F%2FZqxQV4las7ZIJjHO3DPLbo520y%2FyNr7mMtHJBmvO2zthJdDFJSGDIqXGyoPwtHRxqexDR8vlqdCQAlAkQ74NmQBjNoedcDoFGhfhwQ7BH1jkOBNa2iJizNh8xGYSNsOKCpaf0kuuNdEveWXINF6ZDkK7nz9lC%2B%2F9YD6V5M1dhiVLNqKN7AnAB5wGeN%2BN19W5J9DBQGRP3W2%2BqyuMNSMGGUtJyrmDH3ahUE80XMo48Tlilvyf%2B1npj09yZ2KAKn%2FqoyHMi9yS2uLZitUUG2eZtfNJsitjxdt5CoO2gxD1Wh8hzbC6DH3d0cejdJyTnHUaym65XHNyJGA7nse7%2FEaxuhQgFCxZMAKTdZFf0HEFNK4cGApZ6lnLaIb1Iswr%2FNoIrTCP0LfKBjqkAe7uo4wzdiTbdWftFSWrFlb8BWB3XsntTRSPaoiVbhLroI02nqrk0ozOvo%2BYy9ngTLTxUXyeBnip5FlzILswVTkJvphQTkA6Rl9vwnBo20GR7J%2F3LE%2FvjNoRyRckg9SwB93Cd38s59oTRgwMeM%2BYL%2B%2FRLT0K07%2BcTBJH7w4YUpphNQHD1w0ScU%2BYLvnBW2N5EIWC93PIJocuQ%2BlPl19tgZmpYaro&X-Amz-Signature=8bc5c39dddd4b8daea860a807d5baa5ac0597592910b0252550792a242f20e15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHZFSNSP%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyeIDALB%2BG0vtNMOVHot5LtwIAoboFWl3hG4AuOVppmgIhAMTwuU9Xh84P8NvMSsuyeUiW2%2F8m89wTo7Jku71lN1YuKv8DCEsQABoMNjM3NDIzMTgzODA1Igww7XWnBPATIH5o8rgq3AMp7pI9G2SArZl%2F%2BicG%2FrCfP6OtlMu8o%2BfApIDVHty9V7fhRxmRdFns6Y%2BIqj7w%2FtvPQ1ZOkP0hhs6yEy7MH1NoDM1yMQEjYhtPa%2BeLjpulZqQrdDfoCZCx1MY28zPzosciJRVfUKqUZgDtCAruKTQi97YWs5Om9llipw9aDSZIpKhRXo1Zno6%2FdMolwUlZDYvm0ITDAUcRT1LLQU9G5G3g2xGmmAPAbvjVsDEmhzX0LAoKvE4Sd96%2B20%2F%2FZqxQV4las7ZIJjHO3DPLbo520y%2FyNr7mMtHJBmvO2zthJdDFJSGDIqXGyoPwtHRxqexDR8vlqdCQAlAkQ74NmQBjNoedcDoFGhfhwQ7BH1jkOBNa2iJizNh8xGYSNsOKCpaf0kuuNdEveWXINF6ZDkK7nz9lC%2B%2F9YD6V5M1dhiVLNqKN7AnAB5wGeN%2BN19W5J9DBQGRP3W2%2BqyuMNSMGGUtJyrmDH3ahUE80XMo48Tlilvyf%2B1npj09yZ2KAKn%2FqoyHMi9yS2uLZitUUG2eZtfNJsitjxdt5CoO2gxD1Wh8hzbC6DH3d0cejdJyTnHUaym65XHNyJGA7nse7%2FEaxuhQgFCxZMAKTdZFf0HEFNK4cGApZ6lnLaIb1Iswr%2FNoIrTCP0LfKBjqkAe7uo4wzdiTbdWftFSWrFlb8BWB3XsntTRSPaoiVbhLroI02nqrk0ozOvo%2BYy9ngTLTxUXyeBnip5FlzILswVTkJvphQTkA6Rl9vwnBo20GR7J%2F3LE%2FvjNoRyRckg9SwB93Cd38s59oTRgwMeM%2BYL%2B%2FRLT0K07%2BcTBJH7w4YUpphNQHD1w0ScU%2BYLvnBW2N5EIWC93PIJocuQ%2BlPl19tgZmpYaro&X-Amz-Signature=222edebd1e498e9e1d966c79e81d18e9759ffe555d929686ea9f2e20ad846fb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

