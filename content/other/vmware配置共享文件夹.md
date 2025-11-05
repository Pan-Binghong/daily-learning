---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SOETSDI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl46vMLCSXU2eRMTeUTqzqL8WNQfUZ4EB9gO5fZlwhYAIhAKMakhKPnttKV8ESp2HZyWqDFVKRyxaqnxxEZdllRHsyKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKIBifHzkwnOIeUAIq3AOLgs6T3cVLXoS%2Fz%2BrbDLkPNTJolwSeuJhDz4KWit69PtK9yU5jW1VFOS7V2wfT%2FCwf88MW2e66ZXcqaYxxzYof1t9C95cdwujlyE9RAT460QX9QnRzrMamadOk1MFcpLkhl%2BAU9yxgUyaYhZnnFQRwaZCsWTGQsmLNNDHo9a477NWnshbXAtg3rtbUrID8zFbK18FHqqdv0iuQ5Z%2BX8Bjm6L%2Fl1BQzqQTuFVGW16c%2FzjNn%2Fv1SBuhmDd%2FIiKOjnpurvECkVDKW2ju6Gt0gRm91EVehwH0tGgF%2BimPqB0fGZ87NZYUim68kogA2g7nlDrnbDF0OorKIVVRJU9QaU7ORKLkCcyp1L4Ekg9tvnrSsdqhuJBgxT7fbCJwvM9%2BUjxDpR71DGVyi90OXGXoG%2BEkhW5fyc6UsRP%2F94RSPEWJA%2B5jIhjzvsuJPqBJiQIDeOxSz9M9LmQltB8VqklBw4xkokrBf5QeAv%2FWQqRet4B5qGYFQH0Cz9ibbWIpny%2F1wTFjLevUb%2FfvYUq7XIwdsrylyUmox1B97zrJm%2BCunPeAcbCAjDbGWS3zzvsshTPQ49eMPyhiFGjd8KBQV%2Fjv9b%2F%2FEm9aB4DgLYXturq64sUcQY8yhBivga%2FpaeXzntDCwoqzIBjqkAQaBfxxVSVQLqW%2FBGJwVmDS200YtxqTWWgw5aei9kBZQ4iSwYMivP7OXyjiZc4duZTFhEUMimMfJ5yuW3tQMpSSZf4%2F9XvEeV0UpQLXtTDWuDkEKeWeFV1W%2Ft3SMLePLvOiUsFBqKn2Ghys8M2R%2FEY57yGuVLYsnZtTE04o2pkAfaZZRccXqrPzHpeEM18gfzjyBg73Dj29T%2BPVkOCe%2B%2FYaRWnDF&X-Amz-Signature=15507af770e4e63511690c978372cf48ac9dfdd02551405f929db30ce4f027fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



