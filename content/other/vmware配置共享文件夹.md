---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOWYRCAP%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUXktERJPIOKaqXffqnRbbjhxBkIBHAhqkjarPtbniewIhALXOxrlCjnwe%2F2Tl8qiwIpejXVbj9HduTofejj%2FWaxW4KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzBafKOJYI7B9vVu0q3APRe5dVyn4bhCUge%2FxLuskr6lUHtgedBeYICb3wOiYAdkaK%2FTdaS%2FXwkHJx0gnUpVYaW8A4CK86nJtjt1vyk1nVnI8PA0LcvRmmJXaFVrxn2xwOPfoAjNQB6nqvMcZatUjJAg1uyQQMQLzaxwB4%2FBJOogFVjK%2FHRTI%2F4skq9C9LbIXhYE5wNjviHw7hm9%2BbdP5j77xYuWM9OWZ%2FoCYVp%2B3AmWGm4XfHW%2FBGE2iCaoXG6fMHUlwTZx3emG2KiZGWN22QaS5xsupOaIMJruwDwpq4F7IEGNbgSCBwEPXUaODGz%2BZVgOl0d2rE11yV15VZt9i5t6ME9tREjFAH2yJPDk8bFIXDwFL2f9B3PP2KKr4jKQmoPJNzyzEotjQQySyzfGRG%2BDAP%2B4Y6eDmN6JukNyp5%2BazMLOAFc436DYTz9%2FFdcCtD93UH4rZY7Jy1VCs04l3VMyIhrjTTfAszS%2BvHBj9FtcvssyFudD8QC9MBtuqi9v8EMZ3RmvlxqRCsmNiAieBAT3k0H%2FrsbTXhVLPKM%2FX%2FJTGSOGw6nBhxvbZW9P92OJIbxXjdEaOK%2BH4fyyytcz7%2FIsQLfSJh7QBR0uarga6O7i%2FmNL%2B%2BZrH%2BnAu%2FCWspMZVm%2FNaCXMr03BjpqjD%2BtLvPBjqkAUcTSzssGD50%2FOWFzOoeh2YNjnaezQjV5qY6yALVssuCzPI8079Z%2Bc3DvoHIeLZN9S8C%2Fn2RyBIgQmWxI08eL%2BPCunJPbN1kqAIws97yTO1kcbhGp5%2F1qYXKk2ar0mh7q578fhLeewX908hgfa%2B7AAdofUWEi%2F9fO%2Bob5Z5asl15Oxa7empg3DeR1eLFUo1Q4BdfTmNpSn6uZbkFInZba6D98Xkb&X-Amz-Signature=5802b76d5ef4131464e4d6e290762738dc1cf65f5af4a1c0a42f0875a858835b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```



