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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3ZGG5LX%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2qBW0sDXHLGkAjYD%2FFnn0gXuWFk8MTeFkwIRM134uaQIhAKvxejxgVBN8BSIdN9JwH3P5BwFo1uTsG%2BbolCkgwx1mKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2Zc6jAoKKPsPMGJwq3AM0kGDRUoQa%2FK53guSmc372SoPHn8oRcX07FeJBMrUQ%2FqjUljFffemGQ7YjSodYhLGQFtocSiDo6oicSaW95ERyZYSokq7eyVNzgj9fG4Y9FSYnjCvVsfXKYz5YGH86pYbQJsQay54TN9tUr3TZvObZ88TznExVYtojsirWTVvB1Vhj5ZDR8VxmCF6ICD1bEqg1plPSpjg7QUexsYmXq6dZ3KoypUZRc%2B0x0IfRgTgQpTLlPNv6xU%2FZ0jdCwCZOwEf64dfpoOMOWzf%2FiNdRAlPaNZ2YQ9pgA7Tufhtt0rkB4ULYs7YPQ%2BwA%2FEii%2By9Fk68QFvHLtAN9IIM5qNdQaHRr8wjDCtFdjCcDGBb%2FOe8vpF3lxewmwued69MQnNDxy92HV1oZgHyRTHSbhIia0fd834Ej%2F2AmuBf7pB4DTMGp96WzpQfkXKt9n3sUV6L9BiIc8B94ghqDUymy2Tbr3pl2wME2ZRAAtB0Z%2BF%2BGRP%2FEYWPTJg3kZ1XxfL%2F2WS8CRJKjOnGq8XXGvLsY85XWNwgRfXHXzXS2%2BIx0S%2BFeO2sIqWdXLfHYjKz4DlTjltY%2FTHwq0zfKyZ0fc0dBpdyF3rsqfyRmzWOHsxllXlS0hSGue5wCevCO0suoByRQODC9pY3OBjqkAWI03L5%2BC0hV6aWy5%2BrezgpDpwnq6tNnxDrGXCCeYrj3cv7COLk0hF2oY1DTwlBJxm%2BOIxRlJyJSb87bGn%2BGF9%2FykW9OfxbO%2F32kQsXi4MIhCLKLK6ne%2Fq4%2BGLKPx%2Fa7PJgjanbMfLPkU5FqTjkM%2B6ADnVCBptuRps%2BvZV4PFsorotuFHa5RjuS2VTLhBofYae2IrBtndwdji%2F2dyojVNxTIrp59&X-Amz-Signature=6ab0c5683813e60aaaf94be7ed69fd95fc43eda626b11bc4023bd813303d5218&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3ZGG5LX%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2qBW0sDXHLGkAjYD%2FFnn0gXuWFk8MTeFkwIRM134uaQIhAKvxejxgVBN8BSIdN9JwH3P5BwFo1uTsG%2BbolCkgwx1mKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2Zc6jAoKKPsPMGJwq3AM0kGDRUoQa%2FK53guSmc372SoPHn8oRcX07FeJBMrUQ%2FqjUljFffemGQ7YjSodYhLGQFtocSiDo6oicSaW95ERyZYSokq7eyVNzgj9fG4Y9FSYnjCvVsfXKYz5YGH86pYbQJsQay54TN9tUr3TZvObZ88TznExVYtojsirWTVvB1Vhj5ZDR8VxmCF6ICD1bEqg1plPSpjg7QUexsYmXq6dZ3KoypUZRc%2B0x0IfRgTgQpTLlPNv6xU%2FZ0jdCwCZOwEf64dfpoOMOWzf%2FiNdRAlPaNZ2YQ9pgA7Tufhtt0rkB4ULYs7YPQ%2BwA%2FEii%2By9Fk68QFvHLtAN9IIM5qNdQaHRr8wjDCtFdjCcDGBb%2FOe8vpF3lxewmwued69MQnNDxy92HV1oZgHyRTHSbhIia0fd834Ej%2F2AmuBf7pB4DTMGp96WzpQfkXKt9n3sUV6L9BiIc8B94ghqDUymy2Tbr3pl2wME2ZRAAtB0Z%2BF%2BGRP%2FEYWPTJg3kZ1XxfL%2F2WS8CRJKjOnGq8XXGvLsY85XWNwgRfXHXzXS2%2BIx0S%2BFeO2sIqWdXLfHYjKz4DlTjltY%2FTHwq0zfKyZ0fc0dBpdyF3rsqfyRmzWOHsxllXlS0hSGue5wCevCO0suoByRQODC9pY3OBjqkAWI03L5%2BC0hV6aWy5%2BrezgpDpwnq6tNnxDrGXCCeYrj3cv7COLk0hF2oY1DTwlBJxm%2BOIxRlJyJSb87bGn%2BGF9%2FykW9OfxbO%2F32kQsXi4MIhCLKLK6ne%2Fq4%2BGLKPx%2Fa7PJgjanbMfLPkU5FqTjkM%2B6ADnVCBptuRps%2BvZV4PFsorotuFHa5RjuS2VTLhBofYae2IrBtndwdji%2F2dyojVNxTIrp59&X-Amz-Signature=47192325db0ca85b6123ddb68164ecd61222efedecca21e99a382d3ed33933b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

