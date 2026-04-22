---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUIUBJ3O%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQD8jxodOsJy%2Bpa3Wd%2Bpxv7N0%2B4ASc2EooxNPVnht%2BFOAgIgeR%2F%2FuFCtp%2BzXlHhZknkz%2ByIv%2FYZREvpOrwP%2BEgNzrLwq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE99jl80qwEw9540USrcAytvjFRAr3%2F05zsbecdhQ3bWGA6unbtF6gNBfz0Bvvms4gpj18at%2Fw52Y%2Fq9HW9sKyJiq0mixWXn7XZoXJ4Kg5EggY0hpAvnjNdjAVdD0ehbm8yNS%2BGvcrKGhOmMMU4gXgncUSo1290MX3fRxJoqIeBROVhUB2XzHNfPAedFJctIvFtH9HOLQXjEY9EDyyA26pbh8PP65T%2FYjxeWXXDH82d3d%2FU2LMM5hGO90sKFjc5JsmGW10KP420x4MsradvG7%2Fyg1z0s%2BJkK1XMLVNm1ZKbt9JKEIaG6rEAOe0WhVCfC%2FpdGkc60%2FWz2EHm%2FjjDyinTxdUIriFVH%2BBssZd09AecQbzyCUQwrq%2BLlQwLnraZKlkY5Mov5cJrRkvUryVbR9bn4TwBc6ZSHqp0SlVR%2BvXO3DDFwR9hdqy9hBTMwnTagrp0JsBe75jjJydCq%2F7Kxo%2B2EVuqsJxojxvfr3XMn9RcNdpbV05G3lALVeEgyRaNQ%2BiqgRvPoN2toJvYhLCCCvzfaglfbRO1bAW2tSGNvRae7Hg%2F1S53rjQsinJ%2BnFZNG0MV1OIrB8n7VK%2BSscmzXYTiYD1u%2BGyLAKDTX6lSlYQ6HkpudlbLx1Qus%2Fc7TxVi5rQMmMz9b0t0WkkR2MJ78oM8GOqUBYngIws%2BQhL8E8m4cQfpas5Fp2Y7A%2Fsr2hlCq%2B6XMOgZ6RSKFPWGETl0Q%2FlvN7E5T6YFFJKHhnaT4Fk0x5tnTpQ%2Brxl26GAFi%2FZSGV2TXLC06c4Vj99P816qdJuQ8gd4EgiwKv2MwFdm1gtBYxtKNAY%2B6a8AfjCylH15wiTH891Xe9s13lhfQrFrHjXLPdKujxBslll7JDQSFG6R0hWMmGN5QkRP%2B&X-Amz-Signature=ed15501db665b9c01d723ee3f22fdf1ed3d56b750d3de1a28fc4f0f95b6428c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

