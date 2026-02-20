---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOUSWL24%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYEqdDCEKkFCJAhg8iB5ZO42gUg8WCkYHd8sCH35n0lAiBPDjVlSTsjpwXJ9Vr1O%2FQ0F%2F0mikNOBc8JlkqYyqjsPCqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiHeVaafD6%2BB%2FymhhKtwDPx4PtxCykQP3sVyLRT9InzeAamX0fjQ07IpSPY3HeHqpxyjHyLJ2WIEIAjluvwuLxRUoLhgFRZJFclCp%2FaWVB6VlHyjKUHwJP%2FiHkCmVNMGyai5QQ130fAUmMUaeAwnz%2FZqGDJWn9wX1l8%2BqTMZGpGEb8dnJKY0YlsferxUPWgF%2Bj5jtVz3WTlRnqNgfKMKqLIu%2BB1N17tFveuTwlm1u7QgmWH6MqvvHzXbZFBSdTpUGZUR%2Fw62ch%2FnNM0KXZxQFVKy%2BixLjHYGPsmWrtW1Ek%2Bvti3iFx68GofN4iAhu36HWkKZFRoJWfCIO3LiJKVJ7876WrULJO%2Fnoe1ZVJRItc%2BCMcmwJ3pKcayMPs6IwTSpXWIRg1tFPHT3HsJXmyDxbG%2FdAcaeJNCk%2FP%2BEAybMA3tSl61E77W9noHSGa2Yerv%2Bksktit7olemxFf7ENhn%2FoLzGPBUgG%2FgvTUWnBYfULWXmaiGsNIsk5zfOh0OLuMQh50D86LGMJ1pU9%2BpaMsEGzN67LwsTr7i1gHZgrVJJr8QJqNiXt0wNJ7pxt7z6Q36gQ9p7M4e1EXBSGNv6dv0NtFgI%2Bvj7Np0jdziIDiZVXFFJ8fJN4KLBwAoYuWkLPErppFR%2Bqpdb7q%2FhdIBgw%2FpDfzAY6pgHl0rb4w6xK%2FBjrtfSXNg8J3XPiT5hgdxfTRBdV7c3D8gG3%2FksKFSX7p7hfbsLg7%2FgGF5I4ltffo6leI9U7y7mpYkNbho%2FfJDiL7geI3I0mKzrGix4GzDh%2BcLxix%2F5e6aI9%2FOtp7MAB16Dk1ZLsGDWPW9wqzbCsXw88Gfbh74xdJWxKHgo8A2lmBdlaILty6wnu8lLRorw3HSuHzd2jixMjoQAixGH7&X-Amz-Signature=1c7c97ce737724113af65b9a3684327ef8f7dfb5e7ad76a2dae131a60f2776e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOUSWL24%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYEqdDCEKkFCJAhg8iB5ZO42gUg8WCkYHd8sCH35n0lAiBPDjVlSTsjpwXJ9Vr1O%2FQ0F%2F0mikNOBc8JlkqYyqjsPCqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiHeVaafD6%2BB%2FymhhKtwDPx4PtxCykQP3sVyLRT9InzeAamX0fjQ07IpSPY3HeHqpxyjHyLJ2WIEIAjluvwuLxRUoLhgFRZJFclCp%2FaWVB6VlHyjKUHwJP%2FiHkCmVNMGyai5QQ130fAUmMUaeAwnz%2FZqGDJWn9wX1l8%2BqTMZGpGEb8dnJKY0YlsferxUPWgF%2Bj5jtVz3WTlRnqNgfKMKqLIu%2BB1N17tFveuTwlm1u7QgmWH6MqvvHzXbZFBSdTpUGZUR%2Fw62ch%2FnNM0KXZxQFVKy%2BixLjHYGPsmWrtW1Ek%2Bvti3iFx68GofN4iAhu36HWkKZFRoJWfCIO3LiJKVJ7876WrULJO%2Fnoe1ZVJRItc%2BCMcmwJ3pKcayMPs6IwTSpXWIRg1tFPHT3HsJXmyDxbG%2FdAcaeJNCk%2FP%2BEAybMA3tSl61E77W9noHSGa2Yerv%2Bksktit7olemxFf7ENhn%2FoLzGPBUgG%2FgvTUWnBYfULWXmaiGsNIsk5zfOh0OLuMQh50D86LGMJ1pU9%2BpaMsEGzN67LwsTr7i1gHZgrVJJr8QJqNiXt0wNJ7pxt7z6Q36gQ9p7M4e1EXBSGNv6dv0NtFgI%2Bvj7Np0jdziIDiZVXFFJ8fJN4KLBwAoYuWkLPErppFR%2Bqpdb7q%2FhdIBgw%2FpDfzAY6pgHl0rb4w6xK%2FBjrtfSXNg8J3XPiT5hgdxfTRBdV7c3D8gG3%2FksKFSX7p7hfbsLg7%2FgGF5I4ltffo6leI9U7y7mpYkNbho%2FfJDiL7geI3I0mKzrGix4GzDh%2BcLxix%2F5e6aI9%2FOtp7MAB16Dk1ZLsGDWPW9wqzbCsXw88Gfbh74xdJWxKHgo8A2lmBdlaILty6wnu8lLRorw3HSuHzd2jixMjoQAixGH7&X-Amz-Signature=259465c054a894fd674637ed236f35b85f27200986128f62172a5e920f496960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

