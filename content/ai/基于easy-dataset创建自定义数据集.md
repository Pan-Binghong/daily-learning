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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEC46EXA%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQClGIERSoBLS3XnevLlV9hEBoRWvk4fWluD95rJNmpCTAIgBPl54sHf5KqcbUtMfB7sOxv166NC03AVo0cp7jeFjaEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5wY8paP9s6YvP1MSrcAyti6pXb2JkHf%2BdKgIzCjRBmIXQA%2FtMQ7uDzrhCROeyh4AawfBcDz0JF%2BalrKBTDe%2Ba60s%2F0vlkNKfBdCDvaU%2BOe1yXr9149MAql8F%2BJFnBnyBDSfOTKxvEH8VJVYmVEFFRtR2in%2ByKDWtKC%2BydFV3UOKNT2fnm7rwNAVCp6DW38EbPsFjezwdvmGXnjQzDXoXsemu4m9TrPfaE%2FnJahkW3dWkrOg5rRN2VFMrM8R13oKd8qMohKBydx0Bu2XDqgFw3j%2BHB27DRIAMPcjW0vMBTxckmLCVBm34Tz3VQACMUQFAB0OHFQiZZ0ENciJVH03aoJQxBzaR%2FxgGxDpdtr3uF3uvQOD%2FpAbK%2Bu%2FZgH6HctIMF%2FRitAfX2MuA%2FvQPyCgU4cTl74ey%2BYa%2BPW3f%2FRI4fT4yjBqCFUTxGyKUq9jUGAfUDdNiaDFTCKRTg62cX6OOalR%2FjZsRnUu2HfHojRo1jMHCK%2FwB3UnaxMZq7QzpbA4qnrBH18CcUmx5W3m8r3kupn3SVMy4icUJVLJ367XvCSb5qQMoipsKgkwIv6kGjUXkhf3gNkES9jsIqBZUUbH3IpcX8kkpLK5ZUIterSLCOglrcCXHgrQYetzihQJgylespsHQXeQ9TDQCfEMJ6si88GOqUBancKIv62qup9J57yMqW2RStL%2FFcxW%2FLm33NUv%2BEcdn6lWHRdAjoVEm%2B5yhi91AhORa8T%2BhVBE99F0ibfOh%2BFCxWxL2fKdmZ6iEohyedRB1NCGnMiDMk%2B28zVYgSkhtrtKmF6tMjkWqCJPVe%2B3B5WluMkm6YPSdlNj9CkB4LdveEgYkGkacKN%2Bzd%2FaPuMldXIOsZ6DiveYdKyy3mAHHwZu8JYwo%2BO&X-Amz-Signature=edc46aa0cbe6746ef4ef4b6f3710db2b85db2d749c16dab8d61c31892f6eeca9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

