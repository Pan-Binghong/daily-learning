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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7SED52J%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJgPNlY%2B4OfdhKmJtM0nJjBFLloLA89gfSxCIoKYwq9QIhALGZPfgJ%2B6itsvGuzbucu8%2FroRd3nTPOpWSm85s%2BrIbSKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzufO3%2FR%2BcBHDGbF7gq3AMkMkRusORqqGZUe7aiDITd86fgn1G4j605RaFkEmb1ng%2BotHdRljJpWTNsPSayp9%2Fj7E99y4MTZYywJQ98yAob4QfN001jPDSRJaMm6leCFVZhHmG%2BS6%2FNdjgH%2F0laxX1FH6YWKdhzoFML3Cf4ORYanHummQSVwHKWsvjav0XrNhcIkQNnOCujn1zl7MqIJZR27w%2FlBYHPpp%2FgokMILt39xaV2sg%2BNVtwCJmWGhk4oZXmVbky9AWj4YUoRqJNTxFDpdZYya23Rap2CJDSyoOQxYBYDSrgu5WEjgB52SJrm7tsBTMF0rivE233rYR7Rm0ErSqOPuswgf5n9RVAv4STit2Iomk%2B%2FEGEmR5477qeBO15FANbtklmc7222gVjGLTeodRqEscvwRypNnYxVmRKHTEqCLCRFyFoNTBqVK51fkGD%2BIfrs56hCz%2BlP2NmIP%2FteZtozcns00u%2FwC1lraynWU%2F4c4w0H8dnrUXtc%2FIMlRJuAzeexRGzH3mnerFs75iJ2EdXYtZtnRGxChOQlnjXblhzhNfXQVzKNTsFtZNzHiEoxKSuoz%2FqmAGksCFEogb4XCUY5mZNg7dTL3v4JZyYkfu2MfGJrLSt5YEPy%2BrjTtgLUmescSZoj0t1k6DCekvvLBjqkAbY9SpGjISH9q0%2BrQJ2mmNdkv1JQivrWuLLfkDGk4rxwDZ5MBcmuDdga1bAagLmV7FusOr7MD07fcIRBU4EurD1yykvqxkWV6D%2BJRM6Q91wsVu%2B8RwL2fcSKzv%2FhkE0T2sZ7BFrlGiV7hQPqL%2BztfcbAyyHVFtZcC9ujN5YHGFlodNL6pFNDukAuptT0nihnjL3%2FMGfK%2BNuuEbY0wCyimSkJ%2BRNL&X-Amz-Signature=8bbf489b240cc6ec5bc19a225c243a6d1b399676d82c3cbc3d08979fd7ce2be6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7SED52J%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJgPNlY%2B4OfdhKmJtM0nJjBFLloLA89gfSxCIoKYwq9QIhALGZPfgJ%2B6itsvGuzbucu8%2FroRd3nTPOpWSm85s%2BrIbSKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzufO3%2FR%2BcBHDGbF7gq3AMkMkRusORqqGZUe7aiDITd86fgn1G4j605RaFkEmb1ng%2BotHdRljJpWTNsPSayp9%2Fj7E99y4MTZYywJQ98yAob4QfN001jPDSRJaMm6leCFVZhHmG%2BS6%2FNdjgH%2F0laxX1FH6YWKdhzoFML3Cf4ORYanHummQSVwHKWsvjav0XrNhcIkQNnOCujn1zl7MqIJZR27w%2FlBYHPpp%2FgokMILt39xaV2sg%2BNVtwCJmWGhk4oZXmVbky9AWj4YUoRqJNTxFDpdZYya23Rap2CJDSyoOQxYBYDSrgu5WEjgB52SJrm7tsBTMF0rivE233rYR7Rm0ErSqOPuswgf5n9RVAv4STit2Iomk%2B%2FEGEmR5477qeBO15FANbtklmc7222gVjGLTeodRqEscvwRypNnYxVmRKHTEqCLCRFyFoNTBqVK51fkGD%2BIfrs56hCz%2BlP2NmIP%2FteZtozcns00u%2FwC1lraynWU%2F4c4w0H8dnrUXtc%2FIMlRJuAzeexRGzH3mnerFs75iJ2EdXYtZtnRGxChOQlnjXblhzhNfXQVzKNTsFtZNzHiEoxKSuoz%2FqmAGksCFEogb4XCUY5mZNg7dTL3v4JZyYkfu2MfGJrLSt5YEPy%2BrjTtgLUmescSZoj0t1k6DCekvvLBjqkAbY9SpGjISH9q0%2BrQJ2mmNdkv1JQivrWuLLfkDGk4rxwDZ5MBcmuDdga1bAagLmV7FusOr7MD07fcIRBU4EurD1yykvqxkWV6D%2BJRM6Q91wsVu%2B8RwL2fcSKzv%2FhkE0T2sZ7BFrlGiV7hQPqL%2BztfcbAyyHVFtZcC9ujN5YHGFlodNL6pFNDukAuptT0nihnjL3%2FMGfK%2BNuuEbY0wCyimSkJ%2BRNL&X-Amz-Signature=1c01c4677314e411bda4333a7d0e8514ef16dcce3395037b952baa7d85f90427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

