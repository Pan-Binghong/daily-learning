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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466454ILVLX%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwfsMqpR1lQiZDgQyszsS6PgTtAzqxzN1r7keF7jlU8wIhAJSwboOaUWXow8rpWlHreXg6iydGgbSROFBMXjbX934VKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3rsppm5G6qjPuG18q3ANll1iajEXG31buvKqS5muUFopyRbuAYVSf8hMd3S4%2FoWDKpC37BBm85LDf%2BZsRkPX9%2FlF8mdXNjX5G5FxPwK9i83GoCQdpz%2FSiny00Vdpuz8qqRksSq1EcNO3mltw3oXtRDLi6H452esK4YfxjHwBl6v7uLYAkasUNYceHNR7oC51ngJvsO1jsMf0ZrTezZ%2FFCa0IPHLQIlYGPm60gUOF6zDj1xIbBU2sn9WWsZ%2FAgimX3474s3E27%2F57ncUFp6z48GfnHpb9DbQbhdm69%2Fxdf7ipgOaeBrfnnFEP524JHaw0R9KyfOv88AVTpQD3cT%2Bvy1b72EWmgJKgBVXIBvSuKfjrZsU716gCZyipp%2FavQy5ehSVR42p8tOipqeMA1ByOZsipAukURSbrG0%2FWIWhGorjpvPCkPe3Ss%2BMaH4snk%2FgZVSRzdJbemLQ3wDYzyaEddqv8pc2nu8vMelKIms2lx%2B2ncQNvDfhgoE9QSmU0Dh%2B7NpYHuMHtI8TbBhBcxn09FMysBwv70HROLY8bAIl%2Bhu9ZnT0%2F2Y6FMYKPQAlO1PSvGa0Rt1jU3rI7ZTesQ9UEbpepB8ScKeDcl8UdbqCXE7ctLEyIoDzfAZQc0sXAq7em%2FATXATyJFkr8SBDDXmZ7NBjqkAfxzbNhKZHrne0lNPrVMx8jQ4gn2tec2s%2F9tk9QAj9NUTHfWQp%2BqQ1J1Kk%2BaIKdkl3v4OKQWT0PJNsZWlEg8N16F82Ku3o%2FAdEYDsSMu7vseQMOtITdemL74uZfuyu9kPt3f%2BHzhPKouvFVmHrJCOVgjmu9s4UyxwfHrJhFyh534jzxGLRkRfc2oZJ2leIiFs5B8rWHpX3rc%2FGaapp2T8A8Eo6ep&X-Amz-Signature=8eb63f2dbbd32ed86265101709b22385e268e1f39784453e0316b3cf9d32cd92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

