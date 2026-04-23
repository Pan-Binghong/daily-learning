---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XISSP2N%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEe1r5gjgDkKklxOzS5GN4gzy1sTImes78A3NeB3y7FQAiBg%2BhXetEKCPvmw8uR0IKz3k%2FvWOGbjIW%2BNVFX46lA0Jir%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMK2xl2RSKhu6OI%2Bs2KtwD0iuovTpmO3aev1Y%2Bi89NfN37OY8gG3X3oxpivR4XPU7aupPklTAuLtaHDKZAGLpEODwIPXnP8PTRU8Pm6GdKqNwu1udlaWwWM8MyQTiljWQwjE44VBD%2BdW4xFFE%2Bm6dxpHllvIWXyJlZX%2BkK1BlSZYTA8ZNK5b4Ess4jlnltEDiwKlFzs%2FUtK1AUGteVwEpHtRpFM5RzBdbA%2BMpxSQ4Vv76WiJX8runI6po3SnI9p3qLuVh1ub7yrZHR0EvyxnVGWk6OejUc5KwM2au30%2FhB7LEfdar7He9XL9OW2ZSBMeC8uYwS4EC5MOah82EUQIzLL%2Flm%2F8CpVVZau250y9McJEv%2BO%2Bk2xRHh35qqr4yUsPoZ0%2FqMLNLo26yY228mJjgJG1v4os94O5Y3OxIB3D8WogunYLXdJuoPuL4U%2B8lEcQDldvBuz%2Bhwqc7if22Bbp295HZe0T7mQfzhAgsJNk0LszTUAeQ0vShR3onKrfFz398MStuL9kGjMsCTYIpFrIiPqB0ekFGT%2BTe8dWoXlR90Y2Wcav6CBmcXv6MEVNYzwuo5cqA%2F9uyr%2FndrA%2BUztdIS4BvB8SELEdUHm14njKvdNsS7kFIk7kde4suBw6pfWdY7a1TrwENe%2FYlYQhcwpemlzwY6pgF8zavOQw7z7QXQdHjzExgUn2bhx9AKor%2BTJC1Wj1%2FtnnE2EJ8Pnx0fP%2B5IPjSbOJ4GIaN1mOAsq84UxBVsE27ZUh9qnvql76gsPxfi7UXTVEqMZpDvAHnOpgntUUo%2Br2lId5vwHt6%2FJYkCQO%2FbvoRIUcoiXVoBsVR1Ehmt78DHgsHrGM5h9c4GFq9D8xrhY5sbPnLAXK3SUJ29az%2FuAmjsaR6YXkxa&X-Amz-Signature=7a8940ce4b084bf875ea8961492aec4d61a83e313517f6ad3e44122d78101592&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



