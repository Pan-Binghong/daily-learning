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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVM2BAA%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLDGoHa3VsD3Gu%2FxJwUq4Fk1us7Vm0YReZWsyYWK7G%2BQIhAMJ1X%2F1LHsu6CIiqjn6rq9d9RT7MQagWh5Kp%2FPBZbUG3KogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwb9Ojv2f2qBo5H9IEq3AMky6x97QgxRydw3WkExrLoEoxjSLISzretAu6PyxiWsLKvV4qzoTbpyQrYace0M0W3nBTsd8zDBhKem4YmtyGiqicPNhsIRAbhMeB%2Bp8Ma3JbfJ18qJy%2B3NMwH4JT159itfp5B9xrijfoNUXZfXxhKWrHqouihc6AbWxLU7TqH0VCjLqQnlSJj0oZYVDR6gB%2FUB%2BGIN3k8NhDeQTjkuIATMRCYMYq1UIfK8CKh5Pj7Ute7sXrIhPZ9TWVJPwNRab4aJMFNviA0uthg%2BpMJyhZQxQNt6IKbVjnjtCIpp2Y0kDDbCkXRiajQtkNtwlZuPEsDuK%2BnSNPOTZdIL8ctlue6MM5243qicAd2Sx4oWS8DBN7sdAkr4%2FC6Q6Sb1J3ArkSkd0lM5UC%2BzCXXUAnwQvYeTJXOnUbUKZBoZGFbT6pRIkVor5EIMgWDHrw%2Bx%2FETQPQGFpO9JeuqCCQThoX4ANbwkoMUu8aMftLMjpY4REUIC1DvRRA2ZqFZX1TFCX5oslVW3Sc%2FRxgS%2BKIoXFWMjiBP9pVTGB2SQIRRD7o%2FA70aEbMx73SXAU8dMEd%2FFDD4u3JHjGTF0quPpUZKfDwdlTl4PIrv1JbkhBmRg8RtiYUMDrke%2BDkXzWh7pEw2ODDy457JBjqkAS7nnsIXgmkO3nSZn4s75azQKunZzxp3Vg6TQMdjisB0%2BGUvq2S9T6jHOOiJASo71tuu8R7m3GP0ov%2Fiw%2F9apXxuYCbvyIR4FZa0oUEHjj6%2BabruPdM4o1eSNyK8jE8vdSsPk%2BIrIRPS%2FAliLUcNUd5qMDZHxDducCoWVmq%2B4O69b4HWEieOu6aWkusTIVRzKDfbtdakyvCb%2FSnfbV%2F2wrwDKwTm&X-Amz-Signature=75037dab57fdac8ed64331937d357cf9d99c744e414d68358ef84a2c1b94e64b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



