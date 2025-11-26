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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNJI776%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2F%2B3tchXyn%2F0OTLfgZGMqw4ph2Bkg2%2BjrS7tUr9Jl%2FoAiEAlb4B0IgyRYs6R7ANEDCE8bGTiCjKZ7JYTAyl0AzL0SEq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJCCsLbwd3QPZtvP0ircAx1Pz5%2Bs57Y4aksZc9U1GvWxM5zlY5IN6o7bAF8Frzsb6hlRLqvdyItP2ZoiWj%2Bq7sYlLGjC38dDwM%2B3pdQUp%2FzJ0AmKMINPDp57KFdXFysrlDjr87%2Fr%2FH7xp10dhw74Tj0FjjnUHrRcikTZZGgB1nVOyYtbyfym9m0HzG64x40shddppkGRXxl7NyDI0%2B6agFKuo7yS99H0UM%2FI8s%2Fh4hSlJDpyk%2FZt3EkBbmueHfLHqV7QjZGFpLpIjqrHZ12S95djlMTtSnrvag99jQvG4hTKnshgIT5ZbSbnw0WUdYm2TS%2BjiAUN3tsj6fdfHpS%2FRmZzLUZSEy1WMEgUZ8uaewP%2BIstdO5V6gyH7ckvb6A1Yt3aCwAFIzMwQhn9XNfcf32FCsBADSlrhRplk7Zs2JeTX%2BVmKvp2xr9jJBDcECDJyY3GyOQhKqHflxzUEQXGJBiLYpBv335rtJIovmStyC%2F4VQvoUK4hPYnGB72w%2Bt8MlDPjfs9QyUG5RCJSMR3%2BGC3m8Lg2a7CrC0gfkMR0tq4EG8Mc9lxl8sD9LwpfKERBIZlKOPFndSa4ArtNOswDYN4d%2Bm717jxH5uWXhRmKnit63pTJ8oEI1wyeVHI7DtP8kpgElZBOCim4CubwpMLWxmckGOqUB2qohyGpwBq41LC4DIGRnylbXLQ12x%2Fsmx%2Bn2XvdiFFBOuE9XNpuZ9t0aqdmMeBWTIMJGPx18oKFjQX%2Bc4LYOoer8q252bjfxtu%2BoJIuIyjv%2BoRSDF6klKP3ipSBFKtxWbbE%2F01fQxdAlva4SCVoJ%2B8jDoRDzGdiFjcSwd8NbLoRSHlzkLNCeUo1n703m5m4CCjkBXMnyZ%2BUvAkJoeBYRd6PY8TYI&X-Amz-Signature=a996bcfe616f7504976382f791bf1adb670a6b08ce11aa67758ff4046712d32b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNJI776%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2F%2B3tchXyn%2F0OTLfgZGMqw4ph2Bkg2%2BjrS7tUr9Jl%2FoAiEAlb4B0IgyRYs6R7ANEDCE8bGTiCjKZ7JYTAyl0AzL0SEq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJCCsLbwd3QPZtvP0ircAx1Pz5%2Bs57Y4aksZc9U1GvWxM5zlY5IN6o7bAF8Frzsb6hlRLqvdyItP2ZoiWj%2Bq7sYlLGjC38dDwM%2B3pdQUp%2FzJ0AmKMINPDp57KFdXFysrlDjr87%2Fr%2FH7xp10dhw74Tj0FjjnUHrRcikTZZGgB1nVOyYtbyfym9m0HzG64x40shddppkGRXxl7NyDI0%2B6agFKuo7yS99H0UM%2FI8s%2Fh4hSlJDpyk%2FZt3EkBbmueHfLHqV7QjZGFpLpIjqrHZ12S95djlMTtSnrvag99jQvG4hTKnshgIT5ZbSbnw0WUdYm2TS%2BjiAUN3tsj6fdfHpS%2FRmZzLUZSEy1WMEgUZ8uaewP%2BIstdO5V6gyH7ckvb6A1Yt3aCwAFIzMwQhn9XNfcf32FCsBADSlrhRplk7Zs2JeTX%2BVmKvp2xr9jJBDcECDJyY3GyOQhKqHflxzUEQXGJBiLYpBv335rtJIovmStyC%2F4VQvoUK4hPYnGB72w%2Bt8MlDPjfs9QyUG5RCJSMR3%2BGC3m8Lg2a7CrC0gfkMR0tq4EG8Mc9lxl8sD9LwpfKERBIZlKOPFndSa4ArtNOswDYN4d%2Bm717jxH5uWXhRmKnit63pTJ8oEI1wyeVHI7DtP8kpgElZBOCim4CubwpMLWxmckGOqUB2qohyGpwBq41LC4DIGRnylbXLQ12x%2Fsmx%2Bn2XvdiFFBOuE9XNpuZ9t0aqdmMeBWTIMJGPx18oKFjQX%2Bc4LYOoer8q252bjfxtu%2BoJIuIyjv%2BoRSDF6klKP3ipSBFKtxWbbE%2F01fQxdAlva4SCVoJ%2B8jDoRDzGdiFjcSwd8NbLoRSHlzkLNCeUo1n703m5m4CCjkBXMnyZ%2BUvAkJoeBYRd6PY8TYI&X-Amz-Signature=4c9dc190aed2704952d7b14b2c415fb972c3ea5a78840c4a7187ca10acea7061&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNJI776%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2F%2B3tchXyn%2F0OTLfgZGMqw4ph2Bkg2%2BjrS7tUr9Jl%2FoAiEAlb4B0IgyRYs6R7ANEDCE8bGTiCjKZ7JYTAyl0AzL0SEq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJCCsLbwd3QPZtvP0ircAx1Pz5%2Bs57Y4aksZc9U1GvWxM5zlY5IN6o7bAF8Frzsb6hlRLqvdyItP2ZoiWj%2Bq7sYlLGjC38dDwM%2B3pdQUp%2FzJ0AmKMINPDp57KFdXFysrlDjr87%2Fr%2FH7xp10dhw74Tj0FjjnUHrRcikTZZGgB1nVOyYtbyfym9m0HzG64x40shddppkGRXxl7NyDI0%2B6agFKuo7yS99H0UM%2FI8s%2Fh4hSlJDpyk%2FZt3EkBbmueHfLHqV7QjZGFpLpIjqrHZ12S95djlMTtSnrvag99jQvG4hTKnshgIT5ZbSbnw0WUdYm2TS%2BjiAUN3tsj6fdfHpS%2FRmZzLUZSEy1WMEgUZ8uaewP%2BIstdO5V6gyH7ckvb6A1Yt3aCwAFIzMwQhn9XNfcf32FCsBADSlrhRplk7Zs2JeTX%2BVmKvp2xr9jJBDcECDJyY3GyOQhKqHflxzUEQXGJBiLYpBv335rtJIovmStyC%2F4VQvoUK4hPYnGB72w%2Bt8MlDPjfs9QyUG5RCJSMR3%2BGC3m8Lg2a7CrC0gfkMR0tq4EG8Mc9lxl8sD9LwpfKERBIZlKOPFndSa4ArtNOswDYN4d%2Bm717jxH5uWXhRmKnit63pTJ8oEI1wyeVHI7DtP8kpgElZBOCim4CubwpMLWxmckGOqUB2qohyGpwBq41LC4DIGRnylbXLQ12x%2Fsmx%2Bn2XvdiFFBOuE9XNpuZ9t0aqdmMeBWTIMJGPx18oKFjQX%2Bc4LYOoer8q252bjfxtu%2BoJIuIyjv%2BoRSDF6klKP3ipSBFKtxWbbE%2F01fQxdAlva4SCVoJ%2B8jDoRDzGdiFjcSwd8NbLoRSHlzkLNCeUo1n703m5m4CCjkBXMnyZ%2BUvAkJoeBYRd6PY8TYI&X-Amz-Signature=5e178d7929c91f413a594af368c82b2d2763a667f1df12271c9490817eaf6426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

