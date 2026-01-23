---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4FIRJCV%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIHeOqUFp6p%2Blro0JC%2BhgWm%2B%2FT0NBOBig8im9dZ7z%2BrVRAiEAgbB%2BOfXp3Qv3blolvJyoW9DeMaozEIuuI0qrKJfd0EsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuJA%2F8fySHApcKtlSrcAzXaCjNUE5t08h%2FmXqI7X%2FoNhYAjR0Kviu1d3zKDczvH82Q4ieQs7RjV0svnzKzGKHRzFXwhubKcldaPS1QLxDlFMkInCpnEhbAAKtWjsNRouHMYVcEI9o66rwioJHPiaCBaeqCtxNfA1%2BgsCGDhLO9Tbv%2F%2Bc4swNIHILJmXfj8cVnpEyjyqplDCzgZQabTMyt3tHUBaT4pB4QbCRYGs1Ml431leVlIxJQmpIWl9nhWsjKwa9UgJBopDru4NcRyG%2FhpJcthX%2FFgDZyKg31vwC%2BNA4%2F0LdsSVrJChcdiHI3wDagMRGOBRIyaKg5EpByUnR%2FvNsGT0KzES7SgPVDVE%2Bsb2pbObFqX17dMG5cbUBlCLG9rUca1NGRkX7Lp9cO9NlzmJm6CZi1QamHCRJLeUSjfUeUx33YL0osI%2F8BzYrUYwyemP%2FYHpiAUM2pnqPs02IcO%2BvcVCUz6xgyt9NSFaXguH7XjsBThmb2ZjpBWGYOP4pzwa9VuRWQHPH%2Bvp8A31ZskjWTtNBKzBLqTKVDG8fMltwcwmNc1OUv%2FpFUllGs0jnzxA1EG0cV1ekE1X4Hyl2V8Zo%2BVqVGnkCKWVmB7rxcUPdOLi7fyOL2O1I%2Fq4iUDa8O1UuoJnlsLPAcf3MM%2Buy8sGOqUBHsM77xDCIGUtZcrKw%2FcPAkrJVqvGsND%2FaVfwSRq%2BftMt6hS44dyPc22%2FGyMmUunOqj%2FIyfG%2FBy0DzA0%2B0xffU0sZ9Io8KRx0Ar6Y5N%2FOBQXXh%2FjBMJQRy0uKqUJTi2tJQY9vSJdlNUpxWR4ibmkWyIG6kwbemMXq4nT21Dp35bzfiLG4CVCfX4E0DzhFRHaHssKdpBQBgvNpi6%2Fe7tzLOzkE%2FEHs&X-Amz-Signature=11e1bb67a589c63004966dd10a119882087357d6a644dbc68f0fa85b0834b675&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4FIRJCV%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIHeOqUFp6p%2Blro0JC%2BhgWm%2B%2FT0NBOBig8im9dZ7z%2BrVRAiEAgbB%2BOfXp3Qv3blolvJyoW9DeMaozEIuuI0qrKJfd0EsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuJA%2F8fySHApcKtlSrcAzXaCjNUE5t08h%2FmXqI7X%2FoNhYAjR0Kviu1d3zKDczvH82Q4ieQs7RjV0svnzKzGKHRzFXwhubKcldaPS1QLxDlFMkInCpnEhbAAKtWjsNRouHMYVcEI9o66rwioJHPiaCBaeqCtxNfA1%2BgsCGDhLO9Tbv%2F%2Bc4swNIHILJmXfj8cVnpEyjyqplDCzgZQabTMyt3tHUBaT4pB4QbCRYGs1Ml431leVlIxJQmpIWl9nhWsjKwa9UgJBopDru4NcRyG%2FhpJcthX%2FFgDZyKg31vwC%2BNA4%2F0LdsSVrJChcdiHI3wDagMRGOBRIyaKg5EpByUnR%2FvNsGT0KzES7SgPVDVE%2Bsb2pbObFqX17dMG5cbUBlCLG9rUca1NGRkX7Lp9cO9NlzmJm6CZi1QamHCRJLeUSjfUeUx33YL0osI%2F8BzYrUYwyemP%2FYHpiAUM2pnqPs02IcO%2BvcVCUz6xgyt9NSFaXguH7XjsBThmb2ZjpBWGYOP4pzwa9VuRWQHPH%2Bvp8A31ZskjWTtNBKzBLqTKVDG8fMltwcwmNc1OUv%2FpFUllGs0jnzxA1EG0cV1ekE1X4Hyl2V8Zo%2BVqVGnkCKWVmB7rxcUPdOLi7fyOL2O1I%2Fq4iUDa8O1UuoJnlsLPAcf3MM%2Buy8sGOqUBHsM77xDCIGUtZcrKw%2FcPAkrJVqvGsND%2FaVfwSRq%2BftMt6hS44dyPc22%2FGyMmUunOqj%2FIyfG%2FBy0DzA0%2B0xffU0sZ9Io8KRx0Ar6Y5N%2FOBQXXh%2FjBMJQRy0uKqUJTi2tJQY9vSJdlNUpxWR4ibmkWyIG6kwbemMXq4nT21Dp35bzfiLG4CVCfX4E0DzhFRHaHssKdpBQBgvNpi6%2Fe7tzLOzkE%2FEHs&X-Amz-Signature=b3e982f424da7e53e8c18f735c5e79352d82d4629cc12ca08cc470ca066b5b27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4FIRJCV%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIHeOqUFp6p%2Blro0JC%2BhgWm%2B%2FT0NBOBig8im9dZ7z%2BrVRAiEAgbB%2BOfXp3Qv3blolvJyoW9DeMaozEIuuI0qrKJfd0EsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuJA%2F8fySHApcKtlSrcAzXaCjNUE5t08h%2FmXqI7X%2FoNhYAjR0Kviu1d3zKDczvH82Q4ieQs7RjV0svnzKzGKHRzFXwhubKcldaPS1QLxDlFMkInCpnEhbAAKtWjsNRouHMYVcEI9o66rwioJHPiaCBaeqCtxNfA1%2BgsCGDhLO9Tbv%2F%2Bc4swNIHILJmXfj8cVnpEyjyqplDCzgZQabTMyt3tHUBaT4pB4QbCRYGs1Ml431leVlIxJQmpIWl9nhWsjKwa9UgJBopDru4NcRyG%2FhpJcthX%2FFgDZyKg31vwC%2BNA4%2F0LdsSVrJChcdiHI3wDagMRGOBRIyaKg5EpByUnR%2FvNsGT0KzES7SgPVDVE%2Bsb2pbObFqX17dMG5cbUBlCLG9rUca1NGRkX7Lp9cO9NlzmJm6CZi1QamHCRJLeUSjfUeUx33YL0osI%2F8BzYrUYwyemP%2FYHpiAUM2pnqPs02IcO%2BvcVCUz6xgyt9NSFaXguH7XjsBThmb2ZjpBWGYOP4pzwa9VuRWQHPH%2Bvp8A31ZskjWTtNBKzBLqTKVDG8fMltwcwmNc1OUv%2FpFUllGs0jnzxA1EG0cV1ekE1X4Hyl2V8Zo%2BVqVGnkCKWVmB7rxcUPdOLi7fyOL2O1I%2Fq4iUDa8O1UuoJnlsLPAcf3MM%2Buy8sGOqUBHsM77xDCIGUtZcrKw%2FcPAkrJVqvGsND%2FaVfwSRq%2BftMt6hS44dyPc22%2FGyMmUunOqj%2FIyfG%2FBy0DzA0%2B0xffU0sZ9Io8KRx0Ar6Y5N%2FOBQXXh%2FjBMJQRy0uKqUJTi2tJQY9vSJdlNUpxWR4ibmkWyIG6kwbemMXq4nT21Dp35bzfiLG4CVCfX4E0DzhFRHaHssKdpBQBgvNpi6%2Fe7tzLOzkE%2FEHs&X-Amz-Signature=9154a89b63e17d14e1e4684fd0b590ff4c11015e207ba22f3f5ea187993b3c90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

