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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAAGCJRM%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQCW9kqjgyb6jXNuIplXcYmt4JTz0er%2FBWLuSYtW8MUZ4wIhAJlMFuseodkZja7b9EWDBBdEfjHf8O9IpJWUJNbE%2FIH6Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyzI50P%2FwSXZGCDMPMq3AO0Vn2jh5ZJVdfvc9Dfi9SGsV2PEO7B%2FxdlWq91VwY7YffnEtd5ENbxKAcWdanv2Wr1u%2FiNxjlEsV1pJvTMIY75oPnRFF0mJICDkJgO9aKyLfbIwNdDkBIeqwcw61sx2X2ntU8f5YZYlL1J%2FvdteI05B1QPtLLMolFplZXwxFXUiCowxDNK8Rciz%2Fv7VAILG6XDEV8sRl9fe9y4evEVmEiOBjfFg0Y422mszzuGrS3PWvT83OfA48%2FTYXaPYoFGFKEsJkL4g15wjX3skC6NgLSrX7mOnuvCV8YEdgmEsyEYiMnFiuPrf%2B3%2FGSJ8oSJRzMsCljGVaT%2F9cTfrbBtcWfGT0nhtM9lKKb1oXW7auZ23Gcyj2adXExDogaw3X2mQdz%2F48X%2BOs99zHS1K8NQtDzudy5yNUbWl%2BrtP9OFgyyYzf%2Bh6cU%2Bf6sMoY17kuwgSr5rKbWyrMlkG9AFyPgQKYsylJn8bF98rAHKBGxs1FgY3nCt0DztMiy3McRbFnPNN5Hx6yTPSTacQn2xgjmT9fPUkcEM2W6BZUY5CXuv2F14iJ44nl12D5MqTM4p2G0QyjhpDF96GNV8TXIl6OdwigUzwRv5muXANI7hmOXdsd%2FaQdTaYwITccd83ahr%2BQjCUztDLBjqkAb3pU%2BNW%2FamO%2Bade3P00tYDlOI9qewuQ1UJuiKnmqgVqgkdEBZ5c4v%2BqWY1WN%2BYwuHC%2FUYIQu44okAU%2B4ecEX6kIz38tX66oMFzdOpDmbP%2FCFhxmuj%2BmaHU2lpeg%2BTx8KdfP%2FoytVeKKt7xxqRCTzz0TdIRBD0sc%2F9R7jpAtrvMYuEh0Mm%2FHGOweHFPwiMx%2BnDSGeJE6eszw9pR3h9CfBqNRmWkX&X-Amz-Signature=de1de180c04705031d11740c267123ff0f104c8b5fa2d05a2c72a88540968c2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

