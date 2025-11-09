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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCI6B7WT%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDvaK5%2FRMj6nCnGKAABOPiB%2Ba5QPpY7ZNQNm7QUYGFq0wIgVYLtfH8ANHyuuzWn6rbTTAft5eor665awNw%2F6AiQAFUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeL%2BcB8lDE9qlNC9SrcA19JoBIjkHqX2l1GuyUejG3hSTrHfUMV5DQJrBy05n%2Bpd7%2BWrbWlxavRC%2B3u2gMtdqCmFlO1qaxTpx%2BEBTVoYvDx0C3Fns83%2FC9rGEtWl%2BwshhIW9e5B37YtWuKKj7oLx%2FSEDl0MSwmLp5XGs8L3CETeVl7XE50dkBetQbw5J%2Ffa3EJ9HvXg11VSyWTI9jm3BHF2Ykly24vp2eBhabADHT%2B%2BqniTl6XKdyL5nuPnaI4%2ByytK0cRtRw39FNS5BFSSn%2BtCEvJHU0Ek4iQN%2FzUGbutRNavG8%2BKg4CH2wbja7yxJacr0s7yqqEr5WHr%2BXsVDFQh8g%2FPt56Uvycc%2F3LPXQIQ9IgGA3l1mCosd9k3ECFCdwljdPGhKrlgXQyAM%2FEHATlBRy%2BpZp6s2GQ0Jzgo%2BW7KGgTIgKUJpuutrkfDy2N7OeJ0ZvTYjDEFc7UQbeR%2FEx7sNhFlIbidEogqr6WocEWLQkz16dXfPXq5r1c5b3whtBetooNJ5GSgUUonIZi1jVIrjso02IooWM8KGv%2FAr6Z8PSON99gcL10KZ3t4HMQYf8SVWl1jTOu5SF7%2Fp8FRabp3%2FmPWOCOBhyDN3Z9iTv6DWaPLt%2BjzroHO%2Fa1qhnyN6g6bDT1s48NwlxCMaMOq3v8gGOqUBs1MaeAaV89ig9t7bRvixjejTFtTd23hLw9wXWpuQOw0NBoZ0%2FuFbK30IseNsRTma9MeAG5nNev5xxk5fNNsEEw0WF3KTdMK1PcORH9zcOHG2Wj0WC72YaW%2FOh6%2FPfrTdzJ3jK2e8h6hEwAVivQn%2B1lPhNwFfMUjSujJ4mRUMhjOEwnbubLXuGnRYhWT0xOfWWUm50w6nWlnCBAEqZwGQWC2fBLrq&X-Amz-Signature=7ccb1e6b31b340e8c2804cfb21e5a94af443bdfe73ae5d5f596abd156f1869d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCI6B7WT%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDvaK5%2FRMj6nCnGKAABOPiB%2Ba5QPpY7ZNQNm7QUYGFq0wIgVYLtfH8ANHyuuzWn6rbTTAft5eor665awNw%2F6AiQAFUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeL%2BcB8lDE9qlNC9SrcA19JoBIjkHqX2l1GuyUejG3hSTrHfUMV5DQJrBy05n%2Bpd7%2BWrbWlxavRC%2B3u2gMtdqCmFlO1qaxTpx%2BEBTVoYvDx0C3Fns83%2FC9rGEtWl%2BwshhIW9e5B37YtWuKKj7oLx%2FSEDl0MSwmLp5XGs8L3CETeVl7XE50dkBetQbw5J%2Ffa3EJ9HvXg11VSyWTI9jm3BHF2Ykly24vp2eBhabADHT%2B%2BqniTl6XKdyL5nuPnaI4%2ByytK0cRtRw39FNS5BFSSn%2BtCEvJHU0Ek4iQN%2FzUGbutRNavG8%2BKg4CH2wbja7yxJacr0s7yqqEr5WHr%2BXsVDFQh8g%2FPt56Uvycc%2F3LPXQIQ9IgGA3l1mCosd9k3ECFCdwljdPGhKrlgXQyAM%2FEHATlBRy%2BpZp6s2GQ0Jzgo%2BW7KGgTIgKUJpuutrkfDy2N7OeJ0ZvTYjDEFc7UQbeR%2FEx7sNhFlIbidEogqr6WocEWLQkz16dXfPXq5r1c5b3whtBetooNJ5GSgUUonIZi1jVIrjso02IooWM8KGv%2FAr6Z8PSON99gcL10KZ3t4HMQYf8SVWl1jTOu5SF7%2Fp8FRabp3%2FmPWOCOBhyDN3Z9iTv6DWaPLt%2BjzroHO%2Fa1qhnyN6g6bDT1s48NwlxCMaMOq3v8gGOqUBs1MaeAaV89ig9t7bRvixjejTFtTd23hLw9wXWpuQOw0NBoZ0%2FuFbK30IseNsRTma9MeAG5nNev5xxk5fNNsEEw0WF3KTdMK1PcORH9zcOHG2Wj0WC72YaW%2FOh6%2FPfrTdzJ3jK2e8h6hEwAVivQn%2B1lPhNwFfMUjSujJ4mRUMhjOEwnbubLXuGnRYhWT0xOfWWUm50w6nWlnCBAEqZwGQWC2fBLrq&X-Amz-Signature=f2c5e99aed8a16d0fa6fa2ca4e3c9f4d8c4bb31272aeb4cf407bdb206bc54fd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCI6B7WT%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDvaK5%2FRMj6nCnGKAABOPiB%2Ba5QPpY7ZNQNm7QUYGFq0wIgVYLtfH8ANHyuuzWn6rbTTAft5eor665awNw%2F6AiQAFUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeL%2BcB8lDE9qlNC9SrcA19JoBIjkHqX2l1GuyUejG3hSTrHfUMV5DQJrBy05n%2Bpd7%2BWrbWlxavRC%2B3u2gMtdqCmFlO1qaxTpx%2BEBTVoYvDx0C3Fns83%2FC9rGEtWl%2BwshhIW9e5B37YtWuKKj7oLx%2FSEDl0MSwmLp5XGs8L3CETeVl7XE50dkBetQbw5J%2Ffa3EJ9HvXg11VSyWTI9jm3BHF2Ykly24vp2eBhabADHT%2B%2BqniTl6XKdyL5nuPnaI4%2ByytK0cRtRw39FNS5BFSSn%2BtCEvJHU0Ek4iQN%2FzUGbutRNavG8%2BKg4CH2wbja7yxJacr0s7yqqEr5WHr%2BXsVDFQh8g%2FPt56Uvycc%2F3LPXQIQ9IgGA3l1mCosd9k3ECFCdwljdPGhKrlgXQyAM%2FEHATlBRy%2BpZp6s2GQ0Jzgo%2BW7KGgTIgKUJpuutrkfDy2N7OeJ0ZvTYjDEFc7UQbeR%2FEx7sNhFlIbidEogqr6WocEWLQkz16dXfPXq5r1c5b3whtBetooNJ5GSgUUonIZi1jVIrjso02IooWM8KGv%2FAr6Z8PSON99gcL10KZ3t4HMQYf8SVWl1jTOu5SF7%2Fp8FRabp3%2FmPWOCOBhyDN3Z9iTv6DWaPLt%2BjzroHO%2Fa1qhnyN6g6bDT1s48NwlxCMaMOq3v8gGOqUBs1MaeAaV89ig9t7bRvixjejTFtTd23hLw9wXWpuQOw0NBoZ0%2FuFbK30IseNsRTma9MeAG5nNev5xxk5fNNsEEw0WF3KTdMK1PcORH9zcOHG2Wj0WC72YaW%2FOh6%2FPfrTdzJ3jK2e8h6hEwAVivQn%2B1lPhNwFfMUjSujJ4mRUMhjOEwnbubLXuGnRYhWT0xOfWWUm50w6nWlnCBAEqZwGQWC2fBLrq&X-Amz-Signature=3b66319943e7c9d122950c1e1ececacb81bca5e3352b8fce459419efc47bb6ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

