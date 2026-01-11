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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLRXS3RB%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD6LgWodzVXDtNtlnwmC%2Boq%2BfZp8aGFHTwdJntdlfuopAIhANaVUFw91xEX4xCmpIvcfkP72T2h3tWMV5L11xE7q%2FHbKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4xGozH0QrEeTVIp0q3AN3MNox7Bxv5rf9hA2zSh7K5cx%2B4VYwKeP3V4mYzVeKrIeMKasehvx9UBDZ2rJ5xxCs2wjMfoxUCzOOrrZ5hG1IfFA6RUmy9zCcw1bFOX4JpnzdrYBjRCgq3NA%2Btcy4u%2FLGFSCnEJX43zGRR3%2FOz7VVg1wXUx%2F4A0YqRhP6vEL%2Fc%2BWDNWI%2B%2F4JfW8XrYElaYi0RdeOS1t5qBabntaPAC6zBfx4FRv%2FehaA8GAi0a%2B7dDPOqXb8H9XJJXWPWqW4NhvUyw9q6bHK9zmvfWk8KWOwmfhRlkECmWF9oqmWSk8926m626cXTX8Y2wxBUaVN7JPiG86XCfIUyjkVRXNTJtt3ngMpRtpWBcqmZiBXzrI0ebT%2FNSCyygU74hwA1U7EJozNiFYUVVOrBA0Jlky6C2hN15JVwfMEmxK84UIYoWlwT%2BwqV0sTFivvLrDIzr4crE7SnQ%2F2uJmGuuPOEGht3h8Ujd1Rsztvpfsp1d2RZMvyYeIRyvXFV3iiP%2F26CrMqfMnL7oDinOa6Ke8A36jDHNZUQEdxUZE61rt%2FwnSolqmasHlN3skB30DlAdt8ecJCftknKE4SfufBNqh1wt28MZSZkMAm3%2BQqaLjXfnFjy%2FEqFLUFOTB9ycte9lZ4w4TDt%2F4vLBjqkAUYWoRBAEOMm2SEFQybKMRh3TGP7OesJ4dAfYOSYAmftV3k7vlbWarbXheFPiL%2Bb20OlaMQ0neojeJeNAzDHtsMufHYcoJyvqMW%2BQ2isJoQwuz7fy6aq97Q5eE5pAlnvaWKlmLIbGCa9%2F29yXjb0YQeEhoeppvF7vbLZy8Wyx2McC%2F6WuWLpGmyvN%2Fk%2FMV8UX26vo8ksKgJ83ORR410xBpifpr%2Br&X-Amz-Signature=69fe5d65b505eeedd68e2f55987eadb9a88421b6eb770d975a84781744a9cd48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLRXS3RB%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD6LgWodzVXDtNtlnwmC%2Boq%2BfZp8aGFHTwdJntdlfuopAIhANaVUFw91xEX4xCmpIvcfkP72T2h3tWMV5L11xE7q%2FHbKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4xGozH0QrEeTVIp0q3AN3MNox7Bxv5rf9hA2zSh7K5cx%2B4VYwKeP3V4mYzVeKrIeMKasehvx9UBDZ2rJ5xxCs2wjMfoxUCzOOrrZ5hG1IfFA6RUmy9zCcw1bFOX4JpnzdrYBjRCgq3NA%2Btcy4u%2FLGFSCnEJX43zGRR3%2FOz7VVg1wXUx%2F4A0YqRhP6vEL%2Fc%2BWDNWI%2B%2F4JfW8XrYElaYi0RdeOS1t5qBabntaPAC6zBfx4FRv%2FehaA8GAi0a%2B7dDPOqXb8H9XJJXWPWqW4NhvUyw9q6bHK9zmvfWk8KWOwmfhRlkECmWF9oqmWSk8926m626cXTX8Y2wxBUaVN7JPiG86XCfIUyjkVRXNTJtt3ngMpRtpWBcqmZiBXzrI0ebT%2FNSCyygU74hwA1U7EJozNiFYUVVOrBA0Jlky6C2hN15JVwfMEmxK84UIYoWlwT%2BwqV0sTFivvLrDIzr4crE7SnQ%2F2uJmGuuPOEGht3h8Ujd1Rsztvpfsp1d2RZMvyYeIRyvXFV3iiP%2F26CrMqfMnL7oDinOa6Ke8A36jDHNZUQEdxUZE61rt%2FwnSolqmasHlN3skB30DlAdt8ecJCftknKE4SfufBNqh1wt28MZSZkMAm3%2BQqaLjXfnFjy%2FEqFLUFOTB9ycte9lZ4w4TDt%2F4vLBjqkAUYWoRBAEOMm2SEFQybKMRh3TGP7OesJ4dAfYOSYAmftV3k7vlbWarbXheFPiL%2Bb20OlaMQ0neojeJeNAzDHtsMufHYcoJyvqMW%2BQ2isJoQwuz7fy6aq97Q5eE5pAlnvaWKlmLIbGCa9%2F29yXjb0YQeEhoeppvF7vbLZy8Wyx2McC%2F6WuWLpGmyvN%2Fk%2FMV8UX26vo8ksKgJ83ORR410xBpifpr%2Br&X-Amz-Signature=b1d50bfc98cb95b96ca3b1da246a73d3434e633be3c0769e9b9f673257ed4222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

