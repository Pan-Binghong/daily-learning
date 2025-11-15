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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=46118a1396dcb0cfec8339f969f11644508a75bc8707bcef6812c8ada1665c11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=e9b563cfe96a9fcc73b3a72af5eef9d3032a52d44625a08aa13c1c0d03055726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=a88bb6212824b702eb24fd88f19c8a0b56dc7d51a7fd654018b2767d2aa6c75c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=213c15290bc8517786caa77cb215b9a090ccfd9bbf86f51633e3ca71c0cb0158&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=4cd081a58acd9dc6c1cbebc46fbf6b5383f1480fda7c8ccef1e5e515de50737a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=eb54c011713582f4bb21a4aa1abb3e33ffa085225a984e255f25639b4300be26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJRZ4PN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrg%2B3%2Fr2jqZ5tlgo1mlY345v3qPLCEieC8eAHu8zWr8QIgCO1aQG4VVD3ZU57RN4fiB4U3I42y83aAloiIjBocjagq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDJIoMAULTuaAT14LOyrcA6HDMQZCB%2FdzZGtL95leuozkj1qf13Y4m5AVdTA5QE5WggmxgRY%2BC%2F1rbZUKqvjhd%2Fmjg5S06Bi2qw2Eg2umxupSwvTVTt7q6wA4iGVZJFJvci3dwl5PsnpITP1WRL7DgwmoRpnxr5ANu9WjYYJhYxgiZ2EI50Jv%2FRCr5%2FBAzFQr59IvGcQqyHYCznbSJ%2F0Hn88y2198CRnnvdox7S%2BiO8TOA1NPjIcB2Km4WMTn0hz5864S5zVk5FHpJK9XYhfIXi06X2Fjo9aJuqSsXG4CBEVVKHmjh7m%2BXo5yWDhPxOVkbtCEFJSkUCSbc0VaMvj%2Bd6lXHQ84rXd%2B0Z1kwKTF8dRSyGucQUbNVnL5t8iJtn76QuKeJGSaADk5TD2kSTcNal40G4jFjSTUSLssZphh2PjLoS01%2BX2mXB%2BQKage9FoeSafjRbho5kq7OwjWb%2BJzZC3TVFQ2ifte4labUhFP6gbO8BOh8p78pBp3IgjtEwsuVS0146KIORf7Cp%2F4WtXGqgP%2BZveIuBMfkUI82tGKn0nErRqTgvJ0Geyd%2B2rmVNknKnIGnVS7PQC0%2FHnQ4uPHoWwe9TTzjcsgTREgaysrr0XseoHSpQ2vefmlsXTrK7Ze1c%2Ftu0s%2BBCHvDmUtML3A38gGOqUB74MF0Vf0lvErf5toIDdotDUC7bAwsgGvuZfMqFvapdC3fwXLIblQUtWbd10fGMJSqO69FlQelBEHwQgKsVZUhj6EEU5GFAjjrMndsVda9%2BXQ4rP7zcg5H%2FdgWzTj9d6A2293%2Fo6qjrTunM3FpvUH9VRBl5mR2vEryIy8cP4W3mDp8wY%2B58Q5gGzBZ%2BWOsR1Ty6sF7fa%2F3FPbkOKbhMvnVhnEkQIx&X-Amz-Signature=cf82819483e2a1fa114a7a047d6ed5c805b3f2abf975341d87f8e4764dd553b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



