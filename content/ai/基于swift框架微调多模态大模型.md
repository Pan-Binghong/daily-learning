---
title: 基于Swift框架微调多模态大模型
date: '2025-03-21T06:10:00.000Z'
lastmod: '2025-04-11T02:22:00.000Z'
draft: false
tags:
- Swift
categories:
- AI
---

> 💡 记录使用Swift框架微调至推理多模态大模型的全流程，模型采用Qwen_VL_2.5-7b。

---

# 1. 基础环境安装

https://swift.readthedocs.io/zh-cn/latest/GetStarted/SWIFT%E5%AE%89%E8%A3%85.html

采用pip包管理器安装：

```python
pip install 'ms-swift[all]' -U
```

---

# 2. 下载模型

https://modelscope.cn/models/Qwen/Qwen2-VL-7B-Instruct

使用git下载：

```python
git clone https://www.modelscope.cn/Qwen/Qwen2-VL-7B-Instruct.git
```

模型目录截图：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=0fe3169f25e43f34c72a090f1978a4efbfa2544bd4a35ef55cee5f70a38f33ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=bdede30ee4022505858daa21a7ee44b8a7042f106fb807017c7394269610738e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=ab30c962aaa4daa50f66c84591f458dd0bb4dd6d6f94486d86ad7826b180b967&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

输入：unzip llava_ins_image.zip 解压图片压缩包。得到以上红框内容。

<details><summary>数据集截图预览</summary>

</details>

---

# 4. 微调

## 4.1 检查微调环境

```python
pip list | grep swift
# 回显一下内容表示正确
ms_swift                       3.2.1
```

## 4.2 基于WebUI微调

```python
swift web-ui --lang zh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=36097c85e705415a79b7fc08ea8bb00a674fa8408e8ae2d3db4892645d128171&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 4.3 基于命令行微调

参数详细参考：https://swift.readthedocs.io/zh-cn/latest/Instruction/%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%8F%82%E6%95%B0.html

### 4.3.1 微调coco数据集

```python
# 显存资源：24GiB
CUDA_VISIBLE_DEVICES=0 \
MAX_PIXELS=1003520 \
swift sft \
    --model /root/autodl-tmp/multimodal/Qwen2-VL-7B-Instruct \
    --dataset '/root/autodl-tmp/datasets/coco#1000' \
    --train_type lora \
    --torch_dtype bfloat16 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --lora_rank 8 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --freeze_vit true \
    --gradient_accumulation_steps 16 \
    --save_steps 100 \
    --save_total_limit 5 \
    --logging_steps 5 \
    --max_length 2048 \
    --output_dir output \
    --warmup_ratio 0.05 \
    --dataloader_num_workers 4 \
    --dataset_num_proc 4 \
    --streaming true \
    --max_steps 2000 \
    --enable_cache true \
    --split_dataset_ratio 0
```

<details><summary>训练记录截图</summary>

</details>

---

### 4.3.2 微调LLava-Intruction-MLLM数据集

- 进入到数据集总目录下，cd /root/autodl-tmp/LLaVa-Instruction-MLLM 
- 创建微调脚本train.sh，写入微调命令：
- 升级脚本权限: chmod +x train.sh 
- 执行微调脚本: ./train.sh
<details><summary>训练记录截图</summary>

</details>

---

### 4.3.3 微调自定义数据集

- 构建数据集，采用json的格式，数据内容如下:
- 训练脚本:
<details><summary>训练记录截图</summary>

</details>

## 4.4 基于Python代码微调

## 4.5 训练完毕检查

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=777da1872130462bd6f64af40b7e3e74b3cf9619b640b0a1268185bbc3f5453b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 5. Lora合并

https://github.com/modelscope/ms-swift/blob/main/examples/export/merge_lora.sh

1. 找到微调后模型的输出路径，例如output/vx-xxx/checkpoint-xxx 
1. 在终端输入:
```bash
swift export \
    --adapters output/vx-xxx/checkpoint-xxx \
    --merge_lora true
```

1. 合并完成
---

# 6. 推理

推理从底层逻辑讲，分为2种方式，第2种为直接使用刚才微调后的文件。即使用--adapters 后面跟文件路径。第2种为使用--model 后面跟合并后的权重路径。

## 6.1 命令行推理

```bash
CUDA_VISIBLE_DEVICES=0 \
swift infer \
    --adapters /root/autodl-tmp/mytrain/output/v8-20250326-100050/checkpoint-200 \
    --infer_backend pt \
    --stream true \
    --temperature 0 \
    --max_new_tokens 2048
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=7dfc7f351042e95dae5c606d4c3ba8d5650a3a1c75fc9ad1032feb362da4fa8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> curl调用的模板：

## 6.2 界面推理

```bash
CUDA_VISIBLE_DEVICES=0 \
swift app \
    --adapters /root/autodl-tmp/mytrain/output/v8-20250326-100050/checkpoint-200 \
    --infer_backend pt \
    --stream true \
    --temperature 0 \
    --max_new_tokens 2048
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VGNJICU%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIF5SA6JL1BPsFnHVrYUFEbxW%2BL5WaKtq0FRJ0cO0Tsv1AiEAiG%2B58%2FLhSCXKrVmHhgdeE6uC2ZvaHQfJpsvKJUnYKSQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDALWvubeRq8FnHluRSrcA%2FLuC6%2FRXt0u7CGY%2B8HnoCP5HjPCdtrsQKbVE373JQDfJ9ciXrmt2jaqvUriXh2t7q2p2RSuZJgPzG3Fk%2BswLmedioyrsLvLbbVThC227eCawS1ZH4WBdl8e4hcsKi9YcIeFw1cV0CzzvRtOSiksUubUq5AZ84f8qZZ7gVkbxdhEud6PsPH3IaK7h1C8FihYzH0pf%2FaL6S2JvgdasjcTWEiqQk%2F4iTOa9eXqhI4FAptURv2srsi5KpWHR8UxkwRIVQ0soIOEEHPiiV7eZuk8YDSJcDf9%2BYr%2BFoGEtURh9Z525HNE1jhHA1RoScXROIh4rvI%2BS4D%2BHqWrjS%2F%2BlhpZ4Rpx%2B1UFbFF6rMMOjE1%2F%2Fm9JUObSdlCw5I69HvUOfUXusguv2G9e0xfCHaJWm%2B70A6yQoB8wNn88riDRtTgj83BDRHkQgmsnkO62M4mmK5LY6UnBhmX2sA61vD3xdeHJvSDEDq7dMwAbP1MUtSARPwlOZ9i3Sz4IxTbnR6WR01K%2F4WWu%2F3UJJpQ%2F%2F0qR%2Bm4Nz9i3IwelTwx7leQ%2BvBU%2FMTw2222sJ5384LeQZJO0qfjiuizLVrlSCpa0PQLloNaq9gieRnaPeSLMIomDiLgIUV%2BTeWyqj4KtpS3vYvlPMN3tnM4GOqUBgcWHI81wDPyeIkKOWrN%2FrTXSRATIyVfDeV41R8p%2FJs8a5p3V2m41oJQ%2FVyfYG17856bviBU%2Bz9tWzLWlgMwiPyEXWphSA2sEIK%2Fp1MAKBHzSaKqraGxW6afTwZNwWm1eG8ZKCCqfuZlquA0cvbWnTfgaxKaZZrkoYwe%2FGzR3wnB54XhZnYmXH%2BsFo2Uiomb3BABfuylHrrheYJ%2FII2FcZJJKhzSy&X-Amz-Signature=cfd41fc3da704017143a0d5310824590a8ac7d6484203672281d4b89f480bb4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



