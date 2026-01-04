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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=e65429a37e3842b9ff84d5e7d17f93f0b1a0d8d56d1acd18af17b86b5c9e2f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=c4520510f5547bf356f7dd63ad4c2ef9219eb5d723ff00e4cd813686723ce5d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=59869d44d5bccd7e811fa7968007440107e51b2dd8cdba1a388f6adede4677b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=3e47d5b4c0c475622b9214c50dc023d00488bc34c10141087364b243cc10948c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=d285327203d737e6b04c43935be20ee8aff9298c856c18176e9342f3f8154e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=f4b004ce804634112cdd428f2d95b73b4d442fb1c4047751cb39f2af11f95fe3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TONFN2ZA%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIGmRJ9sumA3HNsVzHpyooAYNSeBDRD4gNZ%2BSRLhTjCrtAiBs%2FRCpor8H1OODG%2Frc1xKGqnKXSka3%2B5Yg6wrQPYF0uyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM8xBvk2E8Ym1j4xXxKtwDok3kj%2FGbghytZVmabLk8RlLHI7bL8hJyPl5hiaXG%2FkpAQa57ZeFEY8X8byb1jsAMH6OTSTd1pZOMQy900CVkyg3Y8tLg%2Bb1u7Eg7kDB8UUcsrYN%2F2dLst%2BKMDUVuPMEhiKhm95qdD9XBbe6QZ6N%2FaLUAhqRfhUsgKI38fX54xrOcGwXdi8yA0NRP9wQmPoJASkip0v9sI%2FwZk8vyaNee4%2Bd7Vc%2B2ulWgRHAvDY%2B0ZvydRnM%2BhHQ2Ep%2BGhKSKkVC2cYBhHVdqHqXk7KmB7RdDRK9g25hASNzoVlPPoeQXs8UhOmU%2BoZUuD%2FzxqPdszbi9qhonFQggP2CY0cTBXzr8KnkcCNUv2zJiwgNOB0K%2FgWBTaWvGUT3iIS%2BD1odYzPUEOh5GqTzTqFXsg8W7pBga2xmBoRyaDHqCnUA6EpoZyGLzEQunPmP8b%2F%2FRcuUbFcSvwXbILlgY6vNM1c%2BEIUKhRKCCO6ku4UtxFKZv63Z8JCvzOltaZtO0nTGSrnn9spVnVqVG1X51ik4UD0zOiSsVZLIYOUZJ4xJMNJvNnFT9n%2FhGs97GMGPvLemWmarUqN5qE4shZ8BFBdKXUhGAjCCoL2ER%2FC6hUKEPd9aXoM0ro4yNHcYOnlys0n8M81cwo%2FjmygY6pgFbWMDaCdaAzYwc0mFhsbN6f%2F%2FytmOg1j6yqVUMCFXNb5vraAqoW%2BS9CtQj82%2FxDG%2BC0jhETB%2FGOHZMPYHqyP%2FPnzoLWMfj6%2FzUVCLmR0JSIhhJkqKPrmIRJRfqktB%2B5KNctNKf9y4UJ0a%2FPmBIq%2BL1dtbKt0SZXryj%2FnlfA5P1%2B5yv4PKGC%2Bb5QTGCqcN0KR40AooIhcRFtV2BcmsikUtPGOHObe1S&X-Amz-Signature=82135b0d82ee8a1a7a4074da14a076f80e53214254b0699570b0f33169b303f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



