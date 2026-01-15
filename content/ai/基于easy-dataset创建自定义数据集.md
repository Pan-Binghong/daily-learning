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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRQJ6V5O%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAW3d1qm%2B84IIyox3jTVM5D%2FsH6k8lnT4qfVb3iTEHQYAiAEj8FgdN9%2F4h8qIFMxjLTxvPQFsDtptiMlGlDjlLjjZSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMw%2FVDZoSd3M8Mh%2FrdKtwDKzph8xPEI5aeEkNjTWsrI5AAeuCMdVmOprcFyTAST8NPZpJMgeTtLFu%2BfL2er%2B0xSZlPYRFzLv%2FPh0jbh6bj06diIUtxrV5Cobkr4b3t41edwM9I7Bm2re5of%2BpJfLKLJxN6Cs0pTLHMADTTOBWRUx0klJHGivnnwpXlq8odiHzyUllKdYp3LF2qhdG2cSSXABsIStuPVZYuAMIP7NVKdO2KbSfVMF%2FdAzs23MvKaPSj6E%2F7huPyvP4wMh0QrmwQHX%2FJcNu%2FT5yEIMbdF83mB3MAKzXgK4WTiVq4KI0h09TWWxlHyzJ6EmfTfWq2eLopxFcf%2FtoQy9nPg%2FqINCzfEu94pPpnPOjwLrsuisknLUqA7te7MuR2FUbKEC9QhRPZ6H%2BjAwdvwsFUs7qOrJgdh0nQCru%2BITH9uK3Kh4TzlySVjMMvs5A3GrWMRiwqwejpHqYvJ2roggDTDDrv43%2Fxrpn3a8SZJWLJg%2F2wIAlzCVRuxpBCpRpX1z2B5S450ESZ07xiRZTz8S8fmjW7U%2FZRp5E%2B7JJu3YkyG%2FkAtwah24kLi0r9q%2BAF8%2FY4HSyGKG66IVi1NOJC1qGqxhZpPYLdr7050vpuTLFFNAm5%2F%2FG%2BUh%2FN4DoqZYOCaErHp74woZyhywY6pgE9T%2BTEyJH5TkXb%2FaygG98taQDm%2BJIcWLtd4XkU7v9yJm3R5bsUkB55Bo%2BS8Ij8gasxgq85aYTUJVQHPzJ%2Fg6vFhRct9cNDyjUp7TO2S3QCxHW3XyCyyoWm7LWd%2FuPBc1oOpi%2F%2FuDx2Ycd8ls968%2F0%2Fpb9fdZoeXmVul1HVRl9pawpIVd7fr4%2B04O5vXWWdKGwABi5RioTDnCGWk0GVCLcWexMZYlCL&X-Amz-Signature=cd816ef1c70c526e1848274befdbe5729a2cc4361ae85c15b6fc03a5b751e977&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

