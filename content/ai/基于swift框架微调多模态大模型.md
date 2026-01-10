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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=6758f23e9749ae552c24251a7c99a8a5e10040df1b69aea6bcde15e1753b791d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=331bdfb0227f9accc20cef178711ca2fd0593de2182ba66fee92df1356a9480b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=2e6b18ba7b95f59d253f15db8f84bd0f5afa4faf86a326b60cd1c3124ed456d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=c9207218422e37466bf4ca4bb6cafba48b69d24b2ee2825b1858995d5fc2048b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=3671de7871bc366bad6dca480eca150645d3e9d77e584f1e2e31c994bd56f69a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=db805586327aa28fce43d7e03ef46b27f7989627bdf0458adf6fe8e88793ee4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U77FUZ7K%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKk3yM43adYNYOG2LDr4TXZzmS5vesYS75NifjLnwglAiEArpqvdpR2lMal1lJv4m208h8QdVJBbXtuEfBhD4xsX7wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTz1ahu2GEJFtD1oCrcA2sFnHDDeqDYinqfX0W3AqzXHLo1XopKG8MVTQIPZDKjHh1ecj7dueGvKgkUOAaWCq9lDSfFz3fgZZ5BQgxwzuGrE9Lj%2F69BchE8entpDxu69rJDVa2fgLAaut8UdORI%2BGJmvYAODAn2MWLTxYx6MsD5LAvvFsltPddbOk1ReJxPJKM5uK5yTDOf3ewaSQ0TAvKPUUmijTGwXptTd7avkeMy9Mw9ok3s%2F7g9UV9xC%2F1%2Fs0uhngbfKFxCBOnkJNinlV0M8gsDZWdVmenZxoFX0u57Wu2pzELfR6lq5lFO5BOOdfPxOBguIoPnoy4cAmdqXamC6x0NSYlpGbNtkZbnGn2bODxE3zvyh%2BJbQgxl0PHr9zAdJL8oNX6jRJ6FFjNbvh6EtdNgzeJJFvPSgPkKOyWznXUhk5gSRKHw6mNhr0o7Z%2FwdUYLLT%2FaBPkjegphGXamahM43kEwLVDQIgM%2Br8PNU94MGcb1%2BGyqD9xZ0yEYW8%2F%2FOWwIE5QO9c28cK0EqFiIepr8Ry6Sf1XHWZUkSZyk1XPO5ouTXIqajhywTbEgz%2B6kSVLGIhYUjdK0MLl8bEYxK9WL1hI4ExHWTEeSWctRUtPFOBYUPxuUVeg7B6clNKvR%2BClh9LhaeYcdvMLP5hssGOqUBOZ9IIuyZd4hBt1QlOUP3ZhIEvXBl5q8c3G%2Bu4F2IuZVhXQI%2FucePZETDQJXSm2bUE%2FRPKwIIxvv6l4An72sP2QNa9iNU5w3UoATZ9SsF13MLKWeh2ApU8%2FDYVgxmddW2QuFzknRq3cMGwPJq1Dh%2Ff0cGweWbpCtW0zKOPEJ6IG6ipxOFHnJI%2FAhS7tnPHvb0zN1hjb7Jy%2F45QSJH2QOL73PjBjcW&X-Amz-Signature=b82a697cb274e231298825899f9556cd0ada8c49cca891d0e1dcde7d73228383&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



