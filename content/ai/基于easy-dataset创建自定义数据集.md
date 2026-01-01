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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUIFRENI%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIEV0dBzwjFWIGtAbPqQZH6HOQpJXs3YcKTvTtGA77B6PAiAiHEG7i7gF0wGxWGitqilZGOiVxnNzkyhSC2SEWQka2iqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZLx9UjYSG05D4E1lKtwDitJr6dB1wzqRF74A9j1qeB88rHkfwKsABd1Z4ULEO4AHZFx7Q6nn%2FkA%2Bm3Ea9vKRQsDuGnJW5N97jlBufwvy4%2Bqk0kbXW%2B7x2eCl2lCGIyz2CdUWr%2FSejZRPuFXHakJGXrcAqLvz7OW9NVrN4TaMxEq%2FU3BfVWp39wyTEWCOFur4uSywRGmr4u%2F0bjDGbPJcMkqpKIycjjzYCKK1XPtEC7zbIykjUnDcF2C%2FXEsiXKzCXz9QOpxKokxO93Yd4s1hA2L0vdrLRYXVKkNzjyhr%2F94epI1l3Sx93xRu%2FEaFZ5pgszLqx4oOCZ5o8AXOn48Gi7tyLVEYfgO5BJNuxDnlfKNW2zvl%2BJ1rAqThe5GWak%2BvCWmwbNDIb3Zun9PRcz22qlmLHAqCPt%2F4TR2DV6L9V9CAPczen%2FUUm9AzQqhdx7j4WAd6qNjiiQ%2FID2WGcqfiUjhuScBFulmNdntKjmw1%2BZxAooTeOemUWnIqWon1EmiPp9gOqSm%2BumQfLGgrZ64JrP87My%2Fd%2BW%2BCKNAMJwpJYK%2FtxYnGHOE33gJ1POv1n8rqFQWLEzBEqVUyKJ9lDKpQfrYpMrelR9IA0ATAiYX33UA%2FTuhJLUaPJLcq%2FhblSX5a29F6npEHK69Qjh0w7ZnXygY6pgFJTlBVUtZ20W51bfPvWVGmNEY2tPwYZkQuD5%2BlY7AlWJMp43Shpo1HdkMskmDD%2FSV2g2rpact4sl5kgpkxOi8cwRJvuk124kcSADxL%2FeDnACTZad%2FO2pEH7g4j21TTV08TVVeyvN%2BJacb7bwFURqSmcxY1Zojtq0h9A5eAAQYjUt%2BXwgeeUGTsNMvWoP08Im7PnRDaXcntR%2F1YnQTEHqNHFShhOWg1&X-Amz-Signature=b6907b427f7b1165921bbf034b624300b5af80d064dc0d81850f465657d6330a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

