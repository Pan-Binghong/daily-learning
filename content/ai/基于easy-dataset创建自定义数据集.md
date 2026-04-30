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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNKZVGBZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQC30XPVd0lElFGsoJCn0shuS16dVF2kwFRta5%2BJsZ9PpwIhAJQLK67D1riSSL6gcb8pj8Oi8S0LbItHTJBF1kWkmJGvKv8DCAUQABoMNjM3NDIzMTgzODA1IgzQnyzMWCL62iQFf7sq3AMlrQglskHcOY9%2B9VKTY%2FLbxEHXd1NflYqgenR7tBEdHmYkiUmZDcoOG5nhJ1P6e1qHemRslaZGW4sLrcqP1QCyGRAbs7Ni%2F1bjVvFO5ENzkebAUpJHkWL1UobIv8ZF%2F5KQzEYd%2B%2FXDCGbEB4T7d0xnlg5cUrwglGm1pXSp6P3sdGrnZ7a7TT8zypZ%2FjT%2BbcM0QuRJdmkJxMoYXL8i54XyZpj0p9wbaMXHWcTEE7nvNeMHCp%2BmIZLQ%2BzuyEH8k9t38muPQJvaU1nEoQobOLxVUUG5YQplCaYsC3LPg4y1Ml1z1oVTKl79B7hZw4jkhBd78EYC0Ef5WZ09H7eUBIXYSr0XzRVtgrZHes%2BydALgOPBTa0wnKMefC60QdeBRXdJzDiL4lAoFXzrFk2%2F4oxbJPfZ5S0ymQw0icC1TG0CTy387Cv7uZGJ8mcM4Z7oztPOnoWqWbeSuzznSTV1HwbBcXDLKZUjdw8%2BlcAvqXhT2v23uiknG6V2FK9vXLDaCzN3pEYWss0AHKNoeRwrhIzKdDat0O62rEjlKc%2F1rh5fA79tAYEulgZVV2qPYyM%2FuTD8mlUtA7VmEVegBZm0WBvpWBG%2B0QKW2tkfVTaDsQia0nxg%2BacgFlkPM9WkJfU9DCHssvPBjqkAWdD7kXkttQD3Cl%2BKUr%2FUZK%2FiMyUlSROH95sNj2Uvh86W3QPTrZLfYqyfBU%2FFAjCutfxnousXQwtwhunWislSkJvlHfotAD8TLlmFQ7e5pQVDLsLKUgEPKVnF3EqSj75D6hVRZke0JrjLeUDwffkQkrT7IuXtKKwEFeLSULknbHdiGA0mnSE7vyQqpfCR8vCH2JgGleNdTjrSWaEK7ssBTfXJR%2FV&X-Amz-Signature=65832aec349308f1950a1a1a443af043a987c6c5626d27b0d24b254790f50a90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

