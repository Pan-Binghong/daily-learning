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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=033024a5aefc459981501911c120da3f3ba74c167afcf3ead9e0eefb0dca2b15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=d90d107a0766bf44d8d3c82e738826dea52d186ec9fcf36a1dde8f5fec363d19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=9223188553b6f9278d980769da263b350de62839f3e17216f50c0a4fa4b2ec81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=7cbc7779d84830af22fd8ef72f99aa55e521ce734cb20e9934e20efb90a7ca97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=947234ea1aa9aaecf8810a557bfaa9ae954ca525007c8efe704f98d0c4009cbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=d1399fd431344788575252b8d53c2cbc009ea79bdf0b2f7a6f8734ce6d15acbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YRKKTTN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCLVYkckBDRMFTpERi1TX57rIgYRpa6Nc0fGpvz0a%2FfvAIhAIsh1z0p4eEUqd5qIl7RmQXS6Wry7ws7cwnhSisR1sJAKv8DCBMQABoMNjM3NDIzMTgzODA1IgxVaa7HMkoYSppx2joq3AP6TNk%2F8sLlyAkHlDPXLbPQN7SCtMeXgr48HHkYDoPxmSCCFwq1XQfr8iYERxMYMJ9%2FJWTXLAtvCIQT2MyycHKKW9c%2Bvm3wz5jUCbzUnnDGZRg6JdVEK5wdM3FapFVZtpzNQW420wMm6pZt1SihZF5nRblDwrzkvZ61RnMtrTZnIjspSYbxs87DoIa18av8bltVYfPvoNMjSDbe8MDiD0oim3TFaSOLcOFaJgGevXLFzqky4Z6pgoRus1Ps%2FFAR4Kbaa7j562aYU9P6DlOBaP3gYn8eUmrE%2FmBKX%2FUk6%2F6bcAmIW6ft4cVJ%2FYgSE4amoJxBD4017QKzTP84dadUp0X7h5piJZpEAGrhXatQjxq5AYmWOJQnMfm3ZpOQooe3YFfVJDqbJSIWiluIJxtktYfcpENSKVsHE8NbP9dROhXFBsVqvKoqqf4WJDssi7Feoe13rXwp2yp3WQxA51ftDULEK5qJvlCNVpNbgameH2f2aEL%2FBdI3HGuMEPXPwo8QqQBjEhRRT3G1QTrI8LCratLxrdBrMhfwDLEDjbteeS2T%2Fs%2FD1ih0L4yiY8pXtq2s9cgrZs6jrTEb3BNN5QWOz3ULCD3R4xIhgPtDzwfr5EUUYqtfEAM7IDEu7LLl7zD4jPPJBjqkAZuO4hagdhLWQD41%2Fk1qLF%2B7rhARJ%2BxGwXmL1fIPfZRYJ2MTvCTO%2Bcw38pnG09xsrK10CEO%2B5%2BF5Myq9C7vcjgeTIY9Ar230ZB92xtL0kpCcW%2Bkiqr8bqiaXiDAfjSXdzhRaD%2BzHV5t2VTsypcWq4Or2Hv5oUjodNaFYwvKoG%2F1a7XPk2jg9nvfjPQOn0AFOo2caqEklxvtXJa6lmv3Amfzol26j&X-Amz-Signature=6809d7c4e9ecd9418039684e56ee692223818a7ecc46a57e359b980c9d0f66ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



