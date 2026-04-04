---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VERFZQTW%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOgt5GTvBQhiHNiGdsXSCQPAjOIMK6FP0sbLJnoeatfQIhAOMeL45kr9HQvpef0dtRs1D9lM5bAEBZ1N0IywiMeT%2B%2FKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfA4BObsES6qas0foq3ANXq%2BIdf%2BgWqdDiAyjUPo1c4IquxKn7jWllRvNN%2B%2F5gpf%2FHeEIW%2FnAnNKU9fBZctUu0%2B9FhXGPFbqWBiPm0KeoAE9f3oP%2B9PIDOGfw5wmypGuCZMyPTgQfxgG8Pd5C7hnSccYTYchXzedcYFt0On9VtDI5pwqIBysstYYNHn2C9%2BdCA8Pvn3GcPBU5DcB8mtO7lJgZtu1jFA0LDD7ZUZPZfMSq%2FRJH1oEAxG0JMhT0dAsZEC0TSLXinTPI5kyV%2BiMYOy2qb4Khk0Ihv7ZjqAzosBcKqShShDWm9QPTLxPPPxQ8EBp6U8Si3QipEvyGlxYxZRUlsLdDG0nxZ3yOQJOXQyx3Pq60dqNXMWmoac0GjSvB%2Fund3j9eBPPXm%2FDz2gjmex4Mjx33caoT%2BP3S%2F%2BPyaHdHowY998o2n%2BSnorUSzBSwbySLR9%2FKmdJROA%2Bt1WLL2gUy3a9iG8k%2BLA7HOlUoa2PGguobu51emp%2B0ZgYn3pAvbyfDfOw4o7bJqAOxLCgWR9rUcQ5IG6PSrrJxtrluS9J4%2FjLAvzkUP3byNgSYJKvJcBTylvhHus%2BpBkI75reJ5cpa3xoWVrSGRwSQX1dIKdDO6dXX6AC7OU3xsXM23DXPe2pJAoeQBkQjUiTDc5sHOBjqkARdJXg7LnVRm0P%2F6cnkcEpEQbnTdg9DG0i31UAJcYfYyDwONidQRNarGNeJdATP4zjkfcOQS7s8flboeNi0mKowQtql0MSqGmsK5TmNKRIYHTzSe1KLIqud0HX5A4YnFl%2FS7nsv2Q2KCk2hjHXg6qFx3oWldhLohgoyexF%2FI%2FMx4zOeyH7PtAx7zcZbCwK442CfoQlEdELLPAQ7xx4Z6cvhJWdN7&X-Amz-Signature=74edb20ae9a6c0f554133124cff27b96ff57cd42af9e803bf6bab26026a35f75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

