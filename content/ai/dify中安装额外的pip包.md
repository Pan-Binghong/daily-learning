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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW757S6P%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCu6mex%2BrzdqzxrsjXyA7tosaexuzzgevv2aDC1N0SQXwIhAKP0y8gEOuDqqdTOcmdct3X%2Bk892iUF7VY7cbKRiAJ47KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKE5LdGhnfXfaLtbQq3ANNbJJyMz1DDoKrl%2FkXr2trKvTR73o0AZE0UHK3U1amcFgSCvJqS%2Bg07dcf3aRLE6ZaC3bPeWFtCketL0ouKQ2kC2YL6fNzSVtA3SvRWlB8CGiddaMGdAd9Zbn97Uts8pg%2BwyI9g5WE5JoIdOIQIu7HGsxxPFxeRYLxqLusHlA2ntO0pNmTnVF%2FwGVsGGC9WizcCrFYzfA%2FFsQX9MqWv1f%2F%2Ft3GmASj13Lgrt0ubjQDEb9UEN8TfvowmH2yMgYYHAjWVXADwcBSzegY2bDRrq0GPbXzx3HJH32Bu%2BpZ%2B%2FDPoa31HBAWVvrmWstPQIOiJIrDfDjA772bK7N4yuTYdo6O52VEdYUHn%2BscTxN0d%2BAMewnxLyok%2F8qszGYgGGBNqu5CLE8TDTjIIySB3UcP5Z0zw%2BSCnZFS5k27VPpmk%2BJPjmw0wt%2Bm48He6gbVSJHFDKbTBgHramf0N9U9hq12N2qpa9g8AFp%2FdjAFTOio05%2FgFtPyhA4D9Xs4oi7m4hxEtxcKi0hM4WMEjPpnNpW92dc1l4nYaHwNcGPzgc6ZErJIDcQrzx5q9OeG8QZyFehstnSi6JoS27H%2F0La0CrUiudTaw4Mrh5WNiyafp0th%2Fdowa%2Fsn8k4NkHPbvaZ1BzDR%2BJzKBjqkARgDFTvMshvDzgSsAwvpwmctIUrTCjwPhYqQ%2BltpqY54jmFhqI%2FLhmgaFYf3GNnFKTOJXH9BACUEsaZM1IRVeaiwR29zY5iIFAHJ0ksfmid53YRDJUw%2FCeAIhn001kzZc4jEyT6mcYJuT9tuhI5J%2FwKAcySGi1jHU%2Fb6QezCBEug%2Bh%2BJKp%2FBTNCMusApS9bPlp6xHnXr7U%2Fk9oZ%2BIHRmQsdVksR%2F&X-Amz-Signature=ca11907e33a4196ed1c9391dd4d767d42337ca1ed267a608543287716650a1be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

