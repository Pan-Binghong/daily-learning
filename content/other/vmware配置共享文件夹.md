---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPN7IL5K%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIDDvYcYqJY7v6CN7fxOnWpo1MSKqSHEPl2yO1ybeBYPTAiEAgfpMwvtKT%2F0%2FJ4Kw0MsN3A2xdbeLZasT0UPcsqC8r6Iq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDOMz3RxTo41RPIvmnSrcA2vQSlcnmFCPQvp2ytot%2BBQwYKAclR0sUvLpcQUQBGs8zys9GYj9e9km0fdGh1AlejYL4A6sJxH6UOlbQzFLdKVYmkk0dCvH5FrwqyWWETBYPaOPbWw0PvpZOS0OpL1NwAzbD%2B1tQJ2Xi%2FueSIa93UZ8qWeMCCR3K5PyHOYrNmwNgqD6nGyTeQRmF8aJfPDC6OCCTbRO53DzlZk1jH432dBzFfcUnQKfj85OpwVcJFWYJgClSUugy6566oPoxxzf9FXxuekfTieL56fjigjR61kSZtxqYNhAf7SHyy%2FmJ7jFLgP%2FVyLdZtN9dbFee8Xn%2Fx0EHYYjWNcnq26ZBDZIoRi4LCCgvogn5JkinJpeW418OEL797lkY8DCLAGjznkg3Xv1YgWh9usrfIiplMUkoawgjq3xCUvPw2sXh60u9xLQx3UtBqYMr7EjidnGltSEhxZMOpezAD0z6RUYhEXMYDB2imxdFkSNwrrFNeu15YR4Jrw2iMJCi7VDUPlXPJYRoBvTTf5grVFa6zjTNPVmf7yRdSnaxncQBHA5X35P4SL41shJJchghi7KA7EymG5TID3YRKs1pX0OlKvrcFnzyzIzdW%2F3qYX4v5iyVcl8pCW3J%2BDmHrJ7nQo3NLH%2BMK%2Bx2ssGOqUBdMVa5q%2FgIove8wxRLtqUw2nPm94xNeCANRiRzxuOiCbK8RXLsbTQ%2BDpPMcpQxcvJDy4x%2FJyN2vqPQtkn4CK%2B9lA%2BO0VugXPx58CC3mR%2B2E%2Bm2ZhItQIO%2BzbzHNblWlsOBmfLbTIKQbiKa%2B1b%2BKG4LGQun7vfrWkhVltIUhTMTC%2FZp1ISNIyr%2Bo5y2RtGkwuzAFDeTBHT%2FX4UhQ7rDsSpPqCAXJUe&X-Amz-Signature=83e9dc0f81dad99a14e72017dcd4f2afb265351eef8f18143547d4db62ed4c9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



