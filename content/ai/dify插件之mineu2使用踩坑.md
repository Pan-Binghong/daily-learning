---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULKMS5CX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIH6vAnN7M7zx9ob9dRwvxa7RWzYfoh6ZSOYRGxE0WI9CAiB5HSAm8kcP5faEIEsbJhYKByHc3FF25CO6ffPFyDZ4syr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM208GHc8sZ8nlxDFQKtwDmN5RC7p89rMOxR%2ByyYenTS%2BVIJwJ5s%2B0JXtEp%2FveAXx3ptO9nYQUJ2LaxaMrntKHKnfBwi5PP%2FDsGj%2B68%2BbGv5s2RYhaxBDSIpprJzrGoSMM5WKN2Ah2DFSUwf1b85UA0MHzV42KHNb34LSoWNPkB90IrH3dVZhvhu6GsGl8M6nJU6dtwYPMvFG%2FsjXZSDVv%2BpcK28nb3YnS6E93GnzDZlZ8tx4L2OuQT7c18ZCoRcvOau2CHB3f2jtDox3X%2Fm%2BdTezalzBuM3JO1XFItaB1UEaVBgxZiJpfO26Pxza9XemIFY5kF8xqOneZ7aOz81QtEo%2FpjRay6NcuFZNotkX9uOSbdKHJw4AK6XmX65BF7SfvDhWB5Xthssh40nZd87M616%2B8tTa7JyeZubhXKvZFko0fk4eu68Zm6a6mizMY%2B3nzkyp3hrY8PNjz%2FmHQIgTDrShGsA3ZdV1VO7LLGQ3QNicn8sxB%2FOatujqNnzQ1G4FFTFUtSMniVyvDiY2sY%2BsBCzQvxtasXRVKaViasd%2BJXNVlGgQ8%2FG0UBCzr9idbS4i9qIe%2BmBQ6eUTDCKAt8pso2QJmd2ZJp9UQ%2FCFc%2BKvCjWUTR5mFyOIUCPvBQ3m1M7SGgEF2D7SBsnH%2FmoMw6oT5zAY6pgEVCh11dtsD6phR%2FHZVUsR25Z8qJj1Ta%2FEx5y%2FVPWr6CP406L5LuRmIEh54GaEnXRTUz%2BgdLgoiLdDr9AUbcLg8TpvACfmCyfTcthMD%2FjNbh1PkBvKHnQGPzI%2Fh6cm8ryYC2SZExqkDQTxI3OY6tckxDRJnkihLZcaJ%2Bm5Wrm8qSv%2FHVYoj618TefwAuVmkh5W3qfc9AMhRivU6sK2NO7XyexPekX8L&X-Amz-Signature=9a436afee20916231a24ae8b4f85798d306a0beaaadec8a6318e3074c53663e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULKMS5CX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIH6vAnN7M7zx9ob9dRwvxa7RWzYfoh6ZSOYRGxE0WI9CAiB5HSAm8kcP5faEIEsbJhYKByHc3FF25CO6ffPFyDZ4syr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM208GHc8sZ8nlxDFQKtwDmN5RC7p89rMOxR%2ByyYenTS%2BVIJwJ5s%2B0JXtEp%2FveAXx3ptO9nYQUJ2LaxaMrntKHKnfBwi5PP%2FDsGj%2B68%2BbGv5s2RYhaxBDSIpprJzrGoSMM5WKN2Ah2DFSUwf1b85UA0MHzV42KHNb34LSoWNPkB90IrH3dVZhvhu6GsGl8M6nJU6dtwYPMvFG%2FsjXZSDVv%2BpcK28nb3YnS6E93GnzDZlZ8tx4L2OuQT7c18ZCoRcvOau2CHB3f2jtDox3X%2Fm%2BdTezalzBuM3JO1XFItaB1UEaVBgxZiJpfO26Pxza9XemIFY5kF8xqOneZ7aOz81QtEo%2FpjRay6NcuFZNotkX9uOSbdKHJw4AK6XmX65BF7SfvDhWB5Xthssh40nZd87M616%2B8tTa7JyeZubhXKvZFko0fk4eu68Zm6a6mizMY%2B3nzkyp3hrY8PNjz%2FmHQIgTDrShGsA3ZdV1VO7LLGQ3QNicn8sxB%2FOatujqNnzQ1G4FFTFUtSMniVyvDiY2sY%2BsBCzQvxtasXRVKaViasd%2BJXNVlGgQ8%2FG0UBCzr9idbS4i9qIe%2BmBQ6eUTDCKAt8pso2QJmd2ZJp9UQ%2FCFc%2BKvCjWUTR5mFyOIUCPvBQ3m1M7SGgEF2D7SBsnH%2FmoMw6oT5zAY6pgEVCh11dtsD6phR%2FHZVUsR25Z8qJj1Ta%2FEx5y%2FVPWr6CP406L5LuRmIEh54GaEnXRTUz%2BgdLgoiLdDr9AUbcLg8TpvACfmCyfTcthMD%2FjNbh1PkBvKHnQGPzI%2Fh6cm8ryYC2SZExqkDQTxI3OY6tckxDRJnkihLZcaJ%2Bm5Wrm8qSv%2FHVYoj618TefwAuVmkh5W3qfc9AMhRivU6sK2NO7XyexPekX8L&X-Amz-Signature=ea10a3c82a689a8eda9cd78785214e54fb5e3308d0483927e654a1fc46d262e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



