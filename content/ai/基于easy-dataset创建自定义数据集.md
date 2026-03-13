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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IQZU5UL%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQQXgG5%2F6tINviRX%2BVXb3DrZd21W0aoyF3e7xxuJYfdQIgbL2EuEGi4YeR3TGZfA8z2TT7oKlcD0k2tRSoMaW75%2BsqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN61jNCkvsrU%2Bqou0SrcA5jxXyphk45Uyi2ykMZjXg2Ns903iAkRDa7fbjnHV6rQ4hWGmp0yemZZJFKreWduSqiilsU0NZzJ9w8pjZ%2BQN8hLGynir31Jox40AD2zfvPxhHGPxmpvSvSe0voUs3wqtY5R9YINB3ctDZGc1l18Pxw1oygmhDwtsp74Absdq3nM%2BsiPuv9TS6%2FHvmXkHyTkn86wOEnwnmUW2j4GUvUgUsVw9JkfXuv3%2FxyFxM%2BtWY40j6vhn6HQxTRxyhAHYaPZE0U7Gp9mjphShJaaeHPR7%2BkLoC60kgSra%2BRRiECKWum%2FegLG69Mbbsr79fKsseGkStbceNSmcaQeVJWIqlKwztCys8AgR%2BzjLGEZTyLMsT6VyMKMj22m2iyFP83%2F3wxIwoHO9W1hVOBGtF0XpyY5jjZngJlFEUpBTArQdAy%2BdQ0QBlj2UYBFiYhL6RREKin%2F5DN%2F2cm7kaLFkNAmYmnYH5aKH5fY03ADTerXofbtYBU7mk%2FK3z%2BwKtAERJkHoJ0CfNlkd999hBCvorih1V5Vj0yD4lJWLLjrw3yfCax687W0juADCUgMI8bGByqoM921E7nojKgh3qgp7bCM2gLzanJj3gPYCGGNN76oHhw7QG3QUrooRBc2KT6pAa9aMKe4zc0GOqUBORW34WVBvicock3gBrFWrm7Cq%2FXueHm4JEZBEXDUu9cSDXTwWCMRjGsRC742EvEBNa0lGNWRMvwgBLiDH9%2BRZl%2FfmqQ6crYFMggkVQ9Hyae25hL3nWWFjaZWVurD9INId0urxivAArBjZlYb1TcvIgtzouU0mnIHGyUguiTDcTeiHl9iUDfeQdN%2BjzhAp5B41tDlh6kY51AxnzFbiLXPQ11dw6i9&X-Amz-Signature=645f094bae24d36650c85718e777e79c6ddda7584733c48425a641765e35b543&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

