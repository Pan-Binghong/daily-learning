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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBKS4YG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD0ZYx86ryTXgQnlsGknVqj6qpjJon3LMEKAWSqa%2BOwfgIgTD%2B6ArYwzHMPTLa357wiGxFlfXGpgaT%2BoKLvc%2BW4KkQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPLTOFmz9g8L%2Bek9eCrcA3wZNrHNAt4vv7zG3dySGrOyNGGZ7wr2rmQDlKSykv15yWKrZAlaTwDJvJq2CXJx8crF%2FZJUMqtLjaMeZWAdQj%2BXlbRtV5fiNkhD4sYRRuqXZ2UF73mIJ2UY%2FY6oeuAGJDd6GMcjr6LS0VRA8eL62dKb0YUU7XGOzs2bpUAONOPXqVTfFRmUdQM57Q%2BJeFKfT47VMCG9kk3n1majd2gurcQus7Atq8ZeiqHNnsjDkb5CJ9YXU%2F%2FVBuscyz8ex3j1zCfLf9cd3iew%2BBoEmfFeeSjtZA601zXm53K1C1%2FwaPXvx%2BjWIew7g1HA48Q6Ac8aJAXyo3jz3WpS5CV4sndVmD6g01LMnt%2B2Bmd%2Bz64zbYiOeJPuL5txC8A%2FyvIbgxhjWe2S9QU3OTPSRwNLC%2FbJylBPpJrm5oil9RvRGRU7GrKwAkR%2BvZvK%2F0O763xomVQKjsebQw8TI%2B0bbcmxpnF6S2gAKeOd7dykNIF8vsHFUmsLoxLVJa%2Bt7yb4dnrG6pDYiTnYQlNLNJH%2FT1UnYV%2FCuwaU38zLpy%2FaO2zWNT426Wf65q4HLhb2QmiNC8xQDk0tt3PcbmcxchHakmzYHXq3O6KRePh6QZbH5cLVyY8tvv5iHNKv%2FdmZN4WZgt6EMNvurM4GOqUBBuNAEYF94xkhQVVOjLCROZnVzD0HJerVu13fCuAZrtTs3rBgoHZlxL2RTpBYHXZBO%2B6iNVuiNh6Kd7TARcTGb8syLkvUkcF3U5AX9YyHYzak6czP12QWEFlqHA0vhVMDyDyFUaEdLlZQY34Skx7FV53P%2Ft8z1D8bp0u3GGyIRw8Z%2BpFFXz4KdkH3EwYxyb88Eoc1IYeKyiAIn5tXQ7mv3In94o21&X-Amz-Signature=9064d6def99ee63e9b3ad3373ba7b7a05c06e7036bb99faeabfd30b20e39d716&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBKS4YG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD0ZYx86ryTXgQnlsGknVqj6qpjJon3LMEKAWSqa%2BOwfgIgTD%2B6ArYwzHMPTLa357wiGxFlfXGpgaT%2BoKLvc%2BW4KkQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPLTOFmz9g8L%2Bek9eCrcA3wZNrHNAt4vv7zG3dySGrOyNGGZ7wr2rmQDlKSykv15yWKrZAlaTwDJvJq2CXJx8crF%2FZJUMqtLjaMeZWAdQj%2BXlbRtV5fiNkhD4sYRRuqXZ2UF73mIJ2UY%2FY6oeuAGJDd6GMcjr6LS0VRA8eL62dKb0YUU7XGOzs2bpUAONOPXqVTfFRmUdQM57Q%2BJeFKfT47VMCG9kk3n1majd2gurcQus7Atq8ZeiqHNnsjDkb5CJ9YXU%2F%2FVBuscyz8ex3j1zCfLf9cd3iew%2BBoEmfFeeSjtZA601zXm53K1C1%2FwaPXvx%2BjWIew7g1HA48Q6Ac8aJAXyo3jz3WpS5CV4sndVmD6g01LMnt%2B2Bmd%2Bz64zbYiOeJPuL5txC8A%2FyvIbgxhjWe2S9QU3OTPSRwNLC%2FbJylBPpJrm5oil9RvRGRU7GrKwAkR%2BvZvK%2F0O763xomVQKjsebQw8TI%2B0bbcmxpnF6S2gAKeOd7dykNIF8vsHFUmsLoxLVJa%2Bt7yb4dnrG6pDYiTnYQlNLNJH%2FT1UnYV%2FCuwaU38zLpy%2FaO2zWNT426Wf65q4HLhb2QmiNC8xQDk0tt3PcbmcxchHakmzYHXq3O6KRePh6QZbH5cLVyY8tvv5iHNKv%2FdmZN4WZgt6EMNvurM4GOqUBBuNAEYF94xkhQVVOjLCROZnVzD0HJerVu13fCuAZrtTs3rBgoHZlxL2RTpBYHXZBO%2B6iNVuiNh6Kd7TARcTGb8syLkvUkcF3U5AX9YyHYzak6czP12QWEFlqHA0vhVMDyDyFUaEdLlZQY34Skx7FV53P%2Ft8z1D8bp0u3GGyIRw8Z%2BpFFXz4KdkH3EwYxyb88Eoc1IYeKyiAIn5tXQ7mv3In94o21&X-Amz-Signature=4f26f4905836ff2c1144acce4d0d9601e096e54bf41331565c26275b2dcebeec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBKS4YG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD0ZYx86ryTXgQnlsGknVqj6qpjJon3LMEKAWSqa%2BOwfgIgTD%2B6ArYwzHMPTLa357wiGxFlfXGpgaT%2BoKLvc%2BW4KkQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPLTOFmz9g8L%2Bek9eCrcA3wZNrHNAt4vv7zG3dySGrOyNGGZ7wr2rmQDlKSykv15yWKrZAlaTwDJvJq2CXJx8crF%2FZJUMqtLjaMeZWAdQj%2BXlbRtV5fiNkhD4sYRRuqXZ2UF73mIJ2UY%2FY6oeuAGJDd6GMcjr6LS0VRA8eL62dKb0YUU7XGOzs2bpUAONOPXqVTfFRmUdQM57Q%2BJeFKfT47VMCG9kk3n1majd2gurcQus7Atq8ZeiqHNnsjDkb5CJ9YXU%2F%2FVBuscyz8ex3j1zCfLf9cd3iew%2BBoEmfFeeSjtZA601zXm53K1C1%2FwaPXvx%2BjWIew7g1HA48Q6Ac8aJAXyo3jz3WpS5CV4sndVmD6g01LMnt%2B2Bmd%2Bz64zbYiOeJPuL5txC8A%2FyvIbgxhjWe2S9QU3OTPSRwNLC%2FbJylBPpJrm5oil9RvRGRU7GrKwAkR%2BvZvK%2F0O763xomVQKjsebQw8TI%2B0bbcmxpnF6S2gAKeOd7dykNIF8vsHFUmsLoxLVJa%2Bt7yb4dnrG6pDYiTnYQlNLNJH%2FT1UnYV%2FCuwaU38zLpy%2FaO2zWNT426Wf65q4HLhb2QmiNC8xQDk0tt3PcbmcxchHakmzYHXq3O6KRePh6QZbH5cLVyY8tvv5iHNKv%2FdmZN4WZgt6EMNvurM4GOqUBBuNAEYF94xkhQVVOjLCROZnVzD0HJerVu13fCuAZrtTs3rBgoHZlxL2RTpBYHXZBO%2B6iNVuiNh6Kd7TARcTGb8syLkvUkcF3U5AX9YyHYzak6czP12QWEFlqHA0vhVMDyDyFUaEdLlZQY34Skx7FV53P%2Ft8z1D8bp0u3GGyIRw8Z%2BpFFXz4KdkH3EwYxyb88Eoc1IYeKyiAIn5tXQ7mv3In94o21&X-Amz-Signature=03eaf1cd8e8ee8f21bd6c4b827892c1ea89b6f405608e2a6f62f13e98848c503&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

