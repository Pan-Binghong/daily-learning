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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRKUKMSB%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCT3KpV6HNHWGTTAZjSVqQoLxboLM6Z%2BpuLiXljwNgdaQIhALVxFYvuUjYfGX%2Fx23iDVInur40swY8Lv%2FhGrXrjKK8RKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5azKE4Dyhdg5WkKoq3AN%2Fr4MUYjCks%2Fb9VwY1udng1czGVO6gJfqH8UmdYU4JW0GRy%2FRS4luXc%2F%2BJwxLo%2FiAHHEDB2%2FeqZydR5PalA%2FCrYQpshFrPT1kqs1D5JgebamvtZFtzdD3vROSWgxTMnYPfIM%2B83Ly3%2FAGrHo5s5zaYaT%2B0WL11ue8cD2PzvI7ec9QIHo6EHNQedz4niF%2FeQ3vFSYN19qYpF9iLehWe9qanKb6WJ%2F7Tip8OgFr8zg65jSXDcyDNqaGxohawt6kUU9xc%2B5y6SBAT2DdHQFeVZtDLA3JyCzhzbULhRZP405PD64IvMwsPB2qAGp16saUQJYMVF1xkb0y0i6AudKXG5k17OulnXEQUpdT1PejPzyWqGhtA2uHLAA%2BY8Inp1TIGWiAXf4CvVQbnghQisW9yDikJtheeDOGQQdAwS3Pr8mFju0rfxZCG%2BJjq1GzW9UGfcFtSjiNxiQAuPSDQyUsyEKj%2FU2WQSSBmm2vO6HTlcVp1gUcR31%2BQ92sCpFFUteeN38hp%2BoeRduOnWLnhcYbQIro83laYKLh2b4QuQ5BblGM038Cd62t1JOJDvvKgBtepnoykIyFJsBvyAB3vcw2MShEHfLHa7fU%2BiVTMQ6EVwbHi6zdEvRzKdSJ6XIO39jDz4OTIBjqkAZHcqACsEC6qIOhcLNGKXSZy%2BehAs3%2BGsKGB%2FsXJQesV18dYIEWOkrNfr5ltCjSA25NhtDcfwZzcGdDoCv%2FbWa%2FsqZbW7J9P7m3RgpC9EQ1n1g8QA8JT%2Bp6GDTlU360Sj4Ku%2BlPCBuFKO%2FiMUCk8npdEwhtbfUJtQtl9GfqtGaAu5BdxgX3BqoV3D26vLbLmUx8%2B3glLw7i6AIc0SEcnHbo3Qjyu&X-Amz-Signature=f790eaf455e33963af8a08e9b94e1127738b955d9829add127fb23b9c38688eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



