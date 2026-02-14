---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FN4YR2I%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICILJI%2BIAIg4%2Fsb2X31%2BlZ%2BeC0dolhtl7gDLWU%2Bo%2Fia6AiAC90JmnpovgIhH3iKri69nRbRgxezG3NCiaToSLH5Z%2FSqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcsZX%2Bz3VFfWEH2r9KtwD7ZNin9Zrv9EbXY9IC2edSHc1Y%2Bt4pmHWKwo8AFjqNN8bvnElyKGqqjZKlYVl3A6iXGEWolMG5RZVPMDTzuL73WbMkbfO24En9kcG3hXqzPpiB0TTT54%2FNHt%2BpG8UG0a7K20fLP3NYYUeSI4gcVE2DdfqWttkj6TSCLANrl3se7xkEX5sirCDYeFTAN0aKwVHkm3FqeRTJF4AnbUrKMf4SIS8UXs%2BVRKAt3e8H%2BFDnAsiiHhXWlNeLOIWnI97BeYh2%2F1EeJMebmP5QGcLdnG1IDTHX3vHbXKQ7DlE8zf5XLKW6g5ktN8e6f6FyeRq5vzaI4NwwC71rNkhZ37m2lplzXbC9GVeI0Grwv8Uv%2BFj%2Bbia%2F7w96QcwmvGq0KSNuYK0PS66kYkUlfhOjOkM06ymiekuGy9mwPkf3zOw3rHZOxbXat4B5toGCpxJ%2FfDSCyh4hv1cv7DopQy2efzmi%2B31JKVD3f%2Bz8feRdBudtz46O9SeHXQnmO4JX%2BU6tgTZIhFxxbkxCKEEchymmo3%2FEE9KhKL711WtNhWr2PTxeyPyQJ8j0vOM9SvCwzMt7vrLnkiEs2Xm0CLqZJIgHxZUqVpCIqnhvAQqxt68%2FQ6uT%2BEF%2FCqO%2FucwU16cq%2BYxYVIwzcC%2FzAY6pgGdbvTUG%2BgpqmFlxgNv5a%2BkJOxsjy6lWOIvQP1Qtk%2FCjcIK2N43A4oG8cmcF5B8IfLWlGztZuHGrXvJVr%2Fa%2B9RVnmogwiGOre07S4fmCJ9mH6M5Lrjy4S4DxapJTQcg4OSjixOS5Kk2oMLCbnhXStAy%2FpjA9%2B40WTheE2qWMmtT2yeI0OjkCTalV5D0eAEqemxveoGUvJgDt3GixmZA1YSuATfBR8PF&X-Amz-Signature=127407fcf2509079de1b691d65e5889723beb39e66a48b2741614136c49a2e69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



