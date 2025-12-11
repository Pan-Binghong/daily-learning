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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=e57563cfb7f6800d7b94d8ddabbd619ff5b22d81158fe09f2807ef7b03162ddd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=3cfd9c7fedc9d32aa5d4907f973198a2fe0f1366fb1b2e1f77c2c7883b0e7595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=c270f47dedb28ff3f3805824645789c70e4a9a7014a44b4733d8258722aee849&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=a658bafbcf227b9262ed3dbecafb59cd325d0eff7bd417023cddadbf67a33d4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=0ad9b1f39dd3bd88adc0bae8856114e6a7abd2606e0d3aa0a4ddb46a66921cd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=2f6b522f89c40aa6178f387d001db981894e189efb6f553aff7197d1ec6f6ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STP36Q4I%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCK9S4lq8XqVpF4vIX1npY4mQofRxibC9g2Zzs%2BALQVpwIgdJ1feon5N3jBHbeN5eoZyzLsAHuC42zlnidSW6kknEAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyLgiYYhXXiIMQ0YCrcA3NxldbkN%2Fo%2BW%2BNa3vQ2j8JYBtL3iz%2F%2BOaXJVQEQp0i2oa90QgxVK6%2Bcmr2kDyAjsw7IpCr37ylwwKo%2FO%2BDPLKq6u0iLIOVs%2BqdF1TDLeJyulUBiVzUZ7Sz1Lwa47G8mQRb1DLy3Z22LIcW%2BOk%2FhVjYP7ayIVaMch%2BEJIyavQj7v8AtVZrRwWQ4uVj6yojpU%2FdLKuN7t8BJ%2BUdPRJSpElotmn%2FOHQaJkrDyQrha6lO81Jld49U8fkhobF0tLsrBMMp3dISFod3hFAGMdev9%2FaE4B5mPD2Lill1Jkq%2FJ0t1vDAZle6s57Qb3Q8G0AqnFjC0R0fzRwjwGaUUaSU0GMa4%2B7tVoTBY4CEMwjlh0vl4VvujTa7wOB5n68IIlm%2FRuul%2FvmCzQ4p7GboEuK0szk3hzUT2mPDG60sxGM%2FqGRmRJmQ9UGCV8njWUSM4gxr9CbmjyB5u478wJd%2BDK7zBBsZMsr2nezrNrltNDgyjCHH4LtBiN%2FdcaMfw90eBDi4QK0UjJXvbFQ3kidrgkyzegKOKHFcBUW8AeByU8yYHZlCsjPbfrwTFc8lg8vsrMIuI3VYCsz47kVUO%2B5EdB0Sfnk8I2ZWkmntnK61JaMbBGF4mwweOTd%2B2rBzE25%2FPUCMPW16MkGOqUByhoTLcfoAADcMIzBViQbO5e9D4FrHAemJqTWlbUaZ9Sfkq5KGcRP0KJEZ%2FDxxxYSpgAo4w5trV69%2BGueRnMfqlzpom1u6J5ciDFjQee0%2BHaOiWF6U%2FFB4qTVPr2U7iRhl2Ea8gEB2YDdXWpYKtw18jRTt4hR5sIyogl%2FKwKBD5W%2B41DZKpTzbUXINojA4QYkiWzVOFFqtvrKTJpNLW6OkBDm7Q%2Ba&X-Amz-Signature=19deb72ae530af798edc14e4e5103bed7522c7cb6a69ffcd3cdcfd42e9a5f855&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



