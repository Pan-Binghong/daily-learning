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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=ad831f855322f69a05c9209509470eb6acd7f5afc26dffd7f06d85bff55c04b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=c9e12d9d84ed10d804f8462e271f35b4944fb75a5cd22b32338672c13b8ec03c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=1955e5e57525b5d8274158098ad13dd1c36c9df48be6813b60e3a26bebd26ca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=5a5ba75a2398861ad5bc56cebcea381588c9e556a4fbde330c037c24045289d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=a1be18800df15fa23546f1701644afe543e53939d41a2488b8cd54973a1987f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=1bce8cfb79ccffe7d795a65f28619e7a33f91a4e03d662b28fad11b1997e43d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVIAV3D%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQC%2FGWNdbKcxS%2Fg0h3Gj6Y%2Fi7f9VYVQhgf3fei8lGThWOgIhAIlYFD9FpowOLCL4lOehzLi9vsExpZc5ZAh2trxmpENkKv8DCDAQABoMNjM3NDIzMTgzODA1IgzFNKkKCXHQiDDnut8q3APlX46qE4DBo0Cct9Lm7g5kM1tDrOhQ4yVCYoqFikT7AVrwuAlQdpNQ66agoERWjee%2BZJQp5a4NgD02lKOJmnAr08hXUeIWt4k6%2Fs%2FbXd48LCEKJPxAZuvWhoZJJp9cSuztZBIpGFfPePWZUEKIkc3%2F1KPPb5g0cNfgipf9aJiELJvGFLc3q3aWqnY4WSAPctp%2FYPKzwAR8nG6RaJCcttlzdsWkUDX39Jzw6qVfayno%2BAhNZ6vtD9%2BFUQLrtO516joVcq5rBbr2jR0RXsY%2Fqna7djMZf0r9PK8u1G0XXFp7wf7Nbc7uBjegNGqrMYVWhFkvhQ2B616%2Fl8T7q2c4gDr2%2FX0N1dUS42OsBRtjoX4z2kJ059by%2FK5WIuXFU1BzWSOglPqBDTZJdrMVZ5K5GLA4vDJ1MX%2FTqavT1i9T%2FFfvvjKQLca0Y4v86eUpCfWTOtvXKW0f0N%2BninFltgsQozK8q8Lo6%2B3JFN29%2Ft0VX6%2BO8I0TOq4VQ1NFo4ni0mnn6u5Q15X%2BXWe9HrYkY95kBT7TqAp17%2FWZU19%2BHkmZJyNrAqQSy%2FidkSbGaTZMcA%2FNC%2FBYfNkEhJ9v9nfKprWiaZg%2FyCbTSHPKpqXTrICl1U8CTr9D62BeWYsoLRXdhzCUsdrLBjqkAQ4cKG3ZS1fz%2FpVebOwfKyi5ncB1fFt9WIkbsd6pqgBE5av6AWGO%2BqUr9gwj6tsbffu2rEarZSCVntcl0PEm9Ssfo7rMegLEZfk9XPi5YN%2BX6SuIXsTI2%2FjdJG8Axik1eC0GgC73makVK08vV5%2FAfmECh71sUgNl5VwYkE7GNmXmFZYqxfqTU%2BlrRSfArKzvy1UIhgp1sqGQgEazKElU3d8beFA2&X-Amz-Signature=6c3fc12ad84cd7562640fee0e164a3d8eb467b7de91392442df5f5f74b8a20e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



