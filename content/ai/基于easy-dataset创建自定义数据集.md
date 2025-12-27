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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FMCZYUC%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWbKarU39Wqgt7JycDoBAPoOcCjmC7I%2B9DguGqXhovCwIgP%2BoJC7BXl2fgfzCwLeWxEoDOTOLGfttr4VQgLIGoh%2Fsq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDIOvlSLkIPc9Gt33bircA6jokxQtxX5qZTSYrgmEd%2B6bOjTFBIsIAdprOCyvBdgWyOiw%2B9Oeqj31l2VxuiMmBW3uEPvykWchUaOaIlYJtGI7XKbaf%2BLzoP%2BBXLMpSVueBP%2FHSjlOhebRqblLy6mDZN%2Brey1afXWBdbeNglnH1lP7PkHgFhGQbVvF83ceuULuOMOVJ%2Fh2NkQK82rQ9xb9x5CqZRJOmmIe4C2y5lgeO1LXoEaV9bEYlgN4xDTtRTX9tLTv8NCYFQFkf6Pmwe1ECMVO1ZN%2B%2BDAaANLcMAxSIMmRZ%2BYIln%2BsL2rXKO98zfAEkUwUeJYR%2FygjeJiGTDgU2dUKUMuhhbMoGUjt30Xj%2BOMOI3xiM0QU0qzBo%2BzRRO8P1MXFT7rL26vtn4I%2FhmieP%2FyEZJRLJ9E3%2FQD%2BRik%2FL3hZ5IAVZXMF0EfiU89SCFdNAIfMIYmbw007HEPbwtyVigQznsEMyLjOl4Q0WR6XnUm%2BkmiuLPBDJaaJfOA6SxsVSa1XgMfabBhTD7yXaRnlra%2FZocBJzI18LtsHcN%2BGm7sw9jhjpGt0Qp%2BuUw7ICVI%2BVRV4dQDo3IEU1CudD%2BPEJ80%2F%2BbkuntRWS1o5qp6gXpyBK6XAZkBW218NTRTDud7yFCg0rX2vzgSKBTPRMMTqvMoGOqUBBYGR%2BklT%2BlV%2BZAH%2FGiv6kj%2Fqu7gBacit0KvnnhCptyD%2FfC7fYhS41a6U5aDArBtkK3gxbhcC3Cn6BkTbYsdr%2BV0NQk%2BkFsZjxMIs4UDrqzcBgkoXI0vH%2B36v3SVQApnC40NCO%2Fv8JMymvqOQ5rE3bZW%2BZyJd6PITFZrSD3E4whM4SgpspkM5XfvQQFO0g335Zb%2Fc4Hdwmoz2FfPPVw1L0bwKQOSK&X-Amz-Signature=155161e12365befbdbd09d1acc7f5926c54e126c4640f670c67cbd655f5b48f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

