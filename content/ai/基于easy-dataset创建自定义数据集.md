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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEB2VQ7A%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcn6nu6PqueQQNLkoPTRmg90khFsoBSIPa0bm2yvgCBQIgH%2FMrK%2FqwqWkWGVMOpLzCHtjUsFcZughzI%2BvLe6RmAzAqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIS42AS3Bw6pD2%2FJ4CrcA4yq0Y4xBXWeSbSQZDIbvzIA0yUOVF3WarNtmOrXaFumK%2F8B2MYmiVoYZ8KJyZSO0CuhAjAcWXOqvCTO7JM1ZPzuRmUmjZTbIWD%2Fgzysafr7h5xu2n%2FjZUQ3s4n8FU48SLxkDZmvrVzZ9%2BLQD0VzJ%2B8fTncq49UZme57uU5WK0Tu88yzwzeG%2BTCgsYgCNRHcyBxtDPRcIzzF%2FQoAPrX2%2Fh0Fm40KQPxajkSbwjqP0N%2BGzl536w9%2BuBzTSzvS%2FhRa0aBfJZoEHEzRhVvdv0ROkrnpRgeLeLyfSXjXVvbGhCQ8afYdooDe%2FkhXmfRrWYrf6m4lL7ghrHS8XUT%2BT3ltXCgG%2BWxdWtUTiFKCFGbai28sO2qHHw4p4TzzUP6pWYIq35hkFeRA3LUFApTyRPR%2Frh%2BzkTP8lVW9Kr1x37O4AlUCPWqSSmXrOxWSDzVJAabm5pd%2BRRfBLqQtCAnaFkcdbuq72zKpgabTBjewDk8x1YIVoaRUG%2BXdx2uBRBIxArBU3gPzOofjLwogp1K3TL2TZ%2B2r2XFuZNmSHmaCh%2BabNmRG2kGHXiUI6S%2BsGnhHOMWFQGUotRpa2QXIBZfQSc7DlbM%2F4bCWzruiI7ucqGO8FVL0Y1WWJRMHk5pvXuG4MNS85MwGOqUBAcBlzVXRB2f9uaXEJp8cikMYULZzuRNETXXxywDBhPCnr%2BVteNbLR5UaD7tDRHPhL4g3EYif9qMEKGoP9ECOGbv%2F7f0zFy8b%2BlNRgh%2FoZyUuB5iQN8P8N6L6%2FkcfNudpSgsh8fecoKPEbC5F0RU7lRLCzdG4PYVxhvP5OwuqPm%2FVdmqapHsyr%2Fd77KNmJ%2FewFXmaa2VGyEQM3lqsZbDXFUs5OfCd&X-Amz-Signature=baa044c39624dba4a2de89aafc0874d56e842ff58f2da3d8ee10707a473a0883&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

