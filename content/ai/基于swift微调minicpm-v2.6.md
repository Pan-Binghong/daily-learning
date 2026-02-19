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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVG2TSSR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBubT4RHmPyArq8LKC19TPmI3uEMBhRjkTMKbgtKLq8RAiEA6M%2FUwcu7FQbWEOJFHP54rw49aPNlJ1Jz%2BaPUS8sPq9Uq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDD0uAVRj2C%2BXwJupYSrcAzn0LECXoLj8hqj0jrGBvQxkQBsaDaA0t4diW%2FI0S4Dd0zErQTNd0Km2yr8rhLQPNFzg6bgIzwmF7GJhyGT%2FOpBeFiqZ70SQsisE5ecJ9PmMnQySgsJSJdc6Ve8tqHfuM9lLgt3gZ0FmYgsZU9kpdfQE0bbGQcxd08YlJacyzJinuCz4E3PtRcBwpKqEkOkhXK9K6PO8w85vJUhLhMv6As6Puq7t4kxBiAg1ZdTMOfCzJuNuj7lH0F8UepR%2BW3wwpb67EsyPp7lyMoaUmE20Zed%2BV7dvmD4Q8mJ3GTItXC4P7IdPfRvdHGtAoaqJNk3%2Fl4y%2FRAcMy6NHspYShEgjSIwmy%2FsPDC4e8FHxoSrph4Euy1VXA2ZCyMqBKjOeVkr1zO903cmjidKVTGPRKDR7pu57iedq5UuqRFJIr9B%2Bdjq%2FiiDym17i3h5D1fwUreIEkls2r0M%2BM%2BLCg1mpnY8fxgKqGZIAhaOvugHsptgs0Gix38kL8xWK3zXWgnII%2BpU1aJEKH7xQMd1pvGgC0NVCLzUldo4Td6Hg55e0FKizqVy91dkYJ3BIurKnAZwFj2aJ5E9jjEfIr1f5%2F%2FHqCTkHCzy5AoSnBsNNO15hNushGApA9H%2FCYJZLxtc9ODqEMNjx2cwGOqUBlDoifHwv7Cqn8XUH0X5NM11jE75H6HxRrQMxGfLiNahjMJgXFc7gCuIINiScW8kmueSgcd3DekGrgFMpbCAnoYiy%2B8uuaEDYclVbGTQCQLOMvR8TwcRSeMjrvKCKmJDnR1Vkx%2ByHV%2BaO8UdfiWMOXonIZkDWX2Uh3iJpvutJMLn1XW00%2F2VK2xmaqz2%2B3framwOhQBWXDQbyNXvw40O3oOI0%2FoJZ&X-Amz-Signature=1437e7d663e37a73058d643b6a5b1c42933f51be9a7aba0fdee93288dd46210f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVG2TSSR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBubT4RHmPyArq8LKC19TPmI3uEMBhRjkTMKbgtKLq8RAiEA6M%2FUwcu7FQbWEOJFHP54rw49aPNlJ1Jz%2BaPUS8sPq9Uq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDD0uAVRj2C%2BXwJupYSrcAzn0LECXoLj8hqj0jrGBvQxkQBsaDaA0t4diW%2FI0S4Dd0zErQTNd0Km2yr8rhLQPNFzg6bgIzwmF7GJhyGT%2FOpBeFiqZ70SQsisE5ecJ9PmMnQySgsJSJdc6Ve8tqHfuM9lLgt3gZ0FmYgsZU9kpdfQE0bbGQcxd08YlJacyzJinuCz4E3PtRcBwpKqEkOkhXK9K6PO8w85vJUhLhMv6As6Puq7t4kxBiAg1ZdTMOfCzJuNuj7lH0F8UepR%2BW3wwpb67EsyPp7lyMoaUmE20Zed%2BV7dvmD4Q8mJ3GTItXC4P7IdPfRvdHGtAoaqJNk3%2Fl4y%2FRAcMy6NHspYShEgjSIwmy%2FsPDC4e8FHxoSrph4Euy1VXA2ZCyMqBKjOeVkr1zO903cmjidKVTGPRKDR7pu57iedq5UuqRFJIr9B%2Bdjq%2FiiDym17i3h5D1fwUreIEkls2r0M%2BM%2BLCg1mpnY8fxgKqGZIAhaOvugHsptgs0Gix38kL8xWK3zXWgnII%2BpU1aJEKH7xQMd1pvGgC0NVCLzUldo4Td6Hg55e0FKizqVy91dkYJ3BIurKnAZwFj2aJ5E9jjEfIr1f5%2F%2FHqCTkHCzy5AoSnBsNNO15hNushGApA9H%2FCYJZLxtc9ODqEMNjx2cwGOqUBlDoifHwv7Cqn8XUH0X5NM11jE75H6HxRrQMxGfLiNahjMJgXFc7gCuIINiScW8kmueSgcd3DekGrgFMpbCAnoYiy%2B8uuaEDYclVbGTQCQLOMvR8TwcRSeMjrvKCKmJDnR1Vkx%2ByHV%2BaO8UdfiWMOXonIZkDWX2Uh3iJpvutJMLn1XW00%2F2VK2xmaqz2%2B3framwOhQBWXDQbyNXvw40O3oOI0%2FoJZ&X-Amz-Signature=bf471d2204f8f871c4bb1d7492e0e3359e3450a834e640bfd39b37f122f41dc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVG2TSSR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBubT4RHmPyArq8LKC19TPmI3uEMBhRjkTMKbgtKLq8RAiEA6M%2FUwcu7FQbWEOJFHP54rw49aPNlJ1Jz%2BaPUS8sPq9Uq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDD0uAVRj2C%2BXwJupYSrcAzn0LECXoLj8hqj0jrGBvQxkQBsaDaA0t4diW%2FI0S4Dd0zErQTNd0Km2yr8rhLQPNFzg6bgIzwmF7GJhyGT%2FOpBeFiqZ70SQsisE5ecJ9PmMnQySgsJSJdc6Ve8tqHfuM9lLgt3gZ0FmYgsZU9kpdfQE0bbGQcxd08YlJacyzJinuCz4E3PtRcBwpKqEkOkhXK9K6PO8w85vJUhLhMv6As6Puq7t4kxBiAg1ZdTMOfCzJuNuj7lH0F8UepR%2BW3wwpb67EsyPp7lyMoaUmE20Zed%2BV7dvmD4Q8mJ3GTItXC4P7IdPfRvdHGtAoaqJNk3%2Fl4y%2FRAcMy6NHspYShEgjSIwmy%2FsPDC4e8FHxoSrph4Euy1VXA2ZCyMqBKjOeVkr1zO903cmjidKVTGPRKDR7pu57iedq5UuqRFJIr9B%2Bdjq%2FiiDym17i3h5D1fwUreIEkls2r0M%2BM%2BLCg1mpnY8fxgKqGZIAhaOvugHsptgs0Gix38kL8xWK3zXWgnII%2BpU1aJEKH7xQMd1pvGgC0NVCLzUldo4Td6Hg55e0FKizqVy91dkYJ3BIurKnAZwFj2aJ5E9jjEfIr1f5%2F%2FHqCTkHCzy5AoSnBsNNO15hNushGApA9H%2FCYJZLxtc9ODqEMNjx2cwGOqUBlDoifHwv7Cqn8XUH0X5NM11jE75H6HxRrQMxGfLiNahjMJgXFc7gCuIINiScW8kmueSgcd3DekGrgFMpbCAnoYiy%2B8uuaEDYclVbGTQCQLOMvR8TwcRSeMjrvKCKmJDnR1Vkx%2ByHV%2BaO8UdfiWMOXonIZkDWX2Uh3iJpvutJMLn1XW00%2F2VK2xmaqz2%2B3framwOhQBWXDQbyNXvw40O3oOI0%2FoJZ&X-Amz-Signature=8cd25b39d664cfb36886f65820ab9c23009ad724adb9c69cacee24f2f13c12b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

