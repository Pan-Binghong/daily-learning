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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=ce799771fc304e759eed7c74d0d812fafe52e735ef5aa7f2f534fa883ba212e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=82a1b0c098a11c059089379c617adabc2353d4ce715d123bda807343a133a05e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=40820c05e410c9432d69802111cce0475ae775f2681513cb57f71cf9056f5b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=dc98be9697d47cb2216bf02284f15b5dee5078ede5d0e2071837699397c651eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=d81d46bd338e584c72ea0df8516b2756527a2f0c18228f5818820e1cebbb92af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=8e4d394a5c85d00d57305e76502830fd4210979527f08b24ac7217a85809fb53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7P7TMCO%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIH8Z8IX9C2Rizx7Zo5LhmEwCFW9yisAFcHdI2l7LJ9kYAiAe8aJM%2FWxXRTFf1Kvqz%2F4%2FozfHY5WKdyyjZ8xD%2BDs0Syr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIM2N%2FztGyOomsGn%2FgkKtwD9b3z3XmBfLEvy44kCu9pnfEhQFLKM%2B0F33b5O2TJppAImTTRrQCyivtasHd29%2Ftzor76INaIEu3kz%2FQLolxFKXxErsOMgroInVj3SVp9Q2ie2%2BzXlaf0ZsHi%2Bx9LCIbnY0hPvTe84AHAhTGICK%2BOIDaylpnuF0imKB8m%2B0dFW4d7W9g%2FnRcFYCFKWk70WF1smFeDveZWUMqWNTKmpbn6KVzKLD2iUAY7FhsDF0gtw7wMZ53hesTFcLSEnmW1waYcRXm%2BWexIJwfTO1%2BA%2FmPms7G0on9fiTxfp60K9FZ5NKXT2IG65Afyns%2BMg9l4mY0%2Fq1jMmqKqCKSKJ%2BRU0ECEopcJcsK1moiQEOW5Xevpw%2BNjsSTQNxWBGYSr%2BaNhMvI9nl0kCm1Gb6CwCxVVM1uE1JvHhy4nyS8zxNFKvaWZl%2Buq5XHMe4l8%2F1bnp41Fp0XaP9zcdlOq9IPw6iWC%2FZYmWD4EXO5Dm6jpC3EigS7I%2FHPQBKnNHA4kCmyt4ieT1jY%2FQuAQCejyuF2yR7zUX7JXiHHcCZDfdDg0kNxSKlQP%2FK1kox5oI%2B8tZegHXGO34dNzNJavxHzd5em0Be%2BP%2FF0GzuVsTLjjVu90rzkp3hs4XlKmS8cfHXTaOEP5T5Ewqb6izgY6pgHh6NAKDd1eDedTRBMRfj%2FQhZ4YMzQCjHaWelNKKQon7XyBQZ%2BKIbQ5pZcb%2FR%2F93Au30kyzpN5tjfVSHUJixu3MPqZYNg7gCKBgnyFW0HE3uy9jHaNaHiLS4eLDcrN6Rg4sc17KPEHo7LDRm1%2FjzMaTWicQKoNpqLCCpa00oOoaTVfpKk98coTCVjikGpeE7LJ1CpY%2FRkE0BSyGfXICkRl1%2Bh0qzqJY&X-Amz-Signature=e3cab88d5bef1f54cd931f1eff5ffee824804800581a03f81ddf9202db966aec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



