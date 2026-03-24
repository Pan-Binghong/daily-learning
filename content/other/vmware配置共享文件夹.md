---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NCCIVPI%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMxf%2B84mXNjEYrI76SaARUCBP7lt02of0o2C%2Bj9tFTMQIhAI89A55Htdpsx%2BPEbQ8sXaIrolIjAKwUYtrQSCBWU9qkKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyb9ojnQBDkTw3dt54q3AM8yH0dhLHN507sKSkyT7WJts2TYjde5D9JR5Ww4oIQAbBh60OpzMYHjBhy4UCMZo8Ocl%2B%2FNoojiM9v8%2Frv%2BhzVyeKkrk9RRsye2aWa5bmQufgQgJxbp6nsVd8wgTmdNFsVdMBXLLVswR5b0nahSTbT79uefKRTv%2FCgRAwU8x1MPmaQFIrA7jqFSKATEM3%2Fu2%2BSMC5%2Bbkgg3BiKjod%2BSNwEw820hnGEA5ZKpcQlhl6V%2BdWO1i3C1R2D%2B2rMjvmwxclHJUrD4%2FIzzeStg8RO2W%2FGeZjuehS1%2FRhPK4dv6VP8Az4LBHxuiKbuyI4iC6PnSGqZ9Ki5JR0S8g0bZYsyhBF0bP4P%2B3kZM4Ksdmj3Dk1%2F%2FkMyzo0M6XPtPe6wVfLDFjPk9ngb7Wg1Qott2Yr8bdJEmQ3OvidXybrCEeHo%2FxtYegcTBk6wHdOzNECA4HTbvwoXHB8cWAYkXu1mzKXiRYjaBjcSyZOSszNE6UAZYLcS9eu%2F9xE23yKzyIl%2BCLG33XNPaTMMZROlKcQ9mhGTXggTRJVn7H%2BjD%2F9GwKqPOpAqLECgFuqYns5%2FRtKfXlQWCerGWLL8tmdhWtqXnrdNoNWQbqhOXQRDTYLtZDQS87ajFbt%2FUTsYNAS6MOQSFzDT8ofOBjqkAahg%2B5Pb3q8Gz%2Fg8RLdZVv%2B13Iapa7z0W5s4tvdiL9YToR3tekdwbEgLL3LNUePqO9Ul%2BX2rwCs1ual5yJWjcWfS9fhSbAK1QS2D%2BOZB7wR3lNnbg6DY66OgeGHDc1fBxuD%2FHWDyhcxt5w47iB%2FPea8ZSyf336fMZsZiFHE7sjf5H6d0qBNq%2Bay8A7huPs1uRNpLmidne2OUEhYwEJHh7eR6HT%2Bd&X-Amz-Signature=e1598cbbf51f89006abfaa296a06ff24cee78709356d0ee8e8851eaae76a5fc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



