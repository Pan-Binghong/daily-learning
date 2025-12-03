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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOGCG36N%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQCk7bBKLF9eYJQFKwB5funM%2BwcN1FZa4dVFrJc9Cgs1QAIgN6lPXD361Df%2FzYhBxgh51unqz6%2B0lNlBPjHjHuq8uvQq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDP0%2B7HReLM9CZkWYLyrcA1wmnrjsl3FHxsFdkAcWiXSwBKzCL8etcbPqIWHfWfQeDV8wRfqp%2B4981jdzLVYCeh8fB2LvZjgGSXWBnmk8qmcwc5goBtMIY4du01IYwHshgXCiPAvHUs7Id0%2BGqwHEMRA6HY2hEp6PIhacvvGOrlKitI7w22ZdccqAS6KoJwkger%2F9ky0%2FNCrQt2mfEyZvCj1wcVqJ7Nwrr13goCYtOIiwJNdOHcbdbDPwMD3eXtmywSWk0oxO6%2BeViKENKHP3YkXPX%2BUYelw1tmZvbKL1iTKDLBRS7aKtD1VeEDJ54v%2BH0Sou4aDlF1BRvT4bPTYuWqRELaUwBhCMC0LbgEbPdhmFV2UySusJkmtXVHvcGVG9tzhLM3ip%2Br6HlOirSIs%2FMQGPsyYc1BpLeG4VLLA%2FENQIbUvRS%2B5Y3yAY5IVCMnfD2Zb6XKi4lGw4BFbLCecdNzBp9oTiETPThRZXiyrHw3lIlNQc5bYuPsk58x5QEzQsqWCCzvUPXeCh1Z0inv3SkEmZLPEI6vpoBJzyahyEZY9CEUqO%2FwMCfmkYiWfgF5vqypBzhHP07%2FMXsqOPNra%2BUXntY4chCpYmhaSgscL0i5OxRTDFYESdt9oVw49MY3kPzumLjzouR6l7D0JAMKOWvskGOqUBNFyvEEuPnVj9DkywwwMXq7J8UBgReQFxpqK0fbV2hPToNF2qOrprm%2BiTbgACqvxfjuuJ16KzBFhxGhPeMpbH9QmNxalSbyQTY19ScuTPeHq%2BD0mcRDYqNBGVVPoWboQk9%2FQyr434FCAsHTjaFyEEHi%2FA2%2FU91f7%2BbAPR47pQpGx%2Fsb5fyrlZ2izqdMtLd%2F%2FaWzRiGi0LTslC0s1wISOmcoXc9Bip&X-Amz-Signature=2ce98591edf5a2ed5fe0485a34d310690ad8aa08cce64dd30b07158d63c158df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOGCG36N%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQCk7bBKLF9eYJQFKwB5funM%2BwcN1FZa4dVFrJc9Cgs1QAIgN6lPXD361Df%2FzYhBxgh51unqz6%2B0lNlBPjHjHuq8uvQq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDP0%2B7HReLM9CZkWYLyrcA1wmnrjsl3FHxsFdkAcWiXSwBKzCL8etcbPqIWHfWfQeDV8wRfqp%2B4981jdzLVYCeh8fB2LvZjgGSXWBnmk8qmcwc5goBtMIY4du01IYwHshgXCiPAvHUs7Id0%2BGqwHEMRA6HY2hEp6PIhacvvGOrlKitI7w22ZdccqAS6KoJwkger%2F9ky0%2FNCrQt2mfEyZvCj1wcVqJ7Nwrr13goCYtOIiwJNdOHcbdbDPwMD3eXtmywSWk0oxO6%2BeViKENKHP3YkXPX%2BUYelw1tmZvbKL1iTKDLBRS7aKtD1VeEDJ54v%2BH0Sou4aDlF1BRvT4bPTYuWqRELaUwBhCMC0LbgEbPdhmFV2UySusJkmtXVHvcGVG9tzhLM3ip%2Br6HlOirSIs%2FMQGPsyYc1BpLeG4VLLA%2FENQIbUvRS%2B5Y3yAY5IVCMnfD2Zb6XKi4lGw4BFbLCecdNzBp9oTiETPThRZXiyrHw3lIlNQc5bYuPsk58x5QEzQsqWCCzvUPXeCh1Z0inv3SkEmZLPEI6vpoBJzyahyEZY9CEUqO%2FwMCfmkYiWfgF5vqypBzhHP07%2FMXsqOPNra%2BUXntY4chCpYmhaSgscL0i5OxRTDFYESdt9oVw49MY3kPzumLjzouR6l7D0JAMKOWvskGOqUBNFyvEEuPnVj9DkywwwMXq7J8UBgReQFxpqK0fbV2hPToNF2qOrprm%2BiTbgACqvxfjuuJ16KzBFhxGhPeMpbH9QmNxalSbyQTY19ScuTPeHq%2BD0mcRDYqNBGVVPoWboQk9%2FQyr434FCAsHTjaFyEEHi%2FA2%2FU91f7%2BbAPR47pQpGx%2Fsb5fyrlZ2izqdMtLd%2F%2FaWzRiGi0LTslC0s1wISOmcoXc9Bip&X-Amz-Signature=2717640c9b35ca932bab08de4dc0aa0e9133255b1c486fe08a752e68936480cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

