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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4WFIRF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIGuvZ7e1d9GMXXhcuvcmBp2ZZaunqd9W5dPrI95przWDAiEA%2BuKQ%2FnTHzxir%2FazldlOuCXs8VSF8s%2FdZGb3cq78VjJgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKn2o1KrV5hi508HTSrcA3CcxiSv1A0evN2lEUWskgOxVFMP7uTW8ok72IogCEw2Hj4CWadt6H9o08cl9gdMo1uVPo5bPvCzWW%2BDApNN7vkxDCRGu5nlGTzYF81XFvsgZQIjp%2BSNN7%2F%2B6SvILJQoCNjVX44vrLUqH3ofCn4CcHuxhVdScylWdrU184bcNyfItzr8YALdkSZhLRPWPR6Oz%2FCjbmuPn7Y6JS75K93yeYPSKnKSMZ1GPi8jS72eMF9npYseRhFKUMlNg%2BXPij7P4VeNAlRe3TJHmqjonQRmfg4MkCmeyyEK4JsTSlA5DrqPo99k5uGuWXrEOOw%2FJbNKIFKG8b6GElemmFat7UKts0%2FGJF6FOM0xMUQ8a6rTJQiRwyBO%2FSMxBc%2FRW%2F8QFSK075qm9NIo%2FL5bytlMp8CpP9pGcF0ZPKo7keqxft6CA6ARhXAW3u8qybq0Wi563V7zyAdfX3nTgnCBQuTmmagTNmLwBT3VrUXEkSj9gd0UU47AdgPyhex0ApJyKYPnxH8Gyw4WnqNWmCVBWDtybTvT2MkEj2AQqHsovOdzS%2Bo3OBBEldlUNCkK8NCcJjAOgQ2fJgjqZZn5u9d1cZXuwpFb4uGIQUJl7DlruhnCbFOlrLrQKNwkMTu%2Fn05gU8i8MLSdzM8GOqUBKw5s297P7biCo4%2BpVm9%2Bb0h3M0ewmoivEkEmeyB%2BCH8W1iCPS%2Ffjkt0ga3P5muTbDi7tPAd8uKXu14uf3BVUVCI2yX7s6oTwqimeUuwj5Yb8FshEn1At5QGv14NL5xvZyi%2BMHr%2Fq5Hx%2BoSz9nflEwE4JUb5DYk%2Bj%2F%2FFKZxbzXHDot2woDZrQFpbZ%2FL0iU0PN6ZKirdiQAnRsM6hU%2Fz0L7OpbNW38&X-Amz-Signature=d935987c84985984dc328a4b67a2ffc08a990ce53d68b8cb329b7eb8f2cc12bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4WFIRF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIGuvZ7e1d9GMXXhcuvcmBp2ZZaunqd9W5dPrI95przWDAiEA%2BuKQ%2FnTHzxir%2FazldlOuCXs8VSF8s%2FdZGb3cq78VjJgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKn2o1KrV5hi508HTSrcA3CcxiSv1A0evN2lEUWskgOxVFMP7uTW8ok72IogCEw2Hj4CWadt6H9o08cl9gdMo1uVPo5bPvCzWW%2BDApNN7vkxDCRGu5nlGTzYF81XFvsgZQIjp%2BSNN7%2F%2B6SvILJQoCNjVX44vrLUqH3ofCn4CcHuxhVdScylWdrU184bcNyfItzr8YALdkSZhLRPWPR6Oz%2FCjbmuPn7Y6JS75K93yeYPSKnKSMZ1GPi8jS72eMF9npYseRhFKUMlNg%2BXPij7P4VeNAlRe3TJHmqjonQRmfg4MkCmeyyEK4JsTSlA5DrqPo99k5uGuWXrEOOw%2FJbNKIFKG8b6GElemmFat7UKts0%2FGJF6FOM0xMUQ8a6rTJQiRwyBO%2FSMxBc%2FRW%2F8QFSK075qm9NIo%2FL5bytlMp8CpP9pGcF0ZPKo7keqxft6CA6ARhXAW3u8qybq0Wi563V7zyAdfX3nTgnCBQuTmmagTNmLwBT3VrUXEkSj9gd0UU47AdgPyhex0ApJyKYPnxH8Gyw4WnqNWmCVBWDtybTvT2MkEj2AQqHsovOdzS%2Bo3OBBEldlUNCkK8NCcJjAOgQ2fJgjqZZn5u9d1cZXuwpFb4uGIQUJl7DlruhnCbFOlrLrQKNwkMTu%2Fn05gU8i8MLSdzM8GOqUBKw5s297P7biCo4%2BpVm9%2Bb0h3M0ewmoivEkEmeyB%2BCH8W1iCPS%2Ffjkt0ga3P5muTbDi7tPAd8uKXu14uf3BVUVCI2yX7s6oTwqimeUuwj5Yb8FshEn1At5QGv14NL5xvZyi%2BMHr%2Fq5Hx%2BoSz9nflEwE4JUb5DYk%2Bj%2F%2FFKZxbzXHDot2woDZrQFpbZ%2FL0iU0PN6ZKirdiQAnRsM6hU%2Fz0L7OpbNW38&X-Amz-Signature=bc55ecf958083f7836e278e77e6576dce8e7f7b78a2af5452e2dbcf85259af19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4WFIRF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIGuvZ7e1d9GMXXhcuvcmBp2ZZaunqd9W5dPrI95przWDAiEA%2BuKQ%2FnTHzxir%2FazldlOuCXs8VSF8s%2FdZGb3cq78VjJgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKn2o1KrV5hi508HTSrcA3CcxiSv1A0evN2lEUWskgOxVFMP7uTW8ok72IogCEw2Hj4CWadt6H9o08cl9gdMo1uVPo5bPvCzWW%2BDApNN7vkxDCRGu5nlGTzYF81XFvsgZQIjp%2BSNN7%2F%2B6SvILJQoCNjVX44vrLUqH3ofCn4CcHuxhVdScylWdrU184bcNyfItzr8YALdkSZhLRPWPR6Oz%2FCjbmuPn7Y6JS75K93yeYPSKnKSMZ1GPi8jS72eMF9npYseRhFKUMlNg%2BXPij7P4VeNAlRe3TJHmqjonQRmfg4MkCmeyyEK4JsTSlA5DrqPo99k5uGuWXrEOOw%2FJbNKIFKG8b6GElemmFat7UKts0%2FGJF6FOM0xMUQ8a6rTJQiRwyBO%2FSMxBc%2FRW%2F8QFSK075qm9NIo%2FL5bytlMp8CpP9pGcF0ZPKo7keqxft6CA6ARhXAW3u8qybq0Wi563V7zyAdfX3nTgnCBQuTmmagTNmLwBT3VrUXEkSj9gd0UU47AdgPyhex0ApJyKYPnxH8Gyw4WnqNWmCVBWDtybTvT2MkEj2AQqHsovOdzS%2Bo3OBBEldlUNCkK8NCcJjAOgQ2fJgjqZZn5u9d1cZXuwpFb4uGIQUJl7DlruhnCbFOlrLrQKNwkMTu%2Fn05gU8i8MLSdzM8GOqUBKw5s297P7biCo4%2BpVm9%2Bb0h3M0ewmoivEkEmeyB%2BCH8W1iCPS%2Ffjkt0ga3P5muTbDi7tPAd8uKXu14uf3BVUVCI2yX7s6oTwqimeUuwj5Yb8FshEn1At5QGv14NL5xvZyi%2BMHr%2Fq5Hx%2BoSz9nflEwE4JUb5DYk%2Bj%2F%2FFKZxbzXHDot2woDZrQFpbZ%2FL0iU0PN6ZKirdiQAnRsM6hU%2Fz0L7OpbNW38&X-Amz-Signature=74a588332722e9c34d806e28758d8ceba02897cf52eabd644d5df9f1f03288ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

