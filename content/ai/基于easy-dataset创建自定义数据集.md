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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IA6BCIC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCjFI5Ht%2BnJhULcarkS11mTety6wocXCmoHEfWKoK7e7gIhALv80MoiZHu%2BN3pBXhTRtB8CYM7FhrYdnD6rP2uz290YKv8DCBMQABoMNjM3NDIzMTgzODA1IgwdeM%2B%2BMTWHls6WJoEq3AOminfbfJuky%2BSgl3PC6yjX7E%2FvvGFvwM7gv%2F6u3gn7KbDVi8GD0Ryds%2BRVhnx%2FoS453haxEO%2F7mPMM2FqpBtWSPqIG1oMwr7BO%2FMfmo7AZ%2BwdsR5Lh2SPFdEujYgMRVnEp8ksESzBVpzFkJsXlQcGjsof2gwm4b2ylhaTR19c5TB2TLWTYnjCSHK0M5T7Jgqvl0SOM9VGdPtqwyNBoZmnvjcch4g%2BBapaXy9RVHQoZl4tGZXLy01Nq9UugrWd3z78zZWCVPdcw8WsMi2huJqvMrcRwgHfAEmQ4C8Y%2FO0zDuM%2B0VwAXWGNRNr1BDDhY05zvV8SFMwprTSmZxXZF0wKaOwLb5DSeR1P0xHIUfWvzgG2R%2FrjDfvF8Zjtz4SXtwwwvY4lvYRGHZoItZe9p2ySwE6S6DbgIhWa5rExh4oqJCC%2FBxsz9xgBe2VNA6yxOejQF2PtgkMYF7zvfakTZhSEeAST7dnrSBGdvatt8WxlAIKftCCs00y5HEV1MlXvrJ%2BdAm8saNj%2FB9v4WpPfNz2SA8YjFxBh%2B6nHrYMYgjxJzN5RzkWzO2FHfvcwP6QzVahmr3Ywt%2FcKASdub8dMWW%2FAapHjosJqxMI2DBDj2%2BId%2Bn580RiE6G8kAkhz8YzCbjfPJBjqkAV5LAZpRDP8HG6dL13Mq8O3PY11ZWggxAjY%2FpQJUS%2BhGhVPZ9X%2BOilVbZ4mmftbty27LABWuMfon%2BLNgBb68xqjejQV6jriDPXTQU%2FWOqA89X59R9u90XS7MwXGt0rWCj7QjLY56QT88c2fPlnOor7by6KOscw%2BXhwz0uPQ4iI1ZLavDaeJ%2BNFHh4i%2BopgFRSw5oFpwmatJVkqUushX2v0ZD4j3W&X-Amz-Signature=0dc38b223c2bff39d3a364135997894569e420657929f8baf7dac90aa7c55908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

