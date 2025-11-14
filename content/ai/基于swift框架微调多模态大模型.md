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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=12046c2381db150630c64e6593154b0a135db7166fb94d95bc08221096307c4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=ea42eaf5c4ee4436ba7d2ad278dbeef830bcaab203194f3fae24a13c1344dc45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=1992199112444636343bd6e4584b6be84188c9e600a77d2cee671ad97916b887&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=41da5fcf3132b7386b67eae41796f15e9027e9379d99fd08ec5131cab3916c73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=5c096a7c55234a4d5a7b7c913ed815f54cdfac240365287500fff77899b70e31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=4beb377375cdc98c79a676a0eec3e52d9abb6ba5b2598d6c4dadb03e3caf3182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2K5GCLP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWfes%2BsnFQahvt52IyK5dau9saQcXszGFhGsmRoek1yAIgYOSv%2BFYqMF27I5DWT5sQRNvkeuG2X2rAFZo%2FnHSpCUoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDEzzCr4Euc1D%2Bld1gircA%2B7Ihpg9LuulWzeR6sDVuvzb8EVeWM5NiSOJtF1ddjiHaZ1SlTNBYPkpMUAsfaw1v9ry1gZfFfHU3%2BG0yHo%2FHFvnDpXPU6AptT2GsItrfWKEAL%2FY5ciud8D4OyZDhuASgMSqN5DOnklqgbSB4uOxM9ENL4jdoanaOky91Yny2PpPJhijc3flM3MhITeCtbINZBv%2FKCRcdavrUp722TZLY5bVHa3Zjgl3PWUDG5QbXFWL%2BXzaK7BPKm8Jeb6YtYv2yMr1SefpcEWAUm%2F%2Bkls%2FvnGlNde7CZUIATqNt1y9uhFZNV15T5H0rjJRdPE8XCowleB9hJvpTah5B1cq8IC7MPE0Hzswu0HdgRtplZqrDs0Cel7t%2FLOGmfhdXXu%2FiKEGBStULBOPbL4sLbuDdrqf8Sipu4GNT3hXoNQilolTFS6rYnqzWnVB9h2RC1wUW06N%2FoDbqfAso9ADRPgGypft5zRGyY2pwE7M4Y9H1WJ%2BeaLyAOB99JtXisafE2%2BnbJ2JJQoYVo8s1FZWA7Qho3ZS6vA%2BHd26QkcrT2JRxG5lCGZXqoe5fu4wJZUxypqsbnCRnRpauTlgZ2KuTwZHVey4e2wPhqw49zxUU11zFAtS%2BZGsIJ6%2FpoDy8MsnASH1MOSJ2sgGOqUBEon%2FRJ0P7AvUenOMJKlg31webjY03dEqtXLpyCj6C%2B9qwmkJOmeqZ8xiHENjXuHJi%2BA6O3dsGx2S9V%2BTq1cx4xKexWZsMVm98puTLauKxO%2BYfuKRbbnWwIpZgc2BdT8oiMgRYJTVKnZw8Kws0oAHyEPJUbHePzMHshuLzjSdIWpuH%2BGZqWKmcNq5AnVTo0j%2BgeIoZI%2BXGeyeIYCUQ%2BsSz6AsYdZg&X-Amz-Signature=ae17f7f45b4bdf81d4bcd5637c7df7523ed71aaa5f1190409874c1916602c508&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



