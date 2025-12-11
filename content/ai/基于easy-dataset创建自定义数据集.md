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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MIND2E%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDBRLF%2F5LZyOHDM3jcM2JeyaNQiizY%2FXwPiMfmYPKWvpQIhAKvQykCg3kBjXhn6Q%2FCSVUswJ%2Bjl90YbxEWSoYfvIIpaKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNAgalugcWwfZwjwgq3ANu0Haxh%2BfstHE0PkCxvIeA0Hq%2BZlWl%2BQk9%2FURbHuC9UP23jlszBzaFVv30x0LEeBTp5WjmHRvKAamhpTqHmZAuY%2FcXV5dCF0wrHLmIF2zjsxPYSZni%2BRffOlAD6kEpvJ8fL2m34%2F1fAxw%2F6y7euHKfqCrchc7j0RuXNGrfuBz6cwkV31dDJ2IyPAh%2FhuRhf6Ri9IhtUhXtU5K5OlSYgMXzqWCN7DA8uzRWK9NZRSqMV2OivzAesy5sp6gLqdjLWSXnl3SlDS1wugJalLNoaST88phNwtepSRSawbqI6NlXg48AP7lBFUJb2C%2BXA6K%2FmWp3KTAIMYNGWQbLbY24iITUcQlSDFpvwMs5jIcSfK97APTFg78DtZSVkyE5uHNflCwU%2F%2B1dll5M1qN3Vi3%2FPH2sCcRwhEc1uRO38WyB79NrZQVh%2Fz8vjH6nROKhhbEn4eku0dJOsGF%2FV%2BI2csQgrs8%2F%2BosSa6rJpszGYoll1vdfRcsg9MeidzA%2BLuX5GGBCDMg7bSFfdy5TD4C74dKD3W0%2FwqVQiu8eBvaB5mEgs2r31DUnqeAkBPCAiuL5f535Yd84mnQ5r4gSCX%2F4YxQo5SwhDNn2LssHeee1uHuNbV41%2F4qtQ5VvFxv1WTFXFTCqtujJBjqkARa5okELsJEU8%2B7U0M6fB%2BiHmIKkGOlDYy81Z7tiMtDIT8U5kC46VsqVMO0KzHG%2Fo%2Fc8pK%2BthTR8R2AOh9bwZJ5pYS0zFk0IY4MLqiQdDCgwOQcbqVGGk6veib1RNSndPv7vAVK561onymPsvHzzfDOamDJKGqf3oCuvetQkXEk75CnjwleEq2s8DSnz2iRnnTQ1pIOuGO93sxKljSUr81N1hCGR&X-Amz-Signature=6d45a6d23ff9fe46d1c94cb37022bd033f4c384e0e41e338d1a34019ec0b3d00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

