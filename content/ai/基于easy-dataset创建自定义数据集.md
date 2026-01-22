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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PLMJMLR%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIG949RvQm5Zfgv1diH2FWsHSu3a%2F2CvWj1D%2B8fUgZKzTAiEAvR3H8tu1NSWXtyTM8V4Nb9rUl2VOPn%2BVXqa4LSSSBp8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkf07LkvwsB17TpPircA0NxaVcMHZkftGaKvE%2B9b%2BAMbyjYCGgn%2BOi4o7V%2Bw3p3BnbtA8jZvpuDvkilAvD7xRGgNKkQSp2IKatAmfmHKJ07lV%2Ba%2FaPOLtOxaGsFe4jqJSyV32pkpK5HcjHRYGOkDTLavqT3%2Ff%2BOXytQmVWJJ38GK3NkkL555KewxX%2F3m4JO17RFvIj%2F9rVLjQarAofFciREqt%2Fq%2FEukpsPoizMgBnUyKOWO1Vn%2BAUIQ0YJzKG%2BI7p9Irn%2Bsa1BlKteTJ6QGeKSruN05aCwNDlqFv8KBWwytT9aUVlZOJwpOCMy8vmbCUtq3RcuLNtVvuhD3M62CY42iSK9pa7fkz3OCpPwivF9JDR%2BO7UtP%2Fp3e5ob9%2Bu5R5EEhAVSKKmtXQrhp%2F6v4I%2Bko5sqTLT3h6ztjHfejWDa1m3ENwBlzJ4qi8R6Y4137ycqqzNp89HPDu3f4zWhEJrjM093%2Bzsk5JkRh6lrFuPzlvbRp09vA8mxPW0l7HpnfvMO47sL2DMKX7SzeEplDStbvGQMZ7sQ5Tdxyp7hS09u77s4Xs8nQFdwK%2BKqmtB8X0FNJwcas12d0X3tZn3t%2BCN3z7TyKHvz4H7f3hxwtd%2FN6ue0IMP%2Fu0LgFrs22hYVe%2BCCUHdE1aqyXkzOQMJzYxcsGOqUB2t%2BripV4KxHsuVwjFa962sD8QqjAGLGFqcx38COmC%2BEGHFmIBJOpyggGSC3MpZK0D%2FGnt8FaPLn2fYjvJx0FdupXNAXFa7ECnO77XK733InHUAjde%2Fl1wipGmkJz4%2BrBTsIDWHshYurddrsJwJzFD9w%2FA3XbCVYPapNcQJwfICD56araU5Lm3%2FW7R1lT5XkkjJhKYMgnVtn%2Ffv0T%2F6Ot93Sfq17v&X-Amz-Signature=65db96a6eaecd8179534ea3280b7350d460238acaed6c5a7d74b9e70b54acf32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

