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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=f03bbdf20fed52ae2ce8032c7a3c3c48cc61495521d17cd3cd3af0cc58d57242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=aa3d07ce4bfe9c0de0608ee6f6ca838af62672b3273956b6b96822b464b9d0df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=4e26fb6aeaba78cdea88bef467a3bdf5e47804de399fa7b0094c64321a5511b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=5e5bd3d6f38d37d23816f94a5503535d19f5d0a7878a0f1dcf2e310d2a4f4def&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=d6317f860ff538284101bc643778560e068f653ae615f0e8f69ccc568fa6e725&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=efc812934968768322e7288217e79c9a2991bffa55d02ffc7a0697a8bf86abd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CYMUGDD%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDKbGDRH%2BB5feluNTLOWoRuAW94FoomlwooaoV6s9iSiwIgKQCVUAB%2FYEItZqRlAV7YCG5HtIZViqFLQbyxeKpss5wq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIMcSvYkXW8QTa%2FB%2BCrcA76oZnhvWBkRehkEXVFqdziUNF9fy1k1Z4z1GvVLNzbDfgC2TP4idshAFtNj7g%2B7ABfm91YD%2B9iBYj4fcEjj5hrJbgva07DsyogLHdlFSEOGOPya4J0AQAzGM%2F15%2BdCxI09osf%2FjVKWK%2F8Lhyhy0b3hBNy8uHtzu9CgTywpUhlBowup7VwbF75%2BlwlMyF5xEOsRM%2B4%2FTpH9Gf8c2qIZMNesaMxsYc26FLbiMOWwcxZghvtan87cEJQ%2FsZWrlK%2F35vEVN2tgquNTQM2uLkUPxFRlIJFt6crCALc36fBaPia7mMBkrpTBm0tFs6WM1jgfnsYlTb9sn8IgmgQ3EOSLbLFPrb2TzZVV6yxMBvNqt15V50voUvKr50zNSDo9ADg%2BqxPjPFgs0T4t0neurUZIEAuAIYYArLdsHr3p9zEBeYVJJKA3P%2F2q3sd34Yc56Lbxq7BQZsVFlaknEDmgec4vOvF%2B6lz7jyCh3IJTiesrnNumf6PDhjhw76xsmVSXS4gqVyIXDsYp5oEEAw8rWSkUSoh3vuIJgwo2%2FXwAaTHM6ezmBKdbW65FQux0nT2%2Bs%2Fphp8I%2FVMHeITaqFiI7GODnTRyv216ZK%2Ftv7CJks9a%2Faflhlzk4Z47Lb0h8CNVhuMKvQs80GOqUBZMsGML%2BmeKaLKk4KaLCSRPMi9hLiUvb3Ki5WmpuXfd5CLhwRFji67vAsYsHrU6ZGZW2UVikJ3tsLWDxCc75k7t4qeqJ32FE3gs31hgdpoo048yz8INjeI%2BcRypw4exzvtvOeb6McWGlE5BkSmmR5GC1jkFhPpE97v%2B5S2Bjr7va8zEo0CxJFR6kCNlX1tMmlFPftkyJmDVTlc8j3RRgNVizdP2Js&X-Amz-Signature=1f8791d772437fe313217f4fad1a4fabc9c5ae06d2711f14b719a435a9e4bfa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



