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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBU6PPI%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3N9Djh6kotylA8vLxUJv0HR7xzxJ0j7lxVMm9EsmxBwIhAMg2UMQgwCg7WPsoX4Lnf6HkwpOz%2BhoEOBCOtyHU2Yi0Kv8DCHQQABoMNjM3NDIzMTgzODA1Igwfm%2F6K9MWnFy%2BtgSYq3AMavvu3%2B7LHvpPOso0RY0k28rPODpyIniG10xteL%2FRrPRLQN2sULOQbKOw34bEgPfLebuy5WdX13kezP8fwwaMA482IbfoNtCdRtrXXFKgnoIrQvTyY46EAyBqV%2BW0owXOuJg6pV25Z2qpy6MiN%2FO9NIedKw7%2Fhk1cFqS73wkAG%2F%2FSz50IN4gRpnpzOVYHyFh91qV7fae0fcWzupgcGgRrZp0bW7Rwq5CQWNGEka0FsRitV2avTQMXS0wHwzhN5u5rH2JZq0EoRHINtyR9%2FA8LDeeTLHuo6lQZvD2MQg03JJRMlaupibFoE7fRe1bxw%2BxQ6Nyc5mLlyRiRzQih7B0zJy6lA7O7%2B8Nfr70pJXaReLdYGjtf09Xw8KLPjtzp83VK5IJxxaZNta3liS2mO%2B4WQ0wtpsZAvOtOVFcG5auBf3uyCEx%2FR5B3aDdxuCl4dsL88i49Cq9Sing%2BQF7VklNATUdOpNXFGcRxViH4TMgBa%2F%2FY3IY0FSKxz6P7gYFjPXoYST734akup3eXxpsHxMPDSxQzBNHf7I2BNC65%2BcDk2Gur71UHMKw5B9VWuW4w82bhQ%2B3JEjuNAZbG6ivoUHajPBjLCoz%2B4zlgj%2BKV3ojdvXTntN%2BDhADsaIV7AzzDwrqvPBjqkAcP%2FIXaF4BQdWcpdVJ4FzEqgktKzvjO6WMX%2F%2Fkro59uQ0FeOKn2W0u4TNf7QkxsGWP%2BPnOgvbqr3X3wWgjfobCsj5yrOLXYhOAt2Akrfh3Tw8cmgth8wlAhwCYjsO8ktRFcVEWWeTL90Kj2tDC9RUEgpIkclDddRFCrWi4nKdO71%2BlzFxcF8iZjXJjJV99qiiAHGFbL0DIIi9NFkfjHn4jq%2Fq%2Bkx&X-Amz-Signature=6455b39e70e8bedc9aaa84734b3676fc36f7250a7ec631add36b5f2560d1c987&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBU6PPI%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3N9Djh6kotylA8vLxUJv0HR7xzxJ0j7lxVMm9EsmxBwIhAMg2UMQgwCg7WPsoX4Lnf6HkwpOz%2BhoEOBCOtyHU2Yi0Kv8DCHQQABoMNjM3NDIzMTgzODA1Igwfm%2F6K9MWnFy%2BtgSYq3AMavvu3%2B7LHvpPOso0RY0k28rPODpyIniG10xteL%2FRrPRLQN2sULOQbKOw34bEgPfLebuy5WdX13kezP8fwwaMA482IbfoNtCdRtrXXFKgnoIrQvTyY46EAyBqV%2BW0owXOuJg6pV25Z2qpy6MiN%2FO9NIedKw7%2Fhk1cFqS73wkAG%2F%2FSz50IN4gRpnpzOVYHyFh91qV7fae0fcWzupgcGgRrZp0bW7Rwq5CQWNGEka0FsRitV2avTQMXS0wHwzhN5u5rH2JZq0EoRHINtyR9%2FA8LDeeTLHuo6lQZvD2MQg03JJRMlaupibFoE7fRe1bxw%2BxQ6Nyc5mLlyRiRzQih7B0zJy6lA7O7%2B8Nfr70pJXaReLdYGjtf09Xw8KLPjtzp83VK5IJxxaZNta3liS2mO%2B4WQ0wtpsZAvOtOVFcG5auBf3uyCEx%2FR5B3aDdxuCl4dsL88i49Cq9Sing%2BQF7VklNATUdOpNXFGcRxViH4TMgBa%2F%2FY3IY0FSKxz6P7gYFjPXoYST734akup3eXxpsHxMPDSxQzBNHf7I2BNC65%2BcDk2Gur71UHMKw5B9VWuW4w82bhQ%2B3JEjuNAZbG6ivoUHajPBjLCoz%2B4zlgj%2BKV3ojdvXTntN%2BDhADsaIV7AzzDwrqvPBjqkAcP%2FIXaF4BQdWcpdVJ4FzEqgktKzvjO6WMX%2F%2Fkro59uQ0FeOKn2W0u4TNf7QkxsGWP%2BPnOgvbqr3X3wWgjfobCsj5yrOLXYhOAt2Akrfh3Tw8cmgth8wlAhwCYjsO8ktRFcVEWWeTL90Kj2tDC9RUEgpIkclDddRFCrWi4nKdO71%2BlzFxcF8iZjXJjJV99qiiAHGFbL0DIIi9NFkfjHn4jq%2Fq%2Bkx&X-Amz-Signature=2e4e54d9ad40d438f32087822584909f3081e493537a183692c1f5a684962e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLBU6PPI%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3N9Djh6kotylA8vLxUJv0HR7xzxJ0j7lxVMm9EsmxBwIhAMg2UMQgwCg7WPsoX4Lnf6HkwpOz%2BhoEOBCOtyHU2Yi0Kv8DCHQQABoMNjM3NDIzMTgzODA1Igwfm%2F6K9MWnFy%2BtgSYq3AMavvu3%2B7LHvpPOso0RY0k28rPODpyIniG10xteL%2FRrPRLQN2sULOQbKOw34bEgPfLebuy5WdX13kezP8fwwaMA482IbfoNtCdRtrXXFKgnoIrQvTyY46EAyBqV%2BW0owXOuJg6pV25Z2qpy6MiN%2FO9NIedKw7%2Fhk1cFqS73wkAG%2F%2FSz50IN4gRpnpzOVYHyFh91qV7fae0fcWzupgcGgRrZp0bW7Rwq5CQWNGEka0FsRitV2avTQMXS0wHwzhN5u5rH2JZq0EoRHINtyR9%2FA8LDeeTLHuo6lQZvD2MQg03JJRMlaupibFoE7fRe1bxw%2BxQ6Nyc5mLlyRiRzQih7B0zJy6lA7O7%2B8Nfr70pJXaReLdYGjtf09Xw8KLPjtzp83VK5IJxxaZNta3liS2mO%2B4WQ0wtpsZAvOtOVFcG5auBf3uyCEx%2FR5B3aDdxuCl4dsL88i49Cq9Sing%2BQF7VklNATUdOpNXFGcRxViH4TMgBa%2F%2FY3IY0FSKxz6P7gYFjPXoYST734akup3eXxpsHxMPDSxQzBNHf7I2BNC65%2BcDk2Gur71UHMKw5B9VWuW4w82bhQ%2B3JEjuNAZbG6ivoUHajPBjLCoz%2B4zlgj%2BKV3ojdvXTntN%2BDhADsaIV7AzzDwrqvPBjqkAcP%2FIXaF4BQdWcpdVJ4FzEqgktKzvjO6WMX%2F%2Fkro59uQ0FeOKn2W0u4TNf7QkxsGWP%2BPnOgvbqr3X3wWgjfobCsj5yrOLXYhOAt2Akrfh3Tw8cmgth8wlAhwCYjsO8ktRFcVEWWeTL90Kj2tDC9RUEgpIkclDddRFCrWi4nKdO71%2BlzFxcF8iZjXJjJV99qiiAHGFbL0DIIi9NFkfjHn4jq%2Fq%2Bkx&X-Amz-Signature=cf3e734be9c44a08090058c160cdd8aa42b88f9b41d6eaaf7eb1ff4345757137&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

