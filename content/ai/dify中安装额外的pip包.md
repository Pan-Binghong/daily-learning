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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZU4UFTB%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIG4hbTiDldPBhnFN8HgE5c1vR%2BM72CNhkVNKIFiiBfNhAiEA8WLMErS9fmvRUuZN9RcR%2FjU8M9m2Auds06PWiPCifT8qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4wmMi9%2BsZlAlGriyrcA7SMWhGb29%2FojzD8JKggEPu8wmn7Rb7utdc6BdI1cBb6Cxahu4yfF22H4qy7fOW6WQFUauNqeJSrTwJVn9gENvgYCZ5BPWETHi%2Fptag91DXv1ax2cJwlBE1DjQ2emNAGqnHkro9ALNR6YttddRq94MRUOOta8k%2FizG0lrA2PbrQ%2BKeJGsIvYiK7COjxJ3IUFB7C2IG7I052%2Bwuh7vrftRcvLWz8XnTn2YhiSk%2FH78CJurDAUyV3OdgWykLI%2BXrBwFUIJiXrId%2FUG4mX2ANKXYYHZOtj1cd9GMEE5fW8H8P2QecDyS1HfNAtd%2ByDtwYaW7Ok9%2Bs3Xd2tzYIo5LJQ59F7R476TQMxJgPy%2FXLuUMCquH6NHqNtgXofQoKj1AYcg2FMQb2otVVvUVFdmujKnt478k%2B4rELvHohyQ%2Bu8fySjju%2FDTv1md2gVdvQId6gCLhFGzvArtFGCJaJOsA7lWiQe02Ugrt4N%2B6vr%2Bk3BbegrXcJ6yq7Hv1BHFFsj9zRWzzd2pgOQbqAAsKN%2BqGFXSK5z2XUW73rtSV7NjyWfdgy50lbW7A4BBPEhZDARvZz1C%2B8CARZpKq%2FXlETKVcfjEMVid9fzsA8K0YyLljNsQ7Vx%2Bp0v0bogAwGpfiChlMJHA48kGOqUBBYkTlx2D1ecXgKesl1G2BreYYjiCSEZJafe5c86N4ijbJ8LkqP58zZSvDyFFqfu7lqTUi%2BWxQHaepnrP%2F6fEoQUGWtMc9WYFbTm3YQousMnhm8vBI%2BiTEL75cp3oYP0%2FhbES6TH3MuJq1Y0MZRfvvRld7DW0WxrANdR96p6gBdPE%2FMMB9NgIo10mhyM5AsnSDsM1rKlt0FYtY0WuDFXId1s88EJ2&X-Amz-Signature=0c3b356cd8de95c29c8e7b917a670e126641498dc148b2ef06ae6656a361237f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

