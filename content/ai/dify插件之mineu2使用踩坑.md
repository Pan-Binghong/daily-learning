---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV7XZIZ4%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExI2DsbmbGdXelof8ufQWLxyduh1gY%2F9t6ryn8MWAePAiEA46btG79vu3B1ZJnRFAHx3cAQ%2FNlVytFv%2BcGLY5N%2BQDcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOr1QFN1%2FdqK5KDcyyrcA%2FgCVRub2M%2FY68AWz5%2BmSCe3R3x%2BMLkntK8mwNePV9ywvT1ZUKL1tHWI5EXng2GkIl4s%2FsbNFsFodaXauiESVmqxzv8nEq7AKCBg411%2Fcw0blpdTjOfWjPz26gTEpv48ZZh0kkvr0f%2Bqh1k7LLDyocJaOcZ8JW1gLWUGFAzycKE2kMcm%2FCvy2RV8gvqjt9TE5PY0lciNLL9APG3MC5rCivmPoXq1eAGMcsWo1tB4bL4WK8GWzkFle2f%2BodnYjFIXqPu14VniV%2Blbskg4cKH9lDvvoh5w0pegAUwxmd5yLDkNQqLQJicxiXk88BlSbqxc9oSmW%2FXan5NdWXgcPGuIN724UNh29%2B86pzbYkGnb7pG9DtmDVD1TH1qkrFyg5VukZHSeLHelp8lpBRjGBeSexZOMNBUNdiQ%2Fb1S%2BiWgE1tFojO14kg4F5aqVNnFDa6Mauazv4I0QVdXj9ErqzIaO23bJl2noCjnZDPSlIXw6rx8BsPkNsSH0a2e9J4m5YJwf7hyR9WRxg7%2F9CMJx7Ywp308BnGE7SUYR0NP%2BqD4q0%2BKcvl29FuxRGT6YjdP2ZeamydnluK4KIKUyz4PCZFi0s0r%2FiydWFtLzDRcyeAzJFkDQDQVeiTJkLbEIMRB2MMTN9csGOqUB2T1VP7Q1Lfx3Bwe2%2FFLpaQtv4zHbRl3blF%2FWJfrjft469CiPp%2BLhOPsdvKljljFVt9AHxqyZ7d6FtHfUTLhdvFr989kimsidfjaEQwSkJWAil2M8qSsWUvd4sN%2FM1FOqxPrdHFm9sBTlKnRbeSU06n%2B42ae3xeCejjsoZNY2tMqYalMRKnZoKEoXhX%2Fjzok4zGGpsDzu5BMPXf%2B%2Bb2nxFfZKQ4oJ&X-Amz-Signature=9798ebfa0f063d023f609629bc2070774fefe78adec62fdd9a3c546cb2fc96f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV7XZIZ4%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExI2DsbmbGdXelof8ufQWLxyduh1gY%2F9t6ryn8MWAePAiEA46btG79vu3B1ZJnRFAHx3cAQ%2FNlVytFv%2BcGLY5N%2BQDcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOr1QFN1%2FdqK5KDcyyrcA%2FgCVRub2M%2FY68AWz5%2BmSCe3R3x%2BMLkntK8mwNePV9ywvT1ZUKL1tHWI5EXng2GkIl4s%2FsbNFsFodaXauiESVmqxzv8nEq7AKCBg411%2Fcw0blpdTjOfWjPz26gTEpv48ZZh0kkvr0f%2Bqh1k7LLDyocJaOcZ8JW1gLWUGFAzycKE2kMcm%2FCvy2RV8gvqjt9TE5PY0lciNLL9APG3MC5rCivmPoXq1eAGMcsWo1tB4bL4WK8GWzkFle2f%2BodnYjFIXqPu14VniV%2Blbskg4cKH9lDvvoh5w0pegAUwxmd5yLDkNQqLQJicxiXk88BlSbqxc9oSmW%2FXan5NdWXgcPGuIN724UNh29%2B86pzbYkGnb7pG9DtmDVD1TH1qkrFyg5VukZHSeLHelp8lpBRjGBeSexZOMNBUNdiQ%2Fb1S%2BiWgE1tFojO14kg4F5aqVNnFDa6Mauazv4I0QVdXj9ErqzIaO23bJl2noCjnZDPSlIXw6rx8BsPkNsSH0a2e9J4m5YJwf7hyR9WRxg7%2F9CMJx7Ywp308BnGE7SUYR0NP%2BqD4q0%2BKcvl29FuxRGT6YjdP2ZeamydnluK4KIKUyz4PCZFi0s0r%2FiydWFtLzDRcyeAzJFkDQDQVeiTJkLbEIMRB2MMTN9csGOqUB2T1VP7Q1Lfx3Bwe2%2FFLpaQtv4zHbRl3blF%2FWJfrjft469CiPp%2BLhOPsdvKljljFVt9AHxqyZ7d6FtHfUTLhdvFr989kimsidfjaEQwSkJWAil2M8qSsWUvd4sN%2FM1FOqxPrdHFm9sBTlKnRbeSU06n%2B42ae3xeCejjsoZNY2tMqYalMRKnZoKEoXhX%2Fjzok4zGGpsDzu5BMPXf%2B%2Bb2nxFfZKQ4oJ&X-Amz-Signature=380b79a9bb85ad6525b916aa21fc3cc6de463c0b420bbfbdd79a3feada93c59b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



