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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXWNTTAR%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH3dhw5hwwonHLNloufbwEUtnV2yxj%2B5VoYQ8MI%2FW31FAiB%2FxLJXQIcbWpWRj%2F7Dr%2BAZjWH%2BMcTmwXkm5zcM9SL1Yyr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR1nfZ6l%2BeW6Bd51NKtwDAhpVOnxszaOnHWZWdo6ciZwER8ZEY9mdYJwymfCVPHAIRprYbefEPRQYRgrgnFlIz5ESQN%2Fcv3umow6q0N6h%2FvljnrXrKAUoZljqqqJKWpH2AGVjJoZKVz2IgO7e38sD792BymA92PvIvx2%2BQcCSM%2BpmbzBEADlO3K90N8QVth8xqpKg6ZoivCodqlz4n0IMgnlGwFKRiJIe%2FghbgJRrIgGhn%2F7uQ7PC%2FuD5NE3xHVYPt2WtzZEUK0yNSjtzmhKmvKkQA6GKnWgWP6UwHquDMXHd7Sezn8BKkw587uMM3dDXe2PTnCnRQBJxyzNAdJ%2BeAOfVRzhxCDxS5kfAGXwyymiJX83UpDk0EJWNsmuvZEFJd%2BFie8rkSFcb0a9WsaATcWk7qOe9dOUAYgBtvRHwpa%2BSU3WQDqoEZDyJHH3DakaZZGBpN6vm%2FU%2BgEDjnzGLJ3jHjcof3wJdWsW0NB6%2B4HCmkSHWIeiFLruAr9C%2B1rsImIgnGfco3jCV7Fzj3r6kk1aAIKbYKzj%2B45okUjn%2B%2B%2BGwzP8PZs3ELL0LpapaGYMOgdZwIqfUZv3SGtXbEV%2Bi0x540TMKAKcTMcyowr8oK7%2FsrkdZiev0yGM1h6Pm0%2Fbu9YXYYrS9g%2FPCJvKEwvpblywY6pgEMtiCgo9ZyH9db5V%2BCYIXkZVIk6spar9ITA8dhAM8k9lIbxR6M8ZL7QHnCkQYsSZUIPD9%2FOY%2BqhRMAo%2F7F9GqIUoL9dgnTPJ5G0UcKdgJxd9Hi%2FhhyhHZH6Pw0sw7GPFfNh8KdHHiot8aIoWsi%2B25yeNXrzXvrSnfDgysY2fiistS%2B13ARLqTtet54f3o4%2FM9nZQc0PEDNPu5xsHQZVm%2BPqxriKa7d&X-Amz-Signature=9a6a69d522916a25ae9c0c100cc1d5ec25d7498c7e6b71ef589fbe08b6122464&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXWNTTAR%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH3dhw5hwwonHLNloufbwEUtnV2yxj%2B5VoYQ8MI%2FW31FAiB%2FxLJXQIcbWpWRj%2F7Dr%2BAZjWH%2BMcTmwXkm5zcM9SL1Yyr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR1nfZ6l%2BeW6Bd51NKtwDAhpVOnxszaOnHWZWdo6ciZwER8ZEY9mdYJwymfCVPHAIRprYbefEPRQYRgrgnFlIz5ESQN%2Fcv3umow6q0N6h%2FvljnrXrKAUoZljqqqJKWpH2AGVjJoZKVz2IgO7e38sD792BymA92PvIvx2%2BQcCSM%2BpmbzBEADlO3K90N8QVth8xqpKg6ZoivCodqlz4n0IMgnlGwFKRiJIe%2FghbgJRrIgGhn%2F7uQ7PC%2FuD5NE3xHVYPt2WtzZEUK0yNSjtzmhKmvKkQA6GKnWgWP6UwHquDMXHd7Sezn8BKkw587uMM3dDXe2PTnCnRQBJxyzNAdJ%2BeAOfVRzhxCDxS5kfAGXwyymiJX83UpDk0EJWNsmuvZEFJd%2BFie8rkSFcb0a9WsaATcWk7qOe9dOUAYgBtvRHwpa%2BSU3WQDqoEZDyJHH3DakaZZGBpN6vm%2FU%2BgEDjnzGLJ3jHjcof3wJdWsW0NB6%2B4HCmkSHWIeiFLruAr9C%2B1rsImIgnGfco3jCV7Fzj3r6kk1aAIKbYKzj%2B45okUjn%2B%2B%2BGwzP8PZs3ELL0LpapaGYMOgdZwIqfUZv3SGtXbEV%2Bi0x540TMKAKcTMcyowr8oK7%2FsrkdZiev0yGM1h6Pm0%2Fbu9YXYYrS9g%2FPCJvKEwvpblywY6pgEMtiCgo9ZyH9db5V%2BCYIXkZVIk6spar9ITA8dhAM8k9lIbxR6M8ZL7QHnCkQYsSZUIPD9%2FOY%2BqhRMAo%2F7F9GqIUoL9dgnTPJ5G0UcKdgJxd9Hi%2FhhyhHZH6Pw0sw7GPFfNh8KdHHiot8aIoWsi%2B25yeNXrzXvrSnfDgysY2fiistS%2B13ARLqTtet54f3o4%2FM9nZQc0PEDNPu5xsHQZVm%2BPqxriKa7d&X-Amz-Signature=22213a5d0fd6cde68dff1bcf9cbe88da4d0002ec9704ba1a4cff2cf027fe99bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



