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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=9354c34abe51b1b04199f1af7b40be3ed2b6efba67ff09c591d062eb94e7d272&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=88cd02572a89c0273000c9234a08746458c025e4d52b84221c219bd97ef89caa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=50184cdd59b6b9d5a80760d96eb09acfe51ac85931a86d8705c0b06d4b6a41fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=47a244e20a6733007070c2253c7712a4890213141eaa0a7bf49e9aa4d2302932&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=5732f3111a449957f528a20ea0f1f5b0c247928d2f4056dde19bcf8c5fbc8f50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=1b2fea9cea17b6632fef412cabf2a43f1a93e5499a172d086ecf74d4dc86f274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJVNZJY%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCnhofaiaLnZ2f1g%2FjqmMZJAqFOhyP465m8WxigZ7xoowIhALF4Zz%2F438ABOFEwa4FaNJBdOZirYZpVGzrW659IaL75Kv8DCDMQABoMNjM3NDIzMTgzODA1Igxv4yNFhXnAVzqK%2BPIq3AOoN9z2rKWVv82GBHhem7lceJHTn5WG9dAyeN4f50LmIVF7Xsiao32QCn54A7RJ7PFgC4XaC3QuZkyIX1OyC5x20tbsCnaMMrYEi%2FgE%2FFwnMf5FM%2BDQ1rrdQ8pGu8gy%2BOhCKyAbisHq7nTReqJwHCkJtMshTZakuwskr0e4az3BzVvp%2BHHo5UvRcKiZsHNnxkpZBnYeyyoFxt664yUIYf2qicVIL2i5l5UrhxGekxOMmS4wo4MbyTQMlTS4XuI2dVyNreqBIrQKnU6DZePqVNg%2FoD2iAS98Fw%2FwQ%2BpR%2F9XcQRK8TX1psBF5m3R0NmvEiz3aypRNSF3xKYDD38S683%2Fr1DGxkmxppn9SJyhfaeofEWLrQlUMc3SVLUCROPEDrD3USrfdLxFRELdyFG00T%2BupCqzHYC6S2K6MVFd02NYm66RDvsP%2F8zyBxwJxr4rSgtX%2BEefJ3hSHsiClh4dOIyZbW9b2udDJW83sTDlarKnqp%2Bb%2FunFwcCKqLHh7zSpLr%2FhwkNKt5nrBjcvreyHy2K6E2jP9HvQdhdpcApe6c5y2t6a4kDl651r6%2B%2FO8VRHEunfcw2gKbWJbbRpYU1PmYOUF1MwizCBydVs8PNVo9iJ5Al7PigkUzYR4nghfXzCIqrLKBjqkAWtSs6UvfJomX9sLZj7JyAJZg64NQLc5pE99UmVM03NmG%2BUqU1Mny%2FjtYoLvzMI6EF2PcOwblwAFpcUnC%2BZCpwPBqPF3VCAtBPdsCN01pdP%2BjkcgINUuuBrFJT0UriQEFngzaWOlMngcDtbXNuqsoK3Dz8NXAyglS6%2Br3ZC7PstovgchwQpYHhgWyjhIu5mLIvQspqDGPkN7HARt2nzLyZ20HSbh&X-Amz-Signature=0dd7bfc9afae9d343aadf913d8de079dcde5e2da323e917fad48038e8760ee45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



