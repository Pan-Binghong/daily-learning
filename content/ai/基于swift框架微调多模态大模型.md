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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=f3d7f6139b333baba06b7608469345e7f05ebff61da1fd235733bcfcebc0cde1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=6369eb5ce9c3c32bd1b9967c87163b8fa204e10e9938455db21b03151e5fbfdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=64c47d2182c02cb9c1abce7b6d849c1a6ae034f85763ad6c2ebb9134ba9e86af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=00892e011bc5d24757101ed448f2f7d8d3ac965ec1761f168bdfa35f3acfac28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=3310d33258bc8bfe50730486a7d1b4dfc180f19526fe7545750973fc349d1704&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=24787af03db072f386d325d02817fc61e1ccaa3e5d7821c2dfa4d18cad64b8af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXZAIIOO%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKysa%2F45KeSTXfVQ2qmQQMTV8fxUppBccZUUI%2BmHyaIAiEAlmH3EZyyXggOAjLmfarpZxtVHKHQ44pdu5l6OjB2EycqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKManJ2nENMqQq4fpCrcA8np%2FNVcHlplp9NejFy2UnK0LQGmwjALrcR6pzZsD8j4y4qy87RiF7DWnEK9UR3vwbHcWWgPOex4p%2FioyjnTzXlXYCmpQlNJgx%2BPtJbV3DrEbPPi7JShUD%2B2N79BzGrPv%2F9BiSIQZrDReW66fu4yVVlsw2HaeR71l%2FwyDsb0VfL1UXXnVhPJ1lMFxsxJ0I5AaxSqjG4SC2Cj2a2pRaqkV%2F9LsmjrrK2Ou5oIsCAlTuUF5egoq96o%2FTjwHaDGyd%2BFJn3TcozQSHHUovdKYoUX%2FjdEp5depVteZy%2F%2B7FBs1l6RCOUL6tZVX8rACIw1HOQBCe04Y8zJa9nY%2FIVh6YXQf0Y%2FRso%2FaEvTLSSJgdihFlyUYQvNlxjnFw5El0dP41Ap2Kw1K2%2Bsh5W5JKOxFm6O%2F7CZ4a23uRjvPF1M6ivG9cRMg4aZyiBRIOlvKmz0VNP8o7xHctTuTLvCGbBQr1Z5un5DtUYphVDd%2F9lTTyhhNSraqW2zMjbXRQQk%2FrSGqJgdxqRmwg4bTX2z51dNokpZtgIOs39W7p723shSeSpf8vGZbOCXXHIpJBjCI3XrOa0N%2BkBuzN%2FU8zzLvP2mc7cnz%2FM0bopXzbV7sGsPdlAzlXT2XZMhqfc4jBgTtHCZMM3MnskGOqUBYRctlazmW0TiPLUgfePQZyuzv5QPaNx2oLotsZKQkrQuohLiB4PPv2F5I3F9%2FulAxlCQrnNF1hupvCxb7UWy2wl%2Fa5TKp5%2Bda8U64M49BhzzGPmrbGEQSwshXEJ9wPjGDN1Q89kfzJWqjszxU1B9UnlbIDMA1tZIo6N9Q24hPSUzzt2zTZK0a8fOIphabz6DZXHIKZG3i5H3zKCBn18d0gLAjGV0&X-Amz-Signature=a972effe53959a412eb7abdf2511b9259dee583e97f82a64264af4acc929cc97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



