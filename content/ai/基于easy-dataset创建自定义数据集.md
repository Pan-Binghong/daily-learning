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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BJWFA4F%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfiRSUe%2Fr0qIoxjDW7QDU%2Fo%2BGbwCnvJPKPgp9RK5M%2FCQIhAL7wvUkXBSylMObndTzeiDR8q5u%2BeJtH8b6BkiW9wD2fKv8DCHwQABoMNjM3NDIzMTgzODA1Igwk5LKOEskhyUakXOkq3AOQ611kcfgr4tZy68nGTcuDDbou%2FZ7gGxIA3v595W9KJkJ3O6WB0S4uzuSIQMZ%2F1zGaK5ZE7D0GPKEHEhd43WcdZvxR86c3QcDuNJLsYZEIC%2FZWRUSAaWDLrL14tmJOz%2FG30WnOG7UENA4AnjBv8k4vp%2BYBEf7XjrEKyDV3sFQNlnXfQSA7oyEq2KhlNLfx3hQ4VosquvEfkygpOnl5JJ6nYoUxSO%2Fz3w1%2F95uUiggF2A%2Fq4lhYUQZEk76dfihIGVNA8Mk4ICNifSM5TxSDEj32L3aZ4Vvmz5kMYc2Qot8phanauiwNRvRHHsL9y478fNjf8BtrPi7MTFaHFP8pB5NjdADgrMX8yKmj7Vv6JHtLbynr6O2v3bhb9I0ktvzHqjLZTJ5gFfTVNsov3m8p2d8M190zbazo6IUYNRnCoErhwd81rcro4%2BCHq7qoV47xJjRSCDc1jvFh0MtVvOKnA42ZLom15k58a9%2B6xQ3f8Am%2Bqwg0GGf0K0nqRjrr3hVUSUzd%2BxOtSKcOMWCUZFS2S6P8BPn6ETeegJ%2FlisQAgv0hc%2Fh9ANUDPXqY2blEipfzVtCqmLLF9HeK0qqesJeWVVx%2FzB8te%2BuLL4zvF0Ts9H5RPPbYj3r579CBQ8i2wjC44rzOBjqkARkiBT5GuvFXxGjQRpCGvO9pye%2FZxqto8EtHhjT7ZxYlbCeKY2oCTZ2V14iUwsGLZ59Up6QIHnoLBU%2FCySnvdcCjhy9YIboJaoDPw6FBnK%2FeSFNrhFdVxXveN7CbmYKQnlkPUBsJurHyZQu2SKzySMPDUES3K3%2BRpdCkgMwEwygQ8cwViKpE3hXnuKY8CkFTDdVRU%2FMqaKI4rCb%2FABMFjgp2573f&X-Amz-Signature=c15863e1662ad9c3a1df79cd350393adb855b6a155abe7d5aeccc830f990549f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

