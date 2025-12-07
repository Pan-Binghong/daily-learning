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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L24BVUI%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzwyXF%2BIoZjzBvIhEr2QflYk55OLE21b1Nlj%2BC9s04WAiBFC8NWHMSKU44qiThqx1Dd42w8TbW9CuYBpzhom3bzFCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVNyLqLntuYe41AolKtwDq%2FDMQUA8MCyMi0CcYa4p3EeF5osm%2FLTeTqw2pgQRik9vZG0WS9lqcBxgunvQ2zdsNrzFFLhAT5NP3EycOsWIu8XeZZHMvTF6Flv78q33ppynFt%2BwgPRxfAKkyWiMhPslPDrfzQVPhJhPYflzixinRBl7Gm7rP8BPnDwV3%2Bf5s%2FEvnSJA6oBvrQOvORQYJQk1U5Bn5kYEU1qlQNzn7lRb87%2F8T8nu48o7hZYh64P7HB9TUrWBB82tPIpGmUTJMysKElxCKHRNW3jo0r3yv%2FTKVo8qaPgsekuBPexPBBfW6uXB%2BkrYrmPld3aCrZvefPkFqnGayKGU9rWULpWjx7tvzxv5Lp4U3Es0jpwEjaBVSPJEx0NQxsIi%2Fswu3BG%2BszNU0%2BV4ChgG8PrzWCIFu4Ht80NyKHqpp5jA9IQdV1ldDNW4VxJEcBWAGpKOOH%2FYHM5HFpfuxGc3lcFQGBHMh2Yt915A4jxsEb%2FAERqh1soHLqdAbN3XV%2FusNJ0h3sdXvSE40UfjfDDBp2g1AI22ziiLkISrceHcmZQrzf88aSaqWMgt%2F8Pa6Ycfb37uyZ90fKN3xDo2aWDIK7VEXFy6WFu8XU2yM%2F%2BpDRU%2BUTZ%2BFh%2FUw0LKjL0H%2Bfm0xmh5YXQwuv3SyQY6pgGEhiJJ6GUPI9tWt1t8%2BtcM%2F%2BySzvefZV51v6gvlI7zjPWbCKJmuoCQHSbl7u5bwcHb7CM6MlvoHLHfAlgN8HFYrfZ8P%2Bb41HhqcKR%2BVSwjTQie8KkGEXIAFnmVCbaciSGdl3kjLOGbwUVTv6PtDB84JAWbY9xjjdD7aRqycNT8z0hzoXCibNVNW1cJuEXsJLoqwnEg7S7oxqCHHGFyvmysl2o9aR6n&X-Amz-Signature=5f7a03f2131320a04d6877893a5d040e1592bd550eca2a28cc25690694f4f2aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L24BVUI%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzwyXF%2BIoZjzBvIhEr2QflYk55OLE21b1Nlj%2BC9s04WAiBFC8NWHMSKU44qiThqx1Dd42w8TbW9CuYBpzhom3bzFCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVNyLqLntuYe41AolKtwDq%2FDMQUA8MCyMi0CcYa4p3EeF5osm%2FLTeTqw2pgQRik9vZG0WS9lqcBxgunvQ2zdsNrzFFLhAT5NP3EycOsWIu8XeZZHMvTF6Flv78q33ppynFt%2BwgPRxfAKkyWiMhPslPDrfzQVPhJhPYflzixinRBl7Gm7rP8BPnDwV3%2Bf5s%2FEvnSJA6oBvrQOvORQYJQk1U5Bn5kYEU1qlQNzn7lRb87%2F8T8nu48o7hZYh64P7HB9TUrWBB82tPIpGmUTJMysKElxCKHRNW3jo0r3yv%2FTKVo8qaPgsekuBPexPBBfW6uXB%2BkrYrmPld3aCrZvefPkFqnGayKGU9rWULpWjx7tvzxv5Lp4U3Es0jpwEjaBVSPJEx0NQxsIi%2Fswu3BG%2BszNU0%2BV4ChgG8PrzWCIFu4Ht80NyKHqpp5jA9IQdV1ldDNW4VxJEcBWAGpKOOH%2FYHM5HFpfuxGc3lcFQGBHMh2Yt915A4jxsEb%2FAERqh1soHLqdAbN3XV%2FusNJ0h3sdXvSE40UfjfDDBp2g1AI22ziiLkISrceHcmZQrzf88aSaqWMgt%2F8Pa6Ycfb37uyZ90fKN3xDo2aWDIK7VEXFy6WFu8XU2yM%2F%2BpDRU%2BUTZ%2BFh%2FUw0LKjL0H%2Bfm0xmh5YXQwuv3SyQY6pgGEhiJJ6GUPI9tWt1t8%2BtcM%2F%2BySzvefZV51v6gvlI7zjPWbCKJmuoCQHSbl7u5bwcHb7CM6MlvoHLHfAlgN8HFYrfZ8P%2Bb41HhqcKR%2BVSwjTQie8KkGEXIAFnmVCbaciSGdl3kjLOGbwUVTv6PtDB84JAWbY9xjjdD7aRqycNT8z0hzoXCibNVNW1cJuEXsJLoqwnEg7S7oxqCHHGFyvmysl2o9aR6n&X-Amz-Signature=9f52f0573fe95db3d3ca687638c1b6c237464d16e6ac9a31cf7dac3805a86013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L24BVUI%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzwyXF%2BIoZjzBvIhEr2QflYk55OLE21b1Nlj%2BC9s04WAiBFC8NWHMSKU44qiThqx1Dd42w8TbW9CuYBpzhom3bzFCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVNyLqLntuYe41AolKtwDq%2FDMQUA8MCyMi0CcYa4p3EeF5osm%2FLTeTqw2pgQRik9vZG0WS9lqcBxgunvQ2zdsNrzFFLhAT5NP3EycOsWIu8XeZZHMvTF6Flv78q33ppynFt%2BwgPRxfAKkyWiMhPslPDrfzQVPhJhPYflzixinRBl7Gm7rP8BPnDwV3%2Bf5s%2FEvnSJA6oBvrQOvORQYJQk1U5Bn5kYEU1qlQNzn7lRb87%2F8T8nu48o7hZYh64P7HB9TUrWBB82tPIpGmUTJMysKElxCKHRNW3jo0r3yv%2FTKVo8qaPgsekuBPexPBBfW6uXB%2BkrYrmPld3aCrZvefPkFqnGayKGU9rWULpWjx7tvzxv5Lp4U3Es0jpwEjaBVSPJEx0NQxsIi%2Fswu3BG%2BszNU0%2BV4ChgG8PrzWCIFu4Ht80NyKHqpp5jA9IQdV1ldDNW4VxJEcBWAGpKOOH%2FYHM5HFpfuxGc3lcFQGBHMh2Yt915A4jxsEb%2FAERqh1soHLqdAbN3XV%2FusNJ0h3sdXvSE40UfjfDDBp2g1AI22ziiLkISrceHcmZQrzf88aSaqWMgt%2F8Pa6Ycfb37uyZ90fKN3xDo2aWDIK7VEXFy6WFu8XU2yM%2F%2BpDRU%2BUTZ%2BFh%2FUw0LKjL0H%2Bfm0xmh5YXQwuv3SyQY6pgGEhiJJ6GUPI9tWt1t8%2BtcM%2F%2BySzvefZV51v6gvlI7zjPWbCKJmuoCQHSbl7u5bwcHb7CM6MlvoHLHfAlgN8HFYrfZ8P%2Bb41HhqcKR%2BVSwjTQie8KkGEXIAFnmVCbaciSGdl3kjLOGbwUVTv6PtDB84JAWbY9xjjdD7aRqycNT8z0hzoXCibNVNW1cJuEXsJLoqwnEg7S7oxqCHHGFyvmysl2o9aR6n&X-Amz-Signature=6fc87a94718001fa0387fb70dfe41c65b7eef4c2ee67db02eed8c7fc6ed7fa8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

