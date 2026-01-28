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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WDQDKU7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADAa7%2FomYD%2FWCwMpiRzfHEVmD%2BOBEi3V2B3jZkOwFAdAiEAuP2eMaiYIaMA%2FkSVHnNmZzeHX9Zqb7A8w5FVaSFaCf8q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDB3CLsltVxWfBOpBSircAzyGgHJieqJA0bu7t40Nod09KTkxyIbbKGaUoMTa8YtF1S8WJfBUTg5wtmW9HZq4B96y09NRMrWCHABo2xA0VzOSwzG1Dipld3YyFZH26OyTw8JyxEZjAWKal4PPeA6DBSPc4ovIkybODTE3JjPZnGF8h3MIwcJVhdIyPyyHK3oewDiVLrZ5DA9QtsbfTLolPtEqDiau24hW%2F62PbnbdtFeWKWJuSAdWtayKhY7mwyVdC7zj3uctj70g1ryQhCSDXuBN1GWAxUALH3RDXcfYx1fjH3Ela7%2BSBxpFJo6rIaapSFzK4Yb5UT72LbN4GmLPth7a8DbqK3TdOURBrCrmvYNlbEcErrk5UEattjLsOKRMZfqR73ZvytrblvY6oTTeDF35LXugsofpD2HFGWgNvHHg8xRYwMVemfU3XK3HOR0zuBgmeQOYAQsLwRVflIdULFGV2o9YEXbe2tIJEF1OakfIRuT2oHWOd2yuUYc7JD2r4MPWJx1jxcj0aHzvoDXGiUjJrmYZdRgwktnlyKxR8Za%2Ba7Hev3eUo%2BS8fk8TveX%2Bc%2FSCFZM%2FBwGwz2hpC1UEFFxx7qe8oFZyXsNfzkXYGMaqo6YAPeqlwVlSiDJYYNZQgzjIVbiyq5l%2BI3pvMPiW5csGOqUBKA9t0gXY0jELKV1866LEPdntqoJ7YijatZB4GVnjywAJZG13ACCwEBZqgCcZRseAp9YqNOtPiunwUFk8QxK12%2BCWIWgOhgXhweBu9Rx%2BUHaYC%2FYCQ4idva6wDW7ITFXm5EKrRdFIRCVlsh8uf7LIxOS%2BkyGmPPB%2FlWlBeDtbIHL9AMf6Up1iapuA4%2FHBD6rJaVZsH%2FPr4AMxb1tZTDvNOg37BGzi&X-Amz-Signature=f9b7facca9ecf522c4684d10083589bc191273336abd3497088f922ed7c7d11d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WDQDKU7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADAa7%2FomYD%2FWCwMpiRzfHEVmD%2BOBEi3V2B3jZkOwFAdAiEAuP2eMaiYIaMA%2FkSVHnNmZzeHX9Zqb7A8w5FVaSFaCf8q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDB3CLsltVxWfBOpBSircAzyGgHJieqJA0bu7t40Nod09KTkxyIbbKGaUoMTa8YtF1S8WJfBUTg5wtmW9HZq4B96y09NRMrWCHABo2xA0VzOSwzG1Dipld3YyFZH26OyTw8JyxEZjAWKal4PPeA6DBSPc4ovIkybODTE3JjPZnGF8h3MIwcJVhdIyPyyHK3oewDiVLrZ5DA9QtsbfTLolPtEqDiau24hW%2F62PbnbdtFeWKWJuSAdWtayKhY7mwyVdC7zj3uctj70g1ryQhCSDXuBN1GWAxUALH3RDXcfYx1fjH3Ela7%2BSBxpFJo6rIaapSFzK4Yb5UT72LbN4GmLPth7a8DbqK3TdOURBrCrmvYNlbEcErrk5UEattjLsOKRMZfqR73ZvytrblvY6oTTeDF35LXugsofpD2HFGWgNvHHg8xRYwMVemfU3XK3HOR0zuBgmeQOYAQsLwRVflIdULFGV2o9YEXbe2tIJEF1OakfIRuT2oHWOd2yuUYc7JD2r4MPWJx1jxcj0aHzvoDXGiUjJrmYZdRgwktnlyKxR8Za%2Ba7Hev3eUo%2BS8fk8TveX%2Bc%2FSCFZM%2FBwGwz2hpC1UEFFxx7qe8oFZyXsNfzkXYGMaqo6YAPeqlwVlSiDJYYNZQgzjIVbiyq5l%2BI3pvMPiW5csGOqUBKA9t0gXY0jELKV1866LEPdntqoJ7YijatZB4GVnjywAJZG13ACCwEBZqgCcZRseAp9YqNOtPiunwUFk8QxK12%2BCWIWgOhgXhweBu9Rx%2BUHaYC%2FYCQ4idva6wDW7ITFXm5EKrRdFIRCVlsh8uf7LIxOS%2BkyGmPPB%2FlWlBeDtbIHL9AMf6Up1iapuA4%2FHBD6rJaVZsH%2FPr4AMxb1tZTDvNOg37BGzi&X-Amz-Signature=4879bca5afd77560b6f16cec4a80accd10ed219789a0dcad22f0657ff85fb59d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

