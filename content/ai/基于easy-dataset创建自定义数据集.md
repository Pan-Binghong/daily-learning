---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NAZV4KP%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAS4W7mwTB5a9f6%2F3PypOmfTTpQufrKtjn6WwQZ3H9BWAiBNHKGVYp8BxlCGLXUlqkXql53VHcKTKD9rwHAWPWDzUCr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMhz2aVReJ4AjGXHeoKtwDgwGDTplzUMlibZ3bWzQuJXGqEyG9FxOjyqQ4iFwjG6EbI4T8MLOD8J3DYrN2RKXGd6ba7ZeHjnITYb55KYXJht4BR6h1S0iIIveC9MACRPgxM2tiTnbL8eVv25YmvklNWfB%2F3cwaL1l4Hyw6Jpb3PPZo7XezQX1yLg1dOPfNeM8N88%2FAjpnVo5OohSmJjx7wzi3fKqyYRnO392bIHl%2BFZsLRVh4e7MULZHrPUq1Gv%2Bt%2FSwmDXGorLlqMTrLF7snorWJMsKY%2FrSfDHJbUF1TRIZpFdLAc4BYFAXHc9stgZpz6g%2B69HDbuCLfTCmMjYLXauXO%2FdhDU90cPPgErp2ruVZgdrP3mjDH4lZWs2JnHJoYpgEDyh4Pgrp1%2BfpKF8uW%2B6xQQgXqxH8PR1%2BCgpLFEoPlAug2fYkrdmlsct9JpmqnUYshn%2FGq6zK39%2F%2BkS5wN7pnp99W9MlJrM0lpUPpf9U8vl9LvL00e4SszEV2hXjLczksFE5vpCsequpfFvur%2Ff7tLun6tJ4qW8ihuOXWtYuD2rmSlC6cVIakoGr8K%2F65OtniVJeLBubuHffmopjBDDomRp41MhFxUKQTgILdbnQEC867BBmmWCi9Zo2%2Bgmeo1iBgNXgofM5rweoRwwteHBygY6pgFovuwyuljZ4DXkWALctyQsDeMALUcazO07auWIwa82fzBwY7rIXySJxCxCS1fqzlUNHkJr%2FLus%2FcthHTWsM9z69pAvntPLUn4S5tWFOcp5Mjp39hjdW6vi5t8z4s8SHLHVjYOFnjwt7TNFXuMTF7tniuN%2BuHJb2LeUvzFeL3ykn3YtUtwWWwVo1zJ1uUhW1AwX3bVkxpM9qS%2BMqerTZlZrgD68jC%2B7&X-Amz-Signature=a8c857bc6dc23e2a669bd447079af9960f297328d7a1353ca83c21c33b039286&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

