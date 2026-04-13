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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=52164fa8edcefb99455bac0efd315661947e9cf08250bb56e3740ce20edc45b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=abb33889313294dd635449416882f02d79dc60980f1c542bda930d0398381259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=94846b8b02027f4492eb7a39ccbd0e02b46e8c3d289ea48f70f3f0aa63a25cfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=874c1b699d923a31af79af5902089c0b3816c48de2ae84a4c612a0e9a387b169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=b4dfc15bcce336013ffcfe8915c1bf52d7ac56e6ed86deaf9d339e88d992083c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=9cded96c9b9d2576b3328076327cbe52f59edde428a2e35273f4cf23996714fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR4QESXD%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDckzEwxPw5r5PuqoFfwNFead4pTzcSQ1XcYRUeg6B0AiEAxzbJXtUA1un%2BRMa2ZcjuG3Dj25XwbScoF3NlW5U%2B3HEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKT0hW05%2B0xEhYUimCrcA%2BEwDltzVoxK25OejwdBgdVFwy6W0hzasGl1DknCaTlqGxyQKcMeZgZt%2FZ2RCjwY5O%2FB3p60pt0vhiAw5nwN0%2BWfrv2swebnluxWHraDulcCtwc132vMviv34MSvUkdA9FlCE7K5Gk6N%2FYZxuflpEL5vb52HaqI36Hf%2FQ8o%2FYj090Wqo8PZGmFrdllTBSt3mxrPrP2RMkxfKgGiWarYw2foBeDlEv%2FytGqhQSQoEtxTf0l31yWmTs5o6zyHm39Be%2BkMMRrgVjyVjlROaWbjr%2FU5CfuKjeTE8NHlkJrECi3Zuseht9L5zWmmsXdeAxsk1LyQSteyuCH%2B6YLnOJxCy6bYzPCWAZvtBSq3mvgEO2TScpZnxxpuWsusRpydLL%2F5%2F1lofEBs6m7rPcY49eNlyCL6JhTWMKXs7QfwcibGz8O69eNSDE2BO7%2FrIY7DRe0xX3LI4eyzvOWnZQAaWKAfGas0j%2FTn3xnvEOPCKem1q8%2BKzozHi8MI6U6Pg3XQrTluQfN7HbPt2CNEvXmlRD%2BwtO5HGadGkASMwLuvBSxvLePu7Nzyb9Q1%2FTmuyR1dPtRVnP3FgI9gy4QMHN3slMhWClXMT%2Fjtvr8CYDy48A1iv2ZrCBniL%2BbfCovY%2BJuMRMNiu8c4GOqUB3jjpQWtL0qzEDg0ft2OQ%2BIUn0XXhK3CTsfS7Hxts8EPzpZcsXuYAKp5qD4d1NGV7XRZPT7hT8BK%2FgwYVnEhLLySiWzBfWvcuubzVWMvsInx7RpGKDz9lDlVAXlCXrho%2BhDpV4x%2FnEUgetwGHQEAAuZGIA8q2y9p%2FFVcf2HgxSxEqmRSs6BbdaY%2BnRqVvcqkYjF4tztLZyVIq81SbTfI9C7Rjj5q4&X-Amz-Signature=e15a0ac103d29adf3ede61d6d104d2ede807713f7ad64ae08cd2728187e1bd1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



