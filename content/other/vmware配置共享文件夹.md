---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VWU2VNW%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDQVSXI33mIxq7YAGp9olqrzmIs%2F8OQaZq3PjsbvTcLiAiA04FUuctZ0mOFaelQSaNoICvUAcQ6oQKgZI9rT%2ByyGlSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMRxX3eMZxVOuDQKFhKtwDPNGdHn9yyMTB95306mRe%2FopObbXmf76vciZ%2B83W4fyi1mdWioghYQWKuYb6%2Bu1pC8aT8ZEc2irVWGeZQYh1a77EO9GGObSJrYfZsBQCoJVz2nc5ZbH88UlpaTnqf2BB3sJmh7Iy7XATgeOiP%2Fm5HRfvZ7hx6zHF8Lb5Y3X22JmVXnh2MrBUF5ESndy3GnoVHEht0pXOAGXavmj87%2BMPtDVXowgZd5qKKWl2vRh9xUsULi4K912vVOwGJ6oUUlPDlDmVVjQ83rSdq8gwrCMQI%2Bad4iZPON7dGLxiAlPRUrSt6RlTUm93DwDOWz40zCTblZIb8Zfmz%2BTP%2FwbUBEGfPefSWkkMJjT33uxSEAcfmrP3S%2BPWvjWEhjAw%2B8HNpbuKuqnoJFHI%2BW4Ebp%2BawA3GREgNB6M01TxqpceJyF7ngC7wCHO%2B3EamDvullKi1FxzZbAskYjArT%2FQKdPj5mtpCCFh%2BS9%2BEWTRHJIpViEcntOGomlMI34BOnViDhJVlEjOMmDCiJ7DzZIIi3sYJVCdWeGtC96bpXQ2%2BQuQ%2ByFKVivXHnf8GmlEb1uSDRkiosO8bXGvTfUmlGldIBLcIu35aO86lY3GB6nBWZfgDgk6BtiXWsC6pLMzk%2BZ7GO1JUw3MDDzQY6pgGvA87zby%2FSUKLC%2BzzZAB3tkKhYaObbkrZhTxY6DObxjZVM3x4%2FA%2Bm9qOHByWzQdv9ZAoStovvdd2lZ%2FD%2FMHWP18vp2RqR7%2FlcB6wCLx%2FzZh36nOJLC01tMTdOugwOXqEtBNea%2BszZ9NDlAg8vlex3wAhw1JWzevfxme2NAs78FA5uAIHj71GfeL%2FzjEyR7og9pKxnY8BLXLHHBPnFQzuJY6%2FvY2YZ4&X-Amz-Signature=8ef76c94f6705f6fddbabeca85bc9249d68fd9e0a283b121952a50422bb8f6d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



