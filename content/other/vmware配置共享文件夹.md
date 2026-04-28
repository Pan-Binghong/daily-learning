---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635HIFHT7%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHwhGqV%2BEgB033X0GJBpi7NDX5mUSFBKSIM9n1n5O%2B%2FmAiAFfS%2F9Vmr3TFrZyBzP3w2l2ZS5Mk2JGcCxfRnBo48aeSqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhniZjl1STmx4cWMoKtwDvPmmDsenfJ7qKPII4xfG54apwMo2o6MqQKaV8zSGOA69IJJ5BK%2BXVjZvJqpnObXPLGAgxLwHQ8mXlDX4OaLmKeTYsd2GGw1O4QFzuzkMO%2FT155lEDmYmj62QDhggOl9xGbovTB%2Fw3aqpreOXE%2F9wrzk0BSGZIfmFUvL95624a1TXS%2BtYd4fvUH3dFz34cTVe74fHDoeu9huGrDDg5Te%2BWV6mvbl8fDKY3kiCtWVXJdec5xX30aWsNb6x0kREmzAf%2BXDTA1jx61MHmWScM6HL35XNN7yUUXCzSwKGkTF26QR3sGpy%2BgkWEJuJjVCok%2BVTvNBKNvZ4NIM6kFDzeGr9Qd1k15CQxfkLDDBZ3hrA%2BaLr3bid%2BAvytEA83mJ5h753xKWrpWgQl0vOJ%2BbBXvN8HRgyVN9wKipvPwF4%2BJtSOzXCKfCyOpQR1jVA4KYjGzHVf35OONzkxY3kny%2B9D0K5Kd1u1UXs2IsvI4X%2BJy81iq%2FHFEClsRcrO5pgZc8UOlo6ho4tyjOuZnxw78T2nQxpARTyezmOKg3jL%2BxwvHU4fzUdGZcPRrfKnJsqsvupWthAKjvmv1BaXeP5p8CVAmPMpoJUtjlD%2F8h0OnV8ck4VTNDYpSMG3f5bpXpv%2FwYw%2F%2B7AzwY6pgH6FbeCWb6KiRgQJY9c72ccnershJlw%2FvWOemzYvUgvUDTY49SMCANUdvjvf0O%2FzhPWIjeSbem7y40qCS28aknu8c2uyePdqfmSo%2BFDxlTYYQbfxyBy9mvs878%2Fxt5hdGZhy6lJfpUmYX46sd6Mrp553WNyVw8TgOhUgWO32YWzyT4%2FsdCwhWS%2FrjNINl5Wyn%2Bp9SUtmgcWDsbk%2BNDbyS1tp0ozKcT6&X-Amz-Signature=1ffe7fc479d319c541069b21333a21f68f1ab06b9c770ad11c5cd714f5fc8b69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



