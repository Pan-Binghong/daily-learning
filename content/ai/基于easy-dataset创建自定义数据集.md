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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UG5CIMQ%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICW5lZRNtAiHi1JqyTSYmIma1v6ykbOrms4IZKuSploXAiEAtaGd%2FQIcdz02XJHnp%2FgRSCtDTEH3Xw1CxaMhCLrAuC0q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKe4Dyadwk%2FbHmkzgCrcA9%2FdmBj7Kp1eNfiM4YeqAEUXJZV6EUr8gR7PX5H2naDi0IFIMwEhHRCXNY4dYrjcssyz7gVOzYx8ZznNJzGQOnzLD9vonZBfwnBKxvr%2BXV4Kmr%2FqZ87Hg%2F3WUCOeeAfCfBZiz4mK9vmIgYr7CanLhDWXXKtaZRx6edOAEnyVohBA2z1ksKu1OmGxWV7UQddBAv9COBrfUEIK%2FQQCzkaoX8OmrQ8sgzZq1PVEuJtXcLudXOwcCH2n7U%2BsAhFqoYlL68T4quRzaxmmiRWTI%2FuW%2FZoUlaH7bHGuU%2B1XLFU%2F0QeMTeVVg6I2HAkVBnIqOgsVmWSasuPl21bxz8ikxG7MUUZ09U2qgnJWPWvXnc4TuogC9j4A3LQOcsX5Bir6nd8PlQ2ESihcXm0UfmiMs3i85y6d9ynWYeBb1eA38eMg9A%2FQDFfA3g57xHaQ7glTwlP32t3Mjy01EPkfdR8qI%2BrkcPy0ThR1oGA9GIv8AvwErK3rPVxiPlyOn0XO99IcTQ%2FykucQl5kePmcRiniPW9EMI2rFM2BMevKLXYjWqWZDScUBxM%2FB5Qsb2OSKusMLgbR3uSB%2Bbm8tPwBWHegw5iQ87fbWU8BuCxpTZXPLtMmACr5lASopYPQFbg1CknjNMP2LoMwGOqUBlbPHlG8JLGkYbK3qQsd7aF5rL%2FXTnn9gFu3suBH77d%2F9TkgrkqeQ9OPZGVAWIBBLVA49hrIzCS0hCgblitCLUvjX1vIqfQh8swIVAlRMFmQc7KqyHmiB66%2BIOlWhaIWu0FhL96R3SE6qIcH%2BZbcqZoVQ8uFxk8TA9orFu2LPSbh%2BieC2WEl8%2FeM%2BsAQ29Bsyzn6kgEcpszeYcvjvv%2BCQdNMjTkYh&X-Amz-Signature=bb7c2bb92687fc66e0c2cdcb318f4282c88fb569d1ad874b9f0e4cdbe763f4f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

