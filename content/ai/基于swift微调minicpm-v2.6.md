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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGPMN2Y%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCrtnmrTePVigPtPVfCrxrQF0%2FjugOG5L6yXEAMSWTHJQIgNT47jOh8NftYPNbd%2FseWXMuowo%2FNvC8jNdeDHwF3N7YqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuALw5zKagx35MrtCrcA2e91eOkYb1rKMeC3uiyUgkf07wJbUnL8Kf2l0FWIa3ChRVsL1e8Y7wfiOUu5tWSE8D8UdcdteiWqy0%2FBcLyN7yCM%2FqnNKtlSeDrkxN%2B2va6Fh%2FZN1ICJPMcdrJqeerO0M24p%2FN3Sri4f7Dx77PemrwjldbcHPQsjKwjwJBCNB3sECBOUgGRurfxxSjJgyG3kPMwwRhzhbtbnRHzv35WqvJXHh2QrQMZq3FfEMAFycAIDdrAAAMkg2A84PHN%2FllqEQKnVeRDbypkjqJwSXk8EqPKzMqGhMiRYYnrJObZ2WjawPynKlG0RVmorG5PPdWEWpmh3ZdEQSLaJRirjX8j2WK%2FMxBCEuoMKfRrR5o1Y6nhEJO44XiDDOdZLNK48KVJN%2BD7mdT0GvXBLRj7Z0YZKCG9PEdWY9%2B3fASJJtzVnTOFRgAdbjyPEaIGI3xMN1CRU3jkw9zcizc1LaN08kshOylW%2BZsEAzm5hEQfysn06ds2j%2B9Bd3MH9bioIQ14zXNBXv0ZT9A%2FieLFhSAIFTIOhuIed0Pqf9Po6PdJ9k858pPS4teRwbRdcfS%2FT8OmoByFblKtHRO%2BYoFvEFgLDFwLE8YwUuBJpspHCjW9G2HBqzVJj4vqw2W7HfveBa8rMKesi88GOqUBGFDy1INtYHoCZZEdczcnmV2hHS7fE4R9SYmhav7RP0Lz1hw1TPWSk06XwKjIc26LaStqkU4mu3fFNEzsfSJFW5hC6Kf%2FQNdt%2FTpjFK7PL28k%2B%2FxCAlQTPU0WmYwYRGkh7gpvnHhPhTElqe2zM3fsHYOCddIquSaQma8pXYg210G6dvv%2B1yGXesqmw1vqQPFsfkkukLp2Whh%2FuoSV%2FBomNJI8uEtK&X-Amz-Signature=531cb151f496a557c75f3be595386d1213101f1a7ea7b119cac1e452ac97a431&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGPMN2Y%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCrtnmrTePVigPtPVfCrxrQF0%2FjugOG5L6yXEAMSWTHJQIgNT47jOh8NftYPNbd%2FseWXMuowo%2FNvC8jNdeDHwF3N7YqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuALw5zKagx35MrtCrcA2e91eOkYb1rKMeC3uiyUgkf07wJbUnL8Kf2l0FWIa3ChRVsL1e8Y7wfiOUu5tWSE8D8UdcdteiWqy0%2FBcLyN7yCM%2FqnNKtlSeDrkxN%2B2va6Fh%2FZN1ICJPMcdrJqeerO0M24p%2FN3Sri4f7Dx77PemrwjldbcHPQsjKwjwJBCNB3sECBOUgGRurfxxSjJgyG3kPMwwRhzhbtbnRHzv35WqvJXHh2QrQMZq3FfEMAFycAIDdrAAAMkg2A84PHN%2FllqEQKnVeRDbypkjqJwSXk8EqPKzMqGhMiRYYnrJObZ2WjawPynKlG0RVmorG5PPdWEWpmh3ZdEQSLaJRirjX8j2WK%2FMxBCEuoMKfRrR5o1Y6nhEJO44XiDDOdZLNK48KVJN%2BD7mdT0GvXBLRj7Z0YZKCG9PEdWY9%2B3fASJJtzVnTOFRgAdbjyPEaIGI3xMN1CRU3jkw9zcizc1LaN08kshOylW%2BZsEAzm5hEQfysn06ds2j%2B9Bd3MH9bioIQ14zXNBXv0ZT9A%2FieLFhSAIFTIOhuIed0Pqf9Po6PdJ9k858pPS4teRwbRdcfS%2FT8OmoByFblKtHRO%2BYoFvEFgLDFwLE8YwUuBJpspHCjW9G2HBqzVJj4vqw2W7HfveBa8rMKesi88GOqUBGFDy1INtYHoCZZEdczcnmV2hHS7fE4R9SYmhav7RP0Lz1hw1TPWSk06XwKjIc26LaStqkU4mu3fFNEzsfSJFW5hC6Kf%2FQNdt%2FTpjFK7PL28k%2B%2FxCAlQTPU0WmYwYRGkh7gpvnHhPhTElqe2zM3fsHYOCddIquSaQma8pXYg210G6dvv%2B1yGXesqmw1vqQPFsfkkukLp2Whh%2FuoSV%2FBomNJI8uEtK&X-Amz-Signature=1f6a129778716a479238668bf33905b959b74fdea5f5ee2e27ede86a48611d5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGPMN2Y%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCrtnmrTePVigPtPVfCrxrQF0%2FjugOG5L6yXEAMSWTHJQIgNT47jOh8NftYPNbd%2FseWXMuowo%2FNvC8jNdeDHwF3N7YqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuALw5zKagx35MrtCrcA2e91eOkYb1rKMeC3uiyUgkf07wJbUnL8Kf2l0FWIa3ChRVsL1e8Y7wfiOUu5tWSE8D8UdcdteiWqy0%2FBcLyN7yCM%2FqnNKtlSeDrkxN%2B2va6Fh%2FZN1ICJPMcdrJqeerO0M24p%2FN3Sri4f7Dx77PemrwjldbcHPQsjKwjwJBCNB3sECBOUgGRurfxxSjJgyG3kPMwwRhzhbtbnRHzv35WqvJXHh2QrQMZq3FfEMAFycAIDdrAAAMkg2A84PHN%2FllqEQKnVeRDbypkjqJwSXk8EqPKzMqGhMiRYYnrJObZ2WjawPynKlG0RVmorG5PPdWEWpmh3ZdEQSLaJRirjX8j2WK%2FMxBCEuoMKfRrR5o1Y6nhEJO44XiDDOdZLNK48KVJN%2BD7mdT0GvXBLRj7Z0YZKCG9PEdWY9%2B3fASJJtzVnTOFRgAdbjyPEaIGI3xMN1CRU3jkw9zcizc1LaN08kshOylW%2BZsEAzm5hEQfysn06ds2j%2B9Bd3MH9bioIQ14zXNBXv0ZT9A%2FieLFhSAIFTIOhuIed0Pqf9Po6PdJ9k858pPS4teRwbRdcfS%2FT8OmoByFblKtHRO%2BYoFvEFgLDFwLE8YwUuBJpspHCjW9G2HBqzVJj4vqw2W7HfveBa8rMKesi88GOqUBGFDy1INtYHoCZZEdczcnmV2hHS7fE4R9SYmhav7RP0Lz1hw1TPWSk06XwKjIc26LaStqkU4mu3fFNEzsfSJFW5hC6Kf%2FQNdt%2FTpjFK7PL28k%2B%2FxCAlQTPU0WmYwYRGkh7gpvnHhPhTElqe2zM3fsHYOCddIquSaQma8pXYg210G6dvv%2B1yGXesqmw1vqQPFsfkkukLp2Whh%2FuoSV%2FBomNJI8uEtK&X-Amz-Signature=2ef5f2b8b1ae4c5e9860578bc5fbbe941c52e06c3d5e24bb34ddfed3588e7a76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

