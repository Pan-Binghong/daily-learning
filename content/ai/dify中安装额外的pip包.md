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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVGIXVOJ%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3QKh%2BK3tizf6aoIJiY46r41eNvV4Q4RlLxy%2FrJAqftQIgX3QyLhfiFwRT%2BPPo%2BxWYGZ28hHqrrx0b5KIHDayfd0cq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDCEyoWQcPBhBPGgubSrcA%2BEIyLc3UlDecIz8cPAuhQYKoBw1HSY7dXIyM4LLQN5C40vqs%2FfXKqwjWerg2uClBckvgA55cw5WTFpc0sIw19C5MJ1ZnyKIHw5qSYSJf1l0nQJswduUgUjCvZLJiI4ME%2FdF1WxzAwWMmEEwbrh%2FjY0rvzlPJrQ3TshSL8tvIraQuT0JPKpAfR%2Fm6om1Wi7XKbDGCidfxdLbcb3hnn0QWhjWJfiLOFkOlr9v8y%2Ff%2B6IC%2FBzkGGKQelqeawbMggW4IbS6k8edzwS3Er0ujCRkDkzuJffJqc%2B3RHs0TyyfgW4p%2BoOAgj2d%2BcUlLsI54Q69xpFnc2kgZYGMoPINfCTZ%2FFREQLmvwvMQNGEs7X%2FQ%2FLtbNhJSBM51SPDWbCuIpq4VRka114l5DHt72UeBWtfg3CPz%2BYHtK7NdoG5xY4SbfRZEv9vkN6GZUWwObZa0FNydyzmfvFnxc6RWaTlSLWw6ODCoPUmAbyyG6Yu4ZOu0CDHOIe%2Fm4P8rlka2ZE78TAYQHlYaTecxjIGrgH7VE1%2B5%2BV23opmexE6nYCsHtR553CT7SLusYwpsDQNG3tkriq7IMm8NPtxqmUziCoa1EO5%2B61%2BusALbfx9OjYJD9IgDXAX4KpqaWht3BtIXfPC8MIGw8c4GOqUBAsmvoCojeqz4zN8bb5U9ysvAh%2FsX9KUna8E1HcYEnI0%2FybXvautgTWki0q10eX0Sl2imnFut6FjaNfSw%2Bv%2B7NQcry13uFlNvOTMbVtNiOwU0cInbuG0kTG2wHcqPUv5jS3hYe021badLcoT5X0YqoKzwyuiIC%2FpjtuNkblgMIj6zFPO%2Fdj6el1IPnNAJs4HgO9dpaGU41%2FTHcOh5i2q%2BqUw56z8A&X-Amz-Signature=23e841e53c5019aa1165d72a8eb3fbda09c68814758f280400be0bbb5b51461f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

