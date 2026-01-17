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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGFXDVPT%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrGMOWGKs54tsYGQHgHlb5BjpZPsq6IKcp7xIWHEOzDQIgGSvuAX%2Bgs23UJboDOAOofpcr5I1CLXU5eNvxXkA%2FUGoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDHIvf66XayQ2ULAErircA%2BxfDULsSFGYJ29QxBTqwYiklQJ0by8HysoSQ4IHw5mPBXLJEFLqo3aBUqrAR%2BdyXiXneZZoFIfQ77ioGLDU%2Bp5QJ%2FdFyP%2FFf9wmzvsKCHHshdhCVgrBBaqhafGqBtThEChKfCiBsckkZDL9auxnOK3uCo%2B64VN2VmYlBtNUNhUlMdx1vT5seWBke6j5zMp%2Bby0vgAWjR0EM4yVf9MuOs9zdNxRhgW8g8fEqxmbnu8pwCL3wI3e4GCdiJb1H%2BLn716suazc2UfuOl6A%2F6TBuoP16vQsW%2B6OXZYrV9puHt%2FKtCrGvn7aECRfN%2Bb%2Fy%2BOvL6dRz5QgfqJ74t16SVmWudYHdwvN4eIK26mA%2BNVCZJdYNrv6R4gimnSCBg2JezUyaDwnREoCrYCX9RRXRHWoaMIauW7GQ%2B24EAMNZRycHtYrYkzEu45gN8VC0DSMwBM34Aw2Dth3xa%2FZL4AKN8AUzDC72cf60p2hQbLYNoATNEZbhDJVY9dra%2Fa0H0r13Zc2KiDzsCWQFu7kE54M%2FenzugP1Y0PCsr6Ugge4IlpJ4y%2Bwj4k9X2LStpG7DU5vQr%2BNNCH2PSlTZiA8EjcD9nsUSy4i92PPPzXBB3oFjMsN1BK%2Bgb3f8VKeGHlaWX%2FsqMLrRq8sGOqUBrf3PsJ69sBu7Myc779aYavagk0AzvY1em%2BKFkoI2VK9JkepVKoMAGBmqlsVERiO9GFxkP1uyaL2sQom9bxjdiId%2FOOleD2WPEQptm9rq0QAFslsicKXWv8ykhCBrDgQQyO4YXIA1gru5TB%2BHJpFvbT0DIgRc0ZsZRI0BSa8QYvr%2BpdqKIGLYNdmDfoYgsa7iH%2FQoA%2BDoAKkKglZaIKUbKUUwtbrn&X-Amz-Signature=fda20c678c8e692476c1ba673615a0a177787dc0eb4524c2834ed632e90fd9f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

