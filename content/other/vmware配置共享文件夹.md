---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUJL2DAE%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj1eVFLAblADTenOiKn%2FgN%2F%2BWuUB4BtqMmBm8qfIwxMAIhAJScIcaIfhRaTo%2B%2B5zTBZAyP5Ynl7Vr2UH6Up47Rc%2FktKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKaUiDbRwF24%2FE%2BA0q3AMfVY%2B%2B2nl6VkYI96fqYwGRQa40uJd5cXgZzrbXx%2BK%2FC1pAWPj9ru88nqrwj6EL21dsrvkyZMq5Z%2BQQn1nfrE7G7AfZqmkPF0s12Fv8l8RNCIi24WPP0shKxvQnnM0O71FPFUreoidnCDzHc9lO7Eqt7LGf6vXXay87TlNDXoBZE2srPOPmPtL91AREmZ7Fs1MNq4XYM8EGIDbfbKTuViOISRVq8eLd9%2BPw3Ko7%2FzTBFIZvXvXmoWtkW5oyzs7LCZc1sSvbzT%2FL2Rnr5cbz3sp%2BkVY%2Bo7CnLlG%2BUpteWAbnDA4ovf498kmyw2U0YPfSFz9o7nAKNqgEkjZSoNgHQhygzUwlzakoF7qSju8TrwbPr%2BgDgzAX09Bm8JGgMMD0RDKs2V%2Fja0u%2BJc3P%2F9s8F9Y5TXkabxp8oka%2BUNsD%2F%2F4Qf2lhUbIAsSqCl77S37z0adzIVRCGUjHNvgq7lUbs0CXKLUsytqh0C66wSYSg30ddy9PCer8SKjn8tXcwFo0Zkmtec0s7JGB8cRgrj7jOjW7nsPlgN76g5MTWSIjfpx5bjHM9We4Fe0%2BnUgkvzPbr3CJdA4we2HQuKpMiuR0CMFp%2FuG2qcKlwC97k0KAzKHJy9AFu81s7Hr6F%2B8JXaTDx3vbOBjqkAbprh16HtYHLsups2I2CZWrTMRMzQqFd9ZtOtHKLnuYADBYVl6RbmEoD%2Fk8TArcPi4tO%2F%2FIqxrHSUKTU%2BHU5QLvxUBmDV%2F9JMlnpwofY9hzXCMLl%2B%2BaiimfAIPlQX8GzEeXbFRr%2BmSIHdidQU38KtRHsSm5qbGam8mXyAPmgm9kIQ97I6%2B3JQLz4lsKTUP2pv%2BSzWlHIHlSKgsw%2F7C9%2Bbjs0s8OM&X-Amz-Signature=5446107ce3867be02c7576404350a8e66e544b64cac85769f73269a2972453f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



