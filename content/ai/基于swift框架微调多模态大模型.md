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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7295bb61-8ab0-4070-bd3f-db7e22684aec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=306351e42b7818e90d1aeb7ec34edac5aeaf9947c702c2c5914168157eea6917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 下载数据集

## 数据集1

https://modelscope.cn/datasets/AI-ModelScope/coco/summary

使用git下载：

```python
git clone https://www.modelscope.cn/datasets/AI-ModelScope/coco.git
```

目录显示：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e2c32010-8894-47d7-9179-be87793a8047/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=b91bd45dc7dd4581d331897360ee3800e1e51ae7761cffb1666c41718dc7b1d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details><summary>数据集预览</summary>

</details>

---

## 数据集2

https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM/summary

```python
git clone https://www.modelscope.cn/datasets/wangrongsheng/LLaVa-Instruction-MLLM.git
```

下载后的目录显示为：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9f290508-d14b-49a4-89ef-ecca8291feda/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=50eef783853293ef73dab8801f5c98af5ce2a55fbf9ab0bfe88e698b03c485b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ebb06fd5-bb6f-414a-98c0-d283637dd059/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=7482e30803f2320d5fb3364c5451035d471b4d5968993a23b6ececde0b2ce7fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daac323a-2e0e-41b3-a36f-ac137beb2139/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=f82c8f495d4f5c3891be38afa3157517f53034117bc08a0691f65a257b6c1733&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/be53aea1-24f9-45f5-97b4-d3873d4ec917/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=1739a2911ebf71b320cd2170e1c44f95b956fa4145c81bd42ef6b4cf5abfb579&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0528f89b-d12b-496f-b3f4-61228d8af710/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DKPC5HP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX9cXlF5FoVJsJm%2FvLMldNfrwTKjWmk%2BBV46zkHmxs7QIhAPu2w1udXk2Xkgcnfw99PoMVglFRlQRzHVNuPf3TbhTRKv8DCEwQABoMNjM3NDIzMTgzODA1IgwUs0fWz0959hCtbX4q3AOIcWLHXucSOvvprv7DpdIxxXVdbC%2Fu1QW45DMrC7SLbs7E0XRcxJTVDcVXXGmnfprT0sl4FgtJPyaIC7XpNKn0PHODXiCSUfMb51SyvrMeEgDFdjaZFiFNk3Cg02NsyLxV24ns8j6pcMu9RTWaom0waoIG%2FBusyPjBZn%2BV1V28uepwmYqhOH%2FS2nheulLENXV%2FC3TqksX51dyiEi7OTiKFfTpJ9pfpJMkOt0xylcHtpfUfIYbEL9%2BMUL5J08ecjZMr89GuLWHIpX0vA7XwvNZ1NlA%2BqzIzCRCAZZme%2F1GSCKue4smm9MOo2T8Y%2FuQpTlXJKJt%2FOJ58VwpFeE7q2FhcZfPscXg%2FoFUiU0FXvuXEW4x9WovNawKiPM37WkK97JE6xqct4wCqAH3nWbfJvcDSQLYU%2BcQPIoVClEqYKW%2BCcysW5C%2FKOI3KvA%2F8EQXoFXQReCRaRjnZld6i6dhvaKOueBejsi%2BsjSr2IbtbhnhQunMY155PcTC2HMwCesn%2BB1LEkudJACY1Ct%2Bdtu0xD2C2C0%2BqaparJb3XtjNdYq%2FgwxOjIHJ4f9CCT2K2WRwRrsg25tzS05c791iW4kjhAmbK2lpGNsCA7oGyBwMUv2XcZuaDHZuT132rVYIAMTDp0%2BDLBjqkAXS8JlAsf0RuuE89zMUva%2BzjLnBe3DZKeQTbGHPrF0IL9nzweyQSf3jth9t4FqbI0tO4GaGL%2BG5De8nXUFxqGSsjPFkmaTEZ8dOpjZ7jUP6ivUDDzOCq%2BNhC71mjeAFse8DGtH1CI7cWPanbPez01dATNsHTa8RgBCZOuIVL0OVq%2BlXeq%2F06xZbVi3JCAgomXYz17obclZ%2Fq64%2Bs5fFiNgLZBNtt&X-Amz-Signature=e2a9240c51eb3c40d055e78e42d14769bd9bcedb2afc927eeb13ed585a8e6c8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 7. 坑

1. 命令行启动微调报错
1. 加载数据集，占用大量系统盘内存。
1. 加载大型数据集时，启动流式加载，报错
1. 构建自定义数据集，指定路径加载失败
---

> References



