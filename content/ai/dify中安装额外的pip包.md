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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMTFAVER%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDniHolIwZ3Ifvdb4%2B60eFmYTmCmv20JY%2BAbsbWRhFuQAIgbU%2F%2F%2B3zLdC5KKJgADP6rSDMA%2BqTfgvHUynqJblcGdgAqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNc92ycRna%2F0%2BesscyrcAxbzqyYc17P1rW5v82jsduuGXeTibMfyFN1iaSQVidbjqq%2Bqx59UnvkRUvwkpczUmm4fyLZ%2BlP8%2B2FPPb0ThS%2FqFBR4RdAM5ynV0nAizvc%2FmCmVFTezgB2wf4hKuBmUtkzjLhbV5KIvKESf0k6280K1NdQBWvpLSqW5VQgJ05BgJdORw7vO%2B3Xa7GAdsS7RFLlPmlP5ylbscDnOmuKxsGvv5uKEQRP6TRViFdTg%2F%2F1NPEjRaP7mT2c54NTkXYzOevAJvZKD1GDQmi5BKueDa7I5b4Hm%2BS0CuZiqfZZC%2FbDG%2BbHAqGkNm7sLrOrvfvEV648c%2B%2BI2k8QUu1ExOgMeQKzCMNqpTmnBTLYr6GUoztEa0MaN8ZzcqnkTA7Jt0VeAMM%2FFfyiGnPggdxZylmayv0lJlIm%2Bv%2FR6eIAI6GsrpbgJFzki31xhNaG0ATr3tO4CFK9oxUdkLDB9zgAyt3sf8AjSv%2FuQOKuY1GnX1W0%2BdAq5RUhqdmY2%2Bo06apkrvMCtT393E9MexXHZu28B5FkzazOQryBfTSG2gq3Bw%2FhHTMkXfr0wMzo7qkxGNkH%2F73ywfIuhwo%2BlCm4qX%2BJ9uHtlWELtOH%2BUnjf%2Bfbicr0bzGFc%2Bxd65ERGrXIaiSoNgwMJqBjMsGOqUB1Q2CPerK9BwiHD6e8ekYlvpdzgwblmAjYtwEEJaLxWvQaN7BTm92CexAZUb%2BRlVSmL5ycpb9IitT4halhIBCzSKDzl8eD5Q8a8HBElSq8lf4M5UxC2LOPB9EYxQsIRyvk2Xjk7XLKJpYOeF%2FdafvOjUZQoZAi1C7vlV4sDL%2BVde65Rt%2Fqle%2BO%2BH6E5DIhEWFLffFpd2Nkh0Ogq1%2F0WrtmwOgr4Ip&X-Amz-Signature=027570bc0084ae8fc634fc3b9d09667a1f99543ae3efd3f66dae320bfec7debf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

