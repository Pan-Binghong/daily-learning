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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLELDBHV%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCjClrKy%2BIC90QfcdAgcZNXLptSWLrOtAC6zfxUgy1b0AIhAPa1DQooBs61Il4FouM5OL8207fVY20c02%2Bx%2BcedpQHQKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxNMgTsmqgKoh0Z5s4q3AOxOFWUu6X%2BRpmZhnxt4WRmmIMdPohTReyuS9G8PGeTpzoL9XYzKQ%2FWK7JR79fnl1IwPwHLk0QHwigYvjuuE%2BzYOB8d8F9cD7qyW2QQn900Xi3Zwf9W6qd6mTMPN%2BOobEM2KdCBKfztU5pYVdLUcL6mN0LFPfYky%2BpJXwp2bzsre48rOkVFcMRzpyH5KPOqNYa1KQi6npTP%2FWADPFtV6zT4nHwTSwN%2B2R2bqU%2FYrq73%2FqHKK18Jwma%2BOXf%2BLB7peNK3c5rlzl3ArAxD111zieg2biOGRBJdkmShUfBQRiwuv8aO2hiQSQSMlCr7e2YETHIa%2Fmrwgs2xySNN71WLe4wC68bc4%2B40xTR3q6tUs%2F8Tt1LKYY7r30g2YVDj0yvOviJpY0fG4tZi%2BZJztbxB1Z7eb9PZw%2FRCmLuILCF0%2B14P1nl30PW2MeKZD6ENCG1J6J1pJPaxG12sEkyh%2BlVooRuZFt%2FvlRecEKjibFKAdfk6ORvwRgXQFrc9DmtmGjrPy8SV9EX%2BoDD4oR%2Bds6iYukeP2HEL36Q0nNtWZQL8MZCmptTjWIMXdd3eYmLmHXmca%2Bz5PwwNhrGdQBB5RK2em1So%2BqKPFu6ptTfn2lyAL8afliVOFnvHYa4F90egWTCRuL%2FIBjqkAZL3Zv52j7zhD3q%2BhIH%2FCYWhwqvPTMa9z9H5px6CaJ9gkeKbKPJmLdKEXJNW09yjqrmG4p%2BVsYIIzOnM4ZiVYzI%2BeeY9wy%2BZR1TdOFdgyH7B42krofE1pccPkF2eI6W2dv7Gh84WCKiOVE5fRWGe6QMmnXu7XUSAsud6FyyZMpl2%2BafYoTX7spyJUP4F18jQO%2F4ItibDQCKnKIc6nSP5%2B7lePC1E&X-Amz-Signature=4bbf44af611deb83ede13be3a15a549e5eeccf2d756a20627a97bfab07b5687b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

