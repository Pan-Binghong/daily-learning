---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PVBTWI4%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDPk8zZsURtDdAW%2FJmetnF27Yzg%2FxqsM4G%2B9Lwkgbsi%2FQIhALgjyQ8c7wBTuCA29mhBu9bWIDL9SQ%2BNQngZAN6p%2Fd%2BWKv8DCCQQABoMNjM3NDIzMTgzODA1Igx6w5upVQfbyhcnsR4q3ANenJC8SZVO9voAM%2Fu2TUU2R88cbRn4yWJoDuGo2XacErBLKzjFlIeinIM7UwcWYDlSCiaraBpJBHERxmHZK9RfzS8WIicxAGiJaKbXrZjjeHlRLUm9QGvdRupA7n3Uenf2RdliidSqXOWH%2F6pyByRQScTQTGEUGQgpizN4ajYs75j5T%2FTOv%2F61avnbb1asSVm4toe6tCPTsJ3qMEYnU3BzsWx8VNunhCBOFin1wzlQz1hl1%2FVuKmC2gtTgfvEGqVU5%2Fr8ghTH8g4gKLRDKXj%2FDKxlkQuG8R%2F%2BjqkAegTk7HPhX5QnMptJdRRtkI%2FQ9jGt4AAiI9S8yYIKo7TzS0D5sGy1lHaCJ6sZjF0%2Bpd8flwYawXzg8qDDimhbWetxcKeytzVPu9Pg5Ic2DrnliBhpvoa4V9akH7Gjsi%2BfKe0MmYHR1rV83RTW3SnaynTQols1B9%2FnTsuQeYtv12YnqCO5qEgMfuxlP5ESS2ioZpyA5MUxl5cb8IcT%2BnKqIs7LkeOKAYDRi5sTr6xsFfPUuzA2OLMVRXxjHROXpIQxq8TPrRAy2pI6sSm3xCueMHNHw%2FBnY4Mgq6burYFXyvr%2BsC%2F5umJjLOxuy7OxmtY712%2F6xfNuIF7bTWCGIv18urjCak5DMBjqkAVNz%2BjZLnCYW%2FApYF2ZverzjPEmCq7g%2F4mgAZmBXX%2BWx%2FGnUP8OQLZiL5fvPEo8CH6f2cC%2FxS4zySyyKR3KVMCdkcabqQidhQaZxma1vSET8r%2BTx%2FnSqF2jBMgsHtoX57fAzQahmI5EcQCAs746To0Z61J8ovRtwgCTY5VuposcK76rEqX0E72ABjcrt2exF6GXjFSBXxpAugB0nFsrIjB%2FI5VNl&X-Amz-Signature=8d04b1d37c4f3b4ab05df26f719387d762985dd52497cf4514f1fac92910822f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



