---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWFFIBW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXfPjYuqTDNrkzrmcFZ5WlkVZKRI9sor00I5FXOosQ8gIhALQ0QhoZjtW%2FK3jHiqIxo8MkCYbnS8UxwX3cWroQrQLbKv8DCHQQABoMNjM3NDIzMTgzODA1IgwyZcVuFbdXjjlhWeQq3AOUSzS8RL7STjRBe%2BrBlNLxqLRwd3PiFohHG6CaeyYbVLgKYKzgJQcZiTiMwDgBERqB2egqbevsEPetN4st%2BrzLK1UuUe%2FRC1za7zB7wFkAXqsEv7MGBB84hg7ZtxH4fJiuyFvZn3r33UjA4%2Bbd5pQgD%2FLzvR5QJYkYbVRFf9OTTi93vdr3H34czA81aK06UUhlauewaq47l6%2F19xJyptxR%2FRmjkb1Szb5Gx1jmwwF9e9zo6gHGnBGLpW53mgJwK3LXu%2B8f5pFEnZHW1PcVL%2BW8vBh2UqIpmGkqon5Yi6uY8jQn95cn%2BAX9gszqv5p7K2XgKPRnH%2FGyRDMKCHiciMkryTXN8wAvKHPhvRtMN%2Fohn6uNUKJPEGlXR5MAdap7JVvxu3CdNRCWCw%2BoAq%2BmMZUffG5d9%2FpiFl5ZC5Zq6HU1wGCg6QT1ULD%2FO7Q6tL2UmK4X3%2FBptW5Iq6jOJcgKCJONyVl%2BmiBNYjpCaMJVGnvoEENadSBMlgEO%2FwttJGpuikmzfodMaCTV8vZjEdkJeEQ6QhbrHfYc4vCqjiWCnmxCTsqGgQucV6VAQ38SqaWFpNnQSB5H6SecEGFw55dJKgGamnF0%2B%2BoRcUeBAkStshcI9GefTp3bQX7cWBpCzjDCsYjKBjqkAcFUyG3JPOdWcnrBK3fIV1bxAICVu24WxbSMb1zhhOxXtgTP1EhMCl4InbYQZaWnKqLe72cnciEY5h77KjMc2t1EZGb%2B7vlIVpF379y8Irpeb3N4sWqO61J3xiAIAXByZkq3J5LrYrn5YbgbpuHNHr%2BQytKid%2BqwgI9Pa1M609oA9uDlJqBlIRAFRXgIvcXIKIA%2BJV2yImlMPN0NgerUmTYSt9ut&X-Amz-Signature=5da1049b21cf026fd9f81768783723f8b56413c7e308ebb80b2a203f34f2cce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWFFIBW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXfPjYuqTDNrkzrmcFZ5WlkVZKRI9sor00I5FXOosQ8gIhALQ0QhoZjtW%2FK3jHiqIxo8MkCYbnS8UxwX3cWroQrQLbKv8DCHQQABoMNjM3NDIzMTgzODA1IgwyZcVuFbdXjjlhWeQq3AOUSzS8RL7STjRBe%2BrBlNLxqLRwd3PiFohHG6CaeyYbVLgKYKzgJQcZiTiMwDgBERqB2egqbevsEPetN4st%2BrzLK1UuUe%2FRC1za7zB7wFkAXqsEv7MGBB84hg7ZtxH4fJiuyFvZn3r33UjA4%2Bbd5pQgD%2FLzvR5QJYkYbVRFf9OTTi93vdr3H34czA81aK06UUhlauewaq47l6%2F19xJyptxR%2FRmjkb1Szb5Gx1jmwwF9e9zo6gHGnBGLpW53mgJwK3LXu%2B8f5pFEnZHW1PcVL%2BW8vBh2UqIpmGkqon5Yi6uY8jQn95cn%2BAX9gszqv5p7K2XgKPRnH%2FGyRDMKCHiciMkryTXN8wAvKHPhvRtMN%2Fohn6uNUKJPEGlXR5MAdap7JVvxu3CdNRCWCw%2BoAq%2BmMZUffG5d9%2FpiFl5ZC5Zq6HU1wGCg6QT1ULD%2FO7Q6tL2UmK4X3%2FBptW5Iq6jOJcgKCJONyVl%2BmiBNYjpCaMJVGnvoEENadSBMlgEO%2FwttJGpuikmzfodMaCTV8vZjEdkJeEQ6QhbrHfYc4vCqjiWCnmxCTsqGgQucV6VAQ38SqaWFpNnQSB5H6SecEGFw55dJKgGamnF0%2B%2BoRcUeBAkStshcI9GefTp3bQX7cWBpCzjDCsYjKBjqkAcFUyG3JPOdWcnrBK3fIV1bxAICVu24WxbSMb1zhhOxXtgTP1EhMCl4InbYQZaWnKqLe72cnciEY5h77KjMc2t1EZGb%2B7vlIVpF379y8Irpeb3N4sWqO61J3xiAIAXByZkq3J5LrYrn5YbgbpuHNHr%2BQytKid%2BqwgI9Pa1M609oA9uDlJqBlIRAFRXgIvcXIKIA%2BJV2yImlMPN0NgerUmTYSt9ut&X-Amz-Signature=663bfebeaefd9adefb7840373b7b08e82a6be70d8fbd175bf7d8eb9021dc967b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



