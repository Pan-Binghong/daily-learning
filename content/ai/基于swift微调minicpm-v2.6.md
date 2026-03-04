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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RBD62MW%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmL6Fz5sCdVbXHuRCR2nYX6pnxKGP63gT6IgPlROHjrAIgRoxvbgNjvHsJSsTwZuwEvg2nKpwbjkWrTG1dJ4AX9sQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbP%2BqteYrDtXosJfCrcA9jv5Od%2ByJye21MOuWDEu0lvZIUbzqCNot24ZLJVRCgNtRYKX7n14KM9h2a8YRcan%2FDLdXrXFurVibGTpnI57sQmAS9w5CXzIQnmnbUbXQXF0ytiTkPyM2d%2BPiAUoGZskmJbtUxzNCYA7K1nh8EOph9ndq3tvenEvP6jo9Km31mOep%2Fg73218INitaP%2FcRgl3Lkeydt7im5FjUkiNUgwB4oXjq1ErUafIqF5H6a6OgFc%2BbNP4avS5X8oBW7hSKjtw%2FHY3kkLiXv1KTZ0oLody1NivlE3dUHgFigveGexnHo0MxZ2GcDBQMKIwBldAEy%2FyiR%2Bz9UIandFuxTP7DlFyIpEpDbZK2aLdQ3Px6Tn9DKD39O4ABz7gvzO%2B4%2BA%2B3Zrn%2FUYfvXDErIqNGZ%2Bz2Exs8iYDSv5kvFvkbEJ3uCSJXDtPTlQa%2F%2FbtV6IiN38ilxNGrWGNqekpeOkg3NspfI%2BG7YYPUvZSt0xRwZQiE7MODdzs4PvW0zu3hlobS4LND%2FytOvHQ6NtUus%2FLLEu3t7%2BOHJ9Uhkfyolp%2FjHgm3nwtgRzRN0Hpo7dNvv3CKdfqxBgvpd%2Bh8GnU2jUS5QyiEXlJf5fKgZsi8DikJI6L2Yw89081juHKeso2zeKXcdIMJmans0GOqUBmnEtjHzx7ThJwZUk6L%2BmQEupFQv%2BmbItBQdG254jyfW%2BME04B1GLZeMZ%2FyTC3O%2BDYUuR7DTZT38ORGFfkL5RkKUZsM8PKqWKmUI5QQ27iwCVlGQ3KQpyp1awE5BFGJP4VYme3Y4jYcndzfFy6x99p%2B3XN4G8dEgN6Cswg8qSItFdOGPfsuicgaRViW4lr6lH5nLC4V5WUCpCIclt7Vx8noupRtEW&X-Amz-Signature=a29f7543254a5520790ddbba115b3344e508ea9789fbc20d37887ddbfb777062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RBD62MW%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmL6Fz5sCdVbXHuRCR2nYX6pnxKGP63gT6IgPlROHjrAIgRoxvbgNjvHsJSsTwZuwEvg2nKpwbjkWrTG1dJ4AX9sQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbP%2BqteYrDtXosJfCrcA9jv5Od%2ByJye21MOuWDEu0lvZIUbzqCNot24ZLJVRCgNtRYKX7n14KM9h2a8YRcan%2FDLdXrXFurVibGTpnI57sQmAS9w5CXzIQnmnbUbXQXF0ytiTkPyM2d%2BPiAUoGZskmJbtUxzNCYA7K1nh8EOph9ndq3tvenEvP6jo9Km31mOep%2Fg73218INitaP%2FcRgl3Lkeydt7im5FjUkiNUgwB4oXjq1ErUafIqF5H6a6OgFc%2BbNP4avS5X8oBW7hSKjtw%2FHY3kkLiXv1KTZ0oLody1NivlE3dUHgFigveGexnHo0MxZ2GcDBQMKIwBldAEy%2FyiR%2Bz9UIandFuxTP7DlFyIpEpDbZK2aLdQ3Px6Tn9DKD39O4ABz7gvzO%2B4%2BA%2B3Zrn%2FUYfvXDErIqNGZ%2Bz2Exs8iYDSv5kvFvkbEJ3uCSJXDtPTlQa%2F%2FbtV6IiN38ilxNGrWGNqekpeOkg3NspfI%2BG7YYPUvZSt0xRwZQiE7MODdzs4PvW0zu3hlobS4LND%2FytOvHQ6NtUus%2FLLEu3t7%2BOHJ9Uhkfyolp%2FjHgm3nwtgRzRN0Hpo7dNvv3CKdfqxBgvpd%2Bh8GnU2jUS5QyiEXlJf5fKgZsi8DikJI6L2Yw89081juHKeso2zeKXcdIMJmans0GOqUBmnEtjHzx7ThJwZUk6L%2BmQEupFQv%2BmbItBQdG254jyfW%2BME04B1GLZeMZ%2FyTC3O%2BDYUuR7DTZT38ORGFfkL5RkKUZsM8PKqWKmUI5QQ27iwCVlGQ3KQpyp1awE5BFGJP4VYme3Y4jYcndzfFy6x99p%2B3XN4G8dEgN6Cswg8qSItFdOGPfsuicgaRViW4lr6lH5nLC4V5WUCpCIclt7Vx8noupRtEW&X-Amz-Signature=8befd9c03efd00f6b24aa228577a5b2ca99871c73d889c1f0b47d18dc84aaeaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RBD62MW%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmL6Fz5sCdVbXHuRCR2nYX6pnxKGP63gT6IgPlROHjrAIgRoxvbgNjvHsJSsTwZuwEvg2nKpwbjkWrTG1dJ4AX9sQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbP%2BqteYrDtXosJfCrcA9jv5Od%2ByJye21MOuWDEu0lvZIUbzqCNot24ZLJVRCgNtRYKX7n14KM9h2a8YRcan%2FDLdXrXFurVibGTpnI57sQmAS9w5CXzIQnmnbUbXQXF0ytiTkPyM2d%2BPiAUoGZskmJbtUxzNCYA7K1nh8EOph9ndq3tvenEvP6jo9Km31mOep%2Fg73218INitaP%2FcRgl3Lkeydt7im5FjUkiNUgwB4oXjq1ErUafIqF5H6a6OgFc%2BbNP4avS5X8oBW7hSKjtw%2FHY3kkLiXv1KTZ0oLody1NivlE3dUHgFigveGexnHo0MxZ2GcDBQMKIwBldAEy%2FyiR%2Bz9UIandFuxTP7DlFyIpEpDbZK2aLdQ3Px6Tn9DKD39O4ABz7gvzO%2B4%2BA%2B3Zrn%2FUYfvXDErIqNGZ%2Bz2Exs8iYDSv5kvFvkbEJ3uCSJXDtPTlQa%2F%2FbtV6IiN38ilxNGrWGNqekpeOkg3NspfI%2BG7YYPUvZSt0xRwZQiE7MODdzs4PvW0zu3hlobS4LND%2FytOvHQ6NtUus%2FLLEu3t7%2BOHJ9Uhkfyolp%2FjHgm3nwtgRzRN0Hpo7dNvv3CKdfqxBgvpd%2Bh8GnU2jUS5QyiEXlJf5fKgZsi8DikJI6L2Yw89081juHKeso2zeKXcdIMJmans0GOqUBmnEtjHzx7ThJwZUk6L%2BmQEupFQv%2BmbItBQdG254jyfW%2BME04B1GLZeMZ%2FyTC3O%2BDYUuR7DTZT38ORGFfkL5RkKUZsM8PKqWKmUI5QQ27iwCVlGQ3KQpyp1awE5BFGJP4VYme3Y4jYcndzfFy6x99p%2B3XN4G8dEgN6Cswg8qSItFdOGPfsuicgaRViW4lr6lH5nLC4V5WUCpCIclt7Vx8noupRtEW&X-Amz-Signature=07d22c4d2836efae513fc34d866a9f5844c147e840f2fb8787ded55f7dfdd42a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

