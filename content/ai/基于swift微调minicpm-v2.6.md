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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBO6YCFH%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzBvxpchpspQoO9i7COkvWjO7zzNRi5cNgv8ovFHXqPAiEA4wJ0jHOCjNqpUfR3%2B6sUgbN%2BENyM%2FH8OmVR5ttS%2Fn2gq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDcZ%2B3xLoa%2FRAW7ejSrcAz1B3ldXrNUZA2pnHHNuOeLPiDtbTRvkgYGdBrGNCfqz8YbgTmlndkWCvQJSwigVrrvctErywu5izyy8GZuCOwW9lyE50r8X0FJUeFo390OaCu1CCgxMit2MX23W2dnReSDCFrSnmXN7unwlNndmdim6Qpl8%2B%2Fe8cxjh5QY7%2FkAUDUGC34IzVaA29ZF8pzhnQw24jDLqGEB3pbhkAkoGhrZ9fiCz26Net5kISm1BXsqRogu0QynkHOjHKdTY70GAge3QDFu7XzLhYxnT%2FSp%2FaCCWvJInqMe2VjdxTeL94%2Fh6kFyatqvXxWUXaVYJYfURuWvubPBcIcJAr%2BTywJt2d9OS%2Fhw9bWklzc7Ox3e8J5eYPyooDe1z4kPHYeXk9XiSGH%2FdDTv2CwfG%2F0JOuGXWSg6GZz2dPh6wmzVI2im%2F%2F%2FYDqg8RiLQrmBBR%2Fn27A3YpZxmW%2BosK5QKsBkqArkwqwv7dmv0wQykDIPVvDslWkxYsSxd9d42SO8JQbBq4wiXfRPXSkm6VMDlke7F%2FiZuxXZjmYnS3gnzg2NlN2pcprTO2GTn%2B9qR6aCkU%2B6YabDCiovyAErhVUrbyd%2BtEJ9ZtfrGb1eYPsYLpz%2Bhi%2B1q6ujZs7D298f59zpQtZtULMOqut84GOqUBL3EEKkVG1reuEuDCVdEV0m65kGU%2BolFNonkrMypWjdAaHaIfYYDXx%2FHcG6AsVO161wuvJjlNiCDEgj1fiZn%2Fe6djtxoFt4lRm7AsmOUQZzDpqvnDyiX2HpZ7ctfze32OFNhp6OXNE5m1KVsnYl1ssSorH1kCjE290FHkLmAgkU52yVD3O8m6hpGl6WC8kEk31eUKgS3uC38USKMCw%2B1aoX35Aazs&X-Amz-Signature=716b8aa3e88d33284723e8667a95dc6f5f0a9e4f4b923189ee220a1388b9eee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBO6YCFH%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzBvxpchpspQoO9i7COkvWjO7zzNRi5cNgv8ovFHXqPAiEA4wJ0jHOCjNqpUfR3%2B6sUgbN%2BENyM%2FH8OmVR5ttS%2Fn2gq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDcZ%2B3xLoa%2FRAW7ejSrcAz1B3ldXrNUZA2pnHHNuOeLPiDtbTRvkgYGdBrGNCfqz8YbgTmlndkWCvQJSwigVrrvctErywu5izyy8GZuCOwW9lyE50r8X0FJUeFo390OaCu1CCgxMit2MX23W2dnReSDCFrSnmXN7unwlNndmdim6Qpl8%2B%2Fe8cxjh5QY7%2FkAUDUGC34IzVaA29ZF8pzhnQw24jDLqGEB3pbhkAkoGhrZ9fiCz26Net5kISm1BXsqRogu0QynkHOjHKdTY70GAge3QDFu7XzLhYxnT%2FSp%2FaCCWvJInqMe2VjdxTeL94%2Fh6kFyatqvXxWUXaVYJYfURuWvubPBcIcJAr%2BTywJt2d9OS%2Fhw9bWklzc7Ox3e8J5eYPyooDe1z4kPHYeXk9XiSGH%2FdDTv2CwfG%2F0JOuGXWSg6GZz2dPh6wmzVI2im%2F%2F%2FYDqg8RiLQrmBBR%2Fn27A3YpZxmW%2BosK5QKsBkqArkwqwv7dmv0wQykDIPVvDslWkxYsSxd9d42SO8JQbBq4wiXfRPXSkm6VMDlke7F%2FiZuxXZjmYnS3gnzg2NlN2pcprTO2GTn%2B9qR6aCkU%2B6YabDCiovyAErhVUrbyd%2BtEJ9ZtfrGb1eYPsYLpz%2Bhi%2B1q6ujZs7D298f59zpQtZtULMOqut84GOqUBL3EEKkVG1reuEuDCVdEV0m65kGU%2BolFNonkrMypWjdAaHaIfYYDXx%2FHcG6AsVO161wuvJjlNiCDEgj1fiZn%2Fe6djtxoFt4lRm7AsmOUQZzDpqvnDyiX2HpZ7ctfze32OFNhp6OXNE5m1KVsnYl1ssSorH1kCjE290FHkLmAgkU52yVD3O8m6hpGl6WC8kEk31eUKgS3uC38USKMCw%2B1aoX35Aazs&X-Amz-Signature=babdb5aa84380530eca941be0163ca719f13c6c8032d5e964c82f226034ab292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBO6YCFH%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzBvxpchpspQoO9i7COkvWjO7zzNRi5cNgv8ovFHXqPAiEA4wJ0jHOCjNqpUfR3%2B6sUgbN%2BENyM%2FH8OmVR5ttS%2Fn2gq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDcZ%2B3xLoa%2FRAW7ejSrcAz1B3ldXrNUZA2pnHHNuOeLPiDtbTRvkgYGdBrGNCfqz8YbgTmlndkWCvQJSwigVrrvctErywu5izyy8GZuCOwW9lyE50r8X0FJUeFo390OaCu1CCgxMit2MX23W2dnReSDCFrSnmXN7unwlNndmdim6Qpl8%2B%2Fe8cxjh5QY7%2FkAUDUGC34IzVaA29ZF8pzhnQw24jDLqGEB3pbhkAkoGhrZ9fiCz26Net5kISm1BXsqRogu0QynkHOjHKdTY70GAge3QDFu7XzLhYxnT%2FSp%2FaCCWvJInqMe2VjdxTeL94%2Fh6kFyatqvXxWUXaVYJYfURuWvubPBcIcJAr%2BTywJt2d9OS%2Fhw9bWklzc7Ox3e8J5eYPyooDe1z4kPHYeXk9XiSGH%2FdDTv2CwfG%2F0JOuGXWSg6GZz2dPh6wmzVI2im%2F%2F%2FYDqg8RiLQrmBBR%2Fn27A3YpZxmW%2BosK5QKsBkqArkwqwv7dmv0wQykDIPVvDslWkxYsSxd9d42SO8JQbBq4wiXfRPXSkm6VMDlke7F%2FiZuxXZjmYnS3gnzg2NlN2pcprTO2GTn%2B9qR6aCkU%2B6YabDCiovyAErhVUrbyd%2BtEJ9ZtfrGb1eYPsYLpz%2Bhi%2B1q6ujZs7D298f59zpQtZtULMOqut84GOqUBL3EEKkVG1reuEuDCVdEV0m65kGU%2BolFNonkrMypWjdAaHaIfYYDXx%2FHcG6AsVO161wuvJjlNiCDEgj1fiZn%2Fe6djtxoFt4lRm7AsmOUQZzDpqvnDyiX2HpZ7ctfze32OFNhp6OXNE5m1KVsnYl1ssSorH1kCjE290FHkLmAgkU52yVD3O8m6hpGl6WC8kEk31eUKgS3uC38USKMCw%2B1aoX35Aazs&X-Amz-Signature=982066db410d613feb431559256859c2a25e937dd5e9706324fbf59b8bd89a4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

