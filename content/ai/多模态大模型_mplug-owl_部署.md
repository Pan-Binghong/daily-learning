---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RGAWOGN%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDBz3ijP8AAmJjZRArYRim2EF5ivERoU9ov2qOBfXJTOAiAlnQ1FGgcsDIytY35wssR0nz9zO6SWfCIQal4tagy2CCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7%2Bl%2FuO0LyYpfCEEWKtwDISVCgMe1KEhBLCZbFx6O6bTiosRqZ9EQ5jpTUCmES4IImZaK545G1mQPl%2BlOAj62YJkaYUdsHLnGvHcGds0qHPKu%2BCbH4Og58dw%2FJuFpB%2BJgSB%2B2DFQGEzrPt12UucyLzbqh7uEDxiA2kqkw9LNpDY3UA8ohsm35%2FNHoqhkdHFc0v%2FdlK1LS67CDZru20ILItYVWHOq9Pr5cuiaAHywRT5CXsgobbU883B6geVQ3FDhj%2Fh6B%2F2C3WZFkgshA5ShoEqQTwDcVPBrRt37ThWMVv8efNZL%2FYbr8zv1Gj2cCjKWSrIct7ivIIzH2wNhI%2BStnx6rUd8ZbbEAcFCzRPnbq%2F%2F0uOwS%2FO9mk6aYZ3ag6sBFAXqdyQAmanCS84ExACUKoyXqybuIs6b06hqIaJLt6A2wDLIL6YI7VdhZZW30hekP%2B9jaiEeZVecmN84UyqxQXM%2F9wyUe%2BLUwdgxMXZZG3Shj3c8Xf8z%2BSyUT%2FKcQgfzzHQytBA6aSdLjewtJ8pSUMdG19zwLj6IBv5UDIWY3SHScmTEJ48Ff3ynk3wfNsPzMiCR286ZY7DSWkvs5mLIwy8L0HHwSeAQc3BP138mXiT6tLE2oSgF4IDPCbtx0GA%2BUz1%2BWmKdESVMMmofowueaWywY6pgEcu%2BwgaBbnUjPu4DNp7tv7bB%2FK%2FCUoscK8SRWUUE45%2FkC%2B%2BE0yAFPvj%2Bm0AUGHT8W4oaoOeAFn9nXH66DQL4oxEHoqFlQsyG74pbywsptqmx4FZOyWQ8S0C3pte2IfwDP%2FSg5GrAqAmQzPOVlxvVuR3xZTww7cf6grvn7DRdSX%2Bpl9j%2B6o9DUwaKh8%2FPSD%2FRUlBFmIpB9w3LrguR1Ic%2BQVwfOYtMnT&X-Amz-Signature=73e73c6f5822329cae65a3c47a0ca534833bcf21e98cb2a46ba27853a6d731c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RGAWOGN%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDBz3ijP8AAmJjZRArYRim2EF5ivERoU9ov2qOBfXJTOAiAlnQ1FGgcsDIytY35wssR0nz9zO6SWfCIQal4tagy2CCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7%2Bl%2FuO0LyYpfCEEWKtwDISVCgMe1KEhBLCZbFx6O6bTiosRqZ9EQ5jpTUCmES4IImZaK545G1mQPl%2BlOAj62YJkaYUdsHLnGvHcGds0qHPKu%2BCbH4Og58dw%2FJuFpB%2BJgSB%2B2DFQGEzrPt12UucyLzbqh7uEDxiA2kqkw9LNpDY3UA8ohsm35%2FNHoqhkdHFc0v%2FdlK1LS67CDZru20ILItYVWHOq9Pr5cuiaAHywRT5CXsgobbU883B6geVQ3FDhj%2Fh6B%2F2C3WZFkgshA5ShoEqQTwDcVPBrRt37ThWMVv8efNZL%2FYbr8zv1Gj2cCjKWSrIct7ivIIzH2wNhI%2BStnx6rUd8ZbbEAcFCzRPnbq%2F%2F0uOwS%2FO9mk6aYZ3ag6sBFAXqdyQAmanCS84ExACUKoyXqybuIs6b06hqIaJLt6A2wDLIL6YI7VdhZZW30hekP%2B9jaiEeZVecmN84UyqxQXM%2F9wyUe%2BLUwdgxMXZZG3Shj3c8Xf8z%2BSyUT%2FKcQgfzzHQytBA6aSdLjewtJ8pSUMdG19zwLj6IBv5UDIWY3SHScmTEJ48Ff3ynk3wfNsPzMiCR286ZY7DSWkvs5mLIwy8L0HHwSeAQc3BP138mXiT6tLE2oSgF4IDPCbtx0GA%2BUz1%2BWmKdESVMMmofowueaWywY6pgEcu%2BwgaBbnUjPu4DNp7tv7bB%2FK%2FCUoscK8SRWUUE45%2FkC%2B%2BE0yAFPvj%2Bm0AUGHT8W4oaoOeAFn9nXH66DQL4oxEHoqFlQsyG74pbywsptqmx4FZOyWQ8S0C3pte2IfwDP%2FSg5GrAqAmQzPOVlxvVuR3xZTww7cf6grvn7DRdSX%2Bpl9j%2B6o9DUwaKh8%2FPSD%2FRUlBFmIpB9w3LrguR1Ic%2BQVwfOYtMnT&X-Amz-Signature=2307c0e673c47bbf8484349673d29866fb206d3338e43cb265e546a6b0678476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

