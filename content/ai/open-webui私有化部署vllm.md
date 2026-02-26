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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYJASW6%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCPAUUsThRS%2FToLcMRUrW1cM%2BCAVlO%2F5VrU9Ymg4jGGfgIgXFDftwCnmqATmbHQjDDDSLU69Is2Ownv93uZfPybNL0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDKHKNpJTGocQBCotHCrcA%2F9uljdtkuILV9WXMfhp1c4w3FbYUH6bpspf9VJB28f1vyvlr0t7f2Fc718kSHDHzEXAx5ByG1pI%2B3WCFu3mPZ4lWq%2FNUuzoZ1Wf91Hk05ohysdDcqB4rxgsfy6ph9Ecz7XUbauftkMyLrdBjazZv5lx7Mf7TzOE%2FWn7NyX4f0TbcogDB1L987%2BTOsdjJ8Snn1EwuID88HkzNAVHg5XoyjPbxQKvNTXfM6DXxhj%2B1AponPtNL03ZC8hyCKQ1gmCNq0RCvu%2BWktI3%2FnV53sX4xynyxYQfHE4xd%2FzxhFlHkUJKAwNEQK6UtIHoXzrtxo%2BR3Wy9o%2Bd%2BlTD9GfYS0Ts1PnOeQTaOTlR4%2BCYcsLvfu9UU2kRrxwFe79YDFzqTpO%2BIerKEHRD3gyZP%2BRS6XyIkW4bqNeqbI7kX1OPH71rN%2FTmYIKckEMdhECvHsJjT%2B7wK9yT%2BAsqcNXCl3cXCDT7SVm68scO2siS1MCFHsqhbCuOuiNNbCVFkD8nbkTaJuCC69XzupgMGUCDk31hEUVxvmVFibkuR3VNZP5VTPhXTy9UWFyS4QBVdkNxW0bCezecQ0LKYEfSV8YHNwdekqUHHeMQOFoGUZYVC2p96OaGT7J43Z22F9gATLc7xlM8GMJ71%2FswGOqUBSU6qs97ZyZcIsEAUKhYuDoO9Xia2CqZEwWce%2FgmNLDgElSBDSyhHzO4i8VFjIZIuph7ARiXxapJzg4PXRlYe5NV0TwyaN8WO5BddlunMv4NqZiM5yGYsTbFOYIjSanGaEuw0AcNpmEX1dYFefSwpIV3MfZvVfQZkeY6NW2O6ej94jL4zrjRteu%2FM%2B72CwDR0WM8jjpvfit8%2BiJfh3WpTA5PkwzX6&X-Amz-Signature=f11cd8315523173cd6211a0d951c59b0f6ec87c74c2d24faa6876217b04e0e7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



