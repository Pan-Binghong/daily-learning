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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=905743fec9894c7c2eb9fbac7ba98ec67e1d44c9b0f71c84941253271e00e06f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=959cce7274c44134c2689687f446f356979d42fecc1e550e6673e0ab6cd09342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=1361bbe7eb2cd071ceb5e12828fbe7a6c9e272710e875664395bb4ff3edf13aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=2a85597e5ff4c2e5c55ec1aed292ba4e2a60b2c21cd7badadeda24c1fb9cd980&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=036654f3ee388495431db57ad22cf81c6493387aade2a93b89ac7b216841b961&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=c72f8d1b119c46fbb335d12e83188e8ac55b0260e33a5f1297817d92fc0cc871&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623MPXF3T%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLgTpFQErm%2BbPl3CS4U4GKZvaZYNHBZrC%2Fo58lTc7eWAIhAN%2BA50iv3TEf%2FVkcXJEPN5XavAMV%2BW4awehImFgnSF0GKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykCiGoIjzBYLr%2FerUq3AO6iJhmSHckFJ0FxSltit7rT4vmHZuz46fHS36uh8dkuwFLRdoG2isQINWU5ATU4dvuRt7ilzhVbNHzQyg4uo8lRyhzSylrkeTZ7IvhNofmVMmzWNjgfOWbRABCrGKYGGD7d8Y1nYoJs2f7tepOVuT2D8uZzT9p1F1UDVxYxwx1fks3porVadkhugOufTOxcfqp5dZxxBa4JS4RFhpIPMp7v8u6bun%2FmI0RjwrUj%2Ff1ARIEKEe6x90envkkAH%2FIASCg%2BuVg%2BPU6fYZrr4RpnrL5oEv5GCWIEfrVT09aBz8LFJ47C2D6IuReeOer2jS8aGKr905XFA6QMIBHoBGp2a2k5cC9O0ghtL5ukwbgLPalViWSxnR%2FH7nG5XzZAsa4hMHXR4%2Fa%2FSFuIzx8FZEeBLvXHm0ZrrMrYGb0kn402immGjzIe%2F74sIN13srgNVtTEvilQW81LKnXgvbjaI5oitsfQKdijokaVTYJemKl05YQguidqtDA3%2FFAumJGiTWFa1e9MBaV05%2F7Jccp21hdCYD%2BXiZb0p23q1rsE6qoZ5kvYNADf%2FkTU%2BR%2FkJg2Db%2FX0gDA%2BWpE%2Fl3DLc7RHnY%2For%2Bg6CR7nIIp%2FW9zxa7debyiUQ3AEw8cC3u20PgaejDmgdPNBjqkAa7T%2Fv5oqlhMKJ2%2B2KKG9TcBfH1RexO9GWa%2F8p5M33e2rHnlqQIYhdGBFvjQhzEqQZOwjDijLQWl%2FnR8qZVld8hQcOREmDXwAxirNBvwY8ABEqI5LiohkyNgsFXPSQYEzcpEXvutUtP1XxzIuu%2FMgrkYWyncFAf%2B2b1TnTKKNo7DPS%2FFElC0xItWPQOFvL1ytnhLHkbC3P3UY%2BOnfLNNAKZLFRC4&X-Amz-Signature=65e7e399436c20f22534f3f8b384267cc4a744e7f8660a3d179155e496beddb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



