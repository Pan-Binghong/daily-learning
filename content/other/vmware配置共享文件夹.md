---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA34LMQZ%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIF1rjoIUEh%2BfJvNhEGK%2FVv4g9XDJOCXrr9HVQ4d0zb%2FmAiABNA%2F70ibT1CbimAK4XT7y1VJJzFRkT7LZbAOfxqGVKCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMn%2F%2BR3%2F0%2FFhl5AfW6KtwDR2AhsErcTQclJqoDUTbe%2ByvAeI5cE2QSI8rwXAjq9yBTCeRsU%2B5tSa%2FhiPJ9g1V6QOz0uIy%2Bubrx4N4O3Ue5EBvKtHgmQepmRguTfYOApLOmnrev5v9EbMCsAiXWVBXHz22CINGu6vaK2gQHf858wz5ptO4AcCU%2BAIar4VOsJANANoGC90xjnoFkBmstWc6TADU3o2O6Zy%2FD2W5HnLkVv0RHeNmsf6dAGz4GnBJN34HHZ3FUcGYMETDRwiGJvbxKUoi59i6CbyIaG44DeuxhoQ5PxAL1C1bfI9UX2cu9wEkYWlt8ZsOmn59S1%2FfwoJ3f37i28gGt4yBtJmL%2FHrE8pfcd5pouYksrSm3xs%2F3M3vl7buYvUu%2BQbQ9QpxZn%2BMkvqiy2XdE2nzGOEG%2FgWLnWaKwCOfIv4%2FsBvL5x5XN1A2Pwq4r2eA2%2BVFMv1Got3aoa9F1GRYJyEcna%2BhqFcg5NAb8f27yruu0zVBOqisEnMV28mot8nRFCGO28u0KQl%2BQE70cUBV4uCtdu%2BbDf8jlg%2BsEEHDriqie7Yn7wZJrZY99F1BCfhhf9tBuKTOC606%2Fbd%2BNy6uqRUdtvudCUzMea%2BS1xUCY7qviz%2F5JESO2TV9DqXvTBp7tSFmnwAg4w7ZvmygY6pgEysZPlkojisTdCr79ZR3CgklofZhC0pPJC7KtPGn0QsxszHNpWYnGXygGXl3X9F9l1dSQMnGQUE4apoX3aQOEzSW%2FRmRARyRW9fXMaBzBbMDhxljYB3KiTZAIaUK2qV9cHhLfLWuxmQWjCMHqAUnUhto%2F88ZC8sVGa%2FE34Hjx6BNX16rOCB0O74a9Uts%2BJcd4LsZZs3IGmJueL%2Bn4Bx5XTOOdM%2BlHi&X-Amz-Signature=cba6eca2b05a8a0ad42799c716ea8b8a9d17079fab984d9a31244d2dc8590156&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



