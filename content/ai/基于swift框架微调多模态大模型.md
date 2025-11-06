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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=823b5849441fb2173d42804bc17404715bb5edbed8343e9e3d13a693f3850c82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=4e9203e0e8bb8b7168e740f6300b01ff42783006297edfa12ff220300e95757d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=0537adbfdb6754eee69e63d3252767bf90807faade35d9634c6928a6df88f073&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=7bc3ca2dba823f2b043b98012c3202b50bb2440a5789f48d2fa265a837f26c66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=a5a7bcc688421cdbb699eb4b990858546a5765c320477d082ec95c4ff2599f6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=eff008d16710929eaf8e04ce7e4fd40e055f9d1fb92d4cd6064e290b5dbabb0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKIFAWRJ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq4I%2FtVr75hE26Lh%2B3ZGy9W%2BQTvS4FrX%2B0A0u%2BunzvbAiEA67lReD7v18u5JOWGs2R4olKsUs90aDwMGzGJh8SyrRwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcqOr4%2BFWt9e1gI6yrcA4k5JOHJi7LZtGDWSiv7MdwtK0A8%2BHzx56hww%2BH0RQaL03dJGOSrPL5uTt4jzW%2FJym5cS%2BYs1AaTPP%2Fxk%2FDNSMU62OubL%2BA%2BTpq7dr%2BemaSqbgt%2FqZ9Guch1SM778oH%2BtAWoB6Af5pmGzQmkOuJtJ1yWtVDQJZ96XxocC%2BQ9AYniEzDwBtTviy63iqFpRddtrO7foCaRGITDTjFOx%2BrryNbRC9qsqru1FphpmAkULN0x%2FY4xxu4gQG37ySY2Q6zHc135w%2FD11iZB4tNRu91Ybliq7fmYwGBk3H%2BkDEucxDKpY0KpiIY%2BNnwIEqDp6efZx4agP1Mqn7Q%2FMbqUOx%2B2aSx%2B3ss2yp3tY8pT2PVKWAo1uPu98R60nRzahrgTRqLm%2BSe8MRKcxCJwrQ1AsHj7QUgeEM9RQ6vq%2FIGZLhuQrJ6xGw5kh3uUAbKOphjEMKXj8i8jNEFxOj0WWoBhYht832MyX6ENzosVtBDC0XIbZSWOeyTmsAPOFYNSSRFEEiVVsj2ee1Du2wJy9y06Ls74zCmlFLyutvbF6mEphJomtNX9ke2eCehjcG807S6C%2BvTJcvf4i5qyiXFlqr2zbz1DzHXF0YOE%2BwG2oUrX8fXvdyUu9Cw%2Fcub%2F1ZK51tHoMPaVsMgGOqUBxAZSa%2FLu7274G%2FaaA6JqXxQlyJDKUhsA9%2FhLxArpjhBZjfs%2BXaCNxGVcmRTnjJSTy7VTF3K%2FiMvSls02os1pMiTmTv2R5reLG4IHY1C4W8I%2BrOzbs9ROm5yfBroMVAmqa3TziAVsmmh%2BUSTFmPim5OdB34TL08lKERu2t1roFb%2FwvPUo%2FkLMHPl%2FN76F%2BsXzbWVy%2BEHEJiapV7t0WTbbIlfY43Sd&X-Amz-Signature=8310124a23701cf085e1b03e9e49800ba7f092adfed82ef546be3aeab80c9117&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



