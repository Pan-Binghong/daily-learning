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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OQB6VTL%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAVL%2BPOtdYqRJpfWZtPaWprkfwsO7n%2B54hmeX6ZPNT2VAiBISYDf%2F%2F5d2Ih0at1Z%2FkcGBcEe9Yz9pggV1SnjVU749SqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQFkuVYb8ABKVeYLnKtwDDMDOYVepjNk5tm0nV%2FgMlgsTpzHKhRXAt2Rrs4CXWHEVxJcGykQ23%2F9GTPw4Q9gbmYuPBThtQYy3LiHAC%2BLuAmV8JPrx0TwD%2Fk2PQ3%2FuALD364pENGUIvqe%2BbFIVP2vtXXPuIBLjf%2BhXt7p6pCczWD5F%2BLVM7l57lCHRSNEXoiuOs9%2BANiJWX0YaV5BSB4H6MBeuqDolylZmKDTl2QCTdT9rKzORXluvPoeclgzx6MxljtLjmLacFVrqZYLJvvyBGZIQkP8ZQ%2Fj2i3xR4KlfgUQf6tvn19VdR98d4U9WLUzkcdDAIpskS5RDypbw73sZpWp03otNoXN7Kq7SAnabm%2F5rBeYoc5o6rEbnAjLLeXHoZ9gK82%2FkhoqrpHiUwPLUpe6JFGdzYE4OdL9ShfHCq5RoSV28rgWdNkKYy6WWVukDXwfSP1%2Br2d5w4TVMXwOliILQNMzxQLUsabzWwBgk%2B05aBzvoy%2BszUhg7VHgWv7B9bBaoDw68Q1jBL6LCV3h7PgqzqGyu7QsN72wz3gVxcc7xtPFzHw%2FQLNtbBgwNLhSwEd%2BZsyJURx519NqmI658SA6RuUkW3BgEfocRbTV2fvudm4b0wZkThwR8er9ALB4yDmOoFTsUC6EC9%2Bswg%2FbRzgY6pgHBGetLqMreD51%2FEbNbrhz%2F1kikL5IXy0dwdXvWtzeEc43GyCAKDhs83ovpXcIal9d%2Be062IfeOWTnkqgA0XJFhHZ8iTskgCXKpELvwuYnsJHBC086GEcPfSchXTawQ9ApnFPGJRkQaAMFyqntsJEDILeGpe0LVcQr%2BIUbXERB2iY4fL%2BVrzJvjigS2pntliXn1%2F5Vrc5PRt7TEH6PT%2Bhv7TQOoNwFK&X-Amz-Signature=4b803917bf4264f434bd60e90c3a2c14fcdc013b120340ded06c08c98a176751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OQB6VTL%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAVL%2BPOtdYqRJpfWZtPaWprkfwsO7n%2B54hmeX6ZPNT2VAiBISYDf%2F%2F5d2Ih0at1Z%2FkcGBcEe9Yz9pggV1SnjVU749SqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQFkuVYb8ABKVeYLnKtwDDMDOYVepjNk5tm0nV%2FgMlgsTpzHKhRXAt2Rrs4CXWHEVxJcGykQ23%2F9GTPw4Q9gbmYuPBThtQYy3LiHAC%2BLuAmV8JPrx0TwD%2Fk2PQ3%2FuALD364pENGUIvqe%2BbFIVP2vtXXPuIBLjf%2BhXt7p6pCczWD5F%2BLVM7l57lCHRSNEXoiuOs9%2BANiJWX0YaV5BSB4H6MBeuqDolylZmKDTl2QCTdT9rKzORXluvPoeclgzx6MxljtLjmLacFVrqZYLJvvyBGZIQkP8ZQ%2Fj2i3xR4KlfgUQf6tvn19VdR98d4U9WLUzkcdDAIpskS5RDypbw73sZpWp03otNoXN7Kq7SAnabm%2F5rBeYoc5o6rEbnAjLLeXHoZ9gK82%2FkhoqrpHiUwPLUpe6JFGdzYE4OdL9ShfHCq5RoSV28rgWdNkKYy6WWVukDXwfSP1%2Br2d5w4TVMXwOliILQNMzxQLUsabzWwBgk%2B05aBzvoy%2BszUhg7VHgWv7B9bBaoDw68Q1jBL6LCV3h7PgqzqGyu7QsN72wz3gVxcc7xtPFzHw%2FQLNtbBgwNLhSwEd%2BZsyJURx519NqmI658SA6RuUkW3BgEfocRbTV2fvudm4b0wZkThwR8er9ALB4yDmOoFTsUC6EC9%2Bswg%2FbRzgY6pgHBGetLqMreD51%2FEbNbrhz%2F1kikL5IXy0dwdXvWtzeEc43GyCAKDhs83ovpXcIal9d%2Be062IfeOWTnkqgA0XJFhHZ8iTskgCXKpELvwuYnsJHBC086GEcPfSchXTawQ9ApnFPGJRkQaAMFyqntsJEDILeGpe0LVcQr%2BIUbXERB2iY4fL%2BVrzJvjigS2pntliXn1%2F5Vrc5PRt7TEH6PT%2Bhv7TQOoNwFK&X-Amz-Signature=393999f2179c994bcac8440feda3a051e97832b4bd4dbf37ad6fd2987abac60e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OQB6VTL%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAVL%2BPOtdYqRJpfWZtPaWprkfwsO7n%2B54hmeX6ZPNT2VAiBISYDf%2F%2F5d2Ih0at1Z%2FkcGBcEe9Yz9pggV1SnjVU749SqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQFkuVYb8ABKVeYLnKtwDDMDOYVepjNk5tm0nV%2FgMlgsTpzHKhRXAt2Rrs4CXWHEVxJcGykQ23%2F9GTPw4Q9gbmYuPBThtQYy3LiHAC%2BLuAmV8JPrx0TwD%2Fk2PQ3%2FuALD364pENGUIvqe%2BbFIVP2vtXXPuIBLjf%2BhXt7p6pCczWD5F%2BLVM7l57lCHRSNEXoiuOs9%2BANiJWX0YaV5BSB4H6MBeuqDolylZmKDTl2QCTdT9rKzORXluvPoeclgzx6MxljtLjmLacFVrqZYLJvvyBGZIQkP8ZQ%2Fj2i3xR4KlfgUQf6tvn19VdR98d4U9WLUzkcdDAIpskS5RDypbw73sZpWp03otNoXN7Kq7SAnabm%2F5rBeYoc5o6rEbnAjLLeXHoZ9gK82%2FkhoqrpHiUwPLUpe6JFGdzYE4OdL9ShfHCq5RoSV28rgWdNkKYy6WWVukDXwfSP1%2Br2d5w4TVMXwOliILQNMzxQLUsabzWwBgk%2B05aBzvoy%2BszUhg7VHgWv7B9bBaoDw68Q1jBL6LCV3h7PgqzqGyu7QsN72wz3gVxcc7xtPFzHw%2FQLNtbBgwNLhSwEd%2BZsyJURx519NqmI658SA6RuUkW3BgEfocRbTV2fvudm4b0wZkThwR8er9ALB4yDmOoFTsUC6EC9%2Bswg%2FbRzgY6pgHBGetLqMreD51%2FEbNbrhz%2F1kikL5IXy0dwdXvWtzeEc43GyCAKDhs83ovpXcIal9d%2Be062IfeOWTnkqgA0XJFhHZ8iTskgCXKpELvwuYnsJHBC086GEcPfSchXTawQ9ApnFPGJRkQaAMFyqntsJEDILeGpe0LVcQr%2BIUbXERB2iY4fL%2BVrzJvjigS2pntliXn1%2F5Vrc5PRt7TEH6PT%2Bhv7TQOoNwFK&X-Amz-Signature=3a33f7cbb0190c929bb6e91e99ebaf4fccfb3c65a54b84588744344af33cfb07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

