---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJFIBWMM%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIGuaAxuP8UyiyRi2JE3fFmeYGckl488%2FG%2BXum1RkMhciAiEAtdKetktWhZ1vheSPc5MBbeNn3v6Cntb0PfxdsayUYW8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDEpBJm80DG6m63%2BRASrcA%2F7m9qj9%2B6Y%2FZ%2BOLWmFz%2FM4mtmcZKFZCS99lRJQueDvOt2vrXEOZ%2FEDXhlDR0WlJTsxDW5IMRqkP7bh3GPViRcPMc21ZLUpMbGkZtRVGWdXua3I2EGW8mvXX9eNcUAIjeFx9sim4K4AKtj9BpCy6gjbaAhWbtPWtvdQ%2BhgPPMt%2BJ%2FPEIH2WE8ybI1unqUoLurWg6aoij6C62zZaGZLSXLKXh88NYMfJ7p3IA%2F9wgpdz1dw%2BAvjE5jdOm%2FgyymtLZE3PeVcioLhl9EzsN6PPDy%2FEOQa3DzojkSbLjN0vnWq55d3Pl%2FUbJhsavziWfuQy63jfc4ZGZvZtNYpBlLv0VlyXkBQvWVtGKu%2FzYm6BLYH1ejxMIbq1EfyzPYDyJvaTuqxd%2FD1E1ogwO%2B84rcs4loiRAy5NPvsxP%2FBb%2B462qaSrCyzij4lOijuptdCzlKI9h94RPXSr6j3klGWb9BX3wfy%2BALvcRBf2Uz5ynKk2JNyvXbprFfS1wSlXTfCsVrB6u12xIHP78h3jdt4nL%2BP9srtiXeVt9eKe92Z1ZULUgRhYNYiBBcUErGX38biw9GhmEZjscgzWHqmghwD2XwqxBbyRt8x7q%2FpZspa9fEXLtxqNuLg%2F4K98SbZPhR86ZMKWUyswGOqUBDcV0Sch%2FrR17OJ%2BC0tb3uPj8u8kWsMpSGixL2hrkt%2FT446NifDw6UE5%2BZ1DB5MywjIPMFmTWiqKBWgj3tZCXzaz5oQem99Nompea4ToxGopKfKZMaLpiCjifHNrbB07794JUFgjx%2BL8eCJU822Vf9f3K%2BCPSlXURbRmtE58WG6LaJeL1CMyoJ5Yp9049gxcnVtxJmwnDS52JQVP8PX35QzKqGlm6&X-Amz-Signature=a5b742610e6fe6377c832de31a61b1d3b878ae99d5a6fb21651b98be44b44da2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



