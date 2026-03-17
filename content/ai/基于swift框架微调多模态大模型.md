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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=17a41ed41b00441d581d4faefc8b2ad6b3d12936ca526845b8193f850599148b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=33bffc9912fc8cbd03168bee22d59a31039d54636ed046406584e7e450171566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=59215f79ed1ba5cfb30826345198c21502fd1293890b2c2b2560bd899445107f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=86dfacc50672da5955474a5c2b23f9c3c3551e074c2cb50ba015a6c2ea10e72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=eeac18f5d62d41420eabd39cdf7c82a85de7f6de17ae6fc15a547b83a0724a13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=91f0d22a61b7db1b59cf7ecce5c846c32ffd4e13c2c4bfbe7dd1b8835cc623d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MQG522%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBMynOk6VyU8cNwheH0LBKDaWq77qI33uOSG54ZTE0bpAiEA98tnKv0iW0a38RaUszDyl2K02BKHyI2MefY5Q7OnGjYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4Q9lIWdrC7XsRe3SrcA1Wq0uxJGgN4zAze4Wk3%2FGn9S3tFvCThEmv9RWpSZeFg4pKjAxfJahxnOoeNEaGmQLUVnC%2Bik3xoGcBnuzfv3EusMB1pgT%2F8II3%2FJv4EdCtsM5UXI6lLK%2BXWalpmSuuwPM2aQMZBKrkqIny%2FQbuvrZ%2BW1zkgYjonMRHQga10a0db%2BeWsCavdopwAohvdltZ%2F04wulo9zNfW4Q6JkdQ6zj6OwLxKBEpH63HVRj7vJMn8uhwZ0LBHvWL2nRgc6RcBM%2B7n8egEUWMxYlwhHwD%2FgP21wyTp5FZofLNv8kWmppiOkFfOrWheEnEuAhC3ktsiZqUNCE5mn%2Fg%2B1MZ59AwZtY036scGFVq9rivCGDOx0bBR2Pxyn5AWMRCje0QwvH6ds9JUTq4RGqh1HryE8VslvTTx1Lhnr8rZ73qudoU6QyvQWoCgvaTBHdZwLjOtwvPtY2GIlF2QIftn88aFKFa2YhJMYW7g%2BCK5xANuyd0LIYkK2k4DOAPwd20rco4%2FpBCzn6gAWtudTJrkI%2FBlWArnnKfQHile%2F8RtIK007iDgwJIf%2BV1tTwgk3NOTb9NL51JpWJJ5yk7%2BygzS7fFQIoa%2FVUUzhqX8jgPHXOofv03lvVjndA%2FYPc86uyUJRcrXeMLjo4s0GOqUB19YLX%2F1n3zYTBohSdzHzlByfmbwkVz%2BHxEr9hGrHGYEaYQO9M1Wv1I5ws27paMgKS6ijBx%2BuFc4hjhy0ilyK6QNILrHJ7Vrg74tgAPl4mlHAz82DzSnw%2FZDXvCAL3KEaaaplXsXFiB8vaD%2B5QRg1nhY6%2Bk8lfYX%2FrEmMSaMhT%2FZh%2FQYG%2BP1vdJqQTjn3pe9DValEkwG4osdTNTRA3DpBSxq%2BD6fe&X-Amz-Signature=269219cdf1d4a4eca4a735ac288a99fd7c74e52900fe4de017a6bf79564e0457&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



