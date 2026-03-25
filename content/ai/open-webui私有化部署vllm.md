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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBAJYKQ3%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExs1h8tZV6U0SBwY3BS1wzPLLnDM6Ipp7R9UtbE2n1MAiEAhHSuli%2B0OhBMwcvONjxb4JkShX2VxmG8vp52FL80k0QqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLWzXJpNRM1geRiPdircA%2BV571bt09BzoRVQBh3QgKo3lBUyGY39rA9ynf%2BwqMNvfGfF5OKFFsBghDI3Ilxw3X6BLVQFopZ9RzsuDGFIPlw86z4TKQ5qSTx50DxsIS3dI88CSPMUAxStWlYq5lb3KXthN4SDrme34r0VILxryZDhmL%2Ft%2BjJlPYAdP2oAie24xZyZ%2BRaL3cMZREQIXgJ3BWCXqBM7UHkN51M5trYHnDofrpe7dayMuVaccQjRXIqsgUe%2B43ETuETVDytjErbkjtfHjxhAYo%2FlDauAXNcz0c17bnb8P7r4ZygXB1a3lqZptqfeKncnuX02ciWxYnw5xbctfgn8Rh3J05eUwy%2FPt%2FFxlblW8gMSYzMR7xW1YuyXAxs1RYV06imwh6T51mS73%2Bs%2FzDxBq%2BksJ1oYxE5A5wIC%2BQgkI0JL16xWWsGXoalxJhGvN5zh6FB8rKzNWzx4CE3TxC0BjMHZb0hE8TbLfc9B8VoaNJsg2LZll8yGOhY9wYono410KK%2BKetTO1UuG%2Bleqq%2B8OqAfsEeSq9ra27%2BCS%2B0e4GpFFnlVcSIot6rHgRD5Wmv7uspuyvAm%2B%2BON43vNYFNiizBQBbLZivLvHskSsvVYRhWWXOCwrwXWdIA%2FtCCv1JIyxtr89lyZJMIOmjc4GOqUBNCGcO1EPiUWbKH0bxhy%2By9HgSzGPVK44KWFfaz8Mrc5VLPwX5KJoDKkmqT2vEajpohEUtjFa45rXRt0t1rsvYmU6UrAkiK29e%2B3jNdcXK4coiFV0JSK8aTJLeTRN6u9YE1lmH8oNf%2FD4DHTiLXG0MYczn%2F80zVoIF7L3YbRI718UcdhnJpZ1IvXRM1%2FaYKErVaqhZPSnhpNrgTefgZSTSN9ywhAX&X-Amz-Signature=d83599d7c6edfdcc40a9a604b84ee88366b838ce736e2ca167e3c0b91f842c59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



