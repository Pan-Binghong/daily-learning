---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPATINWP%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0noAIRXJ6hIMX6P%2FvDrBtI1Wbctd5L3PWCeC4s1%2BbswIgDrFFWt%2FqpqBhrwRJx2Gke84SR7anqK8%2B3tVBtgZIO6Aq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDE%2FEaKMTLmY3X%2BEJMCrcA9IBQ24abuUMfqRj8i9saCTmVpQfBYAYZqbfOXFFCtx1oECwNdUnXpc%2BwLrCGn0i0WRHc%2FSuUqA2lc18l2oV0CT%2Fyi8VW3VfQm9xRv8jG0c6dTx3HI8PlXumx1y3H3Mj896bmL5XI61w4LUBCfdSQLAk%2FOaVdIhve8PmBszZ54oayS6T1u0A3%2Fd67gm17tNJlwuo1XxmaBhPedD%2F0c9I6tA%2B%2B8PVQ%2BBIEohH2ysW7%2BikCEKsvn%2BtwFfIkqNIJzBCrCnOwIIsOLetdbuzcDtVHzDbpBa0WPKk33Bd3rrrccgnGLho0iXR9T5kytDXarl7jTRiCXUKhIAynatI7HgZpxoF0Qe4OoCkPXVI2vFJWDjP3i52dRit7NH0Q%2Bd%2BRMPjWWjCLVy9y3ExNSNaOa24OqcHZuE8iNvegoBwa%2B%2BwRpkitsFodkhob6lsjTf%2FusDbxSpDepLLVAVzHwojzGuJws6f64JyUdvt3RjNahOT1PHgRZoYCj0aA2d0EOreF%2FIcXgnR%2Bnt%2B8VXg5nuw436TxuacL1U%2FDYcQI0dvao5m9cYfJwT%2BFN%2FCDoyQp5h7HDfarH%2BE3HsbNJcFDd1E1fS2Vkj10ww5CytNqY%2FZxnSxf1ByZTot9fuEOUm8463vMNGyyM0GOqUBr0zGi5q6GhC0rBho94N0xSJdhkHCBjxJzqqpVmYfM%2BU6ZMM%2FZ7F7BBR%2FLi49zOAKzI9ElfG5n9a86mrlVXEHYuI%2FqL27MifmftP2BouIlDepCf11aov2Gdca2rX1TiRdruVpVGFjUUWtGzV%2BmY4F5hiI3n8cn2ScDf2oQsusR40vzbeZbf6wBSp%2FyZWYb2yRxi%2F5evRB%2FMxrWK7UXzTRRZi%2FALjw&X-Amz-Signature=af3a26fc296778c3027ba58bb903c3a470a4e6b7ed067308abeb3f8e1edd9573&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



