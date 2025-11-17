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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP6N5TG6%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVzfpoiPy9f6cKxbW%2Bywu6ACtNniJP6o9v8T4SByoSnQIgF5UFZG6Sh6VkJVsfudwZYgUgoR%2BP%2FVkdkDES6U7bmR4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE26BsjGs5nZ5a4b7CrcA7RGtEmMMadDYm2vFK9oWcTOBsh9ov%2BboKX3XvxLq86P2lOCOmwIpn1Oyn5cep7fPU7TtNtKXF1kx%2BFZHQuMhLGLNnASwGyUQtgSa5OqaPrn9B3UFOnvT766XUVYn6IjUB5ybfV7q4lM3iWWFSM5Puv0g1EXkEa2JBB29Bb2XFk%2BNAnO57oeJU5qwOCo6tEh3qYSJfxh5R%2FB0FShSuM8Z4Z63GE3MjGc3xGOX%2BP4U8fackwOFNA8AlSr48RAUFHzuf%2BQ4XyZRTLPDYsVoqoGzbFqLMit6PFOwCQWX0%2Bj5wJpPIGTXZxQ3XgdbDGbySu2TsBn4IikOKfFw79ijBby%2FNHkYxpqHIFbDzgfX6%2BkPARKK52yZvazqTIhUYI9eZOUovtDKqZQma4FMh809F95UHII5U2%2BlryK7Dos4WQ2nIwjUGl9X89ZSP0xQwY3n%2F3rb2aOTt%2FzDLDB0XT7DgjQO%2BR4fQ2vVrIi2mhxTsUEEDdLCOI%2B4TBkCSqtS%2F%2FIIduLXjYkbvxaJ8Y9R2Bi1droOCCJ3r6yP2x0n1QAeDOhLj60gXapFwUAtxPvMnSDmMKp5%2FTRxxPrJ3oQy7foEZP4VpWTATPz3YUPpnv5l2nnUdO0X1CWH2RcOfZ1FknKMJSH6sgGOqUBuZUEK9bdcXSzgsgsebFgHsDLgSfmT9krZHimoCFQy8ZsNY4GkpDuH12eJvUrmmBWuHT4n7M%2B1GcO4UEo83rTDTqnmUbk7MYOBWCkrC9cgYzam%2FBlilvwRpntB%2FrjP%2FDgO5f%2F5XUP%2BdaWohFyDKmbb7vEHJrJ4cjI24YG2ukxQezYauPUu3QpMotGnf10jW8zP5dRiNdgVqftGk%2FhGhryiVOkDowX&X-Amz-Signature=77132801e6ab4314d82fd2bd096e7cbfb6ccf0c50f1aebc07081ff4ee12ee3cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP6N5TG6%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVzfpoiPy9f6cKxbW%2Bywu6ACtNniJP6o9v8T4SByoSnQIgF5UFZG6Sh6VkJVsfudwZYgUgoR%2BP%2FVkdkDES6U7bmR4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE26BsjGs5nZ5a4b7CrcA7RGtEmMMadDYm2vFK9oWcTOBsh9ov%2BboKX3XvxLq86P2lOCOmwIpn1Oyn5cep7fPU7TtNtKXF1kx%2BFZHQuMhLGLNnASwGyUQtgSa5OqaPrn9B3UFOnvT766XUVYn6IjUB5ybfV7q4lM3iWWFSM5Puv0g1EXkEa2JBB29Bb2XFk%2BNAnO57oeJU5qwOCo6tEh3qYSJfxh5R%2FB0FShSuM8Z4Z63GE3MjGc3xGOX%2BP4U8fackwOFNA8AlSr48RAUFHzuf%2BQ4XyZRTLPDYsVoqoGzbFqLMit6PFOwCQWX0%2Bj5wJpPIGTXZxQ3XgdbDGbySu2TsBn4IikOKfFw79ijBby%2FNHkYxpqHIFbDzgfX6%2BkPARKK52yZvazqTIhUYI9eZOUovtDKqZQma4FMh809F95UHII5U2%2BlryK7Dos4WQ2nIwjUGl9X89ZSP0xQwY3n%2F3rb2aOTt%2FzDLDB0XT7DgjQO%2BR4fQ2vVrIi2mhxTsUEEDdLCOI%2B4TBkCSqtS%2F%2FIIduLXjYkbvxaJ8Y9R2Bi1droOCCJ3r6yP2x0n1QAeDOhLj60gXapFwUAtxPvMnSDmMKp5%2FTRxxPrJ3oQy7foEZP4VpWTATPz3YUPpnv5l2nnUdO0X1CWH2RcOfZ1FknKMJSH6sgGOqUBuZUEK9bdcXSzgsgsebFgHsDLgSfmT9krZHimoCFQy8ZsNY4GkpDuH12eJvUrmmBWuHT4n7M%2B1GcO4UEo83rTDTqnmUbk7MYOBWCkrC9cgYzam%2FBlilvwRpntB%2FrjP%2FDgO5f%2F5XUP%2BdaWohFyDKmbb7vEHJrJ4cjI24YG2ukxQezYauPUu3QpMotGnf10jW8zP5dRiNdgVqftGk%2FhGhryiVOkDowX&X-Amz-Signature=a1b0caa4a0f709e614a4dc3a631f72b33e01c6825b3783bfd77a4eccbd5bcf06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



