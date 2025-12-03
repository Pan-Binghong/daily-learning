---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EUQYERC%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQDsr65ctdM56syQadzXVDLdEZjL7dzKvroiziAqJURxlgIgQj0uhSFRkYjIkSqW0mMH5DfHcJaSenV%2BjiDOTAWUtLEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDIog30qbAMueQD9XzCrcAwLLCkVKNvdXHDEUo55c9O24bj8YlXXFrK8UGE9SUcIe5EEKTtgPWG7oE8rq4l%2BMAQ0jTAu%2FTKRPRftqdUpjSJX0Bkj9nQ0UNwqH4wJremaQuSr9bs1%2FZIj%2B0GNp1Y0HiPTBzEEQG5weEs%2FS0BqxSxlIw08jRmYO2lmjwU%2FuTp46Du6%2FDywAzgyKIZg%2BRcdPijxa0R%2BTKYfESvabOxxP%2FGRMmxI1kc7AnHyivhprVZohUss%2B6HItTBQ7Of9qQC65mGBlnK%2FIWaYJJK%2FRIWS7icaHmOmxDA4G6DBM3B34cbMU9TJaaTxae9WqB6fG3CzLWLmDZIh%2BVWn65IMHTMDQhdacluaYgPQAhox37q02pEw1FXKVnb8TWs7%2B0qe0Fb%2BrkKvLx723MdAz%2BbhMXvkxASld64z7UDVuhOjtmt7r6pnx7bb0UjBYrWXsuW%2BUl9oyJnQYVoqcP0jabg1HYc%2FW9h2U%2FMj2vuXHmAg3W2jjpJnpmEgvSdcjuK7R5%2BFaxWyisq%2F40MVXFsA9r3PpV89fGyWn2W2usrUU0Ncu6Nj%2BL1LT5jV4c9N1UabISuZIaSazGSpgHdQ58p%2Fho4IttA06%2FlGidQyvrffx7XK03V5SznbwhmLbeya1irm0egw1MNyUvskGOqUBrtC%2Fnqe8UwBwmxtOzdsQq9fpnVkOKaPFcASvU5cu0fj%2Bhj3Ip2JJ%2FH33GMNKEA11lM%2BfV%2BvSG3VJP1iYsO2rRWxRd8PC%2FHOkZ3or6VhCeFxad9xsE7PYaQqMiwEc4u%2FgAvfANutJwIkyywVJVgIepdKtevSmOBqJ3d6nnh8yjIOD3RloaXv%2F5gYmFmvuRhUKkaR5HvSF52LJTRIKO%2BvOqwTLsGIr&X-Amz-Signature=d42e9c00d312e7b1efca5f9c5b4091e0df7d3c52f846f18367683b9888807d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



