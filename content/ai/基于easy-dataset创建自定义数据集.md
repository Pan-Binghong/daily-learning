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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6CMBKSG%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9DdCch%2F%2BsIvW5D%2BxaQg9V0jRQXPbjAMDp%2F3eVYI%2BlNwIhAOAgzteHb0TOi8yhZJ9p3HEPpx1mS13JtGuYfbKqsshyKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGjv4GH%2B7TzNfQgHIq3AOCmhqTikcL4RYQ2CdVXlPRgtiGXXrPF3tyNqNrOMqCYe2vL7mSncNQrm11swYS%2BnSCSJ1kY9sHJocoE1unJWHX60V6rDAh0nGLphk3GynWB1JQvcBsoVRhO3%2FG0n96UlQN%2FbgapW3g8gGNqsRaFTf5%2FmAMyrXnFy5JzKC9VDdFR96xCAZZDEgGRPMFA9ya29UFp9IJOkJ141aO2nDETRtpl3wJgHFogxIPInkBSnD%2BN5Po8MmJ3lNOil695J8dPehLvLwjDhRssu8RRb2sRzePQDg9Uhed8nLumFdu3iEqQFuoFANCF4LfulLpq1aTT942ZRdAN5Qbl9SaeSuFWjJLrD2s%2FEELHSmT5jr%2BBmzkjrq%2FZy0hf0deKR019hNV6iAXDwhBajU9%2Fqco5Xb5tP7YEyOFKoHF44nWZV3y0xYTfNqjAU3fE9x4nOvjHcm%2B05JW2rRYm937%2BsaEagZm7MGHKvw0mOI7oj94q0WdrJo7ZqtVAoEJJTwpjC1q4HFkmBjPyXsDKN6Wo5Gn6j6%2B32zzxywcUteQrqfoXEWSxNsQK%2F6Jgmqrt%2BHfZHGOfAyovcl0EhvwJgbczyAPsAit0zRXleVKSiOMPp5KeUUsBU2v0Hrfrtmli7tudRoTVjCG%2FdLJBjqkAQGOqFbAkCR1f0oZ43NFctssKiRspJ%2FJAigkDYmOFKak5tDMcMeOYWtpK%2Bo6cs4mO7%2FF9W46SZnDB3gMdQpeNIaYIrPYkkThlZRMVudPmS504oprfcnPav6JQR0LHofJFwXcY5UPFioGo2wBNlCXDFuLmc9uoZjmnG30lQU0R7NsiI%2FH4SqsR7WxUFULygNGCX0CPQeb4QawRO1jnye1sexJn7nC&X-Amz-Signature=9eeaa548fc895508d6a76d02c2c22183b84800e2e327965b171cb438b428742d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

