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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA3XUFOJ%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQChRk7djqudZFzLlD%2Fdh8f9xcBfTMZSZl2IjyvLIxn7IgIhAITZO%2Bmh5B%2Fr5HiXwX64autCZyf6BGBS%2FxAY23r%2FHgi3KogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3OhPy9nwVH39nzUAq3AOLURvweKgE36o%2F1rxNLJW2xEh8lRW%2Bu3ulhgfa4ULzaktUZXQYCeXaKTm9K7X5WfLodfon%2F81NwfbJ2ThyIhej7iaxGbJnVtjPX%2F70T0q%2FpTJcPNvYYEoFS5zLpoOrEvKRhl%2BZuzqKeEg9Eg49%2BuFrk5%2BC8fqLKHfhN1QfrVWg%2B2S%2B9VsiKNIeRnm720edT32kQMKeQeeSVjbI%2BrPLy77lXoRixCfzuVxShwB%2FO4yBDyBCpGic3%2BPThspmZYTywVp2VZPLHYwc3Qp4VN6TxBOtppNExl2fqqoIcaQRZCqFNy6Xa5Yp1c6hko2DPA6oQ8tvi%2FdZSW1rbiVhUXHR8gWFBX2I129nlt4xLEdMIgLX%2F2RMIxc%2BGQDIwrUVJTqDpHw00amOBw9TlX3d3TkJFR5ZRVHDAsjIDykWTbX9JpDWP1pkjbDU7pWEF%2B6x0%2BjA2U3777UUDefme8ICD4y5nVM8ZigF63i%2Bx1O4fMAYOukztb72e6oV27R8eIrpwnfCQhvR77nZhzvzMuOSdf5Ka%2FyB2gJEp4C18Rl9t4I4TL5Tt7zgHmny3VeygFaCpsHsCs%2FB1tcqFTBPg6ThSXEq1B4YQuzBRlP%2BGf9UIi%2BUPID9rCwRHcAyBt8jIbE17TDppejNBjqkAUA9rgl7ubtlXGvEcuMKGjvvrj9X6m01oitmQDxB2EaylDCuee%2BEdRWU7lnkeNk9DYbbPaG6miFa8u0lVDhxPFcJXebzP4B5EoDtErlbXFXJi%2BIF2st%2BzUSCQKj0OD52YOmgcPWahHYqE%2BT0MP0GpEB%2FWWYQgP1LWn8w2leqtoR2n9Q0XCHGchUma0Bc0Pfn%2FOzyTVwatXgKOfNJLsQ7s441Sb9A&X-Amz-Signature=22c517cb7a277f63245c9254351b6eca8ed04cfe81183461814e06e985cb3560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



