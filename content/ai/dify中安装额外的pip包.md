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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EI7MONA%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCRAidyt6uC6zJKi%2BCptqd6jR1Bx4VfRWNlsfVv2EI2OgIgZI3lA2te6qND%2BJ3zV0QCqicBITmcDGvrlCpwnLfUo54qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGXDNvvmrR%2BVaH8wuircA6WrF6tLesDBRsAxbYNhVqDm4K9My%2FrYLta8gLBfzTWJhe4v8WOz5hOf%2FrMIzeB5gf1Po9huk12CuqnJ%2BZCpg1K0d3nPvS%2Bj57pj3VmZ8PT6PP8m258tCSMMlOCUXwEJ6O3%2Bps1I7q0BcaXvFakqd0veorw77%2FbMa2ZgMHBdVi0fbwCpHxhsFCroDqbF8b2sRIi%2FL2iO7XfK0lbrJ0WzXRiEIu%2FnVrt%2BcJhDzlgDwPfjgAVcaCmnqe939CQlVWv6SbT5sfCDlus5ANevFfyXChEOVWCfgiUeFKDKZOHB8ZPqk9CkciocgbRtxENNDyHEWqEiVmZSkw%2B8HY7ENF2m2iIphMOOQscWukdSqv%2FInOHU5JV9OW9E%2FGdftuLtrWFB7Kbn53GPumKG3GMYCG2lBZ%2BFEnQsk0WjfGgCaVJbNc6wRuWqHdFOQHO79yDOAmGDKLD1YGXsxulBLizusg3PNfNhIKWNChxLSRr1BsYX4wDuNEarkn6EgHJABG8TKdYBSY3JJRzyHaLVxF4JIVwUjzad49s%2BFQJtXzw1zpzlu41YBDt41xC%2B%2BvbnLb%2FJxrxh4ac6N9BAXasgliZn9Ge02QzQBaF3fn0c%2FOJqzRifWy%2Ba%2BOAruBeyVTj3cYf6MNO%2F3c0GOqUB3x0SJ0VH9RWrbxYffKcLFFrMTtt9k%2Bj4mdvX4hwWuKkUhva%2BwomWytwm7flLrqNxyDZKIYXe6GdY%2FpvtgTg9luMSh1cPox3XfKFVzbQVGaMxZvXhai1MYzIlIW%2FMjNpkN5Hn8NH9cVrljzORKhnGSIw7C2ytqF9A7cf%2B5nbG0c7Q0Wn4yCSS3G2s%2BtjWcOT1za9oIk8J67ys0iXIS%2FSS4kUFyFk7&X-Amz-Signature=76e42ccc49e03b27fcc6a3cce401e8be24d76961b0243a1e5d5e8aa2e06ac6bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

