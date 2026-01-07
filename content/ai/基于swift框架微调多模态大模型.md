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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=0fea9c5b7fccfa5f4d68dbc1a5b1cff94dbfa90bdd8456ea25ff8120c10bace9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=a94d525f910c95f2b2f4b977e26d37750e57b993f417a42bb298980b95385620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=e32d37abcaf20ee52611278b27eaaa824c5ee51bb5107ef96f9da1a7cde18c5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=d517e4f16ab6f21483cd13003b62a9e48a92fa0052404c143cb2c212d1136c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=4d72dbff7b3327667737d6b28c57d9cd94bb705dbf731c9b26f016915a6ee7c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=f6cd4eb5f58591c6331af9fe003f8023c4ab0b6a3e45df94e793827bb9958da4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTAPMA7%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYR34nzHeQQXn8s3lA8Bn7sYUvXDAk%2FKKYdJpRKBdSwIgGoQaLkBv2bTHbP%2BXcjXstCmhEnpZcO99Y2hVUmxUS44q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDJ3l2YMjeJrML0WxiircA1T7Uc7QFHFrIva8l%2B94llVUNaC73jy6iyC4BNl4O4pvvxCixLWAxfkgpRim6Kn9sUfnPqBdOYeNXcmEbDi5Tfv%2FNaByfzolwfmweVBg02jM059J6frj5Sg91WqfsNz26OW0PNMjTeQZA4GBXudz4rALMIoKlsUBjCYajSxxnqCjXdizlZtPuA%2FBHjlcn5O31oET5iTXPT2En%2FAG%2Fm7IgLtxpyhE5VpQ82%2FlLzfdPnK9pqQtRgbgLBwSi%2Bnd%2FjdRjp1LpaVAL9oK77V5o4U5RSP1LbnM3vpujyAfMBu8lPvK14baWY7bmKsa7xh2fkph1%2F3W0u%2BtMhA2HJdGXSeeqLFs5RQ9sq%2F6%2FavhgErSXOPgRA5sOoCsKGUpu2udjmlEwNoQDWkurCm4U6AZ0%2BUbInCEbLlgfVOd%2FJf8v0N5ou02%2BhFS%2B%2F0LD8XXXqOCs00KS49njDzsa6BkbU5%2BzCmAhs9ow68Q%2BRCjp4GCkwoLgnWpDKj6Qnn%2BqA2iT%2B5eMhYAlp%2B551NNr7QfHq4qDCTnml%2FYKPvBJ55q%2FUBc5UHFY%2FvDNw159fZ72uOwN8kv8fX08hO1Gcp%2BrhpJ9jzi8cdEFPeD3Ny1loHN0tzQ5K%2Fb2dUyBu07ofZVEtdrtSZBMIuP98oGOqUBkgIz7rMiDOvph%2BSN5VsqU3FCZfz9l%2B9GkNESzStPvGnDrgjR3zM8q49LxO7euMV3nKC5%2Fqo%2BE9638PMhxMHr%2BBh2%2B6H%2FvohBI4C9uNMAXZKYwWp4SHN4fX4yMgG6fZIiiTbmNgi%2Blvc%2FO05F2APNWRHYiIk6GVd1GpLe73hH0AflPRQYeKZDfK5WUQTkbFwL%2FBJkV5DD7PbejBT2Xl4iCPnF6h8d&X-Amz-Signature=1f87fb2cd0eb8d168677d63cd8bc7d487fc32cfd77a7154e2704de0063e07bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



