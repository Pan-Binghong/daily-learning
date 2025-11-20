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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SACT4AHO%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCICbTVePTZ8oN3l7XgrPxv7koJ9WkDrqnspyKz6hi8d8xAiAfCBDZVVafi8MHXVn4%2Fa3MnnOGq4Q8WBd8fvPpStjqLCqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRRSXBF4wRWbvKndRKtwDPxWyl%2BXpiwVAOzt13p%2F7bgWsaZGhElaOqMl7xjshEkQIYcSff88BX3RR%2BkG5bqHkQzbIGtmR0%2Bm0e788spC1DPC3P3lmnqPfBaizsxGPpat8%2FbZbrWayyduN28rsdBikxMkOWdxRd%2B57y34flZJay6hfAs44DJTNGT9FPJTzpD0E0nuSyywIdHck6SjzRDJl08hb2I2o1u1ui7%2FNtLCVV%2Fzr43l4JN7pYf5iKSmSuV9%2Byd0g7TyjhlPUw5y0sYVU%2B55TCIzRiOv5%2B91GzYaAGvaRN%2BIzJOlSyAMyWDsb%2B69dasdfJkkdEq8acF9xF6WG%2FjUnvajF7HQpU%2BSDLXsh%2FgNgmN%2BDF%2By3fpGPDpzjCWS2fPgINHpGWDMgoEGA0DKZGX9oKsfKcP%2F%2FXcYsct%2Bn70ZRHVz9%2BAQ9GJEdjTgGgogK7DRd4BQr63M%2FyokGpeC6pcptSp1cqxMgs7ud4qLuf5Hevc4Zvn0ZN%2B6Pb80V%2FJLEFM9ZxQG4DPPxQywwetD620bJHQikgJUXbOih82k2X%2BQ4bi%2FspeOeVaJU9X%2FT6fPGzqoXj3aq%2FxrznHJTaH%2FKK%2Br2snjxYsDvht%2F7iAlnFfOFZDa%2F3FEYsUaIauABAHZrDOrGetRHSxVtH9IwjOn5yAY6pgE2p1GrE6svXkO5SYDLpVaNQg27SZpt84Ar3k5bSYdrGIqBXFsj5PhaL3MHt5SLkmFW5hBcjRalPHFt3XFyKNT%2BZAJ71RSZRiBEGufHZ0IbTgSfdoDIxqzkKP9sW00T0DXs%2BH%2BhyuUxrmCzwu4d1DmPEz9bJsnATIYjltBRmycYKgBAKMsEsVZMlD85NH4E%2FJ8YXJJgARCxCihpakKlgAZGXTKdm40N&X-Amz-Signature=f4b53cfad38408b958893f86e39f2757ad633e549983bc24585049583934f61a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

