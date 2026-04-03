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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTAEHVIC%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnZeLt1GNMp0%2BGla716QtgDB1fN%2Fk%2F1pGyu9Mlb58nAAiEA9CN7sGE2cLzkI6JLtlY9mufbkJ7cH42heSvxJtx%2BhSgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEF0oGArSZnwvZVa0SrcAzE2hNNphrzfOEgmlnB2EgP%2BzO2mLy0gYuyCP9ADJd6JTLGsBcD65bbl6MFNqsJRRfUlHj66huqXuTrMYu7%2F99i3ap%2FBNh657bT6NEq9F7K7RJKtqENmYczO55agQHsQOz%2FXVkUYEpJxmvxO3cpbdAHZvn4hEAPa9XRz%2BctnyJutMzbplqd%2F0lvMZKdlmMOubhr1DNQKuGT%2B902aCYdNzoPT%2FKf4DCWCIs7vmTkIfrUjjuk5lCdIY%2FpIaQr49FTQp8Q6ervhAWbIoMjU2XGatMERAkc600%2FaycNpkazq%2F%2BQpERi%2B28SdW%2Fx2QAXeLEusqscPArwNxPth5btwonpcOES6ar6KmEi5fOO%2BmmqiHULYU06ESmpt49iCWWnsmKR7USV7EOV1ywu8Sjng8Y1qx5MSb4ykcoYToaftha%2FP82CuCJmiO0xREV3PGxLS6PY85wOTIPgqkgrE4mRVdBDYLmI68FuoTV0xb6DPmVd38lqZmpwyOiJGAznEGQ7bYq74fOJ%2BOrnZXJZzZf%2Fst6nzD%2FT38WPB3zj4WFOmxaG3N%2FG%2FCapJjsuovfajoshPl2nOdfXhyc9b%2FZo4thrXJQpxCvpDWnuK7Gfm7gbDykvefVmKK625PgoFgzJF6f17MMCvvc4GOqUBlARySR%2F%2Bc8iZqdzeyHePdOGLZXL6uDayQ17H83LVpNA37jyhLUGzm1h4LHwNFXZF5d3njPvCB59wJafU7OF4hwoZU80t8nIcsH1ODalXiFa3pbFpwABsx8E%2BgoE5fM4cPcLEkpJSComTvmVO1BOexLC0kgLzdr4XIpmPySvCWAN8DYlXTpZd7XO13DdxlddGhjT%2BJxYLO6o74sPiVKYSQAatw%2FL5&X-Amz-Signature=5ddc0351978a3db1b3a17e656c569b3db3665caa5a6db88c68e9311986a1c16d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTAEHVIC%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnZeLt1GNMp0%2BGla716QtgDB1fN%2Fk%2F1pGyu9Mlb58nAAiEA9CN7sGE2cLzkI6JLtlY9mufbkJ7cH42heSvxJtx%2BhSgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEF0oGArSZnwvZVa0SrcAzE2hNNphrzfOEgmlnB2EgP%2BzO2mLy0gYuyCP9ADJd6JTLGsBcD65bbl6MFNqsJRRfUlHj66huqXuTrMYu7%2F99i3ap%2FBNh657bT6NEq9F7K7RJKtqENmYczO55agQHsQOz%2FXVkUYEpJxmvxO3cpbdAHZvn4hEAPa9XRz%2BctnyJutMzbplqd%2F0lvMZKdlmMOubhr1DNQKuGT%2B902aCYdNzoPT%2FKf4DCWCIs7vmTkIfrUjjuk5lCdIY%2FpIaQr49FTQp8Q6ervhAWbIoMjU2XGatMERAkc600%2FaycNpkazq%2F%2BQpERi%2B28SdW%2Fx2QAXeLEusqscPArwNxPth5btwonpcOES6ar6KmEi5fOO%2BmmqiHULYU06ESmpt49iCWWnsmKR7USV7EOV1ywu8Sjng8Y1qx5MSb4ykcoYToaftha%2FP82CuCJmiO0xREV3PGxLS6PY85wOTIPgqkgrE4mRVdBDYLmI68FuoTV0xb6DPmVd38lqZmpwyOiJGAznEGQ7bYq74fOJ%2BOrnZXJZzZf%2Fst6nzD%2FT38WPB3zj4WFOmxaG3N%2FG%2FCapJjsuovfajoshPl2nOdfXhyc9b%2FZo4thrXJQpxCvpDWnuK7Gfm7gbDykvefVmKK625PgoFgzJF6f17MMCvvc4GOqUBlARySR%2F%2Bc8iZqdzeyHePdOGLZXL6uDayQ17H83LVpNA37jyhLUGzm1h4LHwNFXZF5d3njPvCB59wJafU7OF4hwoZU80t8nIcsH1ODalXiFa3pbFpwABsx8E%2BgoE5fM4cPcLEkpJSComTvmVO1BOexLC0kgLzdr4XIpmPySvCWAN8DYlXTpZd7XO13DdxlddGhjT%2BJxYLO6o74sPiVKYSQAatw%2FL5&X-Amz-Signature=847d9230f30abb03d2c2f4b396f295ee68286cad2fcbcede1bff0e446871e777&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



