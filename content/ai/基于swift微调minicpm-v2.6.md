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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFGEK3R%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGtIJ4MNYZfD%2BiM8mGVsRUxD21SwFI%2BuZefkATqWGaYsAiAT5x4q15miQXl4k08dA1uIp9RIT2PoKGdAv0NicGqPlyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgFl6G2%2FutiXWD2XLKtwDtq1lg8Lz6VbydiZRxT8Gyu2SX9d9xZGgrazobEsc54pU1wA5QJyQZTt16iCeQTb5Mgg10EBkvOzRmHvLt2l0Jdhy36rpacaDr0muY3ZIB%2BS1rywQwJlEMwN8VXcY%2FK9acEVppO56wgF%2BNs60jVgzBF7w4YU7y1Z6FyUvr7qX64yvPjzbV%2BJJgvjylgJxB0Ts2GV8%2BnE9sR95ZbW%2BCpO7mxr7wXdKniflYdS85ET%2Bk4SovkRwKxwHZxDu7QbteiKKZPF5pjLIj8JrxME9BBcJdGT8lilbClPCVuH7FRIzhN%2FziPZZCKLc7kMlOwBlkeoloeN9k5zKqRjLERJjKDUF2qtI%2FSrHe2Y%2Fw%2B2ocdBjsz5crFLjZ5ghsJ7Ri9tC6Oq3jPVAHENTOA7My5WQWaAmtgPt%2Bs%2BLUXe0kmPveLBaG9Nth%2BKfes7%2BxRyNRhVWrhSXgVhTxC0oTacncRJItr4aQ0faHKLNVRIZK8rwlqgAht3msQTQEHMozW9%2FC5ob29HURYg8bJgFV7kHP94H%2FzNbBgYGfIRQxbl38qNTQQ0a%2FDV05U%2Fy4oRD9frlxTtGi4NJ3Gqsu%2FDP%2Bv3qBMc6qcTmGq4Y3zW3L2KaU4anf20eJWNKPEvsYqgdjz6dvi4wyJG1zAY6pgGN8o%2B6%2FyObwx8Vzb8ugnn2X9AbtPU78IZVBVj3hXMPCWw9hGQHb1ehcXAw9w0stKjir8QD04qQXNmJ1OQdnK%2BWTRgzxBBh8U5ImHnzsjxL%2B3nGcB6PLXdJGOwV6qZcIJEOYCjdcl1k9eQcSf36ywI0vcTH7Dn9CWRU3lnktUgPhqY0%2FuqzhUCKjXEsgieoznO49ece2pE1ir0xUsuIa20PjBICy%2Bvf&X-Amz-Signature=f31a3ae6ae3a91dbbdff92664c6e2135aa749bea28a5865018cebecabc26018d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFGEK3R%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGtIJ4MNYZfD%2BiM8mGVsRUxD21SwFI%2BuZefkATqWGaYsAiAT5x4q15miQXl4k08dA1uIp9RIT2PoKGdAv0NicGqPlyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgFl6G2%2FutiXWD2XLKtwDtq1lg8Lz6VbydiZRxT8Gyu2SX9d9xZGgrazobEsc54pU1wA5QJyQZTt16iCeQTb5Mgg10EBkvOzRmHvLt2l0Jdhy36rpacaDr0muY3ZIB%2BS1rywQwJlEMwN8VXcY%2FK9acEVppO56wgF%2BNs60jVgzBF7w4YU7y1Z6FyUvr7qX64yvPjzbV%2BJJgvjylgJxB0Ts2GV8%2BnE9sR95ZbW%2BCpO7mxr7wXdKniflYdS85ET%2Bk4SovkRwKxwHZxDu7QbteiKKZPF5pjLIj8JrxME9BBcJdGT8lilbClPCVuH7FRIzhN%2FziPZZCKLc7kMlOwBlkeoloeN9k5zKqRjLERJjKDUF2qtI%2FSrHe2Y%2Fw%2B2ocdBjsz5crFLjZ5ghsJ7Ri9tC6Oq3jPVAHENTOA7My5WQWaAmtgPt%2Bs%2BLUXe0kmPveLBaG9Nth%2BKfes7%2BxRyNRhVWrhSXgVhTxC0oTacncRJItr4aQ0faHKLNVRIZK8rwlqgAht3msQTQEHMozW9%2FC5ob29HURYg8bJgFV7kHP94H%2FzNbBgYGfIRQxbl38qNTQQ0a%2FDV05U%2Fy4oRD9frlxTtGi4NJ3Gqsu%2FDP%2Bv3qBMc6qcTmGq4Y3zW3L2KaU4anf20eJWNKPEvsYqgdjz6dvi4wyJG1zAY6pgGN8o%2B6%2FyObwx8Vzb8ugnn2X9AbtPU78IZVBVj3hXMPCWw9hGQHb1ehcXAw9w0stKjir8QD04qQXNmJ1OQdnK%2BWTRgzxBBh8U5ImHnzsjxL%2B3nGcB6PLXdJGOwV6qZcIJEOYCjdcl1k9eQcSf36ywI0vcTH7Dn9CWRU3lnktUgPhqY0%2FuqzhUCKjXEsgieoznO49ece2pE1ir0xUsuIa20PjBICy%2Bvf&X-Amz-Signature=139dddc37f5863a4cb0bba13792dbeea4584a10697c650c9d96a6554e3ef8383&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFGEK3R%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGtIJ4MNYZfD%2BiM8mGVsRUxD21SwFI%2BuZefkATqWGaYsAiAT5x4q15miQXl4k08dA1uIp9RIT2PoKGdAv0NicGqPlyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgFl6G2%2FutiXWD2XLKtwDtq1lg8Lz6VbydiZRxT8Gyu2SX9d9xZGgrazobEsc54pU1wA5QJyQZTt16iCeQTb5Mgg10EBkvOzRmHvLt2l0Jdhy36rpacaDr0muY3ZIB%2BS1rywQwJlEMwN8VXcY%2FK9acEVppO56wgF%2BNs60jVgzBF7w4YU7y1Z6FyUvr7qX64yvPjzbV%2BJJgvjylgJxB0Ts2GV8%2BnE9sR95ZbW%2BCpO7mxr7wXdKniflYdS85ET%2Bk4SovkRwKxwHZxDu7QbteiKKZPF5pjLIj8JrxME9BBcJdGT8lilbClPCVuH7FRIzhN%2FziPZZCKLc7kMlOwBlkeoloeN9k5zKqRjLERJjKDUF2qtI%2FSrHe2Y%2Fw%2B2ocdBjsz5crFLjZ5ghsJ7Ri9tC6Oq3jPVAHENTOA7My5WQWaAmtgPt%2Bs%2BLUXe0kmPveLBaG9Nth%2BKfes7%2BxRyNRhVWrhSXgVhTxC0oTacncRJItr4aQ0faHKLNVRIZK8rwlqgAht3msQTQEHMozW9%2FC5ob29HURYg8bJgFV7kHP94H%2FzNbBgYGfIRQxbl38qNTQQ0a%2FDV05U%2Fy4oRD9frlxTtGi4NJ3Gqsu%2FDP%2Bv3qBMc6qcTmGq4Y3zW3L2KaU4anf20eJWNKPEvsYqgdjz6dvi4wyJG1zAY6pgGN8o%2B6%2FyObwx8Vzb8ugnn2X9AbtPU78IZVBVj3hXMPCWw9hGQHb1ehcXAw9w0stKjir8QD04qQXNmJ1OQdnK%2BWTRgzxBBh8U5ImHnzsjxL%2B3nGcB6PLXdJGOwV6qZcIJEOYCjdcl1k9eQcSf36ywI0vcTH7Dn9CWRU3lnktUgPhqY0%2FuqzhUCKjXEsgieoznO49ece2pE1ir0xUsuIa20PjBICy%2Bvf&X-Amz-Signature=c8deb784ef3d3c318c83b3ef348ac94834f6707677d0c5cb8c1bc0b83fdecbef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

