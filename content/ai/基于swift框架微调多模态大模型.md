---
title: 基于Swift框架微调多模态大模型
date: '2025-03-21T06:10:00.000Z'
lastmod: '2025-04-11T02:22:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=dc1f5267b15a37f00a971c6028fdefd18e8967c78287ec5de9346a7cc863a8d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=04fbe287b8e9fd036853bbfc9d75e59507f26a21335693da88ce4e271df1d13b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=67094f4812a5257bc24436ab6099cff08fa4490014afe6251f1a348c98f02cfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=68c591ebaaff5400e03f2196d9864a6930d09c77d7b728c1bc04ec1dc68f0a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=5b8986d45214a8de837ecf5ef7c0794bb310878d6ad63bb9caa3603075ff0ff8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=a1ac68e9e5b59a62187ffea45d078ac7dfaa0bd6812855938fb8e0545abb24af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2XIMQQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGwKHxk4Kx6LH0cdHphJ6ez%2BWyl2vJipyZje1LyG1pzAiA8dU1Ci2P50FcbDEXmI0%2F751cpfw%2BhPlBlfqWCde9%2BfSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYn5dqY6MwghqgpdXKtwD%2FUhvTOZA8wXO3LgU0s8dSOEHsK6aRunQ%2FO%2F0o5rRFYnOk0NZhaCuaV7MlSLR0z%2FR6V%2F4%2FELTmTfx7TIV6BRgngok%2B2FTZ0ka%2FzJelFtzp7MiBuU%2BgEPgu7XSzix%2Fx5TXtG0a31oMfp8csxK0U9D5%2B47sWmdRCbY2wzNGiJVNj%2Bd9YMAywDSyoNgrK20yPiyz08%2BSHjlBfFTrSlwRsRqwUKR23xfxPNU8jpNasPPx9Mz2%2BHoiwVsC%2FR%2FkmpdWVWhazVByCl9ZaTC0pe1gyM4QJPOyjnku7joKw6zzI8KJDitvfYHnR6dedobJ9DUD%2F0zEsoF0keZf7JnZwMSUGsPNQ9LpGfvucn%2BgEGE9X3zeMmxtGeQOsJ8JWWIVdSeKeEhm0cgXqxyjWmIa9e8klS8iIpW3KJSCVmtg3oRnY9NmtwI20uWjOIGZONvPfn6l2Y6eDxTwWHMlh%2B2cMvG9MO4JMaJJUrNnJGHV94Vtj0MUTmwigqf9hr%2BcFGD2WbYdMsXAlI1iqShZByNUn8ND3KQsDoBLaePMUN4n2i3yDrMKJf62AfesgthcSxrtX6m3nmSgJmmGL3LUNqJRcLCYVSOZJItnXqYDOSgsxyjUsWSlv5o4oN6LUO5X637ONo0wvaOsyAY6pgEW4JNHtucLebY0s%2B7c79h2ihulWGUNQDuFJqOxNya%2BFdT0XUKs8Gcmh1VyGKjrui8xqgYxRar37yHvl2mO2jLkXFs%2FhKpn1Swis4O1if0TvNjWlha34NEElZWL9P%2BXb1RXjzCYa5A0W8TKlljqqMvaSyxqwB6E%2BjFL4EMXI%2B%2B1CmN%2BBE%2B5QXtbDSxagrtAhbKhgbNpL4mThk1rtRNm0aQG2NRlzhrh&X-Amz-Signature=3764760ac59d2a42aa74cd291966ac8206dcfedd309e9bcc53273a3c4b0812aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



