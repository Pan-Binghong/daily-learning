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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=f9b8b41d3f4aa578a50abeae3a05bb7224069a03f9c3282be673c646ac679040&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=4ebe23d378e8c139f8377cfab7a6ae386b09644fc2aa5d06440b6e2066f3f906&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=a4e563a40ec91a466e048241ecbb8c3721d7797c02995fde3ad059f8dde7d838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=018171a22ea8b861ea53c08e3d6713b132ae036cf33bd88c4e0bdd9c749a60ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=020dcf9016cf9c4bfcc4c08423c9eba2cae9b581457150af76e2e020aee3b334&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=532bde1522d9f39ecb1cc44f060d6e12b10d134431bf08218fa33e14896d45b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQVGXH5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBVuYb6QaxoyYTxYo7QKjVDi3MuOsAWE%2BkuF4pxH7UvxAiBq5xveGLBoN6F%2BtWQ4Z34LYn3WU68zJsdxlAlTC9DMviqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKY1GNykyoBTghs17KtwDIWs0CzBkDYh5I%2FbHGVBy6RnS8TdJRHDOKh9UQySNDpoS%2BU0S4%2Bg2d1DC5hiwgkhs7PVatN0ErfLx79T4cMr06mNY09un8fHHF466eKChRWd%2Fqp1DnlWf58AUGK3h5cbtKP3x9jNI6V%2FZjFjXrm%2BbXoIff0O6%2BuylCDg7Gzo7lwyNhkeV5VHArw6EPX5OpRHeC%2BjnM13ULPWPrRcCgSsBonvmwBU6%2Bw87%2Bmuh9YrY1vggvtPzZAGkqw0Q73BdSHGe1iJQk9Cje7rynlElLLGJRJQ3N2HR0agJizXi%2FiTEeYzCrBhE9C9C%2BKxI8jtQK%2FhUwUgMKb0gt4PxkH%2Ba0ILuiDq5z1VE%2BQ67gz79mibZK9sEzJl52FODc6IBb93pUc2345o1JNU8JM7GuIr1ZUtsKJIC%2B596Gmjx4PikSWcJ%2BGzhBesrxMn3l6uAJDTIBuqh%2FzXi7T7ii3GzBQTk7DiPlF6q17LeiLrc6A4dKq33zNtvohiKQWGCL6LXbRkyI95XRqOmnwGv4dJjEi9hUmLUR%2BXa2U8E5pBLKIFv6XicuSlmofUg2BzMosVghTGSx%2BCgaz4X3RxGCa%2Br2sFhrvxOg39hWZN6N%2BFlrUsLwgGD2Pwnhoz2%2FX%2BOivDcYokwkM%2BozQY6pgFXb%2BtZnWgzgzUT%2FGCUvA0XY%2FhbHFad%2FxiD%2B07g%2BVopGcmaQ38n3vlbW0z3vYWNa29gkKECwD7axszKbYRzM3f%2FIzXQ6znIgdUUP8n6JgNawPNspGH34%2FaLPM1EulqmBn3TVkkPXx9d8lmuUtvWUGUqZmr%2BcMEtVlI8Ky6ahoDpPNAlNEQHDPLkjJqwHffp6Rcj%2BZInEhSYCm9HjfNjl4EBk8hJhJKa&X-Amz-Signature=1280de827960ec4c7c27de1c776e4e03d702751e93b8c2b1cbb22653702666f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



