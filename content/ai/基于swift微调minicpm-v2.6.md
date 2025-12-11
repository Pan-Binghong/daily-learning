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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSEA3XK3%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCSjJ%2FMaBGMdBYlLY4JVkSfNjUMcyei4atcKnOwRXzmGwIhAOyWxst2sv4oASNeQeU3Bxrk5YTW92h%2FoSoK53L0xw%2BDKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb3L9cbJ%2BW1ZSC5osq3APVhz7pRXVk%2BbDPvFXp7Xf6gIKl0Yjrb3M9gkhmd5iHbQZwKaTtbrvyt04W0F5LXKs88e7W5%2BoL%2F6sxmzhoqKJpgV4ZyOJzrY8%2FBVgk9jrl71y7DIxHzw9u3fRJeC6w3fxqV43JMRRUgO746yHX88jjNflTmMQrJ2L80quf5VSDZuOG%2B6nD4cAfZ7Dsa%2F50wqr8CPRXJw%2BgpwhCor4rPq668qGx75jF3P0uz39r38jInHecgjeQnXL2wyX68VSnwZxCaSoESyI%2F0bPyas8EIzEiIt2MltvhcwZDTYWmy0LjG7wWwJqBcZUEyDA9DdgMUDQUCLaLK57Drj5rDH8ZfhwwN5QRIedTjhxxO84SHhjLRtM7NRpdWDZ0aXpwaB%2BmnIZOptuE4DYEzE5aiYb8no8Eu8DaynJhzrecDActGZoZ9eNlbOt7PIAO0tFgr%2F8WyOb5zY%2BDzgPo9PnXwyiu%2BG1r8k6qEDeSWTSO6muX8uD6a7KigqiId4YwQBkz2L345mnPeR5oHrQ3uKCFWQwmIr3mNYfFQrfNO7asnykB9wsjPuyCYGKxneL0q9MnpPbBG3t34PFXNBaR%2FCIW66ozU0yCAumq0ykMTgs9RlDgxajJBHvUYs3e4cyPtkqSZDCQtejJBjqkAbWt5lc2MnJTr2%2FRr3IPXNnmmNAHZM%2F85v7wIaRPo%2FmO9UNKaNSZjN0kXkPpT6nrz7Vl%2FwO87JvItgoMtbM%2BYxHhW2UbLdcYaO3KqGz2LVwlUM%2B0z80pgZSGK%2FY5lL1MBozcb3oJL2MEZRdQx7tLb%2Bfl%2B71B7aIyX88yUwzWNwTB5nH9AMCM1xCXzQLMCbIbZGTO8PpjGjX6sMlwikZG7xoSaoXJ&X-Amz-Signature=8eea3e1615ba5dd3eb1e3375796638350f628c45e7fc9d6f605bdb1ec8fe3b25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSEA3XK3%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCSjJ%2FMaBGMdBYlLY4JVkSfNjUMcyei4atcKnOwRXzmGwIhAOyWxst2sv4oASNeQeU3Bxrk5YTW92h%2FoSoK53L0xw%2BDKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb3L9cbJ%2BW1ZSC5osq3APVhz7pRXVk%2BbDPvFXp7Xf6gIKl0Yjrb3M9gkhmd5iHbQZwKaTtbrvyt04W0F5LXKs88e7W5%2BoL%2F6sxmzhoqKJpgV4ZyOJzrY8%2FBVgk9jrl71y7DIxHzw9u3fRJeC6w3fxqV43JMRRUgO746yHX88jjNflTmMQrJ2L80quf5VSDZuOG%2B6nD4cAfZ7Dsa%2F50wqr8CPRXJw%2BgpwhCor4rPq668qGx75jF3P0uz39r38jInHecgjeQnXL2wyX68VSnwZxCaSoESyI%2F0bPyas8EIzEiIt2MltvhcwZDTYWmy0LjG7wWwJqBcZUEyDA9DdgMUDQUCLaLK57Drj5rDH8ZfhwwN5QRIedTjhxxO84SHhjLRtM7NRpdWDZ0aXpwaB%2BmnIZOptuE4DYEzE5aiYb8no8Eu8DaynJhzrecDActGZoZ9eNlbOt7PIAO0tFgr%2F8WyOb5zY%2BDzgPo9PnXwyiu%2BG1r8k6qEDeSWTSO6muX8uD6a7KigqiId4YwQBkz2L345mnPeR5oHrQ3uKCFWQwmIr3mNYfFQrfNO7asnykB9wsjPuyCYGKxneL0q9MnpPbBG3t34PFXNBaR%2FCIW66ozU0yCAumq0ykMTgs9RlDgxajJBHvUYs3e4cyPtkqSZDCQtejJBjqkAbWt5lc2MnJTr2%2FRr3IPXNnmmNAHZM%2F85v7wIaRPo%2FmO9UNKaNSZjN0kXkPpT6nrz7Vl%2FwO87JvItgoMtbM%2BYxHhW2UbLdcYaO3KqGz2LVwlUM%2B0z80pgZSGK%2FY5lL1MBozcb3oJL2MEZRdQx7tLb%2Bfl%2B71B7aIyX88yUwzWNwTB5nH9AMCM1xCXzQLMCbIbZGTO8PpjGjX6sMlwikZG7xoSaoXJ&X-Amz-Signature=3d0206dc363fc6c3acef402bdedeeb200f980f2633647f9b382563b48de682b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSEA3XK3%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCSjJ%2FMaBGMdBYlLY4JVkSfNjUMcyei4atcKnOwRXzmGwIhAOyWxst2sv4oASNeQeU3Bxrk5YTW92h%2FoSoK53L0xw%2BDKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb3L9cbJ%2BW1ZSC5osq3APVhz7pRXVk%2BbDPvFXp7Xf6gIKl0Yjrb3M9gkhmd5iHbQZwKaTtbrvyt04W0F5LXKs88e7W5%2BoL%2F6sxmzhoqKJpgV4ZyOJzrY8%2FBVgk9jrl71y7DIxHzw9u3fRJeC6w3fxqV43JMRRUgO746yHX88jjNflTmMQrJ2L80quf5VSDZuOG%2B6nD4cAfZ7Dsa%2F50wqr8CPRXJw%2BgpwhCor4rPq668qGx75jF3P0uz39r38jInHecgjeQnXL2wyX68VSnwZxCaSoESyI%2F0bPyas8EIzEiIt2MltvhcwZDTYWmy0LjG7wWwJqBcZUEyDA9DdgMUDQUCLaLK57Drj5rDH8ZfhwwN5QRIedTjhxxO84SHhjLRtM7NRpdWDZ0aXpwaB%2BmnIZOptuE4DYEzE5aiYb8no8Eu8DaynJhzrecDActGZoZ9eNlbOt7PIAO0tFgr%2F8WyOb5zY%2BDzgPo9PnXwyiu%2BG1r8k6qEDeSWTSO6muX8uD6a7KigqiId4YwQBkz2L345mnPeR5oHrQ3uKCFWQwmIr3mNYfFQrfNO7asnykB9wsjPuyCYGKxneL0q9MnpPbBG3t34PFXNBaR%2FCIW66ozU0yCAumq0ykMTgs9RlDgxajJBHvUYs3e4cyPtkqSZDCQtejJBjqkAbWt5lc2MnJTr2%2FRr3IPXNnmmNAHZM%2F85v7wIaRPo%2FmO9UNKaNSZjN0kXkPpT6nrz7Vl%2FwO87JvItgoMtbM%2BYxHhW2UbLdcYaO3KqGz2LVwlUM%2B0z80pgZSGK%2FY5lL1MBozcb3oJL2MEZRdQx7tLb%2Bfl%2B71B7aIyX88yUwzWNwTB5nH9AMCM1xCXzQLMCbIbZGTO8PpjGjX6sMlwikZG7xoSaoXJ&X-Amz-Signature=c8ef10b3407919409e25ca712fd582edc5f0e9c35b4e19929d5acba2522572a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

