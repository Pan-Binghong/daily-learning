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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLFWQZJ2%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZ9ETdw1zIo0JNM%2Bz5IgmGchR8fNbo8Q2M%2Bjdg0PFWKAiADbmYg5dVadPHr45gQodbe8gmWW7e9JimPtoz2p8VUSiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdOE618f%2FT%2FAmHAP2KtwDKyYlikMFmwve74rszcT64TGmfMz0vPyt4a%2FRpl%2FjN8v0Z%2Bxm48v%2BRIXgGoZCVrPiSaL08O4k9xKHNY1wFNK6K9HljW%2FIoygn6AHQT1jCFm%2BucWkSVUSSj0tImjtMBq2x7zSscUDZyyetUhtJLC0p5bJoMKfz8B4mT%2FFqvS9Cgq81GN3SnUjhuu7QJvfELgXR%2FQkz0gCFaC0Ta2QtHKF%2B7t5tVXyBxpvg2TEND4Y2CaIxnEu%2Fxx8jBfucYBnXbRiqSsCboQBVmKr278iQUttMSamdsT9l9dcNT67qU2NzpMxdtQ5KYdCqnEwEhjfyAC%2Bd8hZZt3VrXB%2BQfVvj4ZG59t0jPdoc5rr7tWl%2FfblVqhrIVWbdoOa6%2FUzhCUnECMlGvkm8UBth59Kcd4dfxdKdFoAsFssJnMsk52rMbMaZVDoBs0K1uA2v6dCJ2WQGwmEiZ1GTYBsoPTkcOlQQl99B54S48ey5az3tpxGmrM50uU0V1r1vZDg9h7Nw6PbzNhuptMhrZYQSJIAwISbDpxb7RcW5J2sE2hOoUwYAn5kc3yWx7hDs1%2BOtOcDDUn3AbCORYjcOelsXaHjTThRpHJ2wv5bQBhaRL03E7kMkemiekccuuyOJxvREm70eJxMwoZnvyAY6pgG5VGB8k7CQNxZsuG9RNi6VqIcqvQBTLmWPpfYoocSP3ChOFm5JGC4SYPX5E3t32rQuzI9x9mZPx5BYFu1JmB7QgsqKgV8TTkD%2F1ZpinehQH64eUO7AWZBH56cNKuFd87W4JsIC3gPfZlkF%2FAUgsX2SlNAnwVYX0wHmoCy3VTwn2H92l78x9aSu5iRAuLna%2BPurHrPzBg5ehhoPrJGDrXF9cWdEXZSs&X-Amz-Signature=e201e1f86381b75944e0b43b217032b66e956998157c94fb76255409af09b8f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLFWQZJ2%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZ9ETdw1zIo0JNM%2Bz5IgmGchR8fNbo8Q2M%2Bjdg0PFWKAiADbmYg5dVadPHr45gQodbe8gmWW7e9JimPtoz2p8VUSiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdOE618f%2FT%2FAmHAP2KtwDKyYlikMFmwve74rszcT64TGmfMz0vPyt4a%2FRpl%2FjN8v0Z%2Bxm48v%2BRIXgGoZCVrPiSaL08O4k9xKHNY1wFNK6K9HljW%2FIoygn6AHQT1jCFm%2BucWkSVUSSj0tImjtMBq2x7zSscUDZyyetUhtJLC0p5bJoMKfz8B4mT%2FFqvS9Cgq81GN3SnUjhuu7QJvfELgXR%2FQkz0gCFaC0Ta2QtHKF%2B7t5tVXyBxpvg2TEND4Y2CaIxnEu%2Fxx8jBfucYBnXbRiqSsCboQBVmKr278iQUttMSamdsT9l9dcNT67qU2NzpMxdtQ5KYdCqnEwEhjfyAC%2Bd8hZZt3VrXB%2BQfVvj4ZG59t0jPdoc5rr7tWl%2FfblVqhrIVWbdoOa6%2FUzhCUnECMlGvkm8UBth59Kcd4dfxdKdFoAsFssJnMsk52rMbMaZVDoBs0K1uA2v6dCJ2WQGwmEiZ1GTYBsoPTkcOlQQl99B54S48ey5az3tpxGmrM50uU0V1r1vZDg9h7Nw6PbzNhuptMhrZYQSJIAwISbDpxb7RcW5J2sE2hOoUwYAn5kc3yWx7hDs1%2BOtOcDDUn3AbCORYjcOelsXaHjTThRpHJ2wv5bQBhaRL03E7kMkemiekccuuyOJxvREm70eJxMwoZnvyAY6pgG5VGB8k7CQNxZsuG9RNi6VqIcqvQBTLmWPpfYoocSP3ChOFm5JGC4SYPX5E3t32rQuzI9x9mZPx5BYFu1JmB7QgsqKgV8TTkD%2F1ZpinehQH64eUO7AWZBH56cNKuFd87W4JsIC3gPfZlkF%2FAUgsX2SlNAnwVYX0wHmoCy3VTwn2H92l78x9aSu5iRAuLna%2BPurHrPzBg5ehhoPrJGDrXF9cWdEXZSs&X-Amz-Signature=dab72f0a58640e216e4849d4ed3600eb209f19e5fec747ba389cf1b5e3018cd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLFWQZJ2%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZ9ETdw1zIo0JNM%2Bz5IgmGchR8fNbo8Q2M%2Bjdg0PFWKAiADbmYg5dVadPHr45gQodbe8gmWW7e9JimPtoz2p8VUSiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdOE618f%2FT%2FAmHAP2KtwDKyYlikMFmwve74rszcT64TGmfMz0vPyt4a%2FRpl%2FjN8v0Z%2Bxm48v%2BRIXgGoZCVrPiSaL08O4k9xKHNY1wFNK6K9HljW%2FIoygn6AHQT1jCFm%2BucWkSVUSSj0tImjtMBq2x7zSscUDZyyetUhtJLC0p5bJoMKfz8B4mT%2FFqvS9Cgq81GN3SnUjhuu7QJvfELgXR%2FQkz0gCFaC0Ta2QtHKF%2B7t5tVXyBxpvg2TEND4Y2CaIxnEu%2Fxx8jBfucYBnXbRiqSsCboQBVmKr278iQUttMSamdsT9l9dcNT67qU2NzpMxdtQ5KYdCqnEwEhjfyAC%2Bd8hZZt3VrXB%2BQfVvj4ZG59t0jPdoc5rr7tWl%2FfblVqhrIVWbdoOa6%2FUzhCUnECMlGvkm8UBth59Kcd4dfxdKdFoAsFssJnMsk52rMbMaZVDoBs0K1uA2v6dCJ2WQGwmEiZ1GTYBsoPTkcOlQQl99B54S48ey5az3tpxGmrM50uU0V1r1vZDg9h7Nw6PbzNhuptMhrZYQSJIAwISbDpxb7RcW5J2sE2hOoUwYAn5kc3yWx7hDs1%2BOtOcDDUn3AbCORYjcOelsXaHjTThRpHJ2wv5bQBhaRL03E7kMkemiekccuuyOJxvREm70eJxMwoZnvyAY6pgG5VGB8k7CQNxZsuG9RNi6VqIcqvQBTLmWPpfYoocSP3ChOFm5JGC4SYPX5E3t32rQuzI9x9mZPx5BYFu1JmB7QgsqKgV8TTkD%2F1ZpinehQH64eUO7AWZBH56cNKuFd87W4JsIC3gPfZlkF%2FAUgsX2SlNAnwVYX0wHmoCy3VTwn2H92l78x9aSu5iRAuLna%2BPurHrPzBg5ehhoPrJGDrXF9cWdEXZSs&X-Amz-Signature=427c4cf9a69f31a12515b0d00a1c56c6c64ccef5a512959d772dd702ac6e0e6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

