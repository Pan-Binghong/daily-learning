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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=5eb795e66e5ec01a9db0fb8e7b30981715276734d6e76b50c18eb56e28ee9b58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=e39109159064e08c940e1c649ef1713115e47a56f6a70b8a07b41cfd54a0cd24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=57e6a77b998c9e433aa39224e0121f77f288e02b238e57ed237bc9367df2cf81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=2166d3c9d62e2c4b18c95163e0c6313edd9f5e74dff0082586506ecc782e7682&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=b54b32dc141a817ae4fdf3f1a51e28558dc82e2ea19c92160f4767f8175a394f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=a947971ef0b400db86197261dfd84ff0b086ebd4385e32cab8da0be3f4adae1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6QTW3F%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJPVE8WYe9WAmAQB3DRRL9XG9pqzFQtxsu7tHU6DDOKQIhALChhO46tjmvsiAkxzWnbW1dejGyffER4DR2DO9gbV%2BFKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHJokaoYr02yBqQswq3AMM6ysaai7QZ%2BxLjj3PYqvVPcrxmF21N9XKSXyumS7o0p1Ec2pOKEKMwVCI0RNzNGlHzoN%2BOUSXkkIFh4FD2PdZPwh1teYh6Ld5%2BinhBzNinJFgSlUQfCcnAqPLT7DV4NdYs2oYTEegAAwEcs1oj86jt6Jz%2FPlmj20ohuGl1Vd0YfZwtfFKe85g3nz8p2cla%2F2Sswc4xzUNnfkznnNYHGabJH%2FQZsC6VQ%2BcGxxAbZJohTlRGxab8Yd3%2BRCPCGG41fknRAffqp3D9RlnCT2a6mId8GBa68OhQ5hJxENKM0%2FFsXE3IpGwfW8qShR8HwDpQbPS%2B9lSRHL6a9WZqYYL9VJWrmI4q23CYRP7Fydcmmi1tr5UxIzZ%2BtmdCaOjhdJw7p466uSlBVGUKCawURk36r72G%2FBjODmT%2FElDhc%2BY9BiB1QKvJnOzDhc8M5slbbkCu1bYBuohEFMxc%2FyCo2zIX811O%2FhiZmXpbbVqiCgn3PdvlpffCPeCXn3%2FxtsXLkLc8TcuEdJAJwugN%2FQtNIM%2F3I6mLm4CshGHiRFyEIfNQSG3Acc%2F1F%2FEbUsB4Zd3MrdCqXgzf7DCvnG42%2FZSTIII2eQUdkukTHdu5d1C2OWZ6bFyF%2BQZow8lhLA6%2BRAi1TChk%2FzOBjqkAX%2FN%2BVEF0dHzyaTf%2BcfUNuFWL0BUt%2FobKFOx195zBXqLPfarzds%2FBxM%2BLOyEM%2FBpEWXs6CcpqBKtzSu7pgmUUc%2FS%2FIkhr%2BbiHIfe1iKn6E2G2l9GsnHOSagczltAZ2fQ%2BL48GY2JoW%2FmRxVscJx80TYVkSPSkiNcm%2F3K7VO6EGWsgYcIaLSQv1sYiFdzfH2BMDKxdy1qCTfN01qQsyGf6HaV2mSY&X-Amz-Signature=a3ee818823f26129ab420e4b7bf2699b440ca1b71622d5273ae033c95197c268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



