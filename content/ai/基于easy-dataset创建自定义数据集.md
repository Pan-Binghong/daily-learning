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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW4P5NT6%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2Fgli%2FWenz4X9bqgGwc34WXh4zjQ%2BrhOXRzARZPy%2ByGQIgXqleGXyan1CKk%2BttbRBSSa8lijnHUiQiCzTzrbZ1Y3cqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtVqVFqGiumxxI4iCrcA6xtn2VFq8SDh87%2FsT2mKVL%2FL6FfOfFqjxMvaUglrYDH45l7Sfsln2RLrNuQvCso4aPqsdd6iBP6T75X7Z%2F%2Fk32%2Foctu%2FDr%2F%2BA580WEzaQQZC8gCBvXEC3gWKJh5F7vg%2FDekpwXEi1pdENImjMLwqkIBjZM%2FUIJrofaly89BCKeeQ5OM%2FhVaiTluR1qaCDohiSUSVBk%2BJ7S%2BwV%2Bdb1YzfqtzGDMMxCf7OqAeXYTCbRi1lZ4DahP%2FpFCxLU1Wg758XnAE5lROS0M%2FX7qxuI6LcRxz2aW7spXdRNJKECdHghnfnZNiJdF4191r8JHtZ1qCjrwNZDhPy0x7fXHTjRMdS4muwjjakxmE2n%2BRZFmOPGVVVbTgKUZI18RfelAoCXCWJpQw54K%2BkDsdoaptfa%2BzxYXh4YXg1CkftFor67IYMA%2BmcfcCvVUlft2QcLJ2Bw%2FT3gqH%2F5izet13ZDcaA6E8LEc1lp8KiswgWqZhipKUMR7QemVZTB5tw5vcBqCMZEwx6PEvZAmH3jM4dg92QRwXt1EC2c1HGr6loFL0MPBQaT%2Bmxi3dzBAoVA1KWoKMyFuEnbGBLvWpDIfGFwAIV4feptU8gA%2BtdGFdTV51OW08%2F%2B1a2Qswl1MfOT4uIjw5MIvysM8GOqUBPe92wiTzQdRYQ%2FJETEI2fR%2BW%2FWcsIbRtqtzxhZlGIU1VmT9BtR%2FjM1uvKbTqSc0g7cpBhhnZ8MZ%2FztIBw21KElaZBCMz8cgsGI%2BYW2bSC0g4Zkt4VDsHwSzcT42X%2BgTyKommUfbREEKQNh3rlfYFN24bnjOYftrlA%2BnFbb9GMpOXZNEPdsUKwl5qCynhlIAhGf56unIFz5xLiBzaymk%2FDkfWFVne&X-Amz-Signature=2098e305f105ec4ef1d6d5d893ce22ff0a40258d325a755aec8ea87637cd942d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

