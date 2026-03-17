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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WVR2QTV%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCBBQi77zhN6aqAlyZFB5DNdeXYZsIFArZ%2BnZMfkTVb1gIgC62WqAaXpEyg%2BQNTK0WbrRameGs6aULi%2FRDWG1d8deIqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7gtLqGmRWFDAdLvyrcA%2BHB09EbDaU%2ByempYK8XtSn9mUhyafU8Y7BBftRr0sV%2Fkl2pY1DTP6ylZcvoH%2BYl77UHM7URgr9j4mQljDc2GhRNUWAN4fNcn6loIHofr330n7lIPmsQFTe7OVZqZ7U6nREK4MqkR%2FO3sWPlD8LkgWEJhnRQVq9WG%2Bo22ScgNoqlLiGNgmLu457sw%2FofFqFSWXi7KNXN7Ru6IqXgIxGIjS6%2BUXW6Gd3rXcjOQvwqcdVnx7IhoFzOY7kzclxDpQWp1R9rh7sK%2B6lJCuusj0aldHZdlXmWngIHzW51AViAwECfLLQdtorbkSOUvKR59Egu%2Bls4hF6ykDxBhAP5TsxOEeq3y8K9ILKcVP8RgDLsVFDRcrme5f%2Fa6W0CS9d2ZQeBy9X8Ih%2BCaCw9DgEh4LqHOpNInRtLyYhB%2BdDa3odzJGWO8ZMYGp4kITPeaJPw54bRL%2BysR%2FO2R9AWtS2JdBaJgcwI%2FmKK9DYqoNQBofi1xQ3POabvQYvKuod8lsGsfJvOlnVIabRi0tjP7FGfs1aFPVzGaf11dwujgASESZ6xZOJTZ6C1f7KEwBqsREtlHuXmvVbzRHPCaOPimqETER1m026LKovGfetxzE8QjYs3y6NwqX57jBeRGk9X6wLWML3o4s0GOqUBmXVvhKKThucWi5XshJQlu522i2JahDgZy5hErS1ixeyWIiFhPUt7qMG9pNxLcFR1rlmfCwVenKeO7Qr6r2DlGat614JB2zVh6%2FhHkXP3KuLmZM4oCOi9cp%2BkmGfR3%2BZOfBsfEdqIEhsE859EznJeFD%2BREaLSRNl4OtmjpAl2w8mfalUudYWsVC4grNGWYUJY7NAmvjO7HgA3I%2BO1NH5XqcpK5Fb2&X-Amz-Signature=1c683856c64537b304a9b1b747bd63cfa6ec1f160a48a31257353a55b6955bb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

