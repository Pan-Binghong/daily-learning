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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Y7QJWX%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2B%2BBXURiEiMeIXznrVC2LX0WOandzBYfrYRBZZ6tsbrAiEAi4FbIzBplL6raQ2%2BRq7tCb5PxOOUjhe7Wl2TGT2BLToqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG4k%2BzrFSvEJuIXCKSrcA7STst0qpfEM55ylPqK7Jv36L1xSmiJRTLQvQGgPGhUalFmnPTwqogjN2yWMtEZiXmuZzMO5%2BVKiFJalYrckdkyuLAlxO%2FiCUy128EqIKnnQlkZYhSDNCcJmVZhECmYnQbL%2FQ7IGIHM8SALtw7wVOKLWg5HZm9Cpk5EAj0ROjDdlNc4yuAFfIuIzO69t8q5aamOvelMTgEcNlWXH5GjwGWIbFpnOBkLm%2Bc1kyNvEurO1PgJhlSL8oWrbHzDmKoQy2RVDu7MCCFjbhFH8r%2Fnb62%2FAyaZXwVDjByL%2F0hgBhJ8QlqTbSaXSty%2BZ3yxJcbiV9yIBmnDMg1ThmMlAKlexgewmQyECF06iWFNu1FMWrwPVQlv0KWxaHanWcf7XTQ59QCVgrzuNX7ytwKfu5xpFTiuDZHpoBEMwCU5JdrtntAjYdoiquhe8qQeGvnMi4qQvNdpzIJ5EUm0YTFhyVneqjaL8UQpGbvOI9H3S5Qz1HC6DdzoyO3zD5umxRzL1Wz0cqU4u%2FDKEUJIyBm5SZ%2FFd8d3MekVQp4vUZnk1kgaXSYRfB7XP3bN8EEch8F78Fu0EqJQxpZkADNq5uezWpTm1amweGwpX%2FNbdcBpVRX4UhZan%2FjlJvTuCfVYy5zLUMJy2gc8GOqUBNRn4aSFJYv%2Fa4t5zxrdaSsfegL8GXTxn55%2FDINi2J19tlL%2BEVakgiulnQmcv%2Fl5J9D6h1PF5mnwTYgOxMGvUM1LOkNjGYJcrbbYnSOV9IDBBetqNktMRIGut1u29eorUYKpkKrnGhzcC%2FIAw95fQfWJ%2F7oCVdIk944WxGBNbZDlDe6UqF6iamv0aAkswc0zsFEZOBoefnXN3GMoUXNa%2B325wW1ky&X-Amz-Signature=791942cd11fb3795a71a4fea0c6d128bbb172c821be2216dea5879627230d379&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

