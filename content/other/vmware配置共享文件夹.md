---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DVNWQUT%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQC0pGMcRnQaiDDJ24RB1ezNEz7BByF29wSZBM4f9UNTtwIhAPGP9zXot0vlg03FB7oWIJPBHewwBdq%2FcYxSaOudJ2VmKogECPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoOqPNat9VqQvdpCIq3AP3bIljMMlMi0SkKrvTDTGFhkBAgt0%2FIl78%2FxywwNuNHLsE%2F6a1O6hwUyoWYWp2jTRmb5XBlhgrcXLLoNUZldf%2BslM1NcST%2FYYBQY83iti9u9ywYRR1Y%2Fb5SznIhB3%2FhnuH5eN%2Bqe%2F79aSHsh6UUEJQKpVag7px6MSRUHYszhz2GqVoF6GcYrzc9F6HiPITcjL4nRvcr0IVH2X9HSHZeBbEELsICVDHoxER5gtz%2FXupWTagZKIucLBTkxmXGeuNxhI0Gff%2Fhc79%2FWa8XUOPH7Wbox0qNWKWgWppr%2F49p0kRHqeRYGMPP%2B6JIsJT0U0TtrH2AWxuXUxgVsx1dfVMOX4m9Dw3QuwH%2Bp0AoCoXIX0wCDmznRzIYW0IdkLmlsNk%2FKQjIcNWF3T07zz15I8YmXpSxUXJE%2Bs%2FszGi4jwLKWchCv%2Foiied0RM%2BtnF5wbglQPwjRbxQtFmSIF7OI%2BwVW%2FSBUJ9md36EuuCMkfIAjxBHtbg6GyMxHHPIYhZu%2F0YCzEikp8kO8GPvOhHIaBnJ1Q%2F8BOD54%2BxaOVOOpQs82Rw77plhGuGr97eBhvr4Y5Gul3EdVAntqAO1WhPSAQ8O8TrlCoCWpTO3SMYJnsb9pu1t13xA%2FDSYSsfkJkdW%2FzCCitfOBjqkARX3s5USaUtT84XsUvNTtQLJK7x0u5Dcey%2BBxAlvwqepEo6bWERelBuStl3B7kmtoDgE%2FT%2FPtT%2FriRVSD%2BIdkxEmlQ%2FKzr4rXRqI1HNnCqoLoQ2TJS9MqMsP6y%2BfAEMdbyTEksR%2FU2PKbGiNVq8Pdu3AgCq6U5jPKa%2FKM6vyPQ2j1YAU90D%2FOqc0YX8C%2F1AfKqisHMmfTaorZm8aB%2BhE2JiLkZ1M&X-Amz-Signature=ae24dd531e69795a4846ad8d02807a2dec1fd519d00a7885e1424caf9d6e2a1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



