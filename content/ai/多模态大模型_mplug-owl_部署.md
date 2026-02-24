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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YJO6YQO%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQC8XFvm018Ot%2BNe5BkFE%2B2VnngOPhurbZiJOZRYnV8ltAIgWIH7eUfyLULVHfGmDRdqydwK2I8MBVIiwZMZVTM5vuIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDARpUbIwbmTSQN4HUCrcA8tOPNXMONHLeXGLC%2BxRwhBwPogCmHuSRu2mECRArMauAM1l4mih%2FIvVAzoGPh%2F87sepI4ivkwnhVxD0QvOHlqFdAPk5ayWgYZ9lDm8Ah1pxhjdEbKEWc0izAaDWjhwxlGetMlWAlOwJlThnzz0EkkK1lXTii7ohHpuRwFpXsX55nqlbuLpWq2TTvHbQnDLyKgObFqVycgvi4%2FDV4TsFBscxQWtvEZ6lDzHeE4gm3ge6puHsy71D9YHAkM8pA9Gq%2BulRXPAip89mvFoYB96RZzQiVf3oADpTWf1xtdJsyC%2FFrULirB2dMsLJFIZ58Pyetl9%2B4JPE3hxO1P0CtpUSh2b4Imij%2FUwK%2BQoBDxfQxVmqwG9Yy6pVXKKBM2TVvemlgBxhIIRAxUzzbG%2BM4IXtOmK8v1ZzaCEpy2C6OleKDw%2BRBzMwHpERVWl9w4JBx4DNvb8LDMJ4ywNz1JzLlv%2BPDIM5wiAnNccxcfhJ7OzHCawfyTPD%2B1gy4rv8EtwvoeEcWtGcNVWbBoHsu1lyoCcgb8SJjxTkpV4qvK5ffakqctXEE%2F4Vcqy6A2zX1J8FMiw5sEX0ru9dwOW2kpQ779rzvuXnBi3PYbv64hf74mNZfdzm0%2BsCGn%2BthjR%2B2PMyMMK19MwGOqUBM%2Boj%2FFeW6vQSR%2FKbUAIiIkHvaZ1oOAdywX0u4QES8nMejPhGGHOeMwqrbV7QM1RpmYx38izoo1pjQry1986vF0uzh8fJjkGSGTj5WNxF3dYKUEZeKCcOXN3SUpINiXE5lNuIK0UiMNUfgMM2Sx%2BHulhGpkCCMrEuAT%2BgNuZZCpiAG%2BkrmKsKxLFZMwZ%2BnWwJnae6H1Qu%2FWkT1L8FwQlwz6aItcqy&X-Amz-Signature=84b499a8c6f9f74e243352b78b7fbaf06f12209fff27b193289f95964b37a319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YJO6YQO%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQC8XFvm018Ot%2BNe5BkFE%2B2VnngOPhurbZiJOZRYnV8ltAIgWIH7eUfyLULVHfGmDRdqydwK2I8MBVIiwZMZVTM5vuIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDARpUbIwbmTSQN4HUCrcA8tOPNXMONHLeXGLC%2BxRwhBwPogCmHuSRu2mECRArMauAM1l4mih%2FIvVAzoGPh%2F87sepI4ivkwnhVxD0QvOHlqFdAPk5ayWgYZ9lDm8Ah1pxhjdEbKEWc0izAaDWjhwxlGetMlWAlOwJlThnzz0EkkK1lXTii7ohHpuRwFpXsX55nqlbuLpWq2TTvHbQnDLyKgObFqVycgvi4%2FDV4TsFBscxQWtvEZ6lDzHeE4gm3ge6puHsy71D9YHAkM8pA9Gq%2BulRXPAip89mvFoYB96RZzQiVf3oADpTWf1xtdJsyC%2FFrULirB2dMsLJFIZ58Pyetl9%2B4JPE3hxO1P0CtpUSh2b4Imij%2FUwK%2BQoBDxfQxVmqwG9Yy6pVXKKBM2TVvemlgBxhIIRAxUzzbG%2BM4IXtOmK8v1ZzaCEpy2C6OleKDw%2BRBzMwHpERVWl9w4JBx4DNvb8LDMJ4ywNz1JzLlv%2BPDIM5wiAnNccxcfhJ7OzHCawfyTPD%2B1gy4rv8EtwvoeEcWtGcNVWbBoHsu1lyoCcgb8SJjxTkpV4qvK5ffakqctXEE%2F4Vcqy6A2zX1J8FMiw5sEX0ru9dwOW2kpQ779rzvuXnBi3PYbv64hf74mNZfdzm0%2BsCGn%2BthjR%2B2PMyMMK19MwGOqUBM%2Boj%2FFeW6vQSR%2FKbUAIiIkHvaZ1oOAdywX0u4QES8nMejPhGGHOeMwqrbV7QM1RpmYx38izoo1pjQry1986vF0uzh8fJjkGSGTj5WNxF3dYKUEZeKCcOXN3SUpINiXE5lNuIK0UiMNUfgMM2Sx%2BHulhGpkCCMrEuAT%2BgNuZZCpiAG%2BkrmKsKxLFZMwZ%2BnWwJnae6H1Qu%2FWkT1L8FwQlwz6aItcqy&X-Amz-Signature=a044a7a54f52072b483af8306df960fa1614f4d97fd6cb4aa904874ddace2471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

