---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUJ5HTZJ%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeOT7quKz5RZBf%2FN9x9VGBT0p1PhwMViGfxi%2FXMwPkOAiEA2JYXbjOyLvd8UGY2tnXnNxZOKLDZi2Ht4sPP0Z79%2Bgkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDLFVo5qAhzegXlpziSrcA12E%2F%2FCtqT3XPGioY%2BYmm6pZGARCjBKu7DdB00KPsQz6l9B6Kql97%2F5QO9SkDTpFjE5Z8B9gZQ4JpBhUp8g468Qss9mSxf%2BcR2USBJAirkAyYuAnPU098JVGXFKwVDNMhgxjdYDtC6e5nAsds5eqriXarx2tf0X1wEsPaPWiagvfDU9EevUGCF0EXuNM%2BkkRj1SfFCsEOct72ZJlEc7465NPOTof2YlG2lEzeX7kgjOImb7LicjMeXooRFzlxNSeK2t38hmJ7b%2BNEylfVovGM0lg1dZVIg%2Fz1tGsXn5MRozBaU3GXjBS8JIM8qrs83%2FRybxfleybzK0plT6liOvY2hE5Z1kBQ7%2B0LshrjnXbFKmHBY71nkrhoNAFJTmLsMJrLuEsP8Xpr1DtHF2d4Z0BdkCgg50qDLCAlROlGYihE2jsxxkUFCMJXoJo8TkrAGEV4%2F3q%2Bhq1fAz5JKNV3r91H77MMHLFt7en6AMaMmGC8lnPeF2pJIxvIr%2FLwDbakhoj4A2tX1JMtgHm%2F25ju7fB6zwOtu8BMQ%2FR6gR9O78lrhbxK96Dr7IFiiiYfimviIwKBb9k2CteZpXAC2VDju%2BGWu7abXfB1MmWePyyzYIV0vKoA%2BCG05iV95PBtxiKMIezyM0GOqUBtnL1zlX%2FRGTNN6xOhIQv6qGAzhOecm1iN4X1%2BEVACRiWX2NunRttBbQwKr4u6B8LgFRLZcesbHIYu2W%2Fp7ZespJSBoF8gGYcfKMhixcAmS342me1n0DUeRmHe7QJ4G80sn%2BS3i0cSH94jf9Z2fw9du6JcU1ixmoghKWkdQuHIXedhmY6l%2Fh9%2FihEI8yWdCSdHFWV%2BSo7Upt%2FcZys4vjWooG6Q%2Fer&X-Amz-Signature=73fd971a4f5cd5a51257112482777aac38de2ef46240c745dcda33a178e50785&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



