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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKOU5XQV%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCQ2iGJ%2FkhWrJn7lI7L1bGIqnnixk5UvSyiYiKOJjf2swIgPO9sBzoere802a%2BGtSnqjhU4gdBejYLB0PPH%2FIqTsDMqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8g5KDkMjjw6XN%2BpyrcAxbxo0ZcwmqHnqqC1HRtV%2F4PO4VF16v57pfgKu3Tm9JW3DJQeh891ot%2BunzVfS6sC9ml1nmH541pYQy%2BO4SGtr5qdYRDOHlh5B44KLsVrTMj3eACnUbkLkBsXDRTDlYhe6EN6IEIJLkLupI96lcJI0cfeG%2BVMjW9ipek8hO7G0RhfbvLNtRPNkZFVcP7EnAZD9q8GOD38ysP4BtxFY9e0Z2XeDnv97NB2GN8CpZ6IycycpHcfSUujkLTElRIwEDDJ70YcwYdrc3V8HubD%2FKAZTxRpEQrUL4K54r3ykSZQ%2BUxA%2F4%2F%2BNOlAxLlXJPYd3Lhw%2BfQdJPSLekBzGNhQsUIBOEU4zr%2Bx0u3c%2FFiqdqYSE3M5%2F6asEcyMaCOZRjj%2F6DKujdXgMVJBzFy4mzdVizhYgF8gdNaiD8znsfeUMRoWLh3JWfxw%2BFOV0n0fHQ5LMRD3ELBiEz17FKlcrwL1VWNZM9H2TrJH7VCa2k5f2IsYxuIxkSy1STDWyMgRhqyv%2Fu%2BzQXSVEVYa2%2FiLJQYAre2e1RN8swsmbwbzwLLAuW10Y%2B4bpERhcJKzGmXzJsYrY6%2BYjYYzDbT1mD1E5SmykHX3J8yidmBtCqHMAI9pm747IXdr1Ik2o5xIwnPDtCbMJ3pls4GOqUBYhWr8tNFFP0OAUXnip0wGeY1relzM09%2BaC6cjLuAgasjEdQDkm66rA3D0stcwAFWEdeDMwXUY5bVUMgZriO6SdwwF8SWmjdCUZrlqZxGNa7OWhL47L%2BGVzRp7hRAQK8jIkS%2FFOpizODluyh%2B1bzmJ7trYGKLtwStBf7wvUuxL4VpKLKWxHgvSZDgEnjMYT4%2Fo6xXef8SoAwbOfOZWPe6VaWfLuQD&X-Amz-Signature=c604d3036a539aefd82b5f4e3d47ad441d1c29eb9fc0bd839004c98ca85708b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKOU5XQV%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCQ2iGJ%2FkhWrJn7lI7L1bGIqnnixk5UvSyiYiKOJjf2swIgPO9sBzoere802a%2BGtSnqjhU4gdBejYLB0PPH%2FIqTsDMqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8g5KDkMjjw6XN%2BpyrcAxbxo0ZcwmqHnqqC1HRtV%2F4PO4VF16v57pfgKu3Tm9JW3DJQeh891ot%2BunzVfS6sC9ml1nmH541pYQy%2BO4SGtr5qdYRDOHlh5B44KLsVrTMj3eACnUbkLkBsXDRTDlYhe6EN6IEIJLkLupI96lcJI0cfeG%2BVMjW9ipek8hO7G0RhfbvLNtRPNkZFVcP7EnAZD9q8GOD38ysP4BtxFY9e0Z2XeDnv97NB2GN8CpZ6IycycpHcfSUujkLTElRIwEDDJ70YcwYdrc3V8HubD%2FKAZTxRpEQrUL4K54r3ykSZQ%2BUxA%2F4%2F%2BNOlAxLlXJPYd3Lhw%2BfQdJPSLekBzGNhQsUIBOEU4zr%2Bx0u3c%2FFiqdqYSE3M5%2F6asEcyMaCOZRjj%2F6DKujdXgMVJBzFy4mzdVizhYgF8gdNaiD8znsfeUMRoWLh3JWfxw%2BFOV0n0fHQ5LMRD3ELBiEz17FKlcrwL1VWNZM9H2TrJH7VCa2k5f2IsYxuIxkSy1STDWyMgRhqyv%2Fu%2BzQXSVEVYa2%2FiLJQYAre2e1RN8swsmbwbzwLLAuW10Y%2B4bpERhcJKzGmXzJsYrY6%2BYjYYzDbT1mD1E5SmykHX3J8yidmBtCqHMAI9pm747IXdr1Ik2o5xIwnPDtCbMJ3pls4GOqUBYhWr8tNFFP0OAUXnip0wGeY1relzM09%2BaC6cjLuAgasjEdQDkm66rA3D0stcwAFWEdeDMwXUY5bVUMgZriO6SdwwF8SWmjdCUZrlqZxGNa7OWhL47L%2BGVzRp7hRAQK8jIkS%2FFOpizODluyh%2B1bzmJ7trYGKLtwStBf7wvUuxL4VpKLKWxHgvSZDgEnjMYT4%2Fo6xXef8SoAwbOfOZWPe6VaWfLuQD&X-Amz-Signature=971847bd7b9fa30ead726dbce234b9731735ac55af5ad79d55060781d695ce24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKOU5XQV%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCQ2iGJ%2FkhWrJn7lI7L1bGIqnnixk5UvSyiYiKOJjf2swIgPO9sBzoere802a%2BGtSnqjhU4gdBejYLB0PPH%2FIqTsDMqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8g5KDkMjjw6XN%2BpyrcAxbxo0ZcwmqHnqqC1HRtV%2F4PO4VF16v57pfgKu3Tm9JW3DJQeh891ot%2BunzVfS6sC9ml1nmH541pYQy%2BO4SGtr5qdYRDOHlh5B44KLsVrTMj3eACnUbkLkBsXDRTDlYhe6EN6IEIJLkLupI96lcJI0cfeG%2BVMjW9ipek8hO7G0RhfbvLNtRPNkZFVcP7EnAZD9q8GOD38ysP4BtxFY9e0Z2XeDnv97NB2GN8CpZ6IycycpHcfSUujkLTElRIwEDDJ70YcwYdrc3V8HubD%2FKAZTxRpEQrUL4K54r3ykSZQ%2BUxA%2F4%2F%2BNOlAxLlXJPYd3Lhw%2BfQdJPSLekBzGNhQsUIBOEU4zr%2Bx0u3c%2FFiqdqYSE3M5%2F6asEcyMaCOZRjj%2F6DKujdXgMVJBzFy4mzdVizhYgF8gdNaiD8znsfeUMRoWLh3JWfxw%2BFOV0n0fHQ5LMRD3ELBiEz17FKlcrwL1VWNZM9H2TrJH7VCa2k5f2IsYxuIxkSy1STDWyMgRhqyv%2Fu%2BzQXSVEVYa2%2FiLJQYAre2e1RN8swsmbwbzwLLAuW10Y%2B4bpERhcJKzGmXzJsYrY6%2BYjYYzDbT1mD1E5SmykHX3J8yidmBtCqHMAI9pm747IXdr1Ik2o5xIwnPDtCbMJ3pls4GOqUBYhWr8tNFFP0OAUXnip0wGeY1relzM09%2BaC6cjLuAgasjEdQDkm66rA3D0stcwAFWEdeDMwXUY5bVUMgZriO6SdwwF8SWmjdCUZrlqZxGNa7OWhL47L%2BGVzRp7hRAQK8jIkS%2FFOpizODluyh%2B1bzmJ7trYGKLtwStBf7wvUuxL4VpKLKWxHgvSZDgEnjMYT4%2Fo6xXef8SoAwbOfOZWPe6VaWfLuQD&X-Amz-Signature=5e752aeb0724f0a821e76967954b863cb3e294e26aa12967e8e0797e09260ecb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

