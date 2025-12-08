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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GP72AY2%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfQr7mnPg5HibCTZFFhCWJZEyJDyouS%2BgCtCBl6jrkXwIhAMbjSBb30WgJXM9zQ97KJnt8BwYJx9V4jg4j6XPsBa9DKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHGoxROxViAknpq6oq3AOO3qd%2BTEl%2BWu1BhfCFzySxGxQUjFu%2FZnXKHZ0s%2FZMhtEDGy7p5%2FqZC6Sb02Qg6EIN4Y0PL8vnsoxOlArlVnWYt5vbrygVKHon%2Fx7pLAqchZzmvcazUcrOTJf3i84gnXlzJwgZXW%2BTV8UGR7jR6dcADAhk6fBlTQQ2HfbLMkuVJhrBmSeY5rGJE0rfoMC0efXRpOOHTKaUXlBrAIKjjr2mjHpm0soqupO8k1g37nzw0nWEEdDpXyLbqOX5257PG9Nkst%2F0rhPQfQfvMYc6QWa9wJrJl5rd553faoMWCd0FhVJib5v%2B6ST03HXXyx6pxVt2yxsqSMi9BWh1hmLpLyzDHxsBhEnJjSGlqMXsXz3Zdz7Z7yF7vk5Jcj8609%2Fq8YtGbv2F5smSJIe9Q7HRHm760WaAv3rY2GmMRD7rKG3ef6RdoQSd3ReooUyVMkrMxlYGZK%2FDGDaQsnDfMyH7DIMZfJbfSDOGmuOftXgWbtt20J8USUauCCO9F%2F8Aq%2BiyfIfTAY0NR7M6qeExHy%2Bczxgpel5D%2BcVcPgKsHjw2sxXJ4sDPpLI5a64NC1g%2BLNEXNkoxQJCgZauiuQTtUxXx5MY1iR4lwQa7UfWUrLcNy%2BdfEPJRVfNmqOP1ytlrDnjCe79jJBjqkAY22W6NqFJKBRrpDI08Od7olz4exOIQrY0UMQ4qDphKcbPpZzwrijlbqN4Dhls%2F5B33h2qJyNVrWn86hU%2FzY10wnByE%2FNb7hfX7Ly5LZBFs7k2Br2xWal%2BPJ1cWrTShogBRHKtjR1CkZOh0KD3rH9vqCLnRrL28uZxbvQeqVcVPx7ENCTUGOFuX0KRPlzTsOoUI%2F0DRw8mvqQM3NCIl5nyqmSzlA&X-Amz-Signature=2395755db55f8437bce738a1b48da1337a01d38700a6dadbe95423f66f2f4d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GP72AY2%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfQr7mnPg5HibCTZFFhCWJZEyJDyouS%2BgCtCBl6jrkXwIhAMbjSBb30WgJXM9zQ97KJnt8BwYJx9V4jg4j6XPsBa9DKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHGoxROxViAknpq6oq3AOO3qd%2BTEl%2BWu1BhfCFzySxGxQUjFu%2FZnXKHZ0s%2FZMhtEDGy7p5%2FqZC6Sb02Qg6EIN4Y0PL8vnsoxOlArlVnWYt5vbrygVKHon%2Fx7pLAqchZzmvcazUcrOTJf3i84gnXlzJwgZXW%2BTV8UGR7jR6dcADAhk6fBlTQQ2HfbLMkuVJhrBmSeY5rGJE0rfoMC0efXRpOOHTKaUXlBrAIKjjr2mjHpm0soqupO8k1g37nzw0nWEEdDpXyLbqOX5257PG9Nkst%2F0rhPQfQfvMYc6QWa9wJrJl5rd553faoMWCd0FhVJib5v%2B6ST03HXXyx6pxVt2yxsqSMi9BWh1hmLpLyzDHxsBhEnJjSGlqMXsXz3Zdz7Z7yF7vk5Jcj8609%2Fq8YtGbv2F5smSJIe9Q7HRHm760WaAv3rY2GmMRD7rKG3ef6RdoQSd3ReooUyVMkrMxlYGZK%2FDGDaQsnDfMyH7DIMZfJbfSDOGmuOftXgWbtt20J8USUauCCO9F%2F8Aq%2BiyfIfTAY0NR7M6qeExHy%2Bczxgpel5D%2BcVcPgKsHjw2sxXJ4sDPpLI5a64NC1g%2BLNEXNkoxQJCgZauiuQTtUxXx5MY1iR4lwQa7UfWUrLcNy%2BdfEPJRVfNmqOP1ytlrDnjCe79jJBjqkAY22W6NqFJKBRrpDI08Od7olz4exOIQrY0UMQ4qDphKcbPpZzwrijlbqN4Dhls%2F5B33h2qJyNVrWn86hU%2FzY10wnByE%2FNb7hfX7Ly5LZBFs7k2Br2xWal%2BPJ1cWrTShogBRHKtjR1CkZOh0KD3rH9vqCLnRrL28uZxbvQeqVcVPx7ENCTUGOFuX0KRPlzTsOoUI%2F0DRw8mvqQM3NCIl5nyqmSzlA&X-Amz-Signature=bc0e2f21941de25d4f09138097a623d507318c95dd0663b04ba8d370828277f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GP72AY2%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfQr7mnPg5HibCTZFFhCWJZEyJDyouS%2BgCtCBl6jrkXwIhAMbjSBb30WgJXM9zQ97KJnt8BwYJx9V4jg4j6XPsBa9DKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHGoxROxViAknpq6oq3AOO3qd%2BTEl%2BWu1BhfCFzySxGxQUjFu%2FZnXKHZ0s%2FZMhtEDGy7p5%2FqZC6Sb02Qg6EIN4Y0PL8vnsoxOlArlVnWYt5vbrygVKHon%2Fx7pLAqchZzmvcazUcrOTJf3i84gnXlzJwgZXW%2BTV8UGR7jR6dcADAhk6fBlTQQ2HfbLMkuVJhrBmSeY5rGJE0rfoMC0efXRpOOHTKaUXlBrAIKjjr2mjHpm0soqupO8k1g37nzw0nWEEdDpXyLbqOX5257PG9Nkst%2F0rhPQfQfvMYc6QWa9wJrJl5rd553faoMWCd0FhVJib5v%2B6ST03HXXyx6pxVt2yxsqSMi9BWh1hmLpLyzDHxsBhEnJjSGlqMXsXz3Zdz7Z7yF7vk5Jcj8609%2Fq8YtGbv2F5smSJIe9Q7HRHm760WaAv3rY2GmMRD7rKG3ef6RdoQSd3ReooUyVMkrMxlYGZK%2FDGDaQsnDfMyH7DIMZfJbfSDOGmuOftXgWbtt20J8USUauCCO9F%2F8Aq%2BiyfIfTAY0NR7M6qeExHy%2Bczxgpel5D%2BcVcPgKsHjw2sxXJ4sDPpLI5a64NC1g%2BLNEXNkoxQJCgZauiuQTtUxXx5MY1iR4lwQa7UfWUrLcNy%2BdfEPJRVfNmqOP1ytlrDnjCe79jJBjqkAY22W6NqFJKBRrpDI08Od7olz4exOIQrY0UMQ4qDphKcbPpZzwrijlbqN4Dhls%2F5B33h2qJyNVrWn86hU%2FzY10wnByE%2FNb7hfX7Ly5LZBFs7k2Br2xWal%2BPJ1cWrTShogBRHKtjR1CkZOh0KD3rH9vqCLnRrL28uZxbvQeqVcVPx7ENCTUGOFuX0KRPlzTsOoUI%2F0DRw8mvqQM3NCIl5nyqmSzlA&X-Amz-Signature=ed8d9dfb2009a1b21e3b424f991f2a37ad2683ee28a1b6c7386fec6ed9a6341c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

