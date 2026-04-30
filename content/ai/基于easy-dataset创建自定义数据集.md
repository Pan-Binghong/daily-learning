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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ3MEEJN%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDf318m7rFxF8VPLX%2BOl71EzbEvCn45IWPRA6HrEZVMHgIhALHZDXzxE169JhhbxN1izun72ZFjDOrSggfkJvxfaFhxKv8DCAkQABoMNjM3NDIzMTgzODA1IgyCJfGLTnmaLcsO6Fcq3AMx8JV5QauGSyJ%2ByIwv1mCETHVd6F6l7WXtWzQ90dOM6QiUjY0%2FPxnJKBfFOX2FEXIXaDktVVRuPW%2FsXxPf2KePEvW2aQUiVOjVNAgwo05awTAap%2FZYG4sbZ1nZ99iub0Nva3DWIxdIBfRI1ERJfLXaUEMli4HxQ49wZ8uZxKF%2FyLEv4wOTQcUq2HF6qQ260EnKOrYwwmsH%2FXez2YBusVjr8XvXmTqPQt%2FfTVyoBRGARo1XnnwhRfeiXUt8nrBtvE7bY%2B0lFoEA8DnMExEyvw1jTqwd9IN2rpTpsaDjGCnlmLzmW2FeYu%2BnYEZVUmcefQfNXVEBtGOJzJY5%2BIAhOy4YAvkyPHQElVCV2TT6qtCK6MoK6gRSSTTR2gO1vXAs9lRmJSKnWbHjF0SYGKFCPJZGN9yP25P6eh7D2L3ZX2OMlZoOJN%2F%2FLRAkwgJ%2FagkBr687nWuSoZwcJLhnRM6mhct6A7qS%2BUBt2Q3mJythumfosSp5Kpifs%2BARKgDCEzFNH9AzUVe23S9becaUHUDYlRXKLLY56RAZ%2BsuTbPOFWoz8f%2BST1UfFftuxid9d5j%2FSAfbQXQ7tm6ydJ%2F6n2MT3FkHc1VRASAFLNm3WeAd6xFshrbnCPH%2FmzP1NUZkuFzCqm8zPBjqkAfRQO9041FZmRo9GgWaZ%2F7W1v%2BgEjSFDdcrsHfIUZZ2vwzSM6TMaPeavA4gTCMlIeiP2tCHXLsqD26QnpYBES5ipYYnTXGvX7AEumZwJpJGUxSCHtHb97vhKXH8Awq%2FXPLD5vPlFuNRDS3cFddhjS%2BlH7ZxfB%2B1PbwV8UQsZ71GG230C9R9WFdDP7UCWEDMFhiQpKFXktEdtpNnAZfUIwI%2FIxBdB&X-Amz-Signature=0a21b2b9c6ecc773a1ff5aee7e19aab1d8087c007cc0733a5f9e484ea5940efa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

