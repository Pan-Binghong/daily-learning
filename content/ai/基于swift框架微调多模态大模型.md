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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=f35dca736b00ab27a5049c79a809e45d95d931611704c6247940c9b7b87fbbe8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=74f7bf4c025b5df34ed9fb0e200a379e3134f12586df18c4ddb301438e9016d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=e9e489cdaf59a639323a6b7db3f15bd47d06b30c29091e7517824df2e6844f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=ff7716a6dfefa7df338fdaf34da5371647ce7403719bccbd4502bede7a9495bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=a961654971d8f688b5168e4d40e10231699fd4d820d0e1982dea97c9b8335faf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=6c2c692c2bb187f3a538c8d88d8e945a48f05b2a14e76b391f6c5a4e64004b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMIIR2L6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcijA54G3YA39MaLF02zagduLm66stOJSBZJptnAm6cwIhANQJMai8IS2kXiSANbvLf4feSQVa160dMjxWp0iMu6VgKv8DCH8QABoMNjM3NDIzMTgzODA1IgxU8WOnmHQF4nM2tjIq3APilTzoRoCTM%2BbTfNGg2ss7fJtpzA2cO6NnJPvA8Q8tJFG0WiWg%2FMNVCYGgFYmZgTGcRKIubXcFRrp%2FZ0%2BphnciCZtVcFw3mfzxAaHjSEa%2BQkIoJBILmFNfJE2nj6c3%2BX8YFZHi%2FyVlcBdH1AGZFesoiiV4tH6iKbNTjQkZWlBXxFGvNzOyc1qvXPNrk7zrxjtGGI7JpMfHnayX8zZlNXHycBG%2BNL78qfbswKkuag3GZn6FjgHaofCmCAsQ%2B58J%2FqJyuYD6nTykItCOjHrrme67ailCjR1AgH%2FRJ5ZkDybFPSsPTGenk7YI6b%2F5qYcefMfNfRDsBbplGtVRQcHE98G6Zgr8vT8NdHwNvQ6W7Qsglvi6%2BWefMkcgEyRx3EzP5Qgbr6%2B8OqOoM1vAZ9dZaD5mriTGQikaEHWDJH57fh5Tx1RNJBlm0HfZm0ZMxQgRaMO7Q%2FUhQsbgGDmp0WNu9WV3P4rmve8%2BdSi4xbz5oA8%2BuAPBsBdC92Xq5GjPmIylpJhYZO%2BCIRCQWU9dFApj%2F1HEfrMXtnogOKuxlfAQ3%2BRpl2MsUsdYdmLwuJ6Ew9KW%2Fw8%2Fryg7GDpck7idq6t22VH4BWW0U8oxHyBjJI0%2BhKFJK6k8LvvQ8%2Be122AP3TCCrr3OBjqkAYgm0Qm34hqj%2B4t9eil0rXYfE62wSqrSuDP45rWx3akA0dC4VkSRi9Jh7WgZ%2FNbfwT1uKh2mZwr8yeHrbtSTE5ww4hkO%2BK5PwNDIRhWfEBYVJKzu3o7e10%2FC9wjqXtBNeI26pt1c4pYWlXuSaRwpMoQdLZLimLawykxHjId%2Bn4yFKeGgyt7hRMANAI0Cw6ZsRKWKo0y4jF6YxZPzSFcrxkze%2B0di&X-Amz-Signature=9ecaafabdcd425f2da44392e9844ed61ef07afd0d84b6004df42f2def85f7846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



