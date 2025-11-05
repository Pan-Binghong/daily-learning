---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PHLVBEL%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvEZebL%2B3mL9MlKuMHc7UDYkufm%2BBGxkK9uVG0DSE8EAiEA8GNtcphKklx2cdk7nFi0Z8eIQ6iTVD2Hs%2B7gquITDxAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCiCHcln0bAcTQAkPircAxd0%2FQNgLc%2FtcyZz6vFSR994PAEC1EjBdEaoTLXGbLjGaqODvxRv68CJy94sza6aS%2BWaN0rkrxwjri4IcFqvf5Z8PIgr4o13LH8vZMoso1vta0cYw%2Bf7eVSM2RlxCLzmOrw5guT1ogt7oxZqVr3eMquBWur701QOrDnj185bZZptnqRdIs9NPkA%2B8GJJIvY2oMzq1cRKtwGyJaAhsDkblfrjlLv5P6piUELwxVpBFVzAuLqWtVp7P2glLaKXNJEiLziCxpYW08WcF%2BK1rz63n59H6U%2FZqjBiE%2Bq0ZCqdg22l1my7uombF5CJHcVVIfaCRIYinuvV8dtJdGfoBvUe%2BbMR70dWqbDrjgkhx4sP%2BV4dDBOjycTKt%2FQbqSWGbVG04WETl%2BfIwbX7nnOSPXP81vyrvLBBFCXzQCT%2BaEimEB75NZL%2F5ZrzuuLKm%2B797Z1HYB3ah3iaVShO%2B11YasTJeMlkZ%2B%2FKUX066DYXZlmOvOiL%2F8lBmyNbLjyI9ZEzxy2jy%2FYIj4KNagmVK7e7TGxMZ2ozmrGt%2BT7OhOSMCkrEtrKg4KmpTYiYNHMVtitR4zoWEvTELy4BRw4sIn21aGMJcEiMnyosp02Zbm5snVDcqbDIUq%2BGbdsqdw9yDvOKMMKfrMgGOqUBm%2B5Jz8sWDRS52SXjWi0Lnh5FCrtvoTH627Lc3J8Nl5ao82fcO1UKk8vttmoWcx04yJIbBUaaNRFZm5tbiMk%2Fzp74I1IWlHNfhwrgQteCKW5WSVG9k1unkes5svo%2Fsl%2BwrHH3pSQ%2BGLuK1yyiG1j8Tnwq44eOYS7Gl5MdgZHVbOs%2B4MAebNysDJCB3IrgQIEmUi1ZPuQKUQY6Vy5AGaVUjkHFwuxm&X-Amz-Signature=71439a7bd38aefb127dbe38cee3a1eb875964b91df91c7dfdb5f765216d174a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PHLVBEL%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvEZebL%2B3mL9MlKuMHc7UDYkufm%2BBGxkK9uVG0DSE8EAiEA8GNtcphKklx2cdk7nFi0Z8eIQ6iTVD2Hs%2B7gquITDxAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCiCHcln0bAcTQAkPircAxd0%2FQNgLc%2FtcyZz6vFSR994PAEC1EjBdEaoTLXGbLjGaqODvxRv68CJy94sza6aS%2BWaN0rkrxwjri4IcFqvf5Z8PIgr4o13LH8vZMoso1vta0cYw%2Bf7eVSM2RlxCLzmOrw5guT1ogt7oxZqVr3eMquBWur701QOrDnj185bZZptnqRdIs9NPkA%2B8GJJIvY2oMzq1cRKtwGyJaAhsDkblfrjlLv5P6piUELwxVpBFVzAuLqWtVp7P2glLaKXNJEiLziCxpYW08WcF%2BK1rz63n59H6U%2FZqjBiE%2Bq0ZCqdg22l1my7uombF5CJHcVVIfaCRIYinuvV8dtJdGfoBvUe%2BbMR70dWqbDrjgkhx4sP%2BV4dDBOjycTKt%2FQbqSWGbVG04WETl%2BfIwbX7nnOSPXP81vyrvLBBFCXzQCT%2BaEimEB75NZL%2F5ZrzuuLKm%2B797Z1HYB3ah3iaVShO%2B11YasTJeMlkZ%2B%2FKUX066DYXZlmOvOiL%2F8lBmyNbLjyI9ZEzxy2jy%2FYIj4KNagmVK7e7TGxMZ2ozmrGt%2BT7OhOSMCkrEtrKg4KmpTYiYNHMVtitR4zoWEvTELy4BRw4sIn21aGMJcEiMnyosp02Zbm5snVDcqbDIUq%2BGbdsqdw9yDvOKMMKfrMgGOqUBm%2B5Jz8sWDRS52SXjWi0Lnh5FCrtvoTH627Lc3J8Nl5ao82fcO1UKk8vttmoWcx04yJIbBUaaNRFZm5tbiMk%2Fzp74I1IWlHNfhwrgQteCKW5WSVG9k1unkes5svo%2Fsl%2BwrHH3pSQ%2BGLuK1yyiG1j8Tnwq44eOYS7Gl5MdgZHVbOs%2B4MAebNysDJCB3IrgQIEmUi1ZPuQKUQY6Vy5AGaVUjkHFwuxm&X-Amz-Signature=c929ed2d70d3560cbef5c21805b30c29915435dca16dab7e621aeb79210c05f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



