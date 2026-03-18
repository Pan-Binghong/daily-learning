---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVULFFGQ%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICKmKjiLvD%2BwgE8Lu5iEpUccvQRulf3k0aGX2bin27OEAiEAwDWUGIsDq9UMcQg%2FsYVe9UhYki3tImg%2FvsxghePzdkYqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIfZBcRDRjlBYAQ0CrcA6XZkHs15huGHDzlnkfvVWB7LuIe5jC6LcbT1LVgEtE4PztqICjIQOCbjB%2FOWFdga6GEXRsmNu51T0j4RmyYWgnbtfBE0rrhg9RzLc0F06AX63rOvIbaUma3eHfBoYXnDeA3%2B%2BUaTFjSIBMifUQKg4ZCbJfRmKe6ilrEUg%2BcSJidg2hAbqlRUh%2FtGs%2FKu63yDMV5KlAkh29eo4vyDhAviyfkUmkh%2BpYDDMP4qFJu1OtsrgOCHqqDCl7uJRhjf%2FPIGRaMWlwobklep7Sj0xKniEx2AdXYqmWv75uzoZOlw1gJ%2Bg9FpiCeluImITHPyv93GyXY5BKVqDeFmYcDkgBs0NVt7InuM2t3sYbz3pVGgmK76UriM9M8uVGQkksVBJ0EU%2B%2FVH5HbKVM3mCRbr%2BgWkYzelOFC1xUt9txChREzO0STcteuyePRfFhC2hB7RoMfQy1ylVMVvpkb%2FtTT6vZJmQxRgqOcrrq9yexvYfUMYPenSq0%2FxPRx4CHtJAK5KKmbs9MtK8TlgKi4tFJgO%2BUUrMVds5uk6raPnJA26dPfmegudLu2yim4DGVNuNal38daaCEIkQeia%2BPj9bvy5LkUpcKttgczTSHXQARXjP7LXCNybYjGNQ%2B34h%2BlPqTMMP6m6M0GOqUBkt23%2BA9SiR9zFWFU97nRDTMgTRAr2G3D%2FHIYYYduqh0J5txflmxcjhLHabSzMar4VHOl2NY%2BU2gZU%2FDcfniG%2BHbnV9ci%2BA4oi0KAHvh%2BF6DxUIWwYOKwR2VLCvq6f7ueBO8oOhWi6uYph0vTTO8QIi4y%2B6XpnDnkz%2FCtc0QFgL0qAV5u0GsAoofoetFNIIH8KkIudWMHgfRyFkQ9WDynYABLCJ3t&X-Amz-Signature=7bc00ad5c5a5fba210f95a32a0847f47f1036ab6c9c03d3352c3d4ef8976c166&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 分支说明

最常见的三种类型分支，名称与解释。

- main
- develop
- test
开发人员经常创建的两种临时分支。

- featrue（功能）
- bugfix（Bug修复）
---

## 工作环境常用命令

### Git基础常用命令

> 💡 想多看就继续看吧。以下主要涉及：上传并提交，合并，标签等操作。

1. 添加到暂存区
1. 提交到HEAD
1. 提交到服务器内的仓库中
1. 分支操作
1. 拉取以及合并
1. 标签
1. 替换本地改动
---

### Git常用配置

- 解决win和linux换行符格式问题
- 解决旧版本初始化分支名称为master问题
---

### 实战经历

```bash
# 初始化本地仓库
git init

# 创建并切换到 main 分支
git checkout -b main

# 添加文件
git add .

# 初始提交
git commit -m "Initial commit"

# 推送代码到远程仓库
git push -u origin main
```

> References

