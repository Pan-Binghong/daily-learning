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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676UPSTCQ%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2%2BrAYObOtp9GPIqkzft5t9yfHFr0a%2Bms%2FsLmnEfxdhAiB%2FOqCrlwl7Q0d4DzWXMvvZzMrDL1wbTkCgik%2Bj4RR0gyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMmOdqIFyVsD%2BeptsuKtwD7qrmPF3iTJZ89rTWVhdn3XEoVPVAKY0s78Cw2rAUuVSKI4yd%2By2sw1DbZKu5jrY%2FN%2FSmHrXMmR8lo0j0k8u57Z769vCP%2FyEinrvJMdG5xGY%2Fow2gfzvOtWvN%2B6s9KgXkEqkv7q%2FisF%2Bb3PGlKaWvRJaECm0pEb%2BtpFkUXEp0FrdzclZUElPiFIzkH64jpbDOe6zqN33bKOmteaWcsuorwOHubQMbtBpTCGy4kphqQNHCEOsU0IefE9nGEW5noTUTPhqty5RLnXf0mt2EreerFnYLJUiq1hxngOzlKCAvYb9KN4G7Dt0i9pkQlprtjQ1Umd%2BPj%2FuZgv1VbOWtyqQ%2FdHnYLb%2BSWMW3bcGtpWqpjbkThT%2FmpU%2BjOGhs6tlrI0kq2ByOZVum7WOvHucN2MLLUrdPDyXwpclKcPpvvUreTSZ0EVQMSozrmraYKajwq%2FhdE9MXWKdmafd%2BJaCngFTjw2ZVVOVrnBLjrbN%2Ba6dNPprsqsVBcXPbpnk7cL1aas4F%2FbNEkdYFdTEeCC0eM6gk8io6I2tmPLT%2BY7E45S1qiFPNlAXqwVKD%2F07WbaGaIjJh0l7Zq4C7AYdxRJP7rDxMNtOOWAc8A25N5SbgTepUuUjBwCGl4RHYM33moCYw8sDfyAY6pgFcqlze4dmbkLoDVuwJJOxN%2BHINFUa6K92HqLh1uZmOiwRqyBN5E%2BSHInkiW1CRsKdkGS2LIS99mcLe57aRDY0vOHNwrQaWd5pAn8xs%2FUTIfnxFT%2BA%2BBk8fqcgFUp0YgOnULD1ZU6xA40FcfWxZXY1fpQA52F8IraZrinnUMbepOUjbb4LEmivMOQDX%2FRvp1ou2NsbhiMOUIwhznVxy%2FqyYDGsi6XBY&X-Amz-Signature=e58a7abddaac2ffbd4cf347d3ca54d11d47a0337193639834c389ae087274973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676UPSTCQ%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2%2BrAYObOtp9GPIqkzft5t9yfHFr0a%2Bms%2FsLmnEfxdhAiB%2FOqCrlwl7Q0d4DzWXMvvZzMrDL1wbTkCgik%2Bj4RR0gyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMmOdqIFyVsD%2BeptsuKtwD7qrmPF3iTJZ89rTWVhdn3XEoVPVAKY0s78Cw2rAUuVSKI4yd%2By2sw1DbZKu5jrY%2FN%2FSmHrXMmR8lo0j0k8u57Z769vCP%2FyEinrvJMdG5xGY%2Fow2gfzvOtWvN%2B6s9KgXkEqkv7q%2FisF%2Bb3PGlKaWvRJaECm0pEb%2BtpFkUXEp0FrdzclZUElPiFIzkH64jpbDOe6zqN33bKOmteaWcsuorwOHubQMbtBpTCGy4kphqQNHCEOsU0IefE9nGEW5noTUTPhqty5RLnXf0mt2EreerFnYLJUiq1hxngOzlKCAvYb9KN4G7Dt0i9pkQlprtjQ1Umd%2BPj%2FuZgv1VbOWtyqQ%2FdHnYLb%2BSWMW3bcGtpWqpjbkThT%2FmpU%2BjOGhs6tlrI0kq2ByOZVum7WOvHucN2MLLUrdPDyXwpclKcPpvvUreTSZ0EVQMSozrmraYKajwq%2FhdE9MXWKdmafd%2BJaCngFTjw2ZVVOVrnBLjrbN%2Ba6dNPprsqsVBcXPbpnk7cL1aas4F%2FbNEkdYFdTEeCC0eM6gk8io6I2tmPLT%2BY7E45S1qiFPNlAXqwVKD%2F07WbaGaIjJh0l7Zq4C7AYdxRJP7rDxMNtOOWAc8A25N5SbgTepUuUjBwCGl4RHYM33moCYw8sDfyAY6pgFcqlze4dmbkLoDVuwJJOxN%2BHINFUa6K92HqLh1uZmOiwRqyBN5E%2BSHInkiW1CRsKdkGS2LIS99mcLe57aRDY0vOHNwrQaWd5pAn8xs%2FUTIfnxFT%2BA%2BBk8fqcgFUp0YgOnULD1ZU6xA40FcfWxZXY1fpQA52F8IraZrinnUMbepOUjbb4LEmivMOQDX%2FRvp1ou2NsbhiMOUIwhznVxy%2FqyYDGsi6XBY&X-Amz-Signature=c2c73b00b3f188c62cc5b87cb8a9b53ebb1fd7a3ccd3fd5898e7b33579f3f629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676UPSTCQ%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2%2BrAYObOtp9GPIqkzft5t9yfHFr0a%2Bms%2FsLmnEfxdhAiB%2FOqCrlwl7Q0d4DzWXMvvZzMrDL1wbTkCgik%2Bj4RR0gyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMmOdqIFyVsD%2BeptsuKtwD7qrmPF3iTJZ89rTWVhdn3XEoVPVAKY0s78Cw2rAUuVSKI4yd%2By2sw1DbZKu5jrY%2FN%2FSmHrXMmR8lo0j0k8u57Z769vCP%2FyEinrvJMdG5xGY%2Fow2gfzvOtWvN%2B6s9KgXkEqkv7q%2FisF%2Bb3PGlKaWvRJaECm0pEb%2BtpFkUXEp0FrdzclZUElPiFIzkH64jpbDOe6zqN33bKOmteaWcsuorwOHubQMbtBpTCGy4kphqQNHCEOsU0IefE9nGEW5noTUTPhqty5RLnXf0mt2EreerFnYLJUiq1hxngOzlKCAvYb9KN4G7Dt0i9pkQlprtjQ1Umd%2BPj%2FuZgv1VbOWtyqQ%2FdHnYLb%2BSWMW3bcGtpWqpjbkThT%2FmpU%2BjOGhs6tlrI0kq2ByOZVum7WOvHucN2MLLUrdPDyXwpclKcPpvvUreTSZ0EVQMSozrmraYKajwq%2FhdE9MXWKdmafd%2BJaCngFTjw2ZVVOVrnBLjrbN%2Ba6dNPprsqsVBcXPbpnk7cL1aas4F%2FbNEkdYFdTEeCC0eM6gk8io6I2tmPLT%2BY7E45S1qiFPNlAXqwVKD%2F07WbaGaIjJh0l7Zq4C7AYdxRJP7rDxMNtOOWAc8A25N5SbgTepUuUjBwCGl4RHYM33moCYw8sDfyAY6pgFcqlze4dmbkLoDVuwJJOxN%2BHINFUa6K92HqLh1uZmOiwRqyBN5E%2BSHInkiW1CRsKdkGS2LIS99mcLe57aRDY0vOHNwrQaWd5pAn8xs%2FUTIfnxFT%2BA%2BBk8fqcgFUp0YgOnULD1ZU6xA40FcfWxZXY1fpQA52F8IraZrinnUMbepOUjbb4LEmivMOQDX%2FRvp1ou2NsbhiMOUIwhznVxy%2FqyYDGsi6XBY&X-Amz-Signature=c6f2116f0528381c7834f7980240cc66667c559000dcf687ad7080790e8e28c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

