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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJWPIRUK%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIGGD4tA0K7631o717Z2qzUMNE6ExpvzgDYxCDXd3q1vtAiEAjB1kIxlJhytDasiUM5DdOQEPrvrbdKaVzWVNnHFC%2Btkq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDOA%2BPcbKPgyD1KOFEircAwCVe3PjWRlvKfmW2Qh58j%2BCjgEXtwxy3L6C%2F7Gqxb1jVjM0owciGy2rgEavs22wsDNg0csTWx%2BvzZXsM6M9pE6jDx8v8bQSB9V3zOhED1w%2FFXNboezOk0dffw988haviz%2FHNWM0k2ho2ix3%2BJyQ181yd%2BvwapBSXgbAvYPP86XqF2p%2FcHXTdhVrhnjFWF630buiqHrDKlo4XroQavn4o5siEyTjs5Zz6Bhq%2FkBSx%2BBOp6SBNEZ3lsrMKzsarySegQtjyFTV9da9k5k5UBldlpte553w2UJxixvyG%2BdFC8gdmLmlA6KVPdYhIsz5ymxnTZtzFhG2XOejoCBz1PwgSw%2B7n3zAfMEkzXr%2F9Zy6vlRfYRo2ZUXOrBcfXDrlHGp0jgbR5OGz%2FWox%2BXiWmQwDsn%2FriF9Km2Z39InaBVrzYWuR%2BrzLKYUL5FDjJ7yXMxeetQpWgAy82gprzOdmOi7gEBb1TGY4%2FJ1OoiMDa3jKex2wB7uBOQgx2h7i9YELO40w7aWA7hc4vGEnMYF2g3rcAGSRg%2FPKLjggU2A81gQ8POIhqHEhF178bR69iYzYac1Bvutr5qhrkgc%2BdfSgcbvtyTnNQa4XHmY2Mvu1ghfzrnfDSQBbNnRwAiGjD0ArMN6TkMwGOqUBxvvKn9eBxzIe%2BMWZCe1U%2FPxqNq1YqVu07y2lArkhJzl91Ug2oxSdMHeXX5%2BTo%2FMpC%2FQEpqa1XV5xMvRK%2BJ%2FkeJXVmMO77LDkaKFTFuTzqQzgb29h8dmME6OagMAaj9ZH%2FcNUcv85Ib5SlbCguUM7h7OYxlei7lOz%2FZKZQ8o89Bd%2BS1ejqnKxGUTIeHhc%2FSWGQKp3PMTpkoEGgZhqGHLn3gZP2vOe&X-Amz-Signature=86ad2e4df2c11bfd10988b3eca0a525ec23c313489bf941e8452c90339effa48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

