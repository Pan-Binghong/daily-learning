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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMKY335I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHF6BkhnEB6LN0CNT6KlviP%2FYepqHFf9FTb82H2FeaLUAiABZFuk9A5qJYUfDOuVs%2BL7CAiqyiEDP4JBlMlrbW1w8iqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVnz0dPrCtx2kcuVPKtwDWD8P43RzmQdpcx5pAHhy8GhQA6ScUX%2B%2FYPZmK4HbIiXroCt0f3YWnzTG55uPDRFScTncfj8PNmHKaaRNxJ4XwepRi4fBFoJnjEmDtQ7OhPqBkaMNFetPGt%2Fe6Jf6CJBUrsWH%2F7TqlueLVR4oAcubcIt4Eii4XZLUeFgX09Tcqcv4fknMrqBwodbj4Gl7JvJkBSBj4%2Fljam7vYv7lYe4kHdjgJuf9q8JakvKnG%2BT42zKozemHKPD9PWIOOPV44JiSU%2B74KGhcc3m4LhiJBRxewDpF8iorFb%2FmbtgiQVmqSa15AvfqUUmI0C8EltGZNFQGmniTz5l5nwi%2FMo5Bj6zx%2F4I%2BVYSdZlhcU8m2MeOjigeCdC5zpw79nQV9L4iGp5LJHJVGGffTCqluBF3Yh7opEE8vT5Hzu982PTqjMT4KOdkOI0jbGqFuiTPeOgXIjdQeaROSjANnhPxNpI4KdCZ%2Fa1n5m2oPXOwNGomlnfBIDbr5hrlqwO2U8Ajr9acWTNKKvEekCgdm3bMCX5rFXaE5echvA%2FZXxcyZNSielOJOQM9idz0Pr%2BGSaoJ0tWRl7TR33GM856wfZcUlux5YCYvxykrAPR6FMJ17PTIZBB0SDjUNmaANh65CvpChNTww7PGvyAY6pgH5WEUK3wOdKVbrOXFmb9OJITH97fCWkTEzX65Tqylyhp1lAb4zRjsqiZpBgacKVYBUeEt8onUxg9vcozDri%2FqOtl57Nb6OYpOcD32nNy5az7p3LCyNqWqdyK1yCgSSwJ4ABAbbC5LVsaJKypgJRy9nAbX51Y9ihXoEM5UdbX5Eh0qKru%2BUwa1HMz9CZz2YL0RncFwHqdfIHOS47DvXQhAH87zyf793&X-Amz-Signature=67d28878ff4dbeefd40937ca43faee0d39dcbd42948529afb81c40d037dbb49f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMKY335I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHF6BkhnEB6LN0CNT6KlviP%2FYepqHFf9FTb82H2FeaLUAiABZFuk9A5qJYUfDOuVs%2BL7CAiqyiEDP4JBlMlrbW1w8iqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVnz0dPrCtx2kcuVPKtwDWD8P43RzmQdpcx5pAHhy8GhQA6ScUX%2B%2FYPZmK4HbIiXroCt0f3YWnzTG55uPDRFScTncfj8PNmHKaaRNxJ4XwepRi4fBFoJnjEmDtQ7OhPqBkaMNFetPGt%2Fe6Jf6CJBUrsWH%2F7TqlueLVR4oAcubcIt4Eii4XZLUeFgX09Tcqcv4fknMrqBwodbj4Gl7JvJkBSBj4%2Fljam7vYv7lYe4kHdjgJuf9q8JakvKnG%2BT42zKozemHKPD9PWIOOPV44JiSU%2B74KGhcc3m4LhiJBRxewDpF8iorFb%2FmbtgiQVmqSa15AvfqUUmI0C8EltGZNFQGmniTz5l5nwi%2FMo5Bj6zx%2F4I%2BVYSdZlhcU8m2MeOjigeCdC5zpw79nQV9L4iGp5LJHJVGGffTCqluBF3Yh7opEE8vT5Hzu982PTqjMT4KOdkOI0jbGqFuiTPeOgXIjdQeaROSjANnhPxNpI4KdCZ%2Fa1n5m2oPXOwNGomlnfBIDbr5hrlqwO2U8Ajr9acWTNKKvEekCgdm3bMCX5rFXaE5echvA%2FZXxcyZNSielOJOQM9idz0Pr%2BGSaoJ0tWRl7TR33GM856wfZcUlux5YCYvxykrAPR6FMJ17PTIZBB0SDjUNmaANh65CvpChNTww7PGvyAY6pgH5WEUK3wOdKVbrOXFmb9OJITH97fCWkTEzX65Tqylyhp1lAb4zRjsqiZpBgacKVYBUeEt8onUxg9vcozDri%2FqOtl57Nb6OYpOcD32nNy5az7p3LCyNqWqdyK1yCgSSwJ4ABAbbC5LVsaJKypgJRy9nAbX51Y9ihXoEM5UdbX5Eh0qKru%2BUwa1HMz9CZz2YL0RncFwHqdfIHOS47DvXQhAH87zyf793&X-Amz-Signature=492654a72467a788a433c3f1753a92293c2925ba26e0858169ce39b36747db15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



