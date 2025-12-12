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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSODHPW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCet9GZk%2BviRlTVtySKu9gqmJi0%2Bv%2Bsxh18BAtL6Bf2HgIhANZ8Yb%2F0isADtTK8CnFsYH0vL6EuIGBKqbSFbxsDH0I%2BKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw94uWVoKpIGzIlnnMq3APZgwUSo%2FwtHmGTVjfT%2B9IXP4LhV3twzQHp1oojklS61120VOKf3NecG3WIQxnjvZtdzv8p61is2lQzRiXFutYQ4EOCH2P%2BQazKjl%2BqjACoop%2B4CbHxRXxlX5IXg329BQoFMO5N%2By4diNcOZ6bRXkRFNPsWMwmXtePdm1NepntS4qhbEWW65TPvjZ9yuFOnEM9OU9VM51RXIo0NeOGj%2BlFshzaobf%2BC3OJaY6uFZTIPq%2FFWYcOtgsuXFhIh%2FvHp%2F6PwKBJ%2BNipCkgIUaMjSz8jd9GcwIwkY6%2FDQzxGJu9vXU0QBDGnPT04POuzAkr0w2sXrd0aqHJnQzng6NqI7z7J4EsookwMbkHyCc9ln8bya%2Fo9ISKYwYZs%2F6H1ZpyrS9Ujts2aRHARZCxbCSBNVcz%2BVybtD2NlQE8cEADV48gWRAaMi1skJ1mJax%2FrCq7FHmrDnu48WAttznulCfQiV9m%2B2IkoQgVnVjyi%2FKTlcjkzyX3FQ5AEi7v0eOXoc3k8YORJy5MqzhrOzxdUFucy1ZgCI0NLrOpsaSm38XnwUOUT%2BycTjN9aCytsWWmq1O%2BcsrkOicVUMS95ebXc9B9zze1qShHDWDjUBLg2UmRPxXsvx35ZJwpbEQETz9x7CqTCL1e3JBjqkAb7CcosE6f2zWRTPIBTln1FMOPNn%2BIfGzu4K1x%2BxKqUoz0gOH1GWnpci1Av7vahCfSclwpwswzNtsmELVUCEMbB0XZNygyM6YMrblLd3ArbeWCvUtHRJGjnURkTZRnAUJ9NYHl8jmHQbaXPwUmDVkW%2Bfwmax9R5AOtGySWkBb%2BK5hN5AXeuxHB1K56MXPe91bGTLzf71thM2J0JVbDz%2FXtnj1JV2&X-Amz-Signature=fcde6e8ffeba280948d23435ca4b95308cbef7a956a0e124b723adabea2e0ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSODHPW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCet9GZk%2BviRlTVtySKu9gqmJi0%2Bv%2Bsxh18BAtL6Bf2HgIhANZ8Yb%2F0isADtTK8CnFsYH0vL6EuIGBKqbSFbxsDH0I%2BKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw94uWVoKpIGzIlnnMq3APZgwUSo%2FwtHmGTVjfT%2B9IXP4LhV3twzQHp1oojklS61120VOKf3NecG3WIQxnjvZtdzv8p61is2lQzRiXFutYQ4EOCH2P%2BQazKjl%2BqjACoop%2B4CbHxRXxlX5IXg329BQoFMO5N%2By4diNcOZ6bRXkRFNPsWMwmXtePdm1NepntS4qhbEWW65TPvjZ9yuFOnEM9OU9VM51RXIo0NeOGj%2BlFshzaobf%2BC3OJaY6uFZTIPq%2FFWYcOtgsuXFhIh%2FvHp%2F6PwKBJ%2BNipCkgIUaMjSz8jd9GcwIwkY6%2FDQzxGJu9vXU0QBDGnPT04POuzAkr0w2sXrd0aqHJnQzng6NqI7z7J4EsookwMbkHyCc9ln8bya%2Fo9ISKYwYZs%2F6H1ZpyrS9Ujts2aRHARZCxbCSBNVcz%2BVybtD2NlQE8cEADV48gWRAaMi1skJ1mJax%2FrCq7FHmrDnu48WAttznulCfQiV9m%2B2IkoQgVnVjyi%2FKTlcjkzyX3FQ5AEi7v0eOXoc3k8YORJy5MqzhrOzxdUFucy1ZgCI0NLrOpsaSm38XnwUOUT%2BycTjN9aCytsWWmq1O%2BcsrkOicVUMS95ebXc9B9zze1qShHDWDjUBLg2UmRPxXsvx35ZJwpbEQETz9x7CqTCL1e3JBjqkAb7CcosE6f2zWRTPIBTln1FMOPNn%2BIfGzu4K1x%2BxKqUoz0gOH1GWnpci1Av7vahCfSclwpwswzNtsmELVUCEMbB0XZNygyM6YMrblLd3ArbeWCvUtHRJGjnURkTZRnAUJ9NYHl8jmHQbaXPwUmDVkW%2Bfwmax9R5AOtGySWkBb%2BK5hN5AXeuxHB1K56MXPe91bGTLzf71thM2J0JVbDz%2FXtnj1JV2&X-Amz-Signature=2f83012ea3063ded2e4f96725087cf33bd86ad29ce2f715734ad005e0f1d9816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSODHPW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCet9GZk%2BviRlTVtySKu9gqmJi0%2Bv%2Bsxh18BAtL6Bf2HgIhANZ8Yb%2F0isADtTK8CnFsYH0vL6EuIGBKqbSFbxsDH0I%2BKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw94uWVoKpIGzIlnnMq3APZgwUSo%2FwtHmGTVjfT%2B9IXP4LhV3twzQHp1oojklS61120VOKf3NecG3WIQxnjvZtdzv8p61is2lQzRiXFutYQ4EOCH2P%2BQazKjl%2BqjACoop%2B4CbHxRXxlX5IXg329BQoFMO5N%2By4diNcOZ6bRXkRFNPsWMwmXtePdm1NepntS4qhbEWW65TPvjZ9yuFOnEM9OU9VM51RXIo0NeOGj%2BlFshzaobf%2BC3OJaY6uFZTIPq%2FFWYcOtgsuXFhIh%2FvHp%2F6PwKBJ%2BNipCkgIUaMjSz8jd9GcwIwkY6%2FDQzxGJu9vXU0QBDGnPT04POuzAkr0w2sXrd0aqHJnQzng6NqI7z7J4EsookwMbkHyCc9ln8bya%2Fo9ISKYwYZs%2F6H1ZpyrS9Ujts2aRHARZCxbCSBNVcz%2BVybtD2NlQE8cEADV48gWRAaMi1skJ1mJax%2FrCq7FHmrDnu48WAttznulCfQiV9m%2B2IkoQgVnVjyi%2FKTlcjkzyX3FQ5AEi7v0eOXoc3k8YORJy5MqzhrOzxdUFucy1ZgCI0NLrOpsaSm38XnwUOUT%2BycTjN9aCytsWWmq1O%2BcsrkOicVUMS95ebXc9B9zze1qShHDWDjUBLg2UmRPxXsvx35ZJwpbEQETz9x7CqTCL1e3JBjqkAb7CcosE6f2zWRTPIBTln1FMOPNn%2BIfGzu4K1x%2BxKqUoz0gOH1GWnpci1Av7vahCfSclwpwswzNtsmELVUCEMbB0XZNygyM6YMrblLd3ArbeWCvUtHRJGjnURkTZRnAUJ9NYHl8jmHQbaXPwUmDVkW%2Bfwmax9R5AOtGySWkBb%2BK5hN5AXeuxHB1K56MXPe91bGTLzf71thM2J0JVbDz%2FXtnj1JV2&X-Amz-Signature=034b91fc4a283d9884680b8ac78d7e7d8e662f189b8a6e200ebd90b3c7bc8326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

