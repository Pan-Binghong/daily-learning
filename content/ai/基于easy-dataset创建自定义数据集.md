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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS7FJHBC%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIBaoClnO%2FwjER0L7YhYk%2BN0EwKVx1mqs244yHu3GKtRkAiBf1igxKGkBnAJ2%2BA59dfHCJbGCqhe4e8GBTUlMnH21mir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMu828n4RoHUB2hJaWKtwDu%2BGed8geH8ZxV8KVVPeZRy%2BufZlagfokDLY7puurGWnOqAfhTHKwl7lIKopZQ7H2hMFIyY1ZRABTpD9ZWEZQSQb770WrHr53rksjFmLx5c%2Fkfo5lCRvBHUz96PKcVn%2FXir%2BLLwf3C%2FzfP8OGfeIUvmsx3G%2BTzIX1cIhTdD6nDInhClSuCEbJp%2Fhp6WxewVLoFj3%2Bklu1xeEoUgBbijCeXRHJ7io6ciahqp9kz1qDf69LmYSF%2B5ieHWsrqRO%2B3VDMTA%2FnjPcbewxXW%2FbEmGGB0flg4%2B87KSIR9L2%2FSZmXA7Ts7loLDvGYWon8MEAoq82vkYvcBT%2F2OBeTMoYnRE6AYXEEueok9IGOQ8G741O8V7HUAukgxCwhOKXHMee5ywQWmrqpEdPdX89sbVcyNlK6SxxxYyQNVzlgToVK15O2VG7OJP4oP%2BSCWuTj0tbEvBrGLnVavf%2FmYkXyORqvJfaYFiJdierUuPrbjjSmnGcD%2FJwa4jtSJIcXxtacf7Z1X9gCacLhoqjKrndKiFO6ZXYfe6Lij7mdKBR8HMqSpX%2FvpZ9cySZJURuem4gA4%2BDzR6u9p5%2F%2B0vocT6pr3lldfk35HIHbYW%2BdwphD2%2FNmlEUoCP9kozhyNmSRvGlvNnUwq9bhzgY6pgG5t7leethcvpm7cB35ujceeG4FUcLiUhTc87PzY09tX8jXRGAM5P8cCpqnVqJv8Po7%2FcxLNGhiXT2MaJLJf4dbanZwbu4Hpnf2KJrY%2BhVbrxVRd5BKJl17RNGnl4ovoRj0ZEnVZLzAVLrVld5PlHmX3HXpOrxitIF5vqc6uiD%2Bl05Fmkk9o7HgvTKJvKD999EYoTR7R2mI0YuJOlavOKaOU%2F8OUAQT&X-Amz-Signature=fe3a38797b78efebd4a4841538942e5c3b503b1cd2aee369437e034c1aad0264&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

