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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5S7TUJ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FqxREi3TA4ptli3KQajBGd%2BDHpXb5lMaluCboirNv%2FAiEAzwn%2BynEKlprmBFn8LUGjjg3Y75EBT3kZxwMejKLKQ6gqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYr0hxFI0lHCKMNRSrcA8fdryp%2BDTl1%2BxUr59hV3pdd3nagRJbBAOl0xqPzi2sD145t2r6fBjOb4XbUHY1d7qREk8rXVK6p4JGLNdDsdXmjj220MrgUVLNQtuDOvBUlLa0eAtD4pEi4YL%2FCY9b0KLMdAyDbQ5dEpNI%2Btk9uEXw%2BCDOXuLUS0NRiq7dmKmy3Q2arbQp7QZz23GbAfxNUK5muDRUEYx10SaQSnIwSdoTYtoF8wvLpjVcEOdAxDINlb%2B80eqN%2FI7TNaXhea0H90HUWQ1aew6xbUNpgikeWNKzYXtbzHNtAkawtI6eqgE8awh%2FzP8EW3NzwgmxmY2PSz%2FQKR8xdZedFyf%2B8EmapYyK6rBQH%2FTMG%2FUkwFZG%2BSj0FbJJiOf0UJfJZozWJJ%2B%2FYK0BcBDiC%2BMtz9b8b1fF2un6Ve8mekWYg9khooEsy4i%2BYOV1iSONqRyjx9R1rCYezGwXSGg6pYfnrQ7ds71f1J09VlpRi0lkRSqAQMR1XAwKNp14vKhIPdSb2q42ag4UJFsmeMmjYyNVHjlnaDX%2BBMF9UYDIDToBr0XCLdOm%2Fn7B3p7ONpIrykNTPietCNKT%2BveQFySxaOqKHbh%2FREtKzVFcWAhmSmnmEvbEOf8rvRm6EO03Ve3ZaJw0Uj16KMKeR38wGOqUBKpUX5ZvDgGbGC2aB8%2FpyjSgr8GWQtWIF5SBYbAZ9LYmN%2B6UdQLkdrIPDX4YKsQ9e0xreAyz8KIRPKfL7yMvOsbcYe31CKQ7KeZ9AGFJUcedYiD8sD4cOBxQp5y71gopwJTQq2kOUeanj%2BJNbCQTBSku5uZlZblmBw%2FErJUEky37vJmZIj05t0znlAxV4pWEl%2B1SWB7VbMSg5fhOIC7GTULLE8HJW&X-Amz-Signature=aa24f9585e777b234d9f02b88fa8bf16ae89bd83f1304e4eef10e753d2385fcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5S7TUJ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FqxREi3TA4ptli3KQajBGd%2BDHpXb5lMaluCboirNv%2FAiEAzwn%2BynEKlprmBFn8LUGjjg3Y75EBT3kZxwMejKLKQ6gqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYr0hxFI0lHCKMNRSrcA8fdryp%2BDTl1%2BxUr59hV3pdd3nagRJbBAOl0xqPzi2sD145t2r6fBjOb4XbUHY1d7qREk8rXVK6p4JGLNdDsdXmjj220MrgUVLNQtuDOvBUlLa0eAtD4pEi4YL%2FCY9b0KLMdAyDbQ5dEpNI%2Btk9uEXw%2BCDOXuLUS0NRiq7dmKmy3Q2arbQp7QZz23GbAfxNUK5muDRUEYx10SaQSnIwSdoTYtoF8wvLpjVcEOdAxDINlb%2B80eqN%2FI7TNaXhea0H90HUWQ1aew6xbUNpgikeWNKzYXtbzHNtAkawtI6eqgE8awh%2FzP8EW3NzwgmxmY2PSz%2FQKR8xdZedFyf%2B8EmapYyK6rBQH%2FTMG%2FUkwFZG%2BSj0FbJJiOf0UJfJZozWJJ%2B%2FYK0BcBDiC%2BMtz9b8b1fF2un6Ve8mekWYg9khooEsy4i%2BYOV1iSONqRyjx9R1rCYezGwXSGg6pYfnrQ7ds71f1J09VlpRi0lkRSqAQMR1XAwKNp14vKhIPdSb2q42ag4UJFsmeMmjYyNVHjlnaDX%2BBMF9UYDIDToBr0XCLdOm%2Fn7B3p7ONpIrykNTPietCNKT%2BveQFySxaOqKHbh%2FREtKzVFcWAhmSmnmEvbEOf8rvRm6EO03Ve3ZaJw0Uj16KMKeR38wGOqUBKpUX5ZvDgGbGC2aB8%2FpyjSgr8GWQtWIF5SBYbAZ9LYmN%2B6UdQLkdrIPDX4YKsQ9e0xreAyz8KIRPKfL7yMvOsbcYe31CKQ7KeZ9AGFJUcedYiD8sD4cOBxQp5y71gopwJTQq2kOUeanj%2BJNbCQTBSku5uZlZblmBw%2FErJUEky37vJmZIj05t0znlAxV4pWEl%2B1SWB7VbMSg5fhOIC7GTULLE8HJW&X-Amz-Signature=6b2313b36c788a2291668d3e053fe1bb0f151182b56583300022062c47c968c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5S7TUJ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FqxREi3TA4ptli3KQajBGd%2BDHpXb5lMaluCboirNv%2FAiEAzwn%2BynEKlprmBFn8LUGjjg3Y75EBT3kZxwMejKLKQ6gqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYr0hxFI0lHCKMNRSrcA8fdryp%2BDTl1%2BxUr59hV3pdd3nagRJbBAOl0xqPzi2sD145t2r6fBjOb4XbUHY1d7qREk8rXVK6p4JGLNdDsdXmjj220MrgUVLNQtuDOvBUlLa0eAtD4pEi4YL%2FCY9b0KLMdAyDbQ5dEpNI%2Btk9uEXw%2BCDOXuLUS0NRiq7dmKmy3Q2arbQp7QZz23GbAfxNUK5muDRUEYx10SaQSnIwSdoTYtoF8wvLpjVcEOdAxDINlb%2B80eqN%2FI7TNaXhea0H90HUWQ1aew6xbUNpgikeWNKzYXtbzHNtAkawtI6eqgE8awh%2FzP8EW3NzwgmxmY2PSz%2FQKR8xdZedFyf%2B8EmapYyK6rBQH%2FTMG%2FUkwFZG%2BSj0FbJJiOf0UJfJZozWJJ%2B%2FYK0BcBDiC%2BMtz9b8b1fF2un6Ve8mekWYg9khooEsy4i%2BYOV1iSONqRyjx9R1rCYezGwXSGg6pYfnrQ7ds71f1J09VlpRi0lkRSqAQMR1XAwKNp14vKhIPdSb2q42ag4UJFsmeMmjYyNVHjlnaDX%2BBMF9UYDIDToBr0XCLdOm%2Fn7B3p7ONpIrykNTPietCNKT%2BveQFySxaOqKHbh%2FREtKzVFcWAhmSmnmEvbEOf8rvRm6EO03Ve3ZaJw0Uj16KMKeR38wGOqUBKpUX5ZvDgGbGC2aB8%2FpyjSgr8GWQtWIF5SBYbAZ9LYmN%2B6UdQLkdrIPDX4YKsQ9e0xreAyz8KIRPKfL7yMvOsbcYe31CKQ7KeZ9AGFJUcedYiD8sD4cOBxQp5y71gopwJTQq2kOUeanj%2BJNbCQTBSku5uZlZblmBw%2FErJUEky37vJmZIj05t0znlAxV4pWEl%2B1SWB7VbMSg5fhOIC7GTULLE8HJW&X-Amz-Signature=d2d5edb7f72d13e21892da54a3fc6d34928ee6704d7bcdd4f1b6b4f1cc15ab60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

