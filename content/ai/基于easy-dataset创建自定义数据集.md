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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644H3CJID%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIFYDmWFyNbqHe8FSJRSKQUk1NZarQwdE4jpEwwRO9kl5AiAjKfGoybtvIoUVmsAK15RInPW%2BK%2BA%2F00o9eF8sB5K0EiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKO%2FDPHxaxo7IiNeAKtwDnWL1Yy37EuZQEoyoN8W5Q4aG7Rc2CqmHsWWlU1VNcYMYABsgnvSaYvwDftLOdNghXVxKh6gH%2FRNaHpG%2FAIunQnsTHv1KQYe8CjQvmY9gHKrid2GBMYY2zy6%2FgN9s%2FocC4fedxdM8sHxe%2BvsbtaGgzzdDRtw6ApN%2FurIN4IcB1Hqz1AqY%2B2HndxjW%2FbLvPLN%2FRS69uwbPEpyPCC4Ez4e8pL9i4oOKTDtcCBZovn33BKci2d6kFYOGaztWI2%2F%2BLNInAsXTVafMY4N0%2F2rehqJpCPeRbSMfsYaWx7ikNrdldCHQc4ahZrxHkH5TDKz7IhYgXFHWFFrIqtD0wGIN7qN%2B0KboFFZphkmS5UjTOsB%2BvWLFocWOs55GEVnKJC9Ih3pTHyQzJwDtA3TYtO2uS9m4RG%2Ffw8F%2FvYFBYF5XFytUN0X%2FqvFKgZ7UibsyMH2AaVB1Vil549O0Pu%2Fv42CW5eQ1GCJEIWukOb6ZIRau9Xr2Rv3oOkdqQ3qlU5nYBO87%2BYatnxa5Iu%2FeAGCP%2FQh5SuHd3yVrGePJfeNCp55Y%2BSjMm1Wj93iIwEbedR5EyBi71%2BF%2FHf0WyXPExL4HEdmXttEh5OnbWQfwr5kssaKmZys6qoUIB5mruPE6rcjRf1EwsafozQY6pgH4Gt59E18%2Bg3TF7g7c6%2FKWubbOmlmft11BDWTXltj80SYmLaKx7UVx88wgXEXo5qQqbf%2B2f7Tljt%2FEDstC9gy2PUOvdsqCBbjFuAp7X9kRjY7Bo%2BaL%2FwPgk%2ByGRWIb6xCIGEMk0F8VGk6iqOgKWTLbOA%2B2PlhKmszHO1dg6pp4xMLL2n2uNmQTh%2BLsVaGTVwuAiJhwg4iIE%2BHs1BVSAnsSvjzoEYmD&X-Amz-Signature=c453a584f783a843ced40d19f4ab31c42821d4111f111a70a01b2d4b49d27cb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

