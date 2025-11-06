---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662US4C2LH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICwQGTgPmWTVpyHVXiwsKCqVhE55PYZqngAAZ4CdApctAiEAuHrawYmx1l9Dv4TSJvYRJCLR1J47jUcz1%2FmDCd1iq8gqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwEgqdM%2B15aynn7cyrcA15mItJxdmUGwlwpxUgltIvDr6oCksFC7cjsLc1RbR5%2BBEYJ2%2FTfHeamVkSQKJy7yON2iH9cjTVUL2si08hKZ%2BSdgesIop0Ramek1YnIKxNyLrDuuRi%2Fy771BIy%2FRznTzTKXM0huE7Ioz58VLjyir1kaPrI56r5VcrJz4nPjV4FfGxLY0wzmAZiQ%2B4%2BqESbKE4THzsZx8ecYoqNtg%2FkVjP815RiLxU16nDz%2BgELqIJwnEvNzSq7bNqa%2BRTUZmG1sBjvXAaqM%2BnUYm79hgklayxWQZOSmdviDBs9Gw2IEdFMjgALuAIzK%2BU2jT%2BXKmm8tja7DNQA7w2SujCS1E6xh74Tu0tVIgMUchPhCflnduGeyPlR8fh%2B3%2BuUb%2BE%2BzMIcXn1DB3S%2B%2Btg%2BMWeq62hNAEw9opC5KB1RDmJpe594q6fjXvcvJ7mxQvC%2FBrbsweKoNEccK0r93r7JPxvsEdGtM7JMTFe4CvVAyK965eremaUZCshHNeKNMX1BKVARq7OVJ7s1qM0AhDk2jvh168gi3HFHWsWQDkt3RKwfAaJhTMzTimTQquBkONbqo%2FY1trSQKdsSubXcyF5Knk%2BHFo2SAZMze4Nmq6uw8IVJ61M0eh%2FZVLy4qMIUVP7rdr6hEMLPyr8gGOqUBXJkUQwWikOOWF4GoCglg2j6KZytB28EssqUvAXnqYtyR7r9fO2T4cRK3RsVG3FtZHhg2IQsQwhkJ1eNuOvCYRVgrqxYjnPbrdAFYBClN0%2FhROsYfhEVw491XTSfDpY8R5%2Fy4izuHNuXAMkQC1WBO2Escl6FK%2FKLEQTZHX8mkEJaiL2h6HhbGz1Af6%2Buy6NsrQJJORqmfuzBoCMjXA0hM%2FjxHsOee&X-Amz-Signature=5227b6a0b20597a3bab619aba127fc3dc0212eff6ebb8bfc1c5dd560604ca62e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



