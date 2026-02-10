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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOEDB7TF%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAi12697ORud%2FWqt6P1NImHityoGxQjElR9HAGtlv6uKAiEAtpq3Fn%2F0TGit9XpgGgE%2Fg2cRL7mPV4zSrSIrZw%2Bo2dkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcjvWKW329aJxa3cyrcAyMrIOw9uRWximqgpqRLmeK2VbjNUR%2BwygQQDUaBK8F0fL658RWKbQXgZidLNSts7egtBvtXwNXscEL6VUF0DZmug%2FE%2F9B6skvloenogJV2cNDdPycarHpoJ3FOq6ui37f%2BpXmCF0vQ0%2BFSi0Hlbs9EMFaOEBHKjqF%2B0aVGdRZjYpI0kj4y3AD0I68843KJ5FW%2BEB%2FBws%2BJgD0Qg%2BVmVkTD8yJJoj3CpbEa34ldiV9D%2FYUSJMEfjxjzm7bB%2Bm8xnA%2BMO2CxnmM%2FDhFX%2BlfQjEuqaf33jsn4%2BaDklTwTpp%2FlT8El4%2B8MC0Yhv0XNYsAxrQFBaf%2BRN14iCofKvkVgX2nQXS3qNFFFoQ1MX7anauuI1r8O9hOewbhsaN%2B4z%2FR8g2ZfXFc4UBEkbHf%2FbxDEDisrN6XHW%2B4J8eU9%2F5xZtJasfNjSYPI4mrJjtSAW2%2BO1Wzm9O2h88Kk8%2Bj%2ByIpPuNIJhzHCJMs7NAE2h%2FJ5WZUCPQO5XFJMuCu9nGxu1FzDki5ZYXZkrSDSV%2BOPMVP%2BJ72ZkLppLxyTsoMeYGUXAWridhX25Be3UaIzNclP6iim7268imyeKcVMenH6jcwuXZfC7Vr3jM50RaaBSl4bVcRWsJOCLms1K6G6n4DlUZMPzCqswGOqUBp2fjFgVWY3M82%2BN%2BbNv7jAVBFJEZtaTIk%2BJh42tVvtJNrIhJbwhst4O7%2BkZNXRrMv%2BeUR0%2FuVlj8JCrKLFW%2BfVCDnSwiVXO1fRPumGtpWEESOZXHXyroYG6GH%2FjLmx3Q8%2BU6C861LI%2FT00DCiby1XvdldbLYwUAJL%2ByB1AQt7QNZmTfROMS5KOxP0blkaMBkHPqymBVGQn4fJ0OdeOZBP%2BzX5PxU&X-Amz-Signature=d8aaf1f13dfabb617feb95936b936088ce80dc2840f75e11656fec6369f23117&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOEDB7TF%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAi12697ORud%2FWqt6P1NImHityoGxQjElR9HAGtlv6uKAiEAtpq3Fn%2F0TGit9XpgGgE%2Fg2cRL7mPV4zSrSIrZw%2Bo2dkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcjvWKW329aJxa3cyrcAyMrIOw9uRWximqgpqRLmeK2VbjNUR%2BwygQQDUaBK8F0fL658RWKbQXgZidLNSts7egtBvtXwNXscEL6VUF0DZmug%2FE%2F9B6skvloenogJV2cNDdPycarHpoJ3FOq6ui37f%2BpXmCF0vQ0%2BFSi0Hlbs9EMFaOEBHKjqF%2B0aVGdRZjYpI0kj4y3AD0I68843KJ5FW%2BEB%2FBws%2BJgD0Qg%2BVmVkTD8yJJoj3CpbEa34ldiV9D%2FYUSJMEfjxjzm7bB%2Bm8xnA%2BMO2CxnmM%2FDhFX%2BlfQjEuqaf33jsn4%2BaDklTwTpp%2FlT8El4%2B8MC0Yhv0XNYsAxrQFBaf%2BRN14iCofKvkVgX2nQXS3qNFFFoQ1MX7anauuI1r8O9hOewbhsaN%2B4z%2FR8g2ZfXFc4UBEkbHf%2FbxDEDisrN6XHW%2B4J8eU9%2F5xZtJasfNjSYPI4mrJjtSAW2%2BO1Wzm9O2h88Kk8%2Bj%2ByIpPuNIJhzHCJMs7NAE2h%2FJ5WZUCPQO5XFJMuCu9nGxu1FzDki5ZYXZkrSDSV%2BOPMVP%2BJ72ZkLppLxyTsoMeYGUXAWridhX25Be3UaIzNclP6iim7268imyeKcVMenH6jcwuXZfC7Vr3jM50RaaBSl4bVcRWsJOCLms1K6G6n4DlUZMPzCqswGOqUBp2fjFgVWY3M82%2BN%2BbNv7jAVBFJEZtaTIk%2BJh42tVvtJNrIhJbwhst4O7%2BkZNXRrMv%2BeUR0%2FuVlj8JCrKLFW%2BfVCDnSwiVXO1fRPumGtpWEESOZXHXyroYG6GH%2FjLmx3Q8%2BU6C861LI%2FT00DCiby1XvdldbLYwUAJL%2ByB1AQt7QNZmTfROMS5KOxP0blkaMBkHPqymBVGQn4fJ0OdeOZBP%2BzX5PxU&X-Amz-Signature=84e0539994ed83402cd4d05107ce612b53e7c786fb52af067a58eace81c3cab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

