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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N26FPGH%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2df1hMq5IT8mwFmAf107n%2FitwLvygs1OraxUlPrvU3AIhANkK7gwIEtfX%2Btf4vc7YUrWqaBrcudKMKBYsZDN5LS22KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7WoXKnmfhmFBLNCsq3ANXL4plOQU%2FZwcGlboSuoyp85%2FnHvtBy%2F8Ztc4jBPtlIBq9kOgjlIqV3M2cfOTG8uHUg75XO4SG1hOhfOOaMAVkAPRz0cBwDfXt2XzE229wGIXc9mzZ3p4U15RGplnWQSxrR%2B75SN8PHqGNOGf066WNuo9stjU%2BA88TCclp%2FIzxLgyt9qo5J0%2FEzlppy0UElf%2BJrYmVXswiOTbnvM2U%2Fs3hIRTHMO09lfND8%2FCCcWewG31QJbCKLiX%2FUcXDt7L%2F4%2Fqcd%2BG211Gn34ITYfDkwT0wPbN%2FMu4JPLRuXwC7OiD9LdzBmkKFlLKmqKfZr5sHpq4peiwVmLjtpOuWXB6LJNnpLb0URttegMR53CsVklvCyM3Iz1cRHpcEA80XWXpAcfhUglsZbgBKJMlomgNk0qvWNSfYDovOBfH13pM%2B5sOPWNelA7myABlNXYUo0gRowiB2dF7tgX%2B5W7UZgzf47lxMngH7%2FrK9MTpwSP6kaajHShjamknB1hK%2FEiy9%2Bmp6vkeaih7d%2B6Ma%2BQa2O0juKWwoClvNnhYS11jVL%2FFLlGqP18A459%2BKjiUCem7ACf2Q3ni9AO198D7KAzdzB%2BjCKCltF18qOdsoeO0%2FXx%2FX7r7u3XvvVZ6cnDPCWq9c1TCEsszOBjqkAYJx4e6mZGK%2FMbCkQIxgddnq74Ok87A2ttmvd1n7jlhsVnjZ%2FAfi2nrPgMmQAFWB4ISQeTPGWuAaiAHbI9br2GfqJ8MlCUOmNrDBHahFDNPM3%2BtkXN2VpXNMSltf71vC1CFkYshzzpxq%2FUkfTZXc5jV%2BsKWzOdDGsRLNc6Gb8weU00zaclcdZVjgzyp69dIH6bXIMGlkiHYw6fTcJHvBYjUCZdzZ&X-Amz-Signature=66b4f68dcf70b9bf0a6f311e91e20bd6bad5e730b4e4c1000e9006bda7fc0785&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N26FPGH%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2df1hMq5IT8mwFmAf107n%2FitwLvygs1OraxUlPrvU3AIhANkK7gwIEtfX%2Btf4vc7YUrWqaBrcudKMKBYsZDN5LS22KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7WoXKnmfhmFBLNCsq3ANXL4plOQU%2FZwcGlboSuoyp85%2FnHvtBy%2F8Ztc4jBPtlIBq9kOgjlIqV3M2cfOTG8uHUg75XO4SG1hOhfOOaMAVkAPRz0cBwDfXt2XzE229wGIXc9mzZ3p4U15RGplnWQSxrR%2B75SN8PHqGNOGf066WNuo9stjU%2BA88TCclp%2FIzxLgyt9qo5J0%2FEzlppy0UElf%2BJrYmVXswiOTbnvM2U%2Fs3hIRTHMO09lfND8%2FCCcWewG31QJbCKLiX%2FUcXDt7L%2F4%2Fqcd%2BG211Gn34ITYfDkwT0wPbN%2FMu4JPLRuXwC7OiD9LdzBmkKFlLKmqKfZr5sHpq4peiwVmLjtpOuWXB6LJNnpLb0URttegMR53CsVklvCyM3Iz1cRHpcEA80XWXpAcfhUglsZbgBKJMlomgNk0qvWNSfYDovOBfH13pM%2B5sOPWNelA7myABlNXYUo0gRowiB2dF7tgX%2B5W7UZgzf47lxMngH7%2FrK9MTpwSP6kaajHShjamknB1hK%2FEiy9%2Bmp6vkeaih7d%2B6Ma%2BQa2O0juKWwoClvNnhYS11jVL%2FFLlGqP18A459%2BKjiUCem7ACf2Q3ni9AO198D7KAzdzB%2BjCKCltF18qOdsoeO0%2FXx%2FX7r7u3XvvVZ6cnDPCWq9c1TCEsszOBjqkAYJx4e6mZGK%2FMbCkQIxgddnq74Ok87A2ttmvd1n7jlhsVnjZ%2FAfi2nrPgMmQAFWB4ISQeTPGWuAaiAHbI9br2GfqJ8MlCUOmNrDBHahFDNPM3%2BtkXN2VpXNMSltf71vC1CFkYshzzpxq%2FUkfTZXc5jV%2BsKWzOdDGsRLNc6Gb8weU00zaclcdZVjgzyp69dIH6bXIMGlkiHYw6fTcJHvBYjUCZdzZ&X-Amz-Signature=959613ff59aa2909887ef69ca20b5d174bbee79e08ed39d4886cb02a19b5f0fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

