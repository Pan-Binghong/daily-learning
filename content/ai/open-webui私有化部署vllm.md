---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNYZUPG6%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC6YL95qk4RGRb7gRJNUoboqKhsgEofdrxNRsvvxcW9NAiEAg3b0BrwBWg0flTfXTBKPRlW5tmWu48%2Fx4GdCZR8VxukqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbl7JdiElfLlQObBSrcAyTZWB79GXbuc%2BEZV4jq0CyKo8BnG5XOgh4kF9YB9BlRcw7aWVFGFU5zZPa5C7knS4Qph9rjt6TZFi1xqx2X0%2Bb65JfvGSalknDl78%2FP5JyEcs0ybu66WzVSNO4XEjM0MZmX9ymsV44E9yLobNKQEYXuLG7nLJpmGd5yWxfhdbJ4UsmmGIPZI9KDgnh56lzQd1Xhi93y%2B%2BxDix60440moGyo3NjgIl9%2FNt%2B%2FKHv1Z6tDcqfuRtJcs8G9pT1Ka9fcdgor9V6WtQLkIY9io8%2B8ynacasdKJiVmxzqdM%2BPQIkXcNreNF4GjkXD8dtm7jVaseczwiF5Q71R5YfWgZ%2Fn6%2FoCCnWzj%2FtBjfFQcqGp5utQNJpQhav%2FSWTN4lKLQ3QUv%2B0R4sgbISW8AXlbnsu3fwPsN7wcTiqPlHQ43uTG7wvAF1aVCRy7ct9hWiRLjLAJc7Dy5w%2FYCmGNQvSYEstP6Tp9Gt1Gd7PiSOcXzIDkjZfD%2Bl6rvsLIvN7e3cAseVyplzVzpIsgn6%2FyTa%2BzJE23eEkgKWr%2BD7VxwjhxdVy0GOGKYoQk5TNx3iFWA9z8HiXuAxP5JybVAiVSEYsVuroOqJUMED1oY%2F0c%2FWGxG%2Fyq0Nw9NzVQR7H36RhvEhp5aMIO1tcgGOqUBFOCWSnrLFcFAs0%2B1HYUj498Y%2BjTIl2skqG0a66pIuf7S0gPDRP0EtIGkSAuryKDy809NszRwqYuDoEkCME700w5cs5DZw5QHaYOG1hvE0ZDoyxBHoCpiJ5laWhX2WpF3qO3xK1aXlCE1E%2BR9SCaZEyBSfIHCn0LtqLzLbJhamBDD5v8f%2FxVw%2Fukr3uQFHn1EaiQyd6BSEoJdSBAwF%2FvrOmuAvWqm&X-Amz-Signature=16e72e9218418c2998d845a2234d13da919d7f0655a950df491fef550d7fe9ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



