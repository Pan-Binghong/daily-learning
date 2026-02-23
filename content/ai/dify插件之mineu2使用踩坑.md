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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FYXMCDK%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIBhEcKJB%2BAhJbjSLpmaX2fQC5vZK2mx4srjhTyUvUltbAiAYiBPwEc39daoHNkZvobl1a71PYIOsscqfKIDP6xSxvyqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7On941O2R3IU%2BFpgKtwDMxwiL3WeDcrdf8nKfwAHT%2B6EM07WmjHNSDtP0iUcBqerex3g%2BgALxdWqQDSUfgTBfla5e1jVKhVmYZeW3K8n0VqTG0wiVLkiocC7Q1NxD8piF7z7iKklFp1YwDbd%2BWQx1fdJUuty1tZXoGFlb7NZJtp7b9XzTYL3aAizaySzQjqeOhC%2Fo0QFLt0W84tFKEp9uc6%2BwcdHSO5j9bzI%2BFf4%2FaL1Z%2F7DwxqrurY12gbrsPVLvdORUsXZxHNLl6SAiKl9EJscB115l2WAr%2F7pYG%2BiEI2UeBvwqFrJp5iCGD5Kr9w8ZcXGoS9mel1lEPdAjeb%2FF%2Fi2%2FBh%2FMz7klhyh%2FZL7X5VhulMuiAnGL0hHXrEi3I03CHIVEw4Z4Z36xcxxdgPTlXgiTdIdGcazznnN1zs1s1gzEvkhpK9H4T0bzcTujWiJXO9q4%2BZaWmWbsA88aVJj0YkMqelW15VKAp8FERZHypKSy36CKSYoqzf5cQnv2vbzRXYX0%2BISUU7KX%2FzzBec2PEGQcFYFVYq1LsdhALYzMQR3Rb6mSh5n4PZjI3AB9aaoMYEWvexvH508HK2Ajx03xvofU3FPpA21AheiO64z05X9jBGyRc2trvW3Z%2BZpKjqyBFkbGsfA%2BS6%2BhSkwkpPvzAY6pgG%2B78RCHFWwpkwSHtNtCTP2%2FpwMNyGRqF%2BFfjkGmgFA2TA%2FHBeygQIqLZ1o0Vl9RIJ0l9%2BJO%2F4lMOMnT%2FiCMdlhL2E2ZtA%2B1UQyzFdYvaXjzaW%2FJHKgHBTfvqMmstr3lXZzjkNsIAcRzG74RklTAVyNXAoiuJUg155pqeE1NVMV0l0y4VQEC606sg5oAiGmwXzSFSYLPsQNW2qwvRUmzqEF62Oolzjk&X-Amz-Signature=235bda161a7f84e93f093ec5009d593be36634f529153c945fafd29ebad26d70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FYXMCDK%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIBhEcKJB%2BAhJbjSLpmaX2fQC5vZK2mx4srjhTyUvUltbAiAYiBPwEc39daoHNkZvobl1a71PYIOsscqfKIDP6xSxvyqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7On941O2R3IU%2BFpgKtwDMxwiL3WeDcrdf8nKfwAHT%2B6EM07WmjHNSDtP0iUcBqerex3g%2BgALxdWqQDSUfgTBfla5e1jVKhVmYZeW3K8n0VqTG0wiVLkiocC7Q1NxD8piF7z7iKklFp1YwDbd%2BWQx1fdJUuty1tZXoGFlb7NZJtp7b9XzTYL3aAizaySzQjqeOhC%2Fo0QFLt0W84tFKEp9uc6%2BwcdHSO5j9bzI%2BFf4%2FaL1Z%2F7DwxqrurY12gbrsPVLvdORUsXZxHNLl6SAiKl9EJscB115l2WAr%2F7pYG%2BiEI2UeBvwqFrJp5iCGD5Kr9w8ZcXGoS9mel1lEPdAjeb%2FF%2Fi2%2FBh%2FMz7klhyh%2FZL7X5VhulMuiAnGL0hHXrEi3I03CHIVEw4Z4Z36xcxxdgPTlXgiTdIdGcazznnN1zs1s1gzEvkhpK9H4T0bzcTujWiJXO9q4%2BZaWmWbsA88aVJj0YkMqelW15VKAp8FERZHypKSy36CKSYoqzf5cQnv2vbzRXYX0%2BISUU7KX%2FzzBec2PEGQcFYFVYq1LsdhALYzMQR3Rb6mSh5n4PZjI3AB9aaoMYEWvexvH508HK2Ajx03xvofU3FPpA21AheiO64z05X9jBGyRc2trvW3Z%2BZpKjqyBFkbGsfA%2BS6%2BhSkwkpPvzAY6pgG%2B78RCHFWwpkwSHtNtCTP2%2FpwMNyGRqF%2BFfjkGmgFA2TA%2FHBeygQIqLZ1o0Vl9RIJ0l9%2BJO%2F4lMOMnT%2FiCMdlhL2E2ZtA%2B1UQyzFdYvaXjzaW%2FJHKgHBTfvqMmstr3lXZzjkNsIAcRzG74RklTAVyNXAoiuJUg155pqeE1NVMV0l0y4VQEC606sg5oAiGmwXzSFSYLPsQNW2qwvRUmzqEF62Oolzjk&X-Amz-Signature=7630ab2ae69fd85817b24a2d3a56cc22186cdac3fabd7b563791338ff716552e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



