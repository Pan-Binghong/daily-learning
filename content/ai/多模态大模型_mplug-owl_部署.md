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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNGD62CI%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq7n2M7MlqXJ%2FgvU08wmF1PBXLkukE5bzkfeDOnr%2FWiAIgN8%2BeqUosHKmk2v8cDeqWcfwxsKOkVj769dgaa2%2F8heEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJr%2BznhCRngHCgqCSrcA4wJ4c%2Bl5fUOCjY54%2FVTKPKtQZSV5eqaQbBe6OsLbuYmNmop9OL1Op8CNrs1g5XbCXD6i%2BNy0Kml97ten81QONr2yuYGDz9jYHd9RDPYogdT%2Bmj2TsLcAcZittmSlMs62dK0%2BB%2B6Wxgj8AYPvPWdQgLpOAkSQE5OTmhhun54NOqPNC0hejj85V27V0uxeLxnVKexxtbrvA%2BPjooCsnAgGKSHVD1OKGoWCdyHaPaqS39D0lyQHJzMr75NRwbMAax4jycsor2IhZOYKAlnXdOo4uDwq%2B30avHnTk9zXeE7Eqr7maKycJeGLq2LdANv%2FiTikudz8r7POpWigT8Epw%2F%2FfC491YuDffTiMKK5gUfHdOci5cRU%2FfN9%2FZG%2BAoLD%2B1Ag0BzfuFePOXbIYvwP5%2FPcBzwECYG9Ir4MMgId6EmkFuSIi9w2Z3QFx5mLGNITptyXfY%2BTKY3lKoTYBUponjVB236HGRZ4EKdgw%2FAkPibHR5LaAiQ9%2BfV3ceNO3I7ey4MIRvzkTzaUQUjVX6DQ30jxWRJL1UhJ%2Fjcp07Kn0akLilObaoqMmtrKDZJIWsDc%2FJ6y7VCp1UkPetO%2FjLhDEm1yCjxrkb%2BZICFNkwhpznxJlETwjYo0PWB2H07h1ZwqMNXv2MkGOqUBCc5sGQOwQare3TZNaLpjM7P9bfXmXUTUKsU2Y5ktUJkN7FFXGFNeV7WbKvgPXW2DPni43i3pSkhIID6F4kERjAudN52NS5lz6emnmYMCWiebhDZdvDBj2U%2FjbBF0K0Vz859a8EuzC4PMT2izWu7km2rjcC7bjaxSlj2gnYgb2fApo4X5Y%2BKPxoKhuMxaMJM44udFiWlt6tQfACPzuXQ4M20PwwMD&X-Amz-Signature=935f9252133af2e11fba2f7277872f78839ced6628c00c3b7baef6dafca9d5de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNGD62CI%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq7n2M7MlqXJ%2FgvU08wmF1PBXLkukE5bzkfeDOnr%2FWiAIgN8%2BeqUosHKmk2v8cDeqWcfwxsKOkVj769dgaa2%2F8heEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJr%2BznhCRngHCgqCSrcA4wJ4c%2Bl5fUOCjY54%2FVTKPKtQZSV5eqaQbBe6OsLbuYmNmop9OL1Op8CNrs1g5XbCXD6i%2BNy0Kml97ten81QONr2yuYGDz9jYHd9RDPYogdT%2Bmj2TsLcAcZittmSlMs62dK0%2BB%2B6Wxgj8AYPvPWdQgLpOAkSQE5OTmhhun54NOqPNC0hejj85V27V0uxeLxnVKexxtbrvA%2BPjooCsnAgGKSHVD1OKGoWCdyHaPaqS39D0lyQHJzMr75NRwbMAax4jycsor2IhZOYKAlnXdOo4uDwq%2B30avHnTk9zXeE7Eqr7maKycJeGLq2LdANv%2FiTikudz8r7POpWigT8Epw%2F%2FfC491YuDffTiMKK5gUfHdOci5cRU%2FfN9%2FZG%2BAoLD%2B1Ag0BzfuFePOXbIYvwP5%2FPcBzwECYG9Ir4MMgId6EmkFuSIi9w2Z3QFx5mLGNITptyXfY%2BTKY3lKoTYBUponjVB236HGRZ4EKdgw%2FAkPibHR5LaAiQ9%2BfV3ceNO3I7ey4MIRvzkTzaUQUjVX6DQ30jxWRJL1UhJ%2Fjcp07Kn0akLilObaoqMmtrKDZJIWsDc%2FJ6y7VCp1UkPetO%2FjLhDEm1yCjxrkb%2BZICFNkwhpznxJlETwjYo0PWB2H07h1ZwqMNXv2MkGOqUBCc5sGQOwQare3TZNaLpjM7P9bfXmXUTUKsU2Y5ktUJkN7FFXGFNeV7WbKvgPXW2DPni43i3pSkhIID6F4kERjAudN52NS5lz6emnmYMCWiebhDZdvDBj2U%2FjbBF0K0Vz859a8EuzC4PMT2izWu7km2rjcC7bjaxSlj2gnYgb2fApo4X5Y%2BKPxoKhuMxaMJM44udFiWlt6tQfACPzuXQ4M20PwwMD&X-Amz-Signature=514f901de0caee4385d06e344b29f4eef06ac695dc5903d6ace9ec43273c791a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

