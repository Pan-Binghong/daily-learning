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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646SNTSC7%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDW5oXpiPUuD4pWNedGvdYrmSIwxkMg2AeKqgopJiDkAQIgDbU34xeJaD56PJzi935pq5W6FqGFk0bylXpfV1aoc9YqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLx0GAq7D8BCjSrHLSrcAyG7UKo64DAXoL7hCSWhXPZDLDxcp3Dcfko9fdIj0kL5r4w6hac4cXFiGh%2Fi10uXLfBpwwW92bQbJ4Vj%2BYxsD8TVH4dm2HGq%2Fi56bWSCqpaS8QPpXUoAnZ5Fyuze7pcBGMI4UseWQz4imRVDxQsJArXJ8NcdIxhEoYOG4niBLziXkiJORaljU6jzcr0RDtcllHh%2BTSm9lqPZvsEepYrdCvMJSdV4UGOIICtfUqdehn9XhdKb1exV5kWCJ9e1Tg%2BXx0u8EPgLUovPmZPqMoqbh2%2FHkLSjCMqqkUuoUX%2BogD%2BdNSp2Z9uG%2BmhKeKmGvkcFm%2FFdpUs8yHNWB4GoP9cSKxQcN5rldalMEYJ4BeKSA4GF%2BZFX%2F4d4bznIkfIInmsBd4%2FT4cwsdpVFlB%2FZie2EC2042Dh1hSritZXs3xCjdDe%2BkNbMmxcV5CuLGS2Q3tFfrrDTxUcncU0U0E0nv9xHe%2BEFNylUJit2rTwFgOyXmcoj5C%2FINedjMrUpX4eAmdF8%2Ft1tNNL1uHrYorg1Zb5KixoWLErhP8g%2BkCKL8Z0opofX57atlC3jOChjkI2whOyrwVXOsn9AeNxDVqwG8EeWBQ4HBrSTTfLIkX2%2FjFgIRDP5WJgDt1HlYqQ4mLkPMIOIgMwGOqUBECQM4eSIG83YGVOF6vExroQxMj%2Fw24VAlFlUeS5WKQFrxIXjhAD%2FlV8IgyGvN9zjRdCEukhBgRimM90zIvXntpSL0Cfy0l2QD9%2Brh9GiNIImwl0Jyz%2Fwr7pLGRRxuuV6XmofbySbUp9PngqygysLmhsnQYOiH2aUGG312vwAREBLwFyr4vcofgOrQB1wbWFweeVkfIndDl1V8X%2FdXTH1dVNQVlN9&X-Amz-Signature=885272fac98d8bebc3e4300a98e75b04e53b445d9473b8fa8074069730ac693c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646SNTSC7%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDW5oXpiPUuD4pWNedGvdYrmSIwxkMg2AeKqgopJiDkAQIgDbU34xeJaD56PJzi935pq5W6FqGFk0bylXpfV1aoc9YqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLx0GAq7D8BCjSrHLSrcAyG7UKo64DAXoL7hCSWhXPZDLDxcp3Dcfko9fdIj0kL5r4w6hac4cXFiGh%2Fi10uXLfBpwwW92bQbJ4Vj%2BYxsD8TVH4dm2HGq%2Fi56bWSCqpaS8QPpXUoAnZ5Fyuze7pcBGMI4UseWQz4imRVDxQsJArXJ8NcdIxhEoYOG4niBLziXkiJORaljU6jzcr0RDtcllHh%2BTSm9lqPZvsEepYrdCvMJSdV4UGOIICtfUqdehn9XhdKb1exV5kWCJ9e1Tg%2BXx0u8EPgLUovPmZPqMoqbh2%2FHkLSjCMqqkUuoUX%2BogD%2BdNSp2Z9uG%2BmhKeKmGvkcFm%2FFdpUs8yHNWB4GoP9cSKxQcN5rldalMEYJ4BeKSA4GF%2BZFX%2F4d4bznIkfIInmsBd4%2FT4cwsdpVFlB%2FZie2EC2042Dh1hSritZXs3xCjdDe%2BkNbMmxcV5CuLGS2Q3tFfrrDTxUcncU0U0E0nv9xHe%2BEFNylUJit2rTwFgOyXmcoj5C%2FINedjMrUpX4eAmdF8%2Ft1tNNL1uHrYorg1Zb5KixoWLErhP8g%2BkCKL8Z0opofX57atlC3jOChjkI2whOyrwVXOsn9AeNxDVqwG8EeWBQ4HBrSTTfLIkX2%2FjFgIRDP5WJgDt1HlYqQ4mLkPMIOIgMwGOqUBECQM4eSIG83YGVOF6vExroQxMj%2Fw24VAlFlUeS5WKQFrxIXjhAD%2FlV8IgyGvN9zjRdCEukhBgRimM90zIvXntpSL0Cfy0l2QD9%2Brh9GiNIImwl0Jyz%2Fwr7pLGRRxuuV6XmofbySbUp9PngqygysLmhsnQYOiH2aUGG312vwAREBLwFyr4vcofgOrQB1wbWFweeVkfIndDl1V8X%2FdXTH1dVNQVlN9&X-Amz-Signature=972f2991aa89c6d1d62886d778f60966342b4d0ef4240e07ff10373471cb2417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

