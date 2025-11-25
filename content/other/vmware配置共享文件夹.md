---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMDAJEO7%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICG95NauD9IwF6jt7wbDXSn4MXdX1kXbbCotwJnmlJoNAiEAyvHrz77WAkwVLckmHxFREhqsGhzDk2OwbUWey9ywvV4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDK%2BkZRtKUcbXoeH8kyrcAznE9CFi3eyYyVX%2BLW395eZN2P1VRwVivMBWISDIfnpYlnTsOWYBiiQDnDqwFPlkLGQrZZeDINjfmc6W23toFEca5lGVnH%2F6CvErIBH2y%2FxQf3LyKbIu2XnAhuaY86utXmBbuWzzarLKdHDgyg0towuEnok16MiqKqoGKT7ixlv7y6w4AJUNMXxkGADEx5kkIFRf3E4OtpAHSlovy6tfJuqxV0IG8pQPmRxdgvES%2FZSHaGbDxNUyBjcqarxUQ6qmP2Izte9qFyxySjnfrc7ikLVZ%2FFySNb21tuUABelsjRDhg2zkQOLIJ%2FXXisittg5UoLz5p6rIUqDcz7X80b%2Fz7TWSCTWHST4ALulkZqIPfM%2FXdbfTmM3P16aX8OqC51%2Fc9SMeyquR9T3geZAE%2FOiu2cVIjEH%2B4XYAwctngUxJao%2F8FxlPXG8kzCQGRKueyjixnlWi8jNQ2uulD68sCuRLIgK02JLcJDIUAZmY4P8Z4AUeXMYp46KJYGQtKW7Ht%2FexGdkBoGsLwGBVNfXLS6iVnID%2BaMLxmpA0mUJUTx2l92JYVhjyK255YbTFuPod%2FiGmCeEcN1nvIv5h5ZCaWJwbKIr1PqD6XdR2%2FO4lLAae9i2ocVVftqnpTEsHOslSMKirlMkGOqUBC6sXWVA5wKva9R5T05RmhCJIE%2BTKwjPi9MKXZ7fHggos7iGxKV%2FSbPfCSo2O7G6s5K6qiA8rPLWNm5fbUNwpQ5sZSeMg91vjvnmdn52%2Bpv3Uav58NBs1TOsmbDFgGjeprO4BYjYqct%2FrPptaNLXRX2l928FVepmhoEDxPmx9AJv5x7dxbEmY5M6CP5Hi4%2BhN9phwA1FlW2tE%2BVUnPf2b%2FxAQYVjc&X-Amz-Signature=638572d7ed8840a039a1aeb733920288a66c86766600d15e1d3e53612505e912&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



