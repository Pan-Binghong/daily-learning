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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROZMYHRG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCRDUrnYsNB9fdAYzBsmGOobN3zCeFdqA2DkbI0yg6FOwIhAI0xn2VcwKPsJdVLhM1OliXxyA9WWHOQWNEGbAiL7eSlKv8DCCwQABoMNjM3NDIzMTgzODA1IgzHqaz7UamAPlRq0IYq3ANtxh%2FvguUIek3wl8uKp1MzRgzcb6h90xDSv6lNfU3Q%2BnHfYAGVePvFVZ9QWTyrYywtZ1roAG4LNDxHM5MWYII5zDhh8kL8lGnmu8jHFtASAdfF58K6IhVRhQ1mFvw%2BKRFtHk1%2F68nzPCdXb8YEkEFDAcpq0PzAoVatPz6yBwtj0HI9oEhv7Rkjj3Mzd798BPM58ALfOOzQxzQuAgVg%2Fg7nUeiEY0zrKRVgiYEwZeI8QO9F3WnLT6OyodU%2B9aCy9E4HjooHpK8inSixqhKj4VgE2Daln%2FW3qoRwMOJT3C%2Byel%2BkXuACtsJXJB5l6K7QE1m8uMybEhM3c58sCZCPbAzbBF0g4EHfmUvD%2F9zm0dduKXwFQfu%2FH1q74NYvcmEvIJo2p9wvHqUsCsuEyokuhFsoDSkgMHyH0tGvS52VmuifFNJbSXlluc2SOz%2FoRlTvOOa6OP4gTCtzU%2F5rQJwiH3qthz%2FiTtvgJu37k3v1KKoGEdV0WaNQtcmlX7%2FfgSBNVRzPWlQC6%2FbKxSkTaMUm7vIf1kqI1dq0UeSmfwnioQNHfJMLLwvtQNg4DKuDWTQtqi1sfEVODcxgv8hPg69DvsURalWqRRsZY%2BZV8CLtdPb1gFnyWgxIMRh5uN%2BftDCI48%2FIBjqkAdULGUQRMykDPMqKHAoDFYUpO0LXr12%2BgjNP5Mb%2BqMwDkFAE1wRx6evnoL5cIXbKi4FOKkHKOp9aExaFZnNwKHNN%2BlQF1B8ZSTdKo6ZZfMMCHLm7s9OLd3LGn5jOFv%2B%2FzzjK6O%2BBwnOPc5%2BV%2FpYmzHnCFPRCejd9RCiJc6%2FwkUoy2Hzfl%2BJw7Yt5eJidozTqpQk4mQB126UcmJvqj6lEiOLTs4Z1&X-Amz-Signature=8cff2f724db25f478752508859825a3602801bf5724e548647568a249aceeb17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROZMYHRG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCRDUrnYsNB9fdAYzBsmGOobN3zCeFdqA2DkbI0yg6FOwIhAI0xn2VcwKPsJdVLhM1OliXxyA9WWHOQWNEGbAiL7eSlKv8DCCwQABoMNjM3NDIzMTgzODA1IgzHqaz7UamAPlRq0IYq3ANtxh%2FvguUIek3wl8uKp1MzRgzcb6h90xDSv6lNfU3Q%2BnHfYAGVePvFVZ9QWTyrYywtZ1roAG4LNDxHM5MWYII5zDhh8kL8lGnmu8jHFtASAdfF58K6IhVRhQ1mFvw%2BKRFtHk1%2F68nzPCdXb8YEkEFDAcpq0PzAoVatPz6yBwtj0HI9oEhv7Rkjj3Mzd798BPM58ALfOOzQxzQuAgVg%2Fg7nUeiEY0zrKRVgiYEwZeI8QO9F3WnLT6OyodU%2B9aCy9E4HjooHpK8inSixqhKj4VgE2Daln%2FW3qoRwMOJT3C%2Byel%2BkXuACtsJXJB5l6K7QE1m8uMybEhM3c58sCZCPbAzbBF0g4EHfmUvD%2F9zm0dduKXwFQfu%2FH1q74NYvcmEvIJo2p9wvHqUsCsuEyokuhFsoDSkgMHyH0tGvS52VmuifFNJbSXlluc2SOz%2FoRlTvOOa6OP4gTCtzU%2F5rQJwiH3qthz%2FiTtvgJu37k3v1KKoGEdV0WaNQtcmlX7%2FfgSBNVRzPWlQC6%2FbKxSkTaMUm7vIf1kqI1dq0UeSmfwnioQNHfJMLLwvtQNg4DKuDWTQtqi1sfEVODcxgv8hPg69DvsURalWqRRsZY%2BZV8CLtdPb1gFnyWgxIMRh5uN%2BftDCI48%2FIBjqkAdULGUQRMykDPMqKHAoDFYUpO0LXr12%2BgjNP5Mb%2BqMwDkFAE1wRx6evnoL5cIXbKi4FOKkHKOp9aExaFZnNwKHNN%2BlQF1B8ZSTdKo6ZZfMMCHLm7s9OLd3LGn5jOFv%2B%2FzzjK6O%2BBwnOPc5%2BV%2FpYmzHnCFPRCejd9RCiJc6%2FwkUoy2Hzfl%2BJw7Yt5eJidozTqpQk4mQB126UcmJvqj6lEiOLTs4Z1&X-Amz-Signature=99dcc97a6f05d8e40a5a1d010490524e79651276e83387a51242af39783ef80c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROZMYHRG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCRDUrnYsNB9fdAYzBsmGOobN3zCeFdqA2DkbI0yg6FOwIhAI0xn2VcwKPsJdVLhM1OliXxyA9WWHOQWNEGbAiL7eSlKv8DCCwQABoMNjM3NDIzMTgzODA1IgzHqaz7UamAPlRq0IYq3ANtxh%2FvguUIek3wl8uKp1MzRgzcb6h90xDSv6lNfU3Q%2BnHfYAGVePvFVZ9QWTyrYywtZ1roAG4LNDxHM5MWYII5zDhh8kL8lGnmu8jHFtASAdfF58K6IhVRhQ1mFvw%2BKRFtHk1%2F68nzPCdXb8YEkEFDAcpq0PzAoVatPz6yBwtj0HI9oEhv7Rkjj3Mzd798BPM58ALfOOzQxzQuAgVg%2Fg7nUeiEY0zrKRVgiYEwZeI8QO9F3WnLT6OyodU%2B9aCy9E4HjooHpK8inSixqhKj4VgE2Daln%2FW3qoRwMOJT3C%2Byel%2BkXuACtsJXJB5l6K7QE1m8uMybEhM3c58sCZCPbAzbBF0g4EHfmUvD%2F9zm0dduKXwFQfu%2FH1q74NYvcmEvIJo2p9wvHqUsCsuEyokuhFsoDSkgMHyH0tGvS52VmuifFNJbSXlluc2SOz%2FoRlTvOOa6OP4gTCtzU%2F5rQJwiH3qthz%2FiTtvgJu37k3v1KKoGEdV0WaNQtcmlX7%2FfgSBNVRzPWlQC6%2FbKxSkTaMUm7vIf1kqI1dq0UeSmfwnioQNHfJMLLwvtQNg4DKuDWTQtqi1sfEVODcxgv8hPg69DvsURalWqRRsZY%2BZV8CLtdPb1gFnyWgxIMRh5uN%2BftDCI48%2FIBjqkAdULGUQRMykDPMqKHAoDFYUpO0LXr12%2BgjNP5Mb%2BqMwDkFAE1wRx6evnoL5cIXbKi4FOKkHKOp9aExaFZnNwKHNN%2BlQF1B8ZSTdKo6ZZfMMCHLm7s9OLd3LGn5jOFv%2B%2FzzjK6O%2BBwnOPc5%2BV%2FpYmzHnCFPRCejd9RCiJc6%2FwkUoy2Hzfl%2BJw7Yt5eJidozTqpQk4mQB126UcmJvqj6lEiOLTs4Z1&X-Amz-Signature=552d1a0450e457d8cf087a9d7f67f0d5f668c8d1c6272cdddb11d985769e5652&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

