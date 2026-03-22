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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRLX7F7F%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgOav8Yao4KFNwiTaBQl%2FwJk2%2FwaQKNug6kd8khSNRzwIhAJPmxBb%2FhFXxGme7Yn1sJJ0m3WL0uvXtzqUH27jBr7u4Kv8DCFwQABoMNjM3NDIzMTgzODA1Igybp2Vs1aS4hd2Dlgoq3AM05nBRHxcIXGunG8ZSZxo4MXomjvPrivrum4qWc7s8Ef1jXnAduKjoZj2taZGvq%2BEzJzR%2BzM%2BqDXSA3tAo%2BgFsKrhJJvaivrYUBcpzZF76wBzo38YKd3vgeKM7K9z1Yko2KfMXKqwdcgkfJv9XTqO8wkAeM1V0S%2Fkd3VxTUKxqKNN3sIDqTOk6JNHIwMfAQWqCSB1PoW9m18VsiJd0Ha0uS0oxS2VyM4GJUlzdUynCKP05nRFsKVY%2FlOmd4NjIHrs3L3gCnXTdA5dS3mZfsTWmkzKBnP1rdOrufhrR%2F1wlKiUjHIms7PdZnrkew97IqNhJzBK4kdl%2BlcaX%2F7JAneL8EScgeKXnuZcTJBJ0dTC3RwswGRQwXa9cvRTjg6ETEkGrVAxgsp8V%2BN5Z%2BWl4ZfTdlQYgpJ3WujpH%2FM%2B5m%2B9q0zhaGtrNW%2B8XIj1Bt%2FuTiqs5D%2F7Z3xHgFdkTJ1xSPklkxfuL0thm7dgMn0HfoIN7riAARtqTcDIQq0BE2hsXRbvgAHB9yS1gSWiaBKRSB2lBa3r7ODOioXAMMA4sQ36z1d7U3%2FLJlprW3Ipc0KrlJxJmML%2BRKamaLpH1A%2BAAPK6FXPFtaLkFccEkQuKUXDyjSHokEAeMYSKNbZuEITC%2BrP3NBjqkAW6jZAvOlT%2BDpLPpXVA6PWdehBXe3juj%2FVpVeK0GCJX0v16xfx6Vijukge8BvZSf5NdTst7IkO6RHrJj82t7sNezKPSGknY7zxGCz56TpmZfdq737i8iOv1QUXs%2F2YrqUz0Yp4wqGNgUsxWE9IZ3s7oAKraF%2BUtjpmZjpTGitRgVe%2ByroYKzvtgWOUm3515i1o6ab9AEo7wMgt5BD4Np4woAhbFw&X-Amz-Signature=263407f76a483a492d94e93faa7d6bc43b2179ab72eab4c3d5d5f3438dc230c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

