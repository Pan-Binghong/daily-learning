---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JOQF5RK%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYBKYI8MrFqa1EDCwnbxi0M0Jyrmb19QRagJkoC%2BQb2gIhALKnNhwE8NKyUr2GXyAX8g3MjVAnqM2TogBRHxOBZiT2KogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHYC4eQmh2SUExExYq3ANn8lbyTMgAaQ8F01CoFyEj5nyvW9p2OcV6i0ZR3XH%2Br34tFEXsfhsUAqTNEobdY874HXO74Vf4EQ4gs0RVMiuee4dVkskaGHT4hn0Qk4q7pW%2BDeuCTZXcoI5fxj2EPtd1QAjtdTjmW1FdCsPlBnuqlKDd5AH2BDpqGlXx6rRhMvKWeJxHYImYm07r2JqR2YL%2B42NrnVSKa8M%2FvMENcJCPc9Ubc%2BuRg4mQw%2BXcdqF17gTIjZNbHas0s4s0xOBvJtyMFnFedJYRPBeuSTOtVFlaXtuWgAbxnES6PP2qlxWEnO87tLIngAo%2Bgy99cfAmPfXuaWYEXhhC7fKJdPU%2F62rmEpvseVLMIWcIwAURTD04aSCNGH5L8e56DO8pQI5RuzK7eYWVfp%2FyrJvgCs3aN3hDPjDChbwOBs306Vo01LhXgJQPMMeDcITPHo6erXzmE4gIweJsErO7AAWtiqYHkZqUd31uz0t8RNqo4per1saexjER%2BLt2gnUiNy45BpR1x%2F34EAjo1ybqDaoUkn3VhC7qXMkzLq3%2FHtILsbEydAV7rw7JtRKr5uvIxB6oinkcveN9It4Nblb40VIxV3TNCvxxYygzyOWXef%2FAEEh2Akl%2BE1B72Ty3lzYxOslKeBTCDn8fKBjqkAQJInEPOWRw5XXcPJ4Ha5ZSDIANA2weH5BX75QMCMAIRztO%2F2MKwOOeE6eGm8XbJEthfQlG%2FOllJ1GThhx%2Frgai6m6KGH2PVFgOmBtiTpWVHZdPixj4wEbzGK16E6ZLh7Hz%2BhY0AFaNpqRPsNUCGJnNYrXP%2B7VIb9ybvrwwgVSRAwqu9t%2F0iXPmQfIsrLfNiZJede9N0Ov7CvMHd0cHXibuXMYR8&X-Amz-Signature=b06a57adeca90f3f24ecee040dcc1b7e801406da01692990158b189569e7d00f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



