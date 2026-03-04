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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBAHQQYJ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFpVYrp1q1AaYfL5ZmgT0tZYsCaGDjgq2bJBoxSdCye0AiEAy3KOOXsk8tdic8pZDHYqhBe4EU2LiH%2Bb3h71LVz2GWUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH00%2F%2FTmJQyXskU7PyrcA6Xkj9PQzioj%2BqsL%2Biv6DTwQgW3w9kkhBsWxZhR02PVj0Zbmm9dwN0oqTFNxxB486yZI9lr8xML5nt6UrkwWYXY6vV18jCq9U%2BtyM1ymscRcg6YJCY9EDDi3%2F8sH0PkI6Qjeq3TN0CV%2B%2FXtjTIygoqbcpNYqUtCHAURImr%2FO1W8TbT%2Fq41YAXlu8h6WE9kVQgnzoQ5MwUk%2FUbf%2FnEJsQ5hvVk0XmMVuBWc1Rn0STbgLR36bsYQYL408TFITft3QfjkYquHp%2Fe8l6ZmkozJn%2B1L%2BPTUwHmwtgQwkU5fs%2FzUz5eFYMEwX149PN6B%2BqiwZpeUjSL04ydmeOI5yd%2FMKM4qQGBeSbOsIQsCviAX%2FkvJmF0Ra11vprC4LTRXIvZbtuJ9%2Bl3ZowC8N7ywavf8sXPbO2Q8OvH41Onc3RSkRzDpVp1IrmTdZT%2FEeQhtmCchckYmoU0vX4V9a6IMkG0YE2v53EDUMn57ITOr%2BQL2zbenwWw8tjEWaJZP4zdqYpV5zCwOWAKILePTrMyilk0x5IIOQEpR31lEX4B7VS0rPF%2Bfo9Nluyb9niZgnJbdNIwVmJOwZBw%2FFnV9zznzLijbp6hUEKZLkWT0INmJjm1CAB3GxRS1cx7zLEyDFjgw1GMKKYns0GOqUBzjP7Pk%2FWTHNiqkj5hQAFElfVTQH0cC7iUK6plcb1xT9WBdq4iCjBN439ncg%2FFIr31%2Bm5QYpHgLOyHx65Re%2F076fGix1TzoXRlovgKnk9CS1u8i%2FpaGcMpxK9FzTdyBJC0oBEwmtTLBEbHnOEeRNw12ud2sURPjPZPhz7wbnODmWr%2FDGXCVCKrRGhVdrc8EJp1vcsuzrCyKghyS8GvZFOuYfBaEHt&X-Amz-Signature=9d261a7c8e6f5fc537457c895c87fe3cd08c5cbbecf8965cca1b226cbdd83df7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

