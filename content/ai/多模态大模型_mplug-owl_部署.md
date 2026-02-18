---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKDOCSPY%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD42yZn2PwLjSZLkVXWnWpFXQW46%2BgWYEU5W9aRE4KeIAIhAPObj9Iv%2BJAHKtEyBa7YuKZkzW%2B8CVGF%2BFjZWH%2B6Dux5Kv8DCFoQABoMNjM3NDIzMTgzODA1Igz9r%2BddUjLxeckvSEEq3AOd3ajDox6FVcK7sSkVd7I1q11aiXc8Q9WYkv4N5vSxPnufsFWjotYQOPnO21Mz2Ne79r0ebt4Cdsqfvs1yl6a4G9Bo2N5oeC65T%2FP7OtpB3lfLgYyR0ackPjkI31i0yq98p7DoGr1axjfPrrqqXoyGCkzA9JH1PpBv4scFp%2FVZDSh0BxRNKspNSFCmNN148mhOAPzHdksErb%2BMe0VDq76PWd73sZQssblXKR0HWxpDfV8kMxdo0L74gf204WjBkfQHWUtJW1pNu3qy47RVJuL5eDjkiNUpd83UB6rto4QytHTT2SZRoXsVqUZ36RpL3qMM%2FzSGFK2GfOSZLcngfxDckzkONPb5DD8y1xgcJ7QbsZgh3TVJJmD4M2FpTn47SGLqHuuCsiO8FpqYyV3KGrI5yjqqEiwRcBtLV716Mb3Fjaoo7%2FbsbwuyOb8UkoHuWDc6%2BR%2BwloBKq0hIzD1iVMCtBs%2BnseXxTd1pDhiOl2o4p4nnEgv7%2FQlb6zmPBjSnC3H9P5N%2FgpqFUwyt1tDUcpYlDAobTeMXnhs7R4mZZvKdGKJIVBFcV1qsucsxi7taUSLEO2N4kMXlW5wXgf3V44FkKcGbsrQ9QqDHBFGqiuOwE1m7qzeXfj2gj9WpqDCSoNTMBjqkAbLGzkCgNAqIHErvME9zr6Ipo6%2FaIovTWwgZtUPrbpLIUV5b1MVbAxVo5VFDtYX20LIPwMe4VOlqgdb632MIKnq%2BTPpmvkEGggUBlsBdRvw7jc1cEGqs8L7xHLWQ1ZR89OI9mpGpvPWEuzg4iv%2Bv7hSczBjmMtBjmKIatdzRQ1qeXPcrnHd3KRVBgy2L0GxrWdHJon4%2B2GYNaPTkNW0uvzd3ZCy1&X-Amz-Signature=6232ed4c46713a985b6949bd398c08ca3892fee2edad75d977fab94a091bd1a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKDOCSPY%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD42yZn2PwLjSZLkVXWnWpFXQW46%2BgWYEU5W9aRE4KeIAIhAPObj9Iv%2BJAHKtEyBa7YuKZkzW%2B8CVGF%2BFjZWH%2B6Dux5Kv8DCFoQABoMNjM3NDIzMTgzODA1Igz9r%2BddUjLxeckvSEEq3AOd3ajDox6FVcK7sSkVd7I1q11aiXc8Q9WYkv4N5vSxPnufsFWjotYQOPnO21Mz2Ne79r0ebt4Cdsqfvs1yl6a4G9Bo2N5oeC65T%2FP7OtpB3lfLgYyR0ackPjkI31i0yq98p7DoGr1axjfPrrqqXoyGCkzA9JH1PpBv4scFp%2FVZDSh0BxRNKspNSFCmNN148mhOAPzHdksErb%2BMe0VDq76PWd73sZQssblXKR0HWxpDfV8kMxdo0L74gf204WjBkfQHWUtJW1pNu3qy47RVJuL5eDjkiNUpd83UB6rto4QytHTT2SZRoXsVqUZ36RpL3qMM%2FzSGFK2GfOSZLcngfxDckzkONPb5DD8y1xgcJ7QbsZgh3TVJJmD4M2FpTn47SGLqHuuCsiO8FpqYyV3KGrI5yjqqEiwRcBtLV716Mb3Fjaoo7%2FbsbwuyOb8UkoHuWDc6%2BR%2BwloBKq0hIzD1iVMCtBs%2BnseXxTd1pDhiOl2o4p4nnEgv7%2FQlb6zmPBjSnC3H9P5N%2FgpqFUwyt1tDUcpYlDAobTeMXnhs7R4mZZvKdGKJIVBFcV1qsucsxi7taUSLEO2N4kMXlW5wXgf3V44FkKcGbsrQ9QqDHBFGqiuOwE1m7qzeXfj2gj9WpqDCSoNTMBjqkAbLGzkCgNAqIHErvME9zr6Ipo6%2FaIovTWwgZtUPrbpLIUV5b1MVbAxVo5VFDtYX20LIPwMe4VOlqgdb632MIKnq%2BTPpmvkEGggUBlsBdRvw7jc1cEGqs8L7xHLWQ1ZR89OI9mpGpvPWEuzg4iv%2Bv7hSczBjmMtBjmKIatdzRQ1qeXPcrnHd3KRVBgy2L0GxrWdHJon4%2B2GYNaPTkNW0uvzd3ZCy1&X-Amz-Signature=f489096a4185b89f01a6ef0d2d9c11a2b3d938280746deaee64d6c8967e9eeb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

