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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCHWDBAK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQC6kFvXqAygQTUO%2FslrCFy7X%2B8FNsZLDTBVbEOjKe7JQAIhALl59hdae7bBe2fcO2Wf2yoeQvucARhX%2F0bZfEzwc33oKv8DCBwQABoMNjM3NDIzMTgzODA1IgzfzpTPcZS57OaD91cq3AOI38TbbZzFsPgcfRuqElbKt0a%2FCXIjLDKLNSMYk7%2BNLBFc0t6Cyf5YTh%2F5fchUZzAXqpP9xT7a5sBqw%2BkzTU6bc4x9Ue1gIYRbph7lOMEU%2F1LMWrgnj6cOMKH53QS9im2RoGAQ%2FV9fsAAPBZvTmN8N2AyER%2B%2B2dmZ9q3RbXkPCi2rgRP8C3DM235016w6pRddWH1B%2BRsfz5yHy%2Fs3sJEgQNuFWdy1zkf6WKzBMHvzxXlRHuaoA0zomS8qQlMJQKPJnJ9U6LwhPiljLnVcqm1pWw5sEECEQrQj2NGMnOMJJnb31MF4iEfF1BJ9UB7%2B%2FYsIJXPYxC0MAHPRmmKBwyQbztG6F2nUy36jyG252BnBFgpSmYspsGe0EHZ2DfnT4gk0Os4N4CWHi5YZUQr7YJXFQNsywvj0WAWK7ES6LyHVMeD9POy9a1LI0x7ytpOk2JG0%2F6CXEKge6X0puTPLBU8ovN9ccvugWy9Cyh5UpkSk2R1qvGaJZvJJ%2BAAWq9ImfnZ4vYkxajJdMGcYO4nSMvNjdQ3dw4ryVBkMIq%2FXba5A6YSpnmq%2Bgn%2FQWqrdOZJDlEyKS7S24YY99Lnrs%2BWise6R6ik0Gfxg%2FcXCHS62i91IGmvwA5mQuPTcsPr8gkjDHhdbLBjqkAfRgdapGgEt%2F4d26GK%2B6JI7yWSJvDvyKVQlM46%2BfOOvvf%2By2%2B9VilROwAG9VMadBlpmojoxPyoBuZ%2BfyXgGgwx3nAtobB8nFOwdZpBbpg%2Fm%2FpcYAlEgg%2FQmyodxnuUe2sieEelkWCn1I9Qu9nkN4i4xn3npB5cPJU3UAEVrw%2BxULI4lCIGsm9KpX2FRln4NrD7z01urDdB7uwAykIPqprLRn5LrZ&X-Amz-Signature=bd517b3acb9dc6812ab734f5dd249124b7dff534fc21d7e1f58788740c73d859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



