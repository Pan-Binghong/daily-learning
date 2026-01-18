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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=560c00e9fde08635b7b1028dd824925d8abc5c4d313d59baad4968487fd23f4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=c74d107ecd7a32e8cc794bb453d2b34ac8902bcd3bc30002d4d2423f4d0f6c0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=6dbb0973e0d4955af5f647a1455a4ebd07fef1add82cc1d000b9151609e9f20f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=c1fe29d1f55bd16205cd0b2969474294a46be3090ffb97a7e14da63829abe81f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=fee7788140309c1b0e4c2d553ecfd5313a26361c8efcf5a622dc96759245ed78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=fe602ea429c006aa3587e041fb33dea7f38652581216c08c79526274d747f42b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLPEPQ37%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFFW%2BYolKa3xqEUjT2RNPtBWbkPXKwWtbR9gTUhTwPAqAiEA8Sb3Tit9q4GiTbfznPcSxQ4tmnq4S6rr64cp1p4RaeAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDPM58rawD3wx6lV4SCrcA3%2BkGBEsU3t1imHRi0EUN378yNWQtbLMh51ZUXfOr7iddQd0zFO7ggKZSpePRG2oQbfdWBb%2BpQc6hugqvIc1QVggIBOsTdi7fEA1rAk7433RgPJdX7BUUumzRlsZaCryCVn1WWdzrf1naFJFPga4FPzqBelvcr%2BvsrDgcr4S8EnGOW89PVkSy6v2y3j0UYtiNDRRtzSYxYEl5G7Hmbu76sylHqxttsCxInNE122%2FvJbAFohUy9Mlli5AOFkPnkEZGQh7o42y016kB7ti8zQ6n%2B4gBTUgq0mgO3gh3THP7RaSpIwLDXD8bO28EmyND6L5z6yRLRcv0%2BljlGrKGlBaSChwUOSFXPv4%2BeRHsLbN%2Bqk45ybKv28Af%2BXkHeUrnNA5fSXjZCslDSxlbYByrxnPN4tZkEYoZeRUfoMfPWNKgsr08sgjevkSu%2FbMHUxWnk2owqF7%2BkwkksbImqaiN8lXHHSf2hmNpFZFgwrSvmBSd3p2CVWNDtEGRKkiCEymeN47nGlcel8svyqg65JQiSWFWpu3tSugSS%2FrJVn%2FXjyfnFZA9j38MfBHBxXt8HflxnYAFa7JEHx79hwgZ7YPDKHxY4%2B%2B8GYmYwiZSgsvOErAGXhtpnjhOLYq900mmnJgMP2BscsGOqUBf5cAo4axsLgtAAJVp7qHTwSWkqaQ3qsmeijoZGcD3q9gYljqK9iwwOEMF%2FDGFJDwQ4LC1v1%2BLXv0jLH9HV55OkGAFkV1h4dgMp3CHVnUh5iVsO1Eel4OTpz42p1FYaYxUYiTc%2FCWWIozoM8aBQLYncMEwc%2FHmVuZYiRMMx%2F5GFZL%2BoNA8msefPqfo7ElXgiU0zbRV1FqLFgdHJwh61NfDsVaMHTT&X-Amz-Signature=a19bbeaf7c96ba910ad5103e246a4a033cbb01e3d1063314c7bdcdfd9f046ff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



