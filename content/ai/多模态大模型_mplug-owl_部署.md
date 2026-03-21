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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA4GGSH6%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAD3Md%2FJzdNA%2BA%2FrLl8PpsXTlVma2Lwrqpk09iRll8BBAiEAn5Es5jTCHbbcXvjFXTBBNyg%2Fc2ccn2Fl7s80T8i8Mjsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNbjS8fRMKgauHN6DircA8EEKpEsKg%2FAj80zwZuzH%2BDJ93S74%2F96WoGqqA%2BlaSo7ElUtYpyJaeVD2aAVFcvp57BQrtI6xRJYw32WGxjDvm%2Fvv0kInc8aRgImRka7CDhWyn3JfVM67vHr2IR40DxATwqBxcknL3i%2FDhLxeE97OlnV%2FUcJ091SDGnb3rt9XfqicbK%2BsOfO65PzLRIyWDwQOys%2FtHTZpuiz%2FCn%2Ff7iBsrquXeDlcSbRrxxTd1DN5RIgdXtuBFO85mb92DLEi7YRBHs3i7M75VNFqQDtpz1JCjpops5MYbQR8pXdakLoj0QTJ4p2bTV7JrTicpsFM7oGJWfn0LANHmdF6H0kleobfYUs0hnE36%2Bg5opdmch8QR%2FEPpsS%2F%2BgLC1i%2F2dOp72vOLDzWdhPvZ2CdU6jxdS4EhjdiQaZRTsyHGb881n8ZFARw55GNds1FhUreQTEHUXgtpF19f0x0EfKhvrjPpniZ8yraleTtOJH62Oe5SjI4gn9OyamLyFPi8RoXvSGV5Nw%2Fi58BuZ0x%2BSJlX6c0hkPNhHgC5TpmcjBl7eDnpQfZO75m80yokFCMAubMg1TvB%2FHP%2BXDg6GFddOy3f2N7gf60XXSjnfGgnE4LzxLkFw6KLyaRXOVmCt0IKw2Q%2B3jJMO2O%2BM0GOqUBTzQULrnikiSKMZNgO%2F%2F%2FcclB21fp4NLLefqFyUT8KbgXASr5daTlgFJ4HtmVFZvRaYgihSSHcYv61yDqV4VixUPUGSGCjQG%2Bm5fR3b4%2FwFByJNGlGx3rl%2BEOCDZYBy0K5iZqSd%2BxcraUaUA7KjdeC3OVxZj0hiJZ7stasORSamZzgyXni4femmgPVDNUw%2F0D43eQ%2FKTkVApFW9RbJtm%2Bx6MLwv1F&X-Amz-Signature=edd6e1b9195d16cd34549648a7b2d16ba3aafb5049ad7e32538691bca554db62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA4GGSH6%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAD3Md%2FJzdNA%2BA%2FrLl8PpsXTlVma2Lwrqpk09iRll8BBAiEAn5Es5jTCHbbcXvjFXTBBNyg%2Fc2ccn2Fl7s80T8i8Mjsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNbjS8fRMKgauHN6DircA8EEKpEsKg%2FAj80zwZuzH%2BDJ93S74%2F96WoGqqA%2BlaSo7ElUtYpyJaeVD2aAVFcvp57BQrtI6xRJYw32WGxjDvm%2Fvv0kInc8aRgImRka7CDhWyn3JfVM67vHr2IR40DxATwqBxcknL3i%2FDhLxeE97OlnV%2FUcJ091SDGnb3rt9XfqicbK%2BsOfO65PzLRIyWDwQOys%2FtHTZpuiz%2FCn%2Ff7iBsrquXeDlcSbRrxxTd1DN5RIgdXtuBFO85mb92DLEi7YRBHs3i7M75VNFqQDtpz1JCjpops5MYbQR8pXdakLoj0QTJ4p2bTV7JrTicpsFM7oGJWfn0LANHmdF6H0kleobfYUs0hnE36%2Bg5opdmch8QR%2FEPpsS%2F%2BgLC1i%2F2dOp72vOLDzWdhPvZ2CdU6jxdS4EhjdiQaZRTsyHGb881n8ZFARw55GNds1FhUreQTEHUXgtpF19f0x0EfKhvrjPpniZ8yraleTtOJH62Oe5SjI4gn9OyamLyFPi8RoXvSGV5Nw%2Fi58BuZ0x%2BSJlX6c0hkPNhHgC5TpmcjBl7eDnpQfZO75m80yokFCMAubMg1TvB%2FHP%2BXDg6GFddOy3f2N7gf60XXSjnfGgnE4LzxLkFw6KLyaRXOVmCt0IKw2Q%2B3jJMO2O%2BM0GOqUBTzQULrnikiSKMZNgO%2F%2F%2FcclB21fp4NLLefqFyUT8KbgXASr5daTlgFJ4HtmVFZvRaYgihSSHcYv61yDqV4VixUPUGSGCjQG%2Bm5fR3b4%2FwFByJNGlGx3rl%2BEOCDZYBy0K5iZqSd%2BxcraUaUA7KjdeC3OVxZj0hiJZ7stasORSamZzgyXni4femmgPVDNUw%2F0D43eQ%2FKTkVApFW9RbJtm%2Bx6MLwv1F&X-Amz-Signature=b5a81c11365c099322ec6672ec7413af43f6bfd906f6231390bdb1668671eda4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

