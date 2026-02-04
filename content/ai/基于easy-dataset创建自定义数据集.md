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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CD7XECQ%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD7lBJ6gbMySY8gPxFtSbWq09h6akAbF0p2DpaFaRP6xgIhANHT8CDFkgYxE5LQD74nm9xKyudyey8m9A1bsPLjHD2wKv8DCAwQABoMNjM3NDIzMTgzODA1IgyDGvA5UZywdHi8eXMq3AO73Xep6TXh8IuMHktuIun2Cfh2KXblPhyxgR8z0k7BBJYMQg7MHiEjzNF%2FWtujP2H5WIR8fa8U0BxuoOpAFzOakPsRqFBnZdhXDf5t8YW9B6Hfknxr39A0qS3GKnEHIbCr1%2FcRC6%2BZnOtZVt8WXx1UMQByAj7ZS8ErtXcP%2FVrOesz7VnKfb9imeJa5i5QlorwxCfbgK0oe79ExwiGY0EX9nO3datPUbUkRy2F4AIu10Q9Z7XaddQXMWED%2BQVwkcICFYussJhhDwrF00wYSc7iLoiHO8jV76W3P7A4rhHAKBCx5LciKHF264NRryjZTLO9YrbyNZGZlTIwNqbV%2B8sUigZpUweypRmSy8plzvwDRQdmum5GS8N2TgxKwGIIytx4kfcNHHNwIQDBAaFwob%2F%2FyMHnMrnMYN7mNC%2FkUWOrrzfdpQwdORIjO1D5ocn1xuhJvJl9C20VxMIQXznS68NxSFCR6CDnNuX9I4xh3RHbkB5OK0XmKGYRvhj1w7dqBJzkUZaVsmvEy7OC4tA9UnGC1KmBVhCj6AxDHZAhqgG7%2FY47oGOi5sZvDT1AxnxA2VQErmjzhfU78vVmf%2F5PCmoJR7qLGgUobdWlLWvPjmFggaJipjRzpRk4w6IePPTCC6IrMBjqkAREE%2BZgorCcOzxlXA9%2BUQvshDkFu09GD6AWoWjGxlx9YzlwfUuekC1pL5IxoYSPM%2FQjrCneDFuTVQpHqj9ZTXYz2%2BhPFYYYJvwvuK8rjue29Sw26566dwoiVSuyBsVpubBzGO1ppP5pRHPQDFRwHrjhd6g6B%2FAXZ2M4rydjrBrnZezJr5w8q9G2fvyvT5xPKYodPBpYcsc%2B795u3PKcdVWfaUfwP&X-Amz-Signature=6bfe8365bcb38faa1ea702f3d9d0f02ab04bf169a38f7b14d50fb189e79b5fb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

