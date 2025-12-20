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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FZG5ICC%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYvCHweiqXYnqbdXnN2rcVwt5KalX7KjtlJfeNiqNDZQIhAIYfTXvX1MF%2BgfUohJ9rgwoa4AQe1%2Fh5%2BBTeX6WhVF%2BzKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMCbQyrRu%2F6rtmlikq3AMa2V0AVqBhh15y4Lom35HzIzcfMpGdvffQG58VvE6kqo1pD2Pxr5G67Wg%2FAEAN8Hka9GmgDjD8e8pcbuHLGmY4w4FvZfaRjWu1GwsToRUbGv0%2FFRHZIF%2BU4j2sQphs41E6CBaRpUBV7MaFYRD9tPeuNI%2FFg%2BlsYnpcywDf5dimO5UbwaaFC97S8ymn%2FIqbfLpfHmAuQbqXymHJmXFH072sbL%2FCp7zfCtC%2Bc82pRzMs8XkPOAjZtA9KGzX74y66zt%2FO0LTCSINWmeWyKvT7jlwY%2BMHQyDu54CSGKdL6ta8yoWN1BMA0w43AIRAjhtb9Ow%2FDhEcaUoWkWUbCAS%2BY5CetrRouuNz5cIywGu71OYm0MpaIBSmu6nz%2F0%2B8YnYPijbk4BVSGJMTzLo3wWlcejHKpvb1XRj7EAPJ1JnEPmFYR34qEgxMWXoQbykPSQ9%2Bfu5528uMdERnO53N1GpGUhz7kuJdCUsaKzArbWUi2DkNP%2Fwqw4dR0Ofxnofx%2F1HIGPP7VbMn%2BAAWUJeJGdhmA8tHeNtP31zxHW3WxBwP1%2BJaQHKo%2BE0TQrtizzjurOEKnvIyXDdXfd4Hg9kGxz2FXr%2FdXzS9lGD7azYUa3fbn%2FPeFDPmYwDuXCpZf2FCT1zDnhZjKBjqkASv5D99XzZra1tPoaXAMyTIj94mIDXtx7GC9wdow%2FclE3OUO034cnLHKZrTrS6kK1UTt6Rbkjtu8uj2ivhJGqs66m7P3uN1nxcVoK6FXUmpIWhiQagj5K%2B8Q55n%2F7q6ldftKccTqeMqhrIw9ypRJI%2FPWa0ao3EvoAFK9ooEzGf2C2HFvnacWHoR8apxqW6RDmBkTOEWyIIjT1jJsZOunE8SVW81K&X-Amz-Signature=82af098558976b42185d5c78a90fb155c0225acfc8cce5579bf8ded69dcf05d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



