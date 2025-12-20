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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LOJYZNQ%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0ex4XU%2Fxowuc6SzDq4VSk5DDyy9CqiuPux4exWlYEaAiEAg474L6hVVTp7fC6ADCRRtJZLwVbIDw5jK1FRoyt%2BOs8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZyhtxNMD7HHyRmLircA%2BFqJDwwWv3qYJcDop%2F9SlhnIs5zsbp2nvScLBenhPZJrnXLPaxp5tPI%2B7So4dPT0osWprDpLyzikObnEgG2TZw5Na%2BYRJrNReiUiJ7gVESSSnPDVjCEATsY%2FIOsDCC4cExFYghqqqSOOCXMshWrh6uE3cbBr6w9WM1kG8VRaxjM0KTpEbY7XTfnAY%2FYh5WpAHRoHPAUWR0URftXZtIWwyA3AsE6oCWkeHPG45FRl7a0wjS6g1o6HOdSvppzDDXEWjj30M%2Fw27CQzFfwqBcEUvIH%2FHaFl%2FrrrPOc5Ag7eLf5vJMV93z4IOdIuUyXRFX7p761cr0zwf5mVqGEXgyGX0Z3mgzMxyU3jU5RZbkaWp8aNGB7d6CO0IigKdxg%2FJvT9P1H9VsvX0v1VpcMwQqD2mSr%2F54i2g5OR1CNk1IR9rsg5jAFsl7%2FuIzX%2BTTSiDgSZHZA045%2FYPIoKAbPWrkw5T1l8ay8fqrhWbk3gnIJL1WuUmK5VE7%2FE0RCcDA%2FyK6RjEL0rFZScbm4Wqjw%2FOS6vTAxYI2wYZzMXEPeb4vujyQbma5d5Gny8wuywueVMz96JkRVOP14iv2jx9vXKYDv3%2FlDrKzxf%2FGGzMNxsY4SiKZUvcJ6ORrKUls%2FvajOMKeGmMoGOqUB3S%2F6G8nuj5dp7XeY4ozbK3W8iaEUQMybrS%2FrpJQwnLfqJbphIUcmtvPK3ThHnOA59k6hTRDOU1Nd0MNb9KovrgXyBvtIAlwRWd%2FbflOA4f52%2F%2FMff4TyhA3QUwG9sc4plc1190qKom6z2V5eSys149OS7JcMuKzHkqThNYae7%2F6xeXNhvz%2B%2BMLLP6aSM27v15SkQxHW%2BkG6KCuGmTKDTuWKi2nEe&X-Amz-Signature=1f03cdb2a031ddafe8773471562b576db9382c5d6716a25dcf53c33b356e578b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

