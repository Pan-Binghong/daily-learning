---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHBPRXUE%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmk928YraxfNfFaRSXeqwfYYYUpyNMVYQg5nWAKGWjZAiEAgsx0kEQrjamqQ5FnbUMx0ChEAR%2Fu9rdqz%2FaUfekhqR8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FcmfKj5lX7afDU8yrcA03T%2FYRaWo0mlBikA%2BOcQ%2F6%2FDS2smlQgWnsCg7XhzPJsXlrkkmKFxuZPet5YnrxE95WsrobMWE%2FXnCzZ9zJkl%2F2Q%2BV%2BTBu5gtdKmsM7SjxF1smqQ8Vj59XxGVTV8OfkT5qDlVAmmmSHyf1UuG1PoycHXXMMJdo9illMA45CX%2Bvixi%2FvBftgRQBVTR5h1Mi%2FyTVrAEBHtbzRl5bKPgw9wv7wiYRgCZ4hEy9M9pg3ijyVMQHgrVCA9FJuKfrOI7%2FW56Mdc7w9kMn7vzz3zU6YQPHyNNqhh97Q5HUMDsCOxv5QsaaFsVBMpbpiIlzjSVxg0d12M1EIsm%2BLLTz2LK37lkFgZIlkMxk4K0h45D0wL98dD7EvAlcHvsXL2eXPzD3TewuBqDUh41u9rCJ4s8qJhguIhekpHSq%2F%2FMgpZ40ZQUyPx8vaB1LWHSdXloA7pvRJo2DykMmL5xz90Y%2FYnUsgMj1HwK9ir50Ei%2BsPTvGdQSa0BfkkH1bAdKH2r9yZMG1yctxdTJqgnvz%2BcJsJesr7n7ViFRSR577lvGnuT3xaFc1jBoSP7bqXJN0WGDPzP7oUvaipBCpBtzisOSiSRyed%2Fe1itCmtOr8X6q0Z%2BddQZ0M2psuzAlvj9gfAJGMTTMKbM6cwGOqUBR0IM4deziekSa4JVBjQ%2FWzhDu8tHQ66n%2FXJbDDqT1ATYF56w0YP5AbZD7nF%2FuMVr5VUmO65E%2FYa%2F4WqNqhYSb4ScDoBreW11vL7WqBTIlx3Zxgsdn%2FjB%2BmlTv9JG%2F2FlbniVopUNotQ8%2BDIANzJUNsgAwzuLyaYGedTjH3c64yl4aTSZE5e6DZK8uBtu5FSo0t3Ka5%2BT6bcKJSNQWllQZRqJeTDa&X-Amz-Signature=9585ca1d510f447ca9fc6e2235456e61725f5738ccab82317b537a57425c914a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



