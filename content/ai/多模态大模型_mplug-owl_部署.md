---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
标签:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNTK2X%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDiqLDcRC9UwECAgLpWovnHU3mspgW3VuX3NPmB4Gcb%2BgIgJVu%2B2NonF1CYgEmQu1wfs%2BtBy2OEn6w199GUQmYC6MwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0Z9bMvI%2B16XQGK4SrcAxa8GVMY8G7DwjiNlI36cio6vO8r9FvGL30wIvI1R39PF7vLCGgsaJgFeqRnG5jxsyFB9K1%2BonCEvQjQ3EAXiNzJlmOYZ7xgWTnPLKFVGbX0BkTzK6qMcMKHR31TO6NeZZhGwoLOwTzrzTRBwtngIOHLzSoDQaeTLcCDOqAodDhiomEPZWIuod1AI63yqit3PtnbxInI%2BB%2FSRar2Jnjg1i9p7039JaRT4%2FqFUPXfYcjRyU1aZHj5CUgDSpse5oIs7Iw2BCsf34r7CBZbOKcj6AG3LaWqj2%2BZfjASmIYfak74K1ZxTfsLVHCM0QP%2BEGYj%2BWcaovlMIKVkJuvqbkdIs7jqrqe4X6dAOf8SVErwNnS2jRDo8tG%2BRIwH3jUAJkC5pxI4d42WOA9MoIawD6LrYzsjfXmZ2AG7NBzOLmRZlLWFCw1T80PI8wvTPcrmb6gGFICTtlB4tsc9zulQhGkOeijulNDlx04YwoTLuLTdhuhjgZf20O0tqR0X7n7fzYuASm5oXz4UYy0y34JW8HH84e3R4zM6pPtA5YSBo5R3uCR2j9IqZuec683%2FBtSEjEeyxRQ%2BX1jY2o6iM9Z7XS9HC6hc7SnM%2Fu5%2FUyhXS66qGCAu8j8mNeftuibL3ZbZMPKirMgGOqUByTx3MUaXtm8yKW7cLRlx6yGV0nwNsSMu8ldCkbHygME62y1B3v7dLmPbk9m71pNgs%2BmHWJ8JGsaVEFvHAXkbCx%2F5Wv2IrLzJlT0s%2FJKQt6ijiJ2kV7P%2BtG0EBmMWcvd10oxpyq5XeQXLcnwXO2%2BDklfXAZqAWsqZ11epr0rYI8n2ACCdqx%2BVqjSWiYqcJRPg93J%2BXXOpPJh8uPBghYbMqUe9ceTQ&X-Amz-Signature=4cb155022b4cbd6005c0a9abc098a836afdaa0cf2853bd04824f8fc826bc1b6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNTK2X%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDiqLDcRC9UwECAgLpWovnHU3mspgW3VuX3NPmB4Gcb%2BgIgJVu%2B2NonF1CYgEmQu1wfs%2BtBy2OEn6w199GUQmYC6MwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0Z9bMvI%2B16XQGK4SrcAxa8GVMY8G7DwjiNlI36cio6vO8r9FvGL30wIvI1R39PF7vLCGgsaJgFeqRnG5jxsyFB9K1%2BonCEvQjQ3EAXiNzJlmOYZ7xgWTnPLKFVGbX0BkTzK6qMcMKHR31TO6NeZZhGwoLOwTzrzTRBwtngIOHLzSoDQaeTLcCDOqAodDhiomEPZWIuod1AI63yqit3PtnbxInI%2BB%2FSRar2Jnjg1i9p7039JaRT4%2FqFUPXfYcjRyU1aZHj5CUgDSpse5oIs7Iw2BCsf34r7CBZbOKcj6AG3LaWqj2%2BZfjASmIYfak74K1ZxTfsLVHCM0QP%2BEGYj%2BWcaovlMIKVkJuvqbkdIs7jqrqe4X6dAOf8SVErwNnS2jRDo8tG%2BRIwH3jUAJkC5pxI4d42WOA9MoIawD6LrYzsjfXmZ2AG7NBzOLmRZlLWFCw1T80PI8wvTPcrmb6gGFICTtlB4tsc9zulQhGkOeijulNDlx04YwoTLuLTdhuhjgZf20O0tqR0X7n7fzYuASm5oXz4UYy0y34JW8HH84e3R4zM6pPtA5YSBo5R3uCR2j9IqZuec683%2FBtSEjEeyxRQ%2BX1jY2o6iM9Z7XS9HC6hc7SnM%2Fu5%2FUyhXS66qGCAu8j8mNeftuibL3ZbZMPKirMgGOqUByTx3MUaXtm8yKW7cLRlx6yGV0nwNsSMu8ldCkbHygME62y1B3v7dLmPbk9m71pNgs%2BmHWJ8JGsaVEFvHAXkbCx%2F5Wv2IrLzJlT0s%2FJKQt6ijiJ2kV7P%2BtG0EBmMWcvd10oxpyq5XeQXLcnwXO2%2BDklfXAZqAWsqZ11epr0rYI8n2ACCdqx%2BVqjSWiYqcJRPg93J%2BXXOpPJh8uPBghYbMqUe9ceTQ&X-Amz-Signature=3c8e9447bf55dc29c51e90aeef368a81aa7be8675a47c6a80d10f8101b932c4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

