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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TQO4SJZ%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsCll3IC9TYgnsWpxIE13xJr4AmAlE4Ij%2BYNfPcUoISgIgCpz1icDvRrVluGEsGXOy3eoIRJ4874yjUfPcp0f8XrUqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNSCL73dEpkYhMWYySrcAyAhhqS8ywiVmIsAtmnoP10Qp%2B%2Bl3jm2HHyk9IxuhZ0M4l3MYJoTdzzPIQ1gi%2Fsy1syDQwdfLbn4nOuw9iVDKpproXtsnYEOmmD5HSnveAZY09NubEviylSBGv5MKilay7hImJOgEFazMavvwLiO1XhooBn6VQvijcPbgYl7ziUN%2Bd%2FCDAgOef2qb9P3spDF24rhXiU4Ii0Q7Lqm6rEpETDlBMgv2kzfe3XYoXhlUUEY9rJnqaoktLrIrTbx2viW0cx4nZEPzpdMy0DfQy6yObLI8X193Xjua4ZnLeRVFLnHvfrbEgmm5tChT05u9CuDGGgNPAwqxdek9FqQD5%2F4qyDVjNF0TobHapFOlWGGx1u5D%2BeS2xJChs3Q51bvcRRYsTG0aJILcki2lbcjwtZxeX%2B%2FLjhiE%2FJm0WfafTXMEmvL3DWG3AHOVy2TYiOgoBulBbbrP3qxJdgtvOAcd3rCkH3GdUt9H4V6pS%2BRv%2B6Qqf7mgqxOIaM1lDEt02Z2LQJ1jW%2F9gRf2ChkBVSl4HJbmuRJMelzoYnWNKykTfqemIpzbFbQGHcqSa67DzCewp2npeVndpH%2FyOMRasLo%2BhLFQ0zNTgN2ZceaLm52xMQE9bOcKpWjr0WLH2zrVBAsaMKy0gc8GOqUB22yqVon9NNl40YukisGGAMZ6NJs1KRhRd4Nu60D9z14cUrIEYXDcZDxLKbaPWZkN8GrMp7ZGJgVRiFTUtC5d3guMQjiYCYuFOpG2nc%2BvjnMYewJNqMsOS3AJs%2BvSlbEt7IWLyQv4dguEqC55CFFObCKnLha3J2i3%2BOaTe2K54X52nlxQ%2FgawHsG3Y643UWlFhDNpdyM23s%2FNVHTK3oBN05tJKhma&X-Amz-Signature=6fd185b1c27bf1f603715ed4bc9864a669f5c495d3d750853b09615e505088f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



