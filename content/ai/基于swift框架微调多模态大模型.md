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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=f6b76c13c32285acb806dcadc7907c611e7d74b62194083c5993fb7cae965176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=f095b55fa7527571d476119993aae339c8a0b369fc45f159d772adcb6ea6ad63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=36603a2a128c87a2b433628ce67ef9c882bdc5364eeeeb1ba82536a46159957d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=318147e149235b85475e57078a8aa77b0935a23c92948db5b58ec01b83fcd929&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=c1b5d97061048d08e90aee85ac1172493860d537030e467fb8da05fb04097964&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=1a5b29aad4499e528a67716709da4bb2f63334fa15365f54fda836ea364232b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7Q62FN%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxPLNqHoeQwK0FTbGipitSr3S3Jwp5EntrP9E9YChz6wIgZlWPdvwbjkXTyn%2BNcS4TchoUBkz0BW7nOIs1rpGpp6YqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhniCz4EzzObhcPkCrcAw3GFoo%2Fur6cktcr%2FJAenf3TPTbjVe%2F3kIUk8bGEEWHi8y36Ge6g8NHRHQmPXqvTH%2BaS4yxzPnnJt72hZT%2FcFnq7wUwvqVUx2M6Nn5%2BMvNv0bGYRbY3JdOT428axXQqExj7mATlreSspWQy318ZlZarYuPzKb8PFq9qXhNpHNZWnQGQVfJNmdX5CSq1yiK2vXg4xgn7xEq5SB2hA1xC47h%2Fqvl83GQI8O3iAPkEo6y46h6ecyLx9LUDi3XOYTgyXkk4f3HGq3zR2I4bWzLwE1kFNrq6tSd%2FtUDqAZpXtqljNw6r7nFRgJr0L0IdNZbcojKuw3iBKP2vjhGDsXku9wnqBlz0EvssgVeS2X%2BYQOF5c%2BUfbCa%2BlxExIcBTqpFmebE8M4dlef7sg4d%2FHEHhapQ%2F5TtTHFe7zt9rHjYOeaKTeATnoHExAvmq27P6Zj7H7mvBJNIKbtgjQhQZS1qmaMjZ7UABYtythnuzEyVwTdbqzt8j7LBanmzlJh%2Beo2c2IyOV7pMqZy5VzHq1%2FAG62rRLLWZh2wrrh1PTPBuaX5d3T468cqiSfUSnU2ioJeRhOQiwAFlZfcc052SB6L%2F4nfVr05CCWPk3E%2BnQTm9x6WJH285rea0bJa65gQy5NMKnt0coGOqUBjeN9gu3gpX%2FGVgHElCR5yt%2F%2FgHXnE%2BfIlanmwe5vETi66geqQc4jvUOPnOkNfC0y1o6Cq6inE8IJ8tGMX1I2uZGzeqnMO%2BR%2F83paeqhtUqz%2FuOxhQIB1cXgwh6R0tKIGjO%2FboyY6CA2lX9cWqCfR1pLI2r%2F8E4YY5AJ2aWLiCmoLjtBPnrn%2FqYd271P7ufDKYYsxRJGAmFHRbBFOZi2mjCMs5AIb&X-Amz-Signature=aaf8437bc0c380d1ff57982d88dc6cdb154e5680d30cfedc9870d9cb2e8a7787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



