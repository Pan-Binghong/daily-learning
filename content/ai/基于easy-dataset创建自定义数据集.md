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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUB2B253%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTqaubvEgQhFCEFzwLPKNqBk%2Bx3q3WLMgd4BhAVHSSLwIgaJ7omXLf70oOHXK3fwNOCxFEZr0okyDeIWwZ8xcPiLwqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIxUYLd800z%2B68ffryrcA2QmveFBz5XlXuqpCSFPSfH3jRIuGY%2FBdStrFUG1uglVryL954%2BLHRy32Ax8iRZ24406rDC2KlQD1BFJ7UGKK%2FsfvxF58eKjT6avgdGw3NB8vThSZd%2ByIAGGe3NdsQjhbG3NGKlU6rBuYnWcIchbd%2B23DsMZ7%2B%2FYRR8dfIwGnaBRmsJKDTSTwDPQjzGPcLKnSAfTMwZvEBCCljZEmgHEeJmdjm%2Bb2%2Be0XKBRwNDzABDJNlVVLxh7RfiDlOh4tY54Q%2FNsnYok0DD75CgMJrT5IiQ53IHwZlEduWN2wvzYjJRS7CjDuQbJEYfKSZ%2Bc4zpbrYuwZheDN%2FFOwtEkRcBxXcuhYehaWxNAm5Zkr2QVEggI7jn7ZXTcwJxfEbceqOKMcscb2kDF3iuDvXPBNAF5AmCudFW4E%2FZ35CjnU%2BpyClhV7%2BXOtS2ojmFZdHgHgHLUgk7%2BiK2%2FC6WlQP7g3daZJR2WIt69qmfch79YqYA2t1H36%2Fze77H8OXQUfD6aNN4b2IYp6QU62iYrDI4Xz4VfenPtm0LWauG33Nhdx2ShCaYFwecr41GI0NZnSJt264OgHKpgusYxehfyozGmFXwOfBzKZa9hLs9tgNGbnWisZmj98Zw5aSYxQd3PYEFSMI3MnskGOqUBUklmRuU7oOe7Vkx0YupxD0eN%2BVT89%2BWB8r64qLHcyngD7vYEc%2FF5YX0yKIhSU191E%2FUcDWxnbzhZunlW3cwbnPg3I%2BlpHkLa5seWc8mMgZrk%2Bus78UvsXIyjngOKf8OGDFiY8h5EMGufWfhwutuZvATmEuomXQpw2z6RA%2Ftr%2FY8PteVmBbpEFejfhu5770wgJxkJDVl7cw%2Ftt0TqpMDuwds0Twdw&X-Amz-Signature=d65757867337b281ac45ef6ac70e032c065a160f3f308a81ccf85e8a8b8b416c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

