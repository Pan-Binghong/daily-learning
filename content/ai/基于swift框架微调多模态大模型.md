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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=9424e9296db9f465148045b899002c7545c1937c8d438c3602fd484a7765cf55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=93e85155277216f45048eb3d521ed44b0be628520ddb82da274c2103ca8010c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=5f85dab2056ab8ce5c452f906e9f930d6e3097c66a1b778b1a342b2bef8c6805&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=211ed0c91b1a2a7a1607ab1967bd645a61d73b0e3792ba48a0752cd700547f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=38cfa7576c93f00ecd4ae15c3262b945c458d540f15089c3f0312140cb472add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=1f7e9e92c1475eea94fb1c44bddcc68fd740826935f369302737a534013afbe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677WOWLCL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCie%2BqY5KPNri73d8Xf6YVILj5zsfBzWwCpRrGm7lMS9gIhAMMliyF6hehhzCayhjBchOf%2BG8AKS9AQALlQxz1fnuF8Kv8DCAkQABoMNjM3NDIzMTgzODA1IgwN6VoW3YcVMhTaHa8q3ANGsKandH99%2FiHJMUHhgn1SFteWS8fBWaefE%2FR5iQIGh1ER9Uji%2BjDW2jDwiG6KiAY71iX9qZ%2B%2FQPy%2B3ee5yP9vLcreohmyKXWZWwRFPv4TbNnb4C0BBljermZ0RbmzZmSw2ucj%2F2SUyk7IrHZe47DzOPIJbgPIZikNf4Sd4ZcFefkx5CI8YrPqlWxa1AVlV5facs7ah7qFG%2BWCmokGlQaAGmUlGcDaH8pbd9GdIoTWNuGmQ2i1dtpMEN1%2FYXinYdTq1CcBjQVeTOW3PdAblFB9mIysnpJGoEh%2FpTGaodQNWGVYLgQVOvIoWVnD23v28W%2FwSG8lJocakyEA6yVximPp%2B6BITcjj6%2BKJtAUWlUszu9jdwSsetaKnpaZqd0iVtgTP%2FHT48Boyy56C8nFQ8jry%2Bs4YAGDbTq5SIagu2UHWN2nlvDUxqCJPwxeEevtd8zCc6TnH8KVFcj3Onm5wL8%2B3MwYjsbjjLOy%2Bi4iLY09jMSAlF08RXZSS3WTdHuoJmcb8QhGeeFGMgNulKNU28IHJjK9iF4iBX1HEyVgAq4VEjJA8jhTs7YwC9Uo6RmCLVyE8BN9IlI2KIFNw3kypgs81FAOVVTJtRPBDxMfc4g%2BaM1niM%2FakAHq%2BKzfB%2BTDW3rjJBjqkAYfiyWBRLRrl5kK6hpyBNNUlF8vElsqKVEWgbEa26%2FXNDpEAFmLSPLRZDDMjYU6ed32DzUZ4MNQi231Yzjq471y20ItAppUTumf%2F3M%2BOG%2F0XTb9uuYv9nB0UZ0seFxQKhfrXSirxPyv35AHPQCcJJrDuCMP3WysmO60X2d7LaDuht9IB9HepetfDH3PhWNkvRDnjdr%2BBTWOakfz%2FIhGP6t%2Flyo1V&X-Amz-Signature=e1149ec40cee7633e5267e78665d804f1429409eeb6edc31f5b4a475f3849af4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



