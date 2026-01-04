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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DIZYO2Q%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIA%2BztTCRk7UCGujXU4GNx0MLggJ4NWuA5CYvfmndIXZJAiA8IVhzeYn1WiKbmB5NR%2BvfI2mI5RFlsUA9sB4AImtTFyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIM%2B0D%2FPfLprRkMAJDjKtwDQOE7I3LfwmHjiXH0WridRuHKNSt%2FReRd26Tb6AWP%2BcBmpbGN4vjcgmJ1zNTthHrDRLmnsaBrPv9Qi%2FijrzEx0KICRA1aUzdoiCeKAdA8qIXew4yXTx8cMtmP8sdPhwXYw2HHdkb2Jbdjw5dJaMKN8jYlEbuuqnpMQrY54JwDLh8q%2Fadb%2F6JXictgzMrWkj0feSOJJg8ZvFTMHBUPnSFDI7tVsF6%2FqKoEWcdB1Wabz%2Fm6wDZjN9DXeiW0x7%2B0H5eRhLTcdzeHpGSvc6Q3yq25NLLT0gY8AEpNcX6ypf0b5SnQ5%2BXv9jriUCuEb2pqqSch52s6EogApuKG%2FOCLHe6%2ByTwCX82UPmebptPw1KVhg1mf3B1ulhCC%2F7VRQ6taz09Uf0BUfiAPofuMK81MHPAA6K1v62qIqlMk7DprFsQlFH1RDAyZaQCJJeWdbRAlku%2B9ybrNDUmZ09ElGuBbwgFOw3r%2F9qR7r2hfwgSSdUHrIF5Vst4aFGmUJzj3EIM9bNrF5mdT5DWNqsCT8gGoL1TQTwEZGxYFeKgheAID%2Fm94TFcwq3bYMKiAsIKFkajH7l7svvGk6Sz201zE5g9e5tHVYAWd8B5vifCBWZ1rpzLKysFt98MFPuFxDBOZvSIw3p%2FnygY6pgGwQ3Coe5JJD%2FjtG%2BVEiXwchSLpOrM0lIkxxxBav0%2BISA5uwQn12aY1U1e5OVuNVoZJnr%2F%2FSJEQGcY%2FDf84m%2B0CVk1ttfzLxP%2F0wT05u6mwBJ%2BbGa%2BtppjCj2JaC2%2BPBf7CjIvPpmj0Ih4sxoe2bOosntA5fZZKY%2Fzwx7KL%2F9l%2FBNQ05Zj7jHkC0qq32nyTKrafJ339PE6Ni7SINgk7jOdSKdyPaXnY&X-Amz-Signature=9db95b78b5c392cb26b857f3532e1622d7af43d43b1b1164e842ce5f9796c461&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

