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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ4XFEMC%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkt2N1JdotMXwyZ0u%2BtiRDIIZzIcSSkGrODYMUPVvMQAiA8h358HP%2FTxqayKAxauLET%2B5L7B%2B138tfxtmbFEofNriqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPVj7jwfO%2B7Rt4ZuMKtwDbXVZqh9DaM4iRkHlnYwNC30zmaryB2rWrJLGaAnq915qgzfKaxZXHpcD%2BHDmmHolhr6oraHpIYWe%2BPGouBrZLAdzqU0ythh4RbA9KYnBlp4%2BMU0NbkvtZSGUNQ4cyH97iMzhHUtHU79i3LRxe%2BkTYTbrCKITU%2FxmZnNTejeEiOc82x7PWImZC5eqklhv477nMT%2FyPT5xriU6TGy%2FNgrpnWMnG7w4LX6RJakNxO9ntVckoyeNE3eiiChzokczFpi%2FqXxObApLdww8lFzm2jKyYarshBWjYwYP4VLSJhxM%2Fe8I2Ur2s5uRc8qB%2BE5VgEwLDlTzN3QVGf3HfEtCr9p5xeKDluvjV8mPoCBBub56GsMifCEHc6Ya5N0CL3x9NucYLyxWt0QZT6DMWy4gnUaDVBMB734FisZXousruYTH1D7g0U6XH9J1zx8ZqkLc1c5y3uQ7UEskRGzTV%2FQa00CkrZRtNx0Z7Wy6YEavh2uxeE5UeWEQqBRame2CqEdwJE4pjFYNKngpIe6NLTh2sW73ssYfMXT6tfqyDZgUtFvzfoveGDBFbU4a3Q1pznBnB0Vv7gQoVOJDKQVPedgblaUeDBReoCW1P14cEP%2BpMistzBRrL0fX3ZsTVFNaKR4wxpHfzAY6pgEGcHhiiuF5My7gvus0zVndbIXBAVSgtUUhP6RAMm0EikzqG18FU%2FTnx5HCNe70Xi0%2FLZkWRSoi5h7hkscz3Usrz2PyGQjSUhHnXRO9wSVeYOOd5mRyShhcxPnX45bKD6Vb3%2Bs5BDC0zqJzYMGiqeHJocT1X8%2BL3wQT3EmGj7PWG7uzBjTvv1Cpyqxomam%2F6PZsyD1GPs1vWd73qByAGhLH7HnCNUWW&X-Amz-Signature=00286e0e58e9fcf90f5445d624bd525096411aed0c37a509875b89efb56c0a16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

