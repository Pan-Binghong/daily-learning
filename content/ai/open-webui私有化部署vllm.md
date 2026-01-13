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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAS5PSQB%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCw6fNdDOWkj%2Bqzc6PaMKGENeHqQFL9jogGpUgf5N0h%2FAIgRFvUrud6vDtW7OasdPzPRjk5Fk28RwhEFVZpMhhG2CQqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFoY07wPrUhkYID2fircA0GocZ17O3fEulNKXtUxaS%2FH085O3Spk5tHB6FcbiTjqJc5KqRo3Ekh6n%2BuSHvx7vTlxRbsgY0C2cOa0th59As1BJF5tCXQbf8hiwr0WId2HfJXCu4ghgQx%2FCvCXXHkYvFWK6LovAHSUci6FCOacdQEGm%2BhPtjE%2Fgkx1t%2BY%2FDSa3gddWhii2OboT7Xtbetn0w%2FCt6WyF0TVecTdFkz%2Fo2QXifhU9sZ2aOUkJ%2FbBY9Krk12Sj%2FagqkCB9T%2BJmFKywUzxNKpxgkaJN6zbxGthtjtfphPkSDA49pzCpKQ9LFIVqaufbNvMs4rYk95mLJDKaMlSUhJ%2F4xAxM9ajwQwDWOu%2F7Sh6bD6u7fPYOyuTuzyaB4CYKkUo%2BWlTP9T6t5NL4tLU5VYlE%2BLKQgDBD0%2BJ7Mrmt8NcYbUKcZhhhWCWSdXBXZ35FPdTpgEHOAvXrJOnpp2NRvaHZfMkX%2B882261%2Bf0H2YH30vSLKLo7gXmzzCS2aOntqgkSu7OUHYImeoysUEG5MsVhD26igXTepyDFUwS6jU5AfCyfAIW41fXUDDSJdg%2BZtW%2FI6a23oqM6Fr4Fx9E5F14urUN%2BOfe%2BpkQ94B5DNA41cYueynSdFISJEEA4v085F87AhLANtBbQ6MNLmlssGOqUBEzw4AaVZ2VnmQpTutj9AzdStjF3l4JKPqn0OYcKNvKpP8C3F88ZklP%2BTcxED2aTAN94YMTjhjSlTRuwpKE8poPOaywz%2B%2B%2FhIELFOoNwYapCoSgjm%2FRzhz31h%2Bcy7kmAPafdlzVRn3Ukp%2BgEcQFJERa8PhPjLCe1n190f98UzQXJ8aJudjeXTPt3Id%2F2imMdHkUadE7fKBwVRAlOXgKVsWzxmtrwk&X-Amz-Signature=d657da302ef00d263bd4a0fa048361b1ab2028501685a4bfbbea88b798d41317&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



