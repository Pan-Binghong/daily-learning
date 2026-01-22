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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=c7f59a1fa4c9a935fb9131b28682b2b59b72c580509d28ef1680b36b5395c440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=06be2d19995c019078915d6d92e61b4fc035288bfc9b151de51b4d2db7e247fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=c509e1c2830ee40c664dba3cbe388acece41f204aec4c4b703971c8caa599352&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=a47c27e5c277358d556259be6be10ef944de0f32691e5f4edae8eac900765d53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=90b7566950ebdb608847088921296dd626bcbf53f6033aaed01de5f00f36ffcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=124544058869296c3acf8eb57a71956ec9a55a9e721d16a94db7b200343620d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGWEEY35%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHGsEB96mgckzCkfiRGaRoTflLlkSYnvwj84hRkZn64OAiBUGh7K4dyiT78Ic3hG6%2BP6odKKwUEqjTVJVSez1MDVyiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAEMThT8hhadQLSB3KtwDEAzUKWVXmOqhMS1tfANVgfyeDTn1sZed1TpytpFUoxHKqRBvXqKk%2BzE9U%2BA%2FH%2FfQYkNOLSlz7BNaVfOe6uVOBToZOjhsSM9q%2FVk7dzx6%2FcdxZMCB7v0dCZ%2BFiI9k%2FNPNrCZceRjVroUzNkmazaXQXvOwCu7OUPpIhL6DbWXvUwufsAD1qNj2MeGOBQb3rohZBNOWkGOzWVB3%2FG4SEtwBsCBqbo6KaiZFpgdicejCkdEVU256B5WV5Kf8PV5of46q7zZFx6ZVYVJj6QmfFMu%2Fx1vjMMWPqI206N6d45sm4AaYm6%2B4JGAmN2va84t8xBiUljNIpScNVHtNOUshayxjU5wX5EciSh6iy%2FQJvM9Zuc1uoLKz86rPFOGkGPq8WG81ArAD7FDQ5R88%2BTEPMPE4rUt%2FRYh1C1%2F5CQBUyWKanmBaGeQI20KCXk9i592IpkAs8jp4SC%2FerqyxXGqzUGpsJJnWQ20iSQM9cWU9JBqoA3zoHiZ%2FQH3%2FvvzG3Xb%2Bs2F5DJgUlUK6xWGjiLPVmIdz%2FUwGauzfcw3elj1GfFZVDQ6tkoAkhUKBVHrFSjXkSkOUOGJpLAXjQgCr%2B%2F402JIr40vzHd2a0CkU5bzzv9HfqT%2B1aecuyKF3qOn%2Bx14w3tjFywY6pgFx6yYqCsryeSfaghldAgmVUpXeXXCGC1eS4uqf92qMMp%2FKx4Owtd61hV6O6yOj5vw6iEwY29MF4nuCIAIAAx9Y4LIAg05q5UNm9t%2BJ3XJpzDUFgRF98w7PYkWVFP4EiF4NVC1%2FOvUIDdIHk%2BitYghflSwzd0e7Ms%2FReVzbZTuN5K6XaG0R5vd6jejkwvg4b%2BJrgiRowgy44prV3fnEAZ%2F6EOmeTH7a&X-Amz-Signature=2a2f1ebe943e5bc8e7bb1b34de41b3a3f34e5b68a7f3e529ee2279212dff11f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



