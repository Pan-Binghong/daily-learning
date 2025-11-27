---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHVPXXTP%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCae6w7UfgRYrO0Z6F6lN0JveU%2BCXDwNGp25OgGEiqQdQIhAM8isLF7BhfLlGkjmjDtXzTR8y0VHbPOOFrcjVEsZ1ELKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeoMeFpcXSAoEK1eMq3AMsXp7BOZbDV%2F8fFRKZli2kY1DtyGbdU%2F6ADUB5i%2Bpt3Qo3wpLu2ssz0KO1YJ2OXzm3c4MDdPP7QqVfSY8eWToS4F%2FG4KOMFmC%2FLPTluSsSesXDuZqRrVjH9PQOmjIXneVUj5qerTGCdLV2CJAXT4%2FiHsOpXc7lJMZf8dZGH3hqHbEC%2BfT59ME4UfmlZH9VdX6k5dz2RhRNV1l3PBPRJqOi6rbyfbSMnOkwOeUtXaNi8jquZeOOV5wFjrJknJaKKKjTjxDGPy9IxHCvapThBphrS4gK9DWCbeXr5k6PI1e1irv1sJpH8zQcbNSoF9EEY2YtHKlZsqM9uOwl1GCHlRxaJlUel5cQxQc7Oxc0NZSJyCLmPY1x%2FDQ%2FQUBahwbfFW1fZpXkVoS5GJB62gdAwVY8FZUCAMgllXXlByE46lLHHY4aaT8sOUAyiv2gs4D%2Fjf5xUJWF%2FNSk8nHIxp6NAPvWulsGbqRsr%2FjgYShm4OaW12InoXg6MpSEyeM6GYdUQFCbx4pSW1z59Iuta3QjntLEEXCoMxKOf5xI84OgcVMh6HAmyF9RKLxRrknli5TXtDPlg1ne51pd58SC0vb9W4FD0zhFhEPQ%2FDs9xqmvG7%2FP1NJcv3dNQN4IF%2BQsjTCs5J7JBjqkAUvtQDlAiw6MUcy5CBCSVhVnjYK4m9%2FXf5lhhchAWZn56oigXrM4PQ4isTxtaC4hOzFkw6KvhC%2BiZL16f30bcf1Rp30w%2BpbxCy2iUisWOv8LSGCYA%2FYk3a76%2B12KnSqe0rdkROkjzQLVsaW3wqZGnLmMizk9s%2BQ5H3pJPNWL2amb6aWy2auRyQ%2F%2B89E3sKaGQvg95zy%2BrdYBETY7kkHMjxN%2FQWO2&X-Amz-Signature=f3f435b46113fd618d5fdd9dbfce14ab66ea97a2d983a5d8b2553d8b0cdf0be5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



