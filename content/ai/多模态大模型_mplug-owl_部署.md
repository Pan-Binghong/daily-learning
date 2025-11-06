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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57IPLR6%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFOaBsvjO6nMzH8Q3Ju1ibmlFN%2BHJlWCbLK8GC5L0K5AiEA%2F77G36kFNeHZSY0vpoIzGkURW0gNWFcATaS3gHE13AcqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHqREfDJF03EtGdEQSrcA1h4wk7XGM4x1KPKad5RCCLErqug0se01gJ7kKtAyAepZPLBXRcXQ4XTNSbbBnIiq8xS7AsDddTuPiSQpxZv%2B2Ao%2Bk4RPvGri3mAHGEU%2FvDRarIaa2qk9b%2Bh5l3rMVtfVujk1ykmvLfUJuIUhCis2qc5%2FeicpNdcV5v%2BARodS7rdj6Gd6NFLIwWdi4BroDZ09FrodCAEUbeA7pBi2E8toddf956BIQhdb5Rjd3tcT7kSK5tDzyubfW1LYbnQUFr6s%2F9wpHa1AHyHVwDM2uTNBX0U%2BfWFSDP6n%2Fhwzs8sbWOTNQKoJqORHcxF41%2FlJpn0SSaQoru6VWEFwWupKHxu4Z%2BG6ZMaqoyAAS8vJJdMHTpp9HHQv%2B42%2F874E1HW%2Bu%2FbH2kE26a2s7ujyB6Od95RI5JNym461lWfd86z4pKQxtyn%2B3V2YGGRq2XnUo0cR0Ta7M8mE7solG%2FWmKlAKHG1b6H31uRz2dFyAm4YJM9bM%2FXhS%2Bixyc4CbZnF2a1LM1k5523mcvEiaQLtUg%2BFeLJN7iv3Rhvu5Pz8w5CnT2QyqPYdTaE2uFPDYvASQW6Ry3E%2Fjd1RY05RDrxMe7zngrGeoz1UNiYTnoWxQVVndeb%2F855sMpEim6ZDzVI1ZZoGMOzxr8gGOqUBepXNhJYgTDZDTxUN%2FddpZymQYKMl791Y40Uie54LLNG3H1PzoblUWWnfRU7dy%2B4n1VVzaU%2FOAzf3bH%2BOAOzNCO9xRgiu4XLh8ut6ZpwxpLtUnVD%2FBp0b3h8RgFUJnTHcWqo73nK4MkVTK1GAptTANcmXGN0DE8i7AbBF7n6Hrxb5Ps30UCsnsWfbKqSYcmQUyEeRHU0buwS9v9KfKMrd2W7LAc1n&X-Amz-Signature=8288009459505d9295db09cb7005b71e6756d9505a7c85da7c246e24c3637556&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57IPLR6%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFOaBsvjO6nMzH8Q3Ju1ibmlFN%2BHJlWCbLK8GC5L0K5AiEA%2F77G36kFNeHZSY0vpoIzGkURW0gNWFcATaS3gHE13AcqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHqREfDJF03EtGdEQSrcA1h4wk7XGM4x1KPKad5RCCLErqug0se01gJ7kKtAyAepZPLBXRcXQ4XTNSbbBnIiq8xS7AsDddTuPiSQpxZv%2B2Ao%2Bk4RPvGri3mAHGEU%2FvDRarIaa2qk9b%2Bh5l3rMVtfVujk1ykmvLfUJuIUhCis2qc5%2FeicpNdcV5v%2BARodS7rdj6Gd6NFLIwWdi4BroDZ09FrodCAEUbeA7pBi2E8toddf956BIQhdb5Rjd3tcT7kSK5tDzyubfW1LYbnQUFr6s%2F9wpHa1AHyHVwDM2uTNBX0U%2BfWFSDP6n%2Fhwzs8sbWOTNQKoJqORHcxF41%2FlJpn0SSaQoru6VWEFwWupKHxu4Z%2BG6ZMaqoyAAS8vJJdMHTpp9HHQv%2B42%2F874E1HW%2Bu%2FbH2kE26a2s7ujyB6Od95RI5JNym461lWfd86z4pKQxtyn%2B3V2YGGRq2XnUo0cR0Ta7M8mE7solG%2FWmKlAKHG1b6H31uRz2dFyAm4YJM9bM%2FXhS%2Bixyc4CbZnF2a1LM1k5523mcvEiaQLtUg%2BFeLJN7iv3Rhvu5Pz8w5CnT2QyqPYdTaE2uFPDYvASQW6Ry3E%2Fjd1RY05RDrxMe7zngrGeoz1UNiYTnoWxQVVndeb%2F855sMpEim6ZDzVI1ZZoGMOzxr8gGOqUBepXNhJYgTDZDTxUN%2FddpZymQYKMl791Y40Uie54LLNG3H1PzoblUWWnfRU7dy%2B4n1VVzaU%2FOAzf3bH%2BOAOzNCO9xRgiu4XLh8ut6ZpwxpLtUnVD%2FBp0b3h8RgFUJnTHcWqo73nK4MkVTK1GAptTANcmXGN0DE8i7AbBF7n6Hrxb5Ps30UCsnsWfbKqSYcmQUyEeRHU0buwS9v9KfKMrd2W7LAc1n&X-Amz-Signature=d9166d7208884e6df4a5c09f4c1c588f1327bfa04eefb3a732d553e47ffd436a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

