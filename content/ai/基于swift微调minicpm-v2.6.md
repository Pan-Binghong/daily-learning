---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL72ZYU4%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T030956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIFx%2BH%2Ba9auzJipa3caK%2BFzsR9L1vtTJeyfzLNz6DoBSFAiEAyAVL65mu9gSWL%2Bs2ciOpALrlRhwxfDS67zXWjUxHub4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDOt1CoMV6tMWE%2FjW%2FircA8REHbJXQ2R1UmrVwFKomQJ30fwg5EjPXbFwDwZR4A3v%2FxK58NoPNAZBTNtXMK1YKPBpdYKXOeV8uvDQb8LSQUL%2FTBT2xXAg2mMmW80IYWvxEEadq1FzF1WaQV4VlxZPNVkaHC4T9FB%2BR2OovXcPaCf6uYv%2BWolmvCecpGaaGlg58sx0FFfokknxo99HKnLlp83lifdk4rcVEsbXq2DzJFs0tZLLswd1j8n%2BbRHRGRJYHKm8zBgwy4N%2F%2F5sLQ1fFmavAJMpoNjA8q1aXeTm61xqkoGjrYgKMyDfUXDAx1nexy%2Bq7u9NgVGArLUwqc8zvUIY4%2FXkx6nGB2Ttxnvu%2FB3E54bZ%2F4o6RQcxe7nV3gKHHna3vIaXvn9PjVbyVZoX7QunGNQMVV6JUMJZJr3Q4hZDF9Wr2rvMxQDulMnvl7dUbvY1Tngd%2FOGk5Trx%2BKJZHJJX5b0o4FPN3YsJMKtlXtdhWnWpmWOb5UEkaIAQuPav%2BBqSwmsiYt%2Bs2UD6vsyC4cshuWbXjEZRHiAEGgFcOt62Q%2Bz96Ssb6mPz1UxfOtRMCjrfCt2h2islwvz29mVd%2Fpr0U3JfKMrOCLFVL7jk7mOgeU%2FzmDCvzM67hoipq5J7rRc3fxX8a3OeXgj%2FFMKmO5soGOqUBSmz%2Bwc%2FpuirY%2Fm44Up9pVA%2Fp%2F28SZaOTQvSDq8raBBN3Lj96HHbfrO%2F4PIPLWa7wf9ch%2BUSqziFG7sr9nYAShPcMofijByhG4GduPe0DpbLNN7FU8wnCA5IGybZ1Is%2BiIRvn1TTmJQbf75qjSwG1ciZZihFACquM8Vf6G8hVyZ9gnsZWUP%2BF42vlU1qR6IboeOpS3ShdY5ZjnQtZkStaVg6cMBVH&X-Amz-Signature=c49c4595ec042b55b007d5586414202c40c148f9c09cdc7d60a37bbdadb1f2bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL72ZYU4%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T030956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIFx%2BH%2Ba9auzJipa3caK%2BFzsR9L1vtTJeyfzLNz6DoBSFAiEAyAVL65mu9gSWL%2Bs2ciOpALrlRhwxfDS67zXWjUxHub4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDOt1CoMV6tMWE%2FjW%2FircA8REHbJXQ2R1UmrVwFKomQJ30fwg5EjPXbFwDwZR4A3v%2FxK58NoPNAZBTNtXMK1YKPBpdYKXOeV8uvDQb8LSQUL%2FTBT2xXAg2mMmW80IYWvxEEadq1FzF1WaQV4VlxZPNVkaHC4T9FB%2BR2OovXcPaCf6uYv%2BWolmvCecpGaaGlg58sx0FFfokknxo99HKnLlp83lifdk4rcVEsbXq2DzJFs0tZLLswd1j8n%2BbRHRGRJYHKm8zBgwy4N%2F%2F5sLQ1fFmavAJMpoNjA8q1aXeTm61xqkoGjrYgKMyDfUXDAx1nexy%2Bq7u9NgVGArLUwqc8zvUIY4%2FXkx6nGB2Ttxnvu%2FB3E54bZ%2F4o6RQcxe7nV3gKHHna3vIaXvn9PjVbyVZoX7QunGNQMVV6JUMJZJr3Q4hZDF9Wr2rvMxQDulMnvl7dUbvY1Tngd%2FOGk5Trx%2BKJZHJJX5b0o4FPN3YsJMKtlXtdhWnWpmWOb5UEkaIAQuPav%2BBqSwmsiYt%2Bs2UD6vsyC4cshuWbXjEZRHiAEGgFcOt62Q%2Bz96Ssb6mPz1UxfOtRMCjrfCt2h2islwvz29mVd%2Fpr0U3JfKMrOCLFVL7jk7mOgeU%2FzmDCvzM67hoipq5J7rRc3fxX8a3OeXgj%2FFMKmO5soGOqUBSmz%2Bwc%2FpuirY%2Fm44Up9pVA%2Fp%2F28SZaOTQvSDq8raBBN3Lj96HHbfrO%2F4PIPLWa7wf9ch%2BUSqziFG7sr9nYAShPcMofijByhG4GduPe0DpbLNN7FU8wnCA5IGybZ1Is%2BiIRvn1TTmJQbf75qjSwG1ciZZihFACquM8Vf6G8hVyZ9gnsZWUP%2BF42vlU1qR6IboeOpS3ShdY5ZjnQtZkStaVg6cMBVH&X-Amz-Signature=48e67f28408c91350e596bd068b9e43cd466f46b40be3d89ee2a4241e32190fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL72ZYU4%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T030956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIFx%2BH%2Ba9auzJipa3caK%2BFzsR9L1vtTJeyfzLNz6DoBSFAiEAyAVL65mu9gSWL%2Bs2ciOpALrlRhwxfDS67zXWjUxHub4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDOt1CoMV6tMWE%2FjW%2FircA8REHbJXQ2R1UmrVwFKomQJ30fwg5EjPXbFwDwZR4A3v%2FxK58NoPNAZBTNtXMK1YKPBpdYKXOeV8uvDQb8LSQUL%2FTBT2xXAg2mMmW80IYWvxEEadq1FzF1WaQV4VlxZPNVkaHC4T9FB%2BR2OovXcPaCf6uYv%2BWolmvCecpGaaGlg58sx0FFfokknxo99HKnLlp83lifdk4rcVEsbXq2DzJFs0tZLLswd1j8n%2BbRHRGRJYHKm8zBgwy4N%2F%2F5sLQ1fFmavAJMpoNjA8q1aXeTm61xqkoGjrYgKMyDfUXDAx1nexy%2Bq7u9NgVGArLUwqc8zvUIY4%2FXkx6nGB2Ttxnvu%2FB3E54bZ%2F4o6RQcxe7nV3gKHHna3vIaXvn9PjVbyVZoX7QunGNQMVV6JUMJZJr3Q4hZDF9Wr2rvMxQDulMnvl7dUbvY1Tngd%2FOGk5Trx%2BKJZHJJX5b0o4FPN3YsJMKtlXtdhWnWpmWOb5UEkaIAQuPav%2BBqSwmsiYt%2Bs2UD6vsyC4cshuWbXjEZRHiAEGgFcOt62Q%2Bz96Ssb6mPz1UxfOtRMCjrfCt2h2islwvz29mVd%2Fpr0U3JfKMrOCLFVL7jk7mOgeU%2FzmDCvzM67hoipq5J7rRc3fxX8a3OeXgj%2FFMKmO5soGOqUBSmz%2Bwc%2FpuirY%2Fm44Up9pVA%2Fp%2F28SZaOTQvSDq8raBBN3Lj96HHbfrO%2F4PIPLWa7wf9ch%2BUSqziFG7sr9nYAShPcMofijByhG4GduPe0DpbLNN7FU8wnCA5IGybZ1Is%2BiIRvn1TTmJQbf75qjSwG1ciZZihFACquM8Vf6G8hVyZ9gnsZWUP%2BF42vlU1qR6IboeOpS3ShdY5ZjnQtZkStaVg6cMBVH&X-Amz-Signature=2d6f6917821ce8b00a561bfe80cdde86ab7bd13c68594d5ab7f4cbf864eaef75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

