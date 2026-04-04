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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD5YPQRI%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJmwFT0S7yGjr8nFLZorQ1OYBK8J2oIIouR7HVcFlKmAiAU5GYBTwrlCfRBVTrxnhuQdhZboM1Mga4ocjIjRPEwiiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuYZvXBINag0HCTczKtwDptvt4dEeB%2BvLoPr5KM%2BhcCH%2FUrjeMWk%2B4TS9H091NBSn9W6vAt35BbGewcdS6Fmkj0O4ecyb23DEh%2FbVlcsaGlVw26zU2n6Bw5cBRyhlDrfPjRM22MvwpTPKu6cXIzrnwY1zLplWhIU17HpZNNLEQukn8DOQnvMbX%2BR6eB5uJbeYzuelqnfR3bpaTHRZdwGI4cXxnUZXChZgU0SRfjBal01lTP%2BzaHNbixx%2BQC3bhhyI5e6mNQXmZzOljtFk3FW3GM47S%2F7yRfewSyDp1qQvFzPReOvyxOKK16Z0hNhySnetTDNW4EpO3%2FXotOxa%2By2xJj4ImvVHBRS8rPM27XOUuHFifJ34KyOR9WN5lSSNH5gwHiwIqdU3EAg8R%2Bt2vs%2F4isjzhH7XzWeN7N9zzh05CRiHV254sL7ePTXcF%2FpA%2BNKFeZ%2FWQQdyIor0w0v5XkLyPhO9CZSs40nyP43g3x5X%2FuzNWc10%2Fa7O7i5fngrnkiQ7wyel3W4tTVC12ggk%2BsfpEp%2BPTJRiJweG6uXxlNBOV0H%2BIs3mJ5fLTTZhvaEcnorWdskRVvwHOe%2FiPblx4h9Pb%2BftGxvi3wy2Y%2BkjOmTMEBERN68227dJysGcoGq40ZOVlNvATs4DPCwVYMgwt%2BTBzgY6pgEANwa4ewadKG3N9tsc92hTA85VjC3Cav%2BX6U%2BUqWuGeYfe3pQDZrbHnnNe9%2BB4lxQoY2obASZL%2FZwESAkA57ptqnuxTg%2F3SawJV6tyWJelPEd8hIjsCn5WrqYoFOPfTAzKWaQ48kgqdW%2BMShwEL6k8NzSzFbdKJI%2Fcqnnm0Vx7DFBfSOSztSe0Y3e6anTnYCgKnMr0uO9FgUWKqhk9ewHtqCXvEaUx&X-Amz-Signature=eff7dbe5fb8689151e072b09d7ee27b8a6f8e57cdbff20e7e9d3cc2c1820814a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD5YPQRI%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJmwFT0S7yGjr8nFLZorQ1OYBK8J2oIIouR7HVcFlKmAiAU5GYBTwrlCfRBVTrxnhuQdhZboM1Mga4ocjIjRPEwiiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuYZvXBINag0HCTczKtwDptvt4dEeB%2BvLoPr5KM%2BhcCH%2FUrjeMWk%2B4TS9H091NBSn9W6vAt35BbGewcdS6Fmkj0O4ecyb23DEh%2FbVlcsaGlVw26zU2n6Bw5cBRyhlDrfPjRM22MvwpTPKu6cXIzrnwY1zLplWhIU17HpZNNLEQukn8DOQnvMbX%2BR6eB5uJbeYzuelqnfR3bpaTHRZdwGI4cXxnUZXChZgU0SRfjBal01lTP%2BzaHNbixx%2BQC3bhhyI5e6mNQXmZzOljtFk3FW3GM47S%2F7yRfewSyDp1qQvFzPReOvyxOKK16Z0hNhySnetTDNW4EpO3%2FXotOxa%2By2xJj4ImvVHBRS8rPM27XOUuHFifJ34KyOR9WN5lSSNH5gwHiwIqdU3EAg8R%2Bt2vs%2F4isjzhH7XzWeN7N9zzh05CRiHV254sL7ePTXcF%2FpA%2BNKFeZ%2FWQQdyIor0w0v5XkLyPhO9CZSs40nyP43g3x5X%2FuzNWc10%2Fa7O7i5fngrnkiQ7wyel3W4tTVC12ggk%2BsfpEp%2BPTJRiJweG6uXxlNBOV0H%2BIs3mJ5fLTTZhvaEcnorWdskRVvwHOe%2FiPblx4h9Pb%2BftGxvi3wy2Y%2BkjOmTMEBERN68227dJysGcoGq40ZOVlNvATs4DPCwVYMgwt%2BTBzgY6pgEANwa4ewadKG3N9tsc92hTA85VjC3Cav%2BX6U%2BUqWuGeYfe3pQDZrbHnnNe9%2BB4lxQoY2obASZL%2FZwESAkA57ptqnuxTg%2F3SawJV6tyWJelPEd8hIjsCn5WrqYoFOPfTAzKWaQ48kgqdW%2BMShwEL6k8NzSzFbdKJI%2Fcqnnm0Vx7DFBfSOSztSe0Y3e6anTnYCgKnMr0uO9FgUWKqhk9ewHtqCXvEaUx&X-Amz-Signature=43a78a92f6644e71afda745a435a97c142ce96ec9c95ef1445c9f2b701d3b30a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD5YPQRI%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJmwFT0S7yGjr8nFLZorQ1OYBK8J2oIIouR7HVcFlKmAiAU5GYBTwrlCfRBVTrxnhuQdhZboM1Mga4ocjIjRPEwiiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuYZvXBINag0HCTczKtwDptvt4dEeB%2BvLoPr5KM%2BhcCH%2FUrjeMWk%2B4TS9H091NBSn9W6vAt35BbGewcdS6Fmkj0O4ecyb23DEh%2FbVlcsaGlVw26zU2n6Bw5cBRyhlDrfPjRM22MvwpTPKu6cXIzrnwY1zLplWhIU17HpZNNLEQukn8DOQnvMbX%2BR6eB5uJbeYzuelqnfR3bpaTHRZdwGI4cXxnUZXChZgU0SRfjBal01lTP%2BzaHNbixx%2BQC3bhhyI5e6mNQXmZzOljtFk3FW3GM47S%2F7yRfewSyDp1qQvFzPReOvyxOKK16Z0hNhySnetTDNW4EpO3%2FXotOxa%2By2xJj4ImvVHBRS8rPM27XOUuHFifJ34KyOR9WN5lSSNH5gwHiwIqdU3EAg8R%2Bt2vs%2F4isjzhH7XzWeN7N9zzh05CRiHV254sL7ePTXcF%2FpA%2BNKFeZ%2FWQQdyIor0w0v5XkLyPhO9CZSs40nyP43g3x5X%2FuzNWc10%2Fa7O7i5fngrnkiQ7wyel3W4tTVC12ggk%2BsfpEp%2BPTJRiJweG6uXxlNBOV0H%2BIs3mJ5fLTTZhvaEcnorWdskRVvwHOe%2FiPblx4h9Pb%2BftGxvi3wy2Y%2BkjOmTMEBERN68227dJysGcoGq40ZOVlNvATs4DPCwVYMgwt%2BTBzgY6pgEANwa4ewadKG3N9tsc92hTA85VjC3Cav%2BX6U%2BUqWuGeYfe3pQDZrbHnnNe9%2BB4lxQoY2obASZL%2FZwESAkA57ptqnuxTg%2F3SawJV6tyWJelPEd8hIjsCn5WrqYoFOPfTAzKWaQ48kgqdW%2BMShwEL6k8NzSzFbdKJI%2Fcqnnm0Vx7DFBfSOSztSe0Y3e6anTnYCgKnMr0uO9FgUWKqhk9ewHtqCXvEaUx&X-Amz-Signature=e47101c1157701ec05b0353267246238817fc41de79b3c3a7a50640e611567c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

