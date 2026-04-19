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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XHDSOAA%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCkAHMZKh5Yzr1CyGURuA1sWOo5qmiMW8AR75QN4oiHsQIhALWY96Knl7f3ZCgfynDKthSgBHrzhiF9U%2B7PFuoqdi1rKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6g%2BqeiyTjNDbFa68q3AOcbu7X%2BJi230mlVdE9SiOs0uJkcXJZ0kQTVbTZjfe2baG8sClVMAD5AaoYNR3fO3%2Ffscas2bV0Z980sTUo5HZu4xK5XtM8s3QVOEcHyp7Exla3hebqSpjZOThxfjZe4yVcIWVkCbQEOUFUPKFEEwoZRQMF5aTfUFoSsCZvpg5b%2FxpP4j6ecLCeR5I5oPxDwTH5SCAM2EvLHhJmzjM%2F8ZdmTk00apxkLXcABR0zNIrEa4mv6wOg7PWfET1Vvp4%2BQIgdiqBi4Wl9oQtIwWSGhNR8qThoKKZeilv%2BZtLUMxXvBbO9YvxzHIL8aVexg0gmpvgMDCcdGAPz1YjefQZ3UCMWS75y9qX6g2dlsK2td2LtVKdRFjp1wk6MZHA1ELO0pLaxSN71nIwui%2FIornRsYrAGJrxWXSUHL5aDIs%2BTPlm27lFvtU3nRA%2BSSkgohmU50e4WNbMhdr%2FyqCRKzIRkb7RaHViXhDxBPOo3hcUYfVVQ%2BokT%2B6RID6fDonjwinhkNoXez7KOd6ByIi%2BiB81RRKPMgJ2aAFZlj7R8I0xsE%2FJWF0skwZlk9S1gdCS8WJcVctK7huo6JT7WsFJ6b1ers5axNQi%2BwYhwZukQ3UtofSVPAh1%2FMxAb%2F1SDdVcLejDj3pDPBjqkAS0Z%2BHhwKTJRoJuvV0YPpW7XH%2Bvq4Gt9nrUpVRe2JMTIdhYyIMaI8vyWCqYEm0OfMwTvZQlhlOBIc7zE8XUthkR2UloLFcPV%2FULq5on4Eqr%2BKRM%2BdTqSPmw2fG30H%2FX2A1z%2BibrM2acGAIyeACXulwC%2BEPRkbJV3ZhaIKu6YHIrHH7V2VUY4PA2zhR9u%2Flu6ZHp8r5ut4SvKI0y1hMicSj3qIcCI&X-Amz-Signature=db13005034ad742ef65e669670abf45024ef6a2bc0135fb45a5d85bbd04579ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

