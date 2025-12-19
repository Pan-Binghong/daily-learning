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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3FQXLN%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHah6cowX9XiEK6qSqOr4FhqmuHtXMUv6V%2BoG%2B0fZY2IAiEA8kHpGMBovUoAqsy325IROQu9DIxkjHC6f8jG%2F7UJoNUqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDVwIh5eK7KfUqlWSrcAxw5%2FfN%2B%2B1WikzRBghvMP2yXGF42HN0JDDFwqz6PnsYwHFOly87u0Sp5zwJ90jdZcEhDMariBFdd7MATkzD07axhUPhh%2FQHMXkyFN9byWrvQUAd8aMVqJhL3YaXfPiQPQH4h%2BsFjMEFTZHgH5y9b%2Fy%2FvkIqG%2FI5pOZkSq0GNt14hCZL3IdmUMDZYTiYzoAYZIihZJHRd4VYUfCK8nPOx9o0WcmFOk3bNBOEDlFTxVXTr1z5DKmvHvMbdqKUl0Gq4rdeHb60%2FRGy1r0J875nuJa3x8SRYHDF8As%2Fy65wAa9Vqp0wiISqirbtW9Eg%2BXnPQ4UUWmnilYVzl54Kz981QsYnUYsc5xLFUs0zq2sT7ao4b6X02W8Vz9eyqG%2FxnhqujlffWfsqzGk9V95AIQA%2FgI8QeLldS%2FwpL71n8nGl%2BO8sB3dUhB9ILvG27LnxnZtoIqftd5ckI%2F8I1hGOasWPj81H95Z8jg5mCND%2Bhp2ZbeRHLSiR4rrFi6vu0yyovP9o9v%2B3lwS%2FEx577xpKs9m2yam7ythPd9gtnU%2FxAff%2Fw6SszZsWIbhNfU1lxtPWC03ERNacdQl6qOqMdlzUhIQ0Hj4aY4spME0VSXBNCZ5Y8FsONCxHTDj%2Fo3BKS6TfeMOHhksoGOqUBRnRNNl%2FjwIgB9vUe8vGi2ln5haaFu3cemQO%2FbpekLRU0fLZ9wu4mYQX0T4f3IaybJKb6v5%2Fy3HFFfZRv5hfU7bBCaeqxP5ynXekQ2CWo2zyfGvwwk3YzRR%2BVxlTBNHPtsWEeJZ8wpDjoeit7MFeSU1%2BXeeEEiywA3tycETIUNgF5lhDlo7ucne60bFbPhpKTGnFIKY5MlUw4zLo4BphGcwOD%2Bprp&X-Amz-Signature=29fadd3d0bd277d6559154f090a42cbc4d6bdfa4a757e063dfbc6d421803261e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

