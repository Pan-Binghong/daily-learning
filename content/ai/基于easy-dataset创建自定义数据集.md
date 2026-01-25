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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XQ3TTG6%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIEZxfr7XEJGSvXBXLQz3d8FmQhyrIM01YC2U%2BR1gT69HAiEAsLpl9E4PDGzfjt8HPT6gPOud9JpgScF%2BtMLvqHCIyfAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDGR2b3CwwiYJrvQACyrcA6lQG2r3FROMPEu3U048enMqAb%2B7pMgGCujM%2Fq3NVoXQHhyHz9aECgs7zKrRcBmZiyrUXwTDvWQZyxKbe6jxlNM%2B7z8%2Fp73W5QpjJ%2BWbhCUzlUS7L4s1I0TKeSSN4eowhEr8uXpKjCc%2FaaM%2Fj3sZ5Xk052X9wBmh1jMuBxyDeJry%2FrWz%2Bxi4EaVPAkY3J9N0RDANNcUXpj65%2FQPRKKUGXWGxTgbI1HJ8OJOo36FW2B6LfmbK0MiGSFwRiiBCbxaXEYHneAEgpaO55FPfr9k2UUn87nBGr6BUfbWYT8jOqXccrmD5Wh0XoFXsE0wtySZleg7SnuWr1SQSOLFtJKIs7AkGDzJB93lYtF5Lp8pUWTaOH6YIjLoEoI9VngNJbYJTktoBVs3MdMajlbyxrzvhoWfT6AvJqmrLgxJ3WsQ2WVrwdzsYQTXagBZQOYe8W8las64IIc%2BCbTAWMeHWCEbji6ZcwOeu%2BS9WzZjbbNfbPQ%2Frt7ammSOIdudA6xDUCd41aGCrSiMiBSKdoIj6JJDPL9p7VcRslzwUSlCvVvaeJXL8fSCGqgxa5jUteWR5hfgHOvdmU4O%2B90ewTpOmcPfoxi0QYmtuOMAb7fXo1us%2FyKekhAfT6KEF2gb%2B7oDLMO2F1ssGOqUBKmE7BTC%2F5tfao9EttdYrjjHpHZUOZqwKFzJPr9WtE0nURWvTfwntQLuNN8TFP1R3F5F9Dz6n4Ae7UxFn1Fl%2B6pFBoEPIu4SHhmy6d5NzBcAg05zjJMAKFgi32BReAt0jlwUeRlRJ8F4dYRwBCBOcE5lYcWowBKKOj9Z%2B3j0hFNccDEzkluwTnEqMKuzo3tLheTSypflNYmYiS0C1AmRIywYiZiXj&X-Amz-Signature=81d09d1cd77dacf52d3ccf2db6a9869a01d2d52422bd9e317f95b08448dad686&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

