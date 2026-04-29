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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=7203f453004c6d2603004d744c104a268af66571c99d334ae494e52b44b1def0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=b39f80a225cde2d424c3ca773db177a3ba263d97253e036f747c4331e2293c77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=911cfa38e9943555a220e34df40dab6b9736baf647a5db3310f71dd1c0469cef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=774c3e0a7d5911bed0abe041d02947fa9e91306ce823956c0455c63fb43723ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=fd848f7afa9ef40ae3cd1b61f36fb6f2c721f8648867db26be6a28c52fa543e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=8a89b188510b6207539a4df2c184722e7fc32a337969d207c350877bbe76802b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466625N3VVF%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICTdz48Ghb%2Bhxz7kutdqb9dV%2B%2BiptR46ZcUKyrrEZKXIAiBWOFO%2BUWr0GpKTDnxX03bbdzO3%2FnAOxuuP3oNPeyqUPyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxemHRr3G9YvhBL%2BKtwDG6kr5nbtKm%2F%2F%2BCJclDNJ657vdm5Ws0%2F%2BqiKmNYphdQ%2F58OKtT%2Bc3dQWW5Woe9NbKZDDoIDl6HD2iq1L42yZvk5zKve7m%2BoreKfQst070diTV0fhN7wXEYYdB8kMfdAjhXRJ0cTQw5oDfVNbsg97DsU4Gv2W%2BKlPOcYB5kjAAvLMBwU6Ky%2FsbOdWaq70c2WceJQZpRirz7wrGXS7Gso1PkLJWATEWnQ%2Fzl3CrJphVV3h%2BbqE9%2Fc9rMzj%2BpNHxkDKv5Y%2FiH8duvWABAxy5AzsCWoCtC7fxFzPJljfDozCAFzvkR0eWV%2BgG3n6lQC9O8ZdSfqr%2B0wT%2BM1bUSC0SRC39UCgmt4r1jB9YGL9J2oKvLMHeIw5fpI3xuCFL55fjUADdm%2FTV2FZlpSnvbxvnvjuHhk1laP%2BPak9Qv9F43UEzLB1He7oKh60GB51%2Fm8PRm5sgipZ7jAxx6HBI89kflCh8cWa%2BmOZ%2B0nLdpLBxNVQYIrsKKqHP00fh%2Fg0l9C4MQPDDJm69jf%2BdADOUf7S35X1RamVshCTzrUieDx0TmnoBvjGdwhPjE8jZ9gpz3r4LA7tUwTgAUneVX6%2Bj%2FxfaLNp%2B5QHFt%2Bfe5G3UTvzE4Qsy3TUmW9qeLu10kd13SgEwvJHGzwY6pgFu7bsWHZ2z1%2FRKGM%2B8V7GXUjrAP%2BE0YgG0gbCDZOVqdxFxG0saYRr3YNcPMcllqr2o6NP446RtrxbFD7b2H4TEE2yZj1AmBVf%2BQdXVLfAEEMt1vkg37zDlaJIvj5IHbtth8fxrkjwrwoHwTHS%2FVVVVCI%2BMKPZO%2FXPPPcV6xX4EKMIdVGr18tZBY93%2FAafK%2FSKvGyZfcjHE7qv3jSnBzdJ7jeVSAFjp&X-Amz-Signature=8b03571ecd808aa2a7ba32d85dbf63d34d32b7eda7641dbe3a86028215ab1e55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



