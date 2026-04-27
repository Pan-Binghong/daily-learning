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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I4VSPS7%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3SWC6KBr0VCMHG1jHakOoQLp3mKoPnZ2%2BxgOk4iRKRQIhAM8JX01gK8cuuIW3Ko%2FPRzGuxmIRppgS9B%2FiiKvWGrw2KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bu7x7nM0TuS0WT7Aq3APofUrGexRyy%2BY30zIlYqflxWVpRI3GNP7ePowGBhFN0RJNTxPR%2FjH1gjhLHJahjQqZfyITph9koKQb83H3qmjBA0Wlb6qevTKrZs33HSRRKIK3A1M19ITeNq02QHIUsdoSt727%2F%2F64eF1ZgVTU%2BU5LAe21VZoSjoHVg1RBMFB7KKPlEiqScTi%2F4tuGMy5eJk0%2F%2B8s4cFm30u9QtwlCLUZODtOTA%2FGAlJaRrxaZsBBv5PCKwVycr5I3ZOau4OhTSxakBjrWvm7yGlZrs57gXHvTXZZF29u97ssEtdJzUlxqTSicWoNz7SG2a8ISvjBxz5NRmtQXELaOq%2BDIOzpCYV96m6HCyAZDMC%2FZ7QXhbmlTepk43Ew1fPdFnigyq7JOUD3Rf9%2B%2BPodh%2BNEq70VjqYgZFpKmBs13fUPzSoBVGCWfEv1MqqSjl64BbMvJc5esCQM3ySs5ppIc4tiQTQQpgQ1Lz9pOWWoyBZrOv%2F0Jk%2BrA6kJWGGzmWZHqOltvOXPxfY42San3FFld1jcAPupet%2F5GptKT9m6mVh%2BjfFAZy0zpAW0QRtoXr9EkHm4%2B3If70L2nCh0ZMHj0RvpUZiQ8n0xO7D%2FG4YVSP%2BIe2O%2BgLzw1KzbZkttnj0NG9ijDyTCptbvPBjqkAQ%2FvOEbRXPY2P45n7WFFTVYzfXpq8t7f64HpbPnC92kFRvVxzOVN2JCXpsKepsQWordFoEkYycELceAD8EtAWxdD%2Fk6cD2ErQ3wJBbx1yJtO28NoO4B9XltuciTel8%2Ff6ykr7PuQPfvY3qY543sYTW9j8GCtr2QCsHHyrOBN3UDgERd99nctoAOTREh3JDZozISaUK%2Fju9G618Q4jhSaPMamB605&X-Amz-Signature=eee961e1cd4a1076500509bc554a8aa24af1f200e274d88f9845c4ccce810767&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I4VSPS7%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3SWC6KBr0VCMHG1jHakOoQLp3mKoPnZ2%2BxgOk4iRKRQIhAM8JX01gK8cuuIW3Ko%2FPRzGuxmIRppgS9B%2FiiKvWGrw2KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bu7x7nM0TuS0WT7Aq3APofUrGexRyy%2BY30zIlYqflxWVpRI3GNP7ePowGBhFN0RJNTxPR%2FjH1gjhLHJahjQqZfyITph9koKQb83H3qmjBA0Wlb6qevTKrZs33HSRRKIK3A1M19ITeNq02QHIUsdoSt727%2F%2F64eF1ZgVTU%2BU5LAe21VZoSjoHVg1RBMFB7KKPlEiqScTi%2F4tuGMy5eJk0%2F%2B8s4cFm30u9QtwlCLUZODtOTA%2FGAlJaRrxaZsBBv5PCKwVycr5I3ZOau4OhTSxakBjrWvm7yGlZrs57gXHvTXZZF29u97ssEtdJzUlxqTSicWoNz7SG2a8ISvjBxz5NRmtQXELaOq%2BDIOzpCYV96m6HCyAZDMC%2FZ7QXhbmlTepk43Ew1fPdFnigyq7JOUD3Rf9%2B%2BPodh%2BNEq70VjqYgZFpKmBs13fUPzSoBVGCWfEv1MqqSjl64BbMvJc5esCQM3ySs5ppIc4tiQTQQpgQ1Lz9pOWWoyBZrOv%2F0Jk%2BrA6kJWGGzmWZHqOltvOXPxfY42San3FFld1jcAPupet%2F5GptKT9m6mVh%2BjfFAZy0zpAW0QRtoXr9EkHm4%2B3If70L2nCh0ZMHj0RvpUZiQ8n0xO7D%2FG4YVSP%2BIe2O%2BgLzw1KzbZkttnj0NG9ijDyTCptbvPBjqkAQ%2FvOEbRXPY2P45n7WFFTVYzfXpq8t7f64HpbPnC92kFRvVxzOVN2JCXpsKepsQWordFoEkYycELceAD8EtAWxdD%2Fk6cD2ErQ3wJBbx1yJtO28NoO4B9XltuciTel8%2Ff6ykr7PuQPfvY3qY543sYTW9j8GCtr2QCsHHyrOBN3UDgERd99nctoAOTREh3JDZozISaUK%2Fju9G618Q4jhSaPMamB605&X-Amz-Signature=3b9ce11d7aac47422a7687bef60378e34499e6c40297c62dd28efaf19829c868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I4VSPS7%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3SWC6KBr0VCMHG1jHakOoQLp3mKoPnZ2%2BxgOk4iRKRQIhAM8JX01gK8cuuIW3Ko%2FPRzGuxmIRppgS9B%2FiiKvWGrw2KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bu7x7nM0TuS0WT7Aq3APofUrGexRyy%2BY30zIlYqflxWVpRI3GNP7ePowGBhFN0RJNTxPR%2FjH1gjhLHJahjQqZfyITph9koKQb83H3qmjBA0Wlb6qevTKrZs33HSRRKIK3A1M19ITeNq02QHIUsdoSt727%2F%2F64eF1ZgVTU%2BU5LAe21VZoSjoHVg1RBMFB7KKPlEiqScTi%2F4tuGMy5eJk0%2F%2B8s4cFm30u9QtwlCLUZODtOTA%2FGAlJaRrxaZsBBv5PCKwVycr5I3ZOau4OhTSxakBjrWvm7yGlZrs57gXHvTXZZF29u97ssEtdJzUlxqTSicWoNz7SG2a8ISvjBxz5NRmtQXELaOq%2BDIOzpCYV96m6HCyAZDMC%2FZ7QXhbmlTepk43Ew1fPdFnigyq7JOUD3Rf9%2B%2BPodh%2BNEq70VjqYgZFpKmBs13fUPzSoBVGCWfEv1MqqSjl64BbMvJc5esCQM3ySs5ppIc4tiQTQQpgQ1Lz9pOWWoyBZrOv%2F0Jk%2BrA6kJWGGzmWZHqOltvOXPxfY42San3FFld1jcAPupet%2F5GptKT9m6mVh%2BjfFAZy0zpAW0QRtoXr9EkHm4%2B3If70L2nCh0ZMHj0RvpUZiQ8n0xO7D%2FG4YVSP%2BIe2O%2BgLzw1KzbZkttnj0NG9ijDyTCptbvPBjqkAQ%2FvOEbRXPY2P45n7WFFTVYzfXpq8t7f64HpbPnC92kFRvVxzOVN2JCXpsKepsQWordFoEkYycELceAD8EtAWxdD%2Fk6cD2ErQ3wJBbx1yJtO28NoO4B9XltuciTel8%2Ff6ykr7PuQPfvY3qY543sYTW9j8GCtr2QCsHHyrOBN3UDgERd99nctoAOTREh3JDZozISaUK%2Fju9G618Q4jhSaPMamB605&X-Amz-Signature=68ee9cb9e77d6b9208a1e9ca42c7000d1e95cf5dee5dcbf442c115255cef7564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

