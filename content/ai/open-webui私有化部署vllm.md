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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V32NV2GZ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDBf2mZztjPeOHKq9hHABYFe%2FsGL%2Boq%2Fy7TCYyLnRhqSwIhAI3lrvUDrRBplllkM7C72GYmcFf8UAH7%2FeWX%2BXb9MmM%2FKv8DCD8QABoMNjM3NDIzMTgzODA1Igw44vKoV%2FFTO00vBhoq3AP2AvNGC80mDIfO7Pkgi16lb7sx6tYgEMHb%2BDqzE91rGGMaHbYeRjwuIz4v3FtjBsvOoYWUXXy5hHGx4m0fnpB1Q3Zhh0Q4yMhxeadDUDu9%2FonpcOSskqfdLN6uk5ssqlNJ2DjuHl8JDxInk66H0EJcj0wGtrou%2FKo%2BVNFq%2BZchvG4Ikc%2B6zgM62X7kDdWkFfUfgu3A29cOYV%2Bq4ijLyVEXQ02Qkgw6JslIyE847%2FLJ1RSSlsUlr4CasOA48Rt2G34%2BqjdFK6yyy6wJskCXtGWCmhmHE3Obhq5q81U9VaVd6oxGmgCfHUOuTf0ZZ6drnrPQJTLdVyaU5HfoTPUv1ZRDbCGr91oxNsuP7Jj%2BJKSV1bUHpMqW%2FTtXxn6axjlYVtokZS7YV0CCECohZ0EnFLi6P00xQRIpC2LL3lWd%2BuFwGTF8%2BQPR%2BWH1Rvr2a7V9OyvBZP79Cm1wpok56IGyhpZkqrPPf5Jv1T9sfHBI7i55jA7JkxLDyE52gryN%2FldcwkchNa5RN4Mqxp7iaNoOZeQ0eoP1b978kt1whjZcsczn5%2FgGKjXuDYOZZmAmHbfjLXxp8z8VoXnMdpEfdx%2FIJp9bOopT%2BOUs7HWW2YQk1StTOzDSPxmjeGMjdJFF0TCx2vzJBjqkAUJtd42G1LJPzn0lGMJI5Ibie4Ui503Lb4%2FbcnUOhq1zNqUZSysNMCK8J2mX%2BopBSoTaaxFMLJwcQfX0eJdB78d2g2ORulB7ObazYinVvwbXBQRriy7ywtcP%2FEOl1DGswH6G5y9fxevjgObklB11gMI04vigjSZbXbes7V1KJaYxAPBF1o8SPpZiTHdiaYWgXZJvYAsbCfkdT4lQdpc3JdwkT9iv&X-Amz-Signature=b06ad5ff663210ac18c7a23ccb4c1a4b0eb8a915b320a7ea5be7bab5a4c79c3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



