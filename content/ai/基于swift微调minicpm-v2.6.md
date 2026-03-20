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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIATDVO7%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCbamVVVsy2z3A%2FLmMEGsFCX%2Fmc3qVS9834uGS02NiPnAIgbU7vztex3wN9n6gs2OCI0HRRkbQLoyMNoi9wM3isyKQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDkFBC1a%2BfXYxalChyrcA7Rdd5QwnvGrMBmoruXHXUNIZp90C5M%2BP3vloZb1MQetvKftTZ6%2BWZRzQ1Br0anrlRJgj7fsFIGu723f9OTuHbLjkiSCdM9p1oVb%2Bsue3cFZygCLX0OPXtSDM0%2FKqEwWPNLnNfyhQ81r3jq%2BgilULtqZKXIEgffvHOiLh6TBjOUDzRDT0QZIByVGi2AVbOw7ymcDxqKGj999TCR1D0oSs5YTk5XK7pixXBzZSSb9s6WSeaqWU7fFfv8Plgr6lKXVCDGzl9%2FXWUlI95G3KvoK%2FcIMj5nS3fpH4X3KjV7KyBW6kwjP7vu2LZSBfX6G3vC3b85sjeviDkBQsfr%2Fi%2F%2FqFTMiVOByGrnggJQaajAi86ZKpGRQGMvlbnd8To9lsbwyE1eY6VcwaMsbN%2BI%2B%2BQPAuHKdXU3hxfnNvba%2BqgJ2pt479xRvKr%2BzjRAZWmOMqCvQY3n%2BWoWuXmoIS40tsyjaBBosxyKvVX%2F0UWA4unrigglUDdXy2hFghLgBBRk2pbf9cvALhLP0q%2BremvVR7W%2Btbgf5IDqOsFdxiwDPKq5UGoPkL5ytVf6M4Pk%2B125vj%2Bnu4Bz9zBNp2wklnpEmEfBqJz8ataQSfKm9Ig9MM0NgfDZz%2FtYNcDgyaNqsKu1gMOm48s0GOqUBnQheWWCgJQJZd4s2%2BBVIijIaBevShKtDa2DcVuEJsCcUjTkllrPxqg4ZjQ7iGta5WL0wbcHRPMp88Dtb6%2BMJoM6NfYsb6QMlAsafhM%2BFjNewCbehREaWFPpmCR1SHQsNX37eHUxcB2Ud1L7HNxYW5iBdbzIvlqTziZhsbK4KZWTM2SS9uhAqkkNi07PYWf8WgFAG%2B0KwsYos%2BiU6Xs2HGO5SWiCc&X-Amz-Signature=f48a5a583ea539f5fdd89df64046ebff8341c7d91920b3c1057f600d4dc68a0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIATDVO7%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCbamVVVsy2z3A%2FLmMEGsFCX%2Fmc3qVS9834uGS02NiPnAIgbU7vztex3wN9n6gs2OCI0HRRkbQLoyMNoi9wM3isyKQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDkFBC1a%2BfXYxalChyrcA7Rdd5QwnvGrMBmoruXHXUNIZp90C5M%2BP3vloZb1MQetvKftTZ6%2BWZRzQ1Br0anrlRJgj7fsFIGu723f9OTuHbLjkiSCdM9p1oVb%2Bsue3cFZygCLX0OPXtSDM0%2FKqEwWPNLnNfyhQ81r3jq%2BgilULtqZKXIEgffvHOiLh6TBjOUDzRDT0QZIByVGi2AVbOw7ymcDxqKGj999TCR1D0oSs5YTk5XK7pixXBzZSSb9s6WSeaqWU7fFfv8Plgr6lKXVCDGzl9%2FXWUlI95G3KvoK%2FcIMj5nS3fpH4X3KjV7KyBW6kwjP7vu2LZSBfX6G3vC3b85sjeviDkBQsfr%2Fi%2F%2FqFTMiVOByGrnggJQaajAi86ZKpGRQGMvlbnd8To9lsbwyE1eY6VcwaMsbN%2BI%2B%2BQPAuHKdXU3hxfnNvba%2BqgJ2pt479xRvKr%2BzjRAZWmOMqCvQY3n%2BWoWuXmoIS40tsyjaBBosxyKvVX%2F0UWA4unrigglUDdXy2hFghLgBBRk2pbf9cvALhLP0q%2BremvVR7W%2Btbgf5IDqOsFdxiwDPKq5UGoPkL5ytVf6M4Pk%2B125vj%2Bnu4Bz9zBNp2wklnpEmEfBqJz8ataQSfKm9Ig9MM0NgfDZz%2FtYNcDgyaNqsKu1gMOm48s0GOqUBnQheWWCgJQJZd4s2%2BBVIijIaBevShKtDa2DcVuEJsCcUjTkllrPxqg4ZjQ7iGta5WL0wbcHRPMp88Dtb6%2BMJoM6NfYsb6QMlAsafhM%2BFjNewCbehREaWFPpmCR1SHQsNX37eHUxcB2Ud1L7HNxYW5iBdbzIvlqTziZhsbK4KZWTM2SS9uhAqkkNi07PYWf8WgFAG%2B0KwsYos%2BiU6Xs2HGO5SWiCc&X-Amz-Signature=5c1c626a0733a7bf1c6a76eacd65dfeda0b4ddcdfb31d644ec4889bfd1c5725f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIATDVO7%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCbamVVVsy2z3A%2FLmMEGsFCX%2Fmc3qVS9834uGS02NiPnAIgbU7vztex3wN9n6gs2OCI0HRRkbQLoyMNoi9wM3isyKQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDkFBC1a%2BfXYxalChyrcA7Rdd5QwnvGrMBmoruXHXUNIZp90C5M%2BP3vloZb1MQetvKftTZ6%2BWZRzQ1Br0anrlRJgj7fsFIGu723f9OTuHbLjkiSCdM9p1oVb%2Bsue3cFZygCLX0OPXtSDM0%2FKqEwWPNLnNfyhQ81r3jq%2BgilULtqZKXIEgffvHOiLh6TBjOUDzRDT0QZIByVGi2AVbOw7ymcDxqKGj999TCR1D0oSs5YTk5XK7pixXBzZSSb9s6WSeaqWU7fFfv8Plgr6lKXVCDGzl9%2FXWUlI95G3KvoK%2FcIMj5nS3fpH4X3KjV7KyBW6kwjP7vu2LZSBfX6G3vC3b85sjeviDkBQsfr%2Fi%2F%2FqFTMiVOByGrnggJQaajAi86ZKpGRQGMvlbnd8To9lsbwyE1eY6VcwaMsbN%2BI%2B%2BQPAuHKdXU3hxfnNvba%2BqgJ2pt479xRvKr%2BzjRAZWmOMqCvQY3n%2BWoWuXmoIS40tsyjaBBosxyKvVX%2F0UWA4unrigglUDdXy2hFghLgBBRk2pbf9cvALhLP0q%2BremvVR7W%2Btbgf5IDqOsFdxiwDPKq5UGoPkL5ytVf6M4Pk%2B125vj%2Bnu4Bz9zBNp2wklnpEmEfBqJz8ataQSfKm9Ig9MM0NgfDZz%2FtYNcDgyaNqsKu1gMOm48s0GOqUBnQheWWCgJQJZd4s2%2BBVIijIaBevShKtDa2DcVuEJsCcUjTkllrPxqg4ZjQ7iGta5WL0wbcHRPMp88Dtb6%2BMJoM6NfYsb6QMlAsafhM%2BFjNewCbehREaWFPpmCR1SHQsNX37eHUxcB2Ud1L7HNxYW5iBdbzIvlqTziZhsbK4KZWTM2SS9uhAqkkNi07PYWf8WgFAG%2B0KwsYos%2BiU6Xs2HGO5SWiCc&X-Amz-Signature=4ef4c67612708edad847ea2f242e1a2b205faa481269451e7ebe049c26e681b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

