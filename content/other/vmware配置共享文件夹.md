---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3S7QR6I%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIE3L93r9tLuB2PNaIr47rXOJMu1qDfnKcsxh%2BUead7MYAiA%2Fi0I3Z5QnHujddi31hKK5aHrFwfKdHJEz8swCSHwA%2BSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4rZbCLPKq7Xhk9leKtwDU%2BXhrQHOP8ZwMyKGhoSxtnq3wj%2FPsrZ4VRM9HF%2BEtj7WrocR5744b2oIbJPuxnZRY3a0VtJ8lW%2B9lDAUYcyJH6fDBjRyr9yoVFGqRp3orvqT5BsaNl9Vj7cKowYVR8rgogcZSsDiJ9p1RnaK5nlfkzchFqxVs94nhNUgqTryVWVsD0b3FspIAURdNYc0FYC60HqraoX8cztOfg0m%2B9QLWwIE7Dm%2FBdMwSKSNsd15JEjgD2Ogpbin8uscTx1ANsEj7KnmX7WAW7lq8QWgJM3Ldv4t4nRamefNcJQQQzw6MLkMPIIylXVw%2FI9XLzrOlxWHXXkQGWrXAk3%2BSwyE%2BmOem3Ic7s2EvDFjUVd1UcL9BFKu%2BxlcwA9Ka8%2F3Ee5tvp6lnadTXyBK9M1K7Z25Bha6N%2FnPpbLfnI4h%2Fg9%2Bovx2oHGbeX7B3tTwJHEbFaEXpnZMbqsPhwaOMq1yv0t2aQUA1Qb%2BV7XCVMtklFJaIBbqIfsHQWjLnRvKPEbYMscooP25k0cI3OP98yxLJAckkH1m4OOItWjGNu7maJC1Vl6etQuYhagnpglPF0Tmw3Riua9ZKADEoKZufNMnhKNLCgtwliEMWM2d4JR%2BW%2BPiX9DzKU71LFOBZcVAyHotmaYw3oeAzAY6pgGCxIoKkL5DnAKgAgn9xff0qWlS1to0m4VyhiNC16%2FMwSxZxG%2FG2pY%2Bfi%2Fsr4LTiZ5jM9Zjo4WUxvHE0PhM25CxUpveIjkN1iYeRnmsK2cMeusfj0N9BomUSlbr9swTBdWjscR7nEXRtANc%2BBu1IrETOxtNrgyEw0yABrjsktsOTWHrqj3ObpDvQ1d%2B1yGWl8g%2Fy6nHV%2FnF8nRFogj8n%2FmaEVQIgaRz&X-Amz-Signature=1668cc693eb170311785efe6e8adb959ad34935d3d20a3e00deff001579ece0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



