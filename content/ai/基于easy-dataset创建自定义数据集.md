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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW7IOK62%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD%2FMWT8yQUeu%2Fg5ZmK1iyy9mGYDQWlddo7xt3HzhyYiWAIhAOb0wkl3OWx4AY8RkrgZe5icApg%2BacP5H6n3rKK4EKnOKv8DCAwQABoMNjM3NDIzMTgzODA1IgxLrc2UeIhofHnjV5Qq3AOySFyGCCno9zJ825VtE9rAUXIPxF3QtOyuTzFs3jpLuujTNO9hzB1YJxdx6D8wHFcGJbVv88e6T7bj51gwd92%2Bf8%2FzV7zrTKUe6TlyWRBulb74cSk43mn9FOyp125vVof%2FnlvxQklX6Uu%2BPylzZw1q5wWSzpoUun6Z4ZEB9%2FnRRJiHy7ZySUEFqBM5fsMMm05%2BJMKbov5kXzvh74RvwUNt71%2Bt5GvKuG0t0Qeso4WGObZBdcwKVO39z1AeNaYJF80Vg70clz1lR1MF71VmmyNNZ2KQcbP33Zu8FbQMjNQy0qfStEYYTVYy%2BsOa2WXvOSDZn%2B2o%2BWf9RbXQQOXzNvK8I6JYJhtt9H8dCEZc06b3vlL3%2B3S105iiLi0u%2B9pvT9BX%2FQyKym1cwPZBMNgoxRuxytnMd6rRRKA1wxAnmHM4cmSyovsw1X2SkiHzokhr%2FoXANC6hrVO64kcT4ZY64Dk27BbOVA1n2Jizzra2Y6CrW0LW5PoEBGw3go5AXQXBglma90dJxtMwIODrIyk1lV8K7HQW8NJOEhzIU93ugTnVkao55n8Df1Jkp4O0iasIVG%2Br2BCb7z9K8JFVM%2BwNPt1eKSKCBcqgDFcAmtyWyOg4KSu%2FFLzSu08xhEi%2B5TDHsdzOBjqkAQL1OsgGCGgDHWjMJQYnsisIqyYFUzuUE2ucyvjqMSwWoRb%2FPKRiH48EmsjBZkiRNkwL1pZBN%2FLt40unD%2F%2FQHggeaezi18sC4Ja9nfW9%2FZ1spuJSq8Yl7sAmRohr7atUWpZXctX8pkM3WxKyjEqy2%2Byhzn8Z1rTsP1H%2BpPoBLzk%2Fl%2FamR57y8y7lNI7EOixSuKegAfLJnj1v6iqCXSUSnrhX%2FjAB&X-Amz-Signature=56e93d451444b9f8d2c23bd82e373c5c8ef29da56bbd80106f08c59f351ca452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

