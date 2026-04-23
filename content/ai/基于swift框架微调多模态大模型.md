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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=49962705339536d5becd1065b607e94d6fb9781ab223d249609327ff3f601ad9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=b02ae3796dfb36f80145276c29a123d26771c6cd12cd9a11e39fc7d21cf58fa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=220bd1023d3c9a499e45234c0049bf7e5ed5cf311b2aaa993e01d59434dfe8db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=bb5d5e3049dcde6db459016a6595e05f8a0c9fb569ce2568e5a9ac77a22347a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=7b337f1123cae2f252d25ae5e79cd8b8c9968b26bdeb1ebe3dc79d113c33773b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=e2dee5ad8223140de2c1045e1c7bf45bb3decfcf5bd42a76f04c2bdcf378082e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ5GH2L%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJIO7oTa3rgV7LNVce6p4B337Aj9HjaOxn1AIT2goitQIhALTe2HUMHECARjhKjtOQrlRmYe8LArTwUmzlYYmwIGQzKv8DCFwQABoMNjM3NDIzMTgzODA1Igz8vroDO270rubHLBIq3ANqBzR7YwF77b63thXgVyu%2BIXaNW4Sd8KmHiiK8n739etIDmldK%2BU4ULmceB2D4jumRITZb2Ph9TehzPbIqpzBIR7G9vMTenYVijLPxPj5b8VVEkFHDxVcWyNpP%2FD3sDOnvCJtCgaB5tZaiJXNI1TWWRR%2F9pFM6FSwgtT8Z128sCpiRuwGe1FO4rJmjxOoswHygAN8X%2BEf5YqbAY7JPuXsFoVdZHuVlP46cCdHf3HDmX5K87bDG4vzk4cDDZA4%2FNZN0K6XAvjoto%2BvttEswwUaKWqks6rf9N6ybYLUPuhMQ1mASUnEmeO5CvU17Mdwzs7sZ6QqlkDqjOrZbGYfi8Ru73amdMi%2Ff%2BY%2FGxd%2F%2BQMfYFevD9tOPrhDv74ROta%2B4dRUyjHvFaH2GsGtKQjrr597hkp6%2Be6hIJfytmMcmyRxtXt6PUSKOuVxeW8sZFNugi8gFtV2c8n9avWmWl3p86Oqa5fZ%2FjJSTrrohlhfK1F1iNrqkhbNjsS7Os%2FO38F%2BFAMh5joHMzsEHqeE%2Bvl7I98snioafRT1SxYQVrYaQGi7iWwHAza7Pg0JzsIAawFGgAoOyPClTlrgb67FU2in8rfLTXUFCL5LH562wlD77KtwfLM5%2Br2U465I0T1hGpDCFoKbPBjqkARK0opnlbYGv28P1lGEkSuJYUwPOHTuZenWhoA8TXTZ5STRqIdWOfhV0Heiqv3MTrQWLxVCN8pV%2BM6ARkKci%2F03paLvUuTYbi%2FgHXwqHhj%2F2wnex%2Bji%2FW%2B8KMWoDmiH2exyrAOz5h6b49qjeoaGAvLPUug85mXuEbG%2ByEmwSaHKE%2B6m%2BSsRAjfUtlrnG2dldS4OpY%2F2hffxRSE81xjrbG9lGHv%2Fo&X-Amz-Signature=b7e0d94479bf8db8716af22391c25679d3bbebdcc296331f3debe13f168e551e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



