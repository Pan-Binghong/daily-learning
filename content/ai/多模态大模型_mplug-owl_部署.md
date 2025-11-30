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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QONSHYT%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIFIAwYeJ3BKQSFIAsr1CMPz3rgR5CKauQtq%2B8Eu0LfwoAiBpGf2Ysh65NJuxGOOaa%2BVGB1IaNGivHESYuQ2nITIOlCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCTAp7xtl%2B52LlXThKtwDIJOIpZhSqjDKmOmsS1oVXG265oLcSS8CSGG7VuN0c4x%2BEpwHFKruntmoDP8omqvhFXbvs9slw3EsH38lepKjM8l2V%2BZhz74lPJM9UpMPa27q1ThsTTK6RpzXr9U7i8Rh5c2qTf08dpqrFhen5oCGHZovBqnYgOcQTn80U7j190AUVJg42rTonT8rndzmJREQsmen3st3merDfajKs5fnYDE9SwpkKM2m1%2FMEx38kaRuVJZ5ZkWfjf8v5Kv5tPyQdqP%2BRl8RGZm%2F9%2BujPuTQwTOis4wezj1LKIEhkKDSfyzdYmbIx0XwzBPksVQJVWS%2BqQTX4krTO9Y4bX9bR4N0YZI4ZGCxQUc7JHeJRlnEmbmVSDSQb5jgFnJpSD%2Bk5NcqniK%2BECXozL5YeFC0fsGgKT3XTOlEyHLBlu7Rc38ZFvr6TA8ZZxieynxmRpzWKgQsLqB1la%2F1eGic4%2FcMkeuu38z1VxeoUsaHK8p9B8ajbZSgwkSGnFfyXjJs8UWd9QQmmEBG0CnrGNVOYWI3IqvthoCe4OeSYxLqLiJA%2BjDF13kNlGNYsMOUk%2B4rz87OEWFAnAKFKrXKMqk138opNAKh7cxFjpiBMTpt66C1%2BAjHAFfQcQvPbzb7cAZZmaAgwpc6tyQY6pgEt5iZm3T7dr357kVw0bcVQepcX5wDYZXFHmxTB24X%2FOsGqb%2F8eMKBs5MJWJKQcOCTSxAxagcLV4zw7v6f7M6BRvy0vZTiqfVzNIBCYvzlnmHUzuVhzxo%2Bxw%2FdUQeinQZKXXj%2FpRNm4t8D%2B4U4oxRUXVeq1qXuXNhF0X7Vy5HFtH0U7pEUv5bhcCk9j9sc2e37%2FGAE2VJJhnnQChSmAFtn%2B1aaY9Thq&X-Amz-Signature=b2e539ba233c1eab05638cb3d104c9785741b459fcfdb87b548ab9b5aae80e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QONSHYT%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIFIAwYeJ3BKQSFIAsr1CMPz3rgR5CKauQtq%2B8Eu0LfwoAiBpGf2Ysh65NJuxGOOaa%2BVGB1IaNGivHESYuQ2nITIOlCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCTAp7xtl%2B52LlXThKtwDIJOIpZhSqjDKmOmsS1oVXG265oLcSS8CSGG7VuN0c4x%2BEpwHFKruntmoDP8omqvhFXbvs9slw3EsH38lepKjM8l2V%2BZhz74lPJM9UpMPa27q1ThsTTK6RpzXr9U7i8Rh5c2qTf08dpqrFhen5oCGHZovBqnYgOcQTn80U7j190AUVJg42rTonT8rndzmJREQsmen3st3merDfajKs5fnYDE9SwpkKM2m1%2FMEx38kaRuVJZ5ZkWfjf8v5Kv5tPyQdqP%2BRl8RGZm%2F9%2BujPuTQwTOis4wezj1LKIEhkKDSfyzdYmbIx0XwzBPksVQJVWS%2BqQTX4krTO9Y4bX9bR4N0YZI4ZGCxQUc7JHeJRlnEmbmVSDSQb5jgFnJpSD%2Bk5NcqniK%2BECXozL5YeFC0fsGgKT3XTOlEyHLBlu7Rc38ZFvr6TA8ZZxieynxmRpzWKgQsLqB1la%2F1eGic4%2FcMkeuu38z1VxeoUsaHK8p9B8ajbZSgwkSGnFfyXjJs8UWd9QQmmEBG0CnrGNVOYWI3IqvthoCe4OeSYxLqLiJA%2BjDF13kNlGNYsMOUk%2B4rz87OEWFAnAKFKrXKMqk138opNAKh7cxFjpiBMTpt66C1%2BAjHAFfQcQvPbzb7cAZZmaAgwpc6tyQY6pgEt5iZm3T7dr357kVw0bcVQepcX5wDYZXFHmxTB24X%2FOsGqb%2F8eMKBs5MJWJKQcOCTSxAxagcLV4zw7v6f7M6BRvy0vZTiqfVzNIBCYvzlnmHUzuVhzxo%2Bxw%2FdUQeinQZKXXj%2FpRNm4t8D%2B4U4oxRUXVeq1qXuXNhF0X7Vy5HFtH0U7pEUv5bhcCk9j9sc2e37%2FGAE2VJJhnnQChSmAFtn%2B1aaY9Thq&X-Amz-Signature=c05d6e12b715f000bc53e6ec0dd263e8b93afe422784044ce69136af6119787b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

