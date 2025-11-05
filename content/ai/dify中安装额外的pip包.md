---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SY4EXUJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChynPPHy8sB3AHWejcn82Q%2F%2BJdeRDTgQn2Ui8wgwXHmwIgf6C1Jtej1ns6gldjKExT9kDlHPdF9FnDw%2Br%2BiJDPN1AqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA81m2k6sOgEgF2kxSrcA6diK3%2BjkGDflbszv9X85Hmk69ftNt2Q25EOoL7Viz3PYnKlXuPKTv%2BQc3Tpt%2F54yhMFcletvtvifEMYLCybtzCSOdI%2ByElJ2%2Fn%2BMCuIbyLLVmyQAYOd5yjgS%2F1ymQ%2Bt869LnaR6pakGLAPxxQDUveInL4bwX9pzdwz%2BNKqcC1oy8x6uWACkg52Pumx%2FhRYcFwFNbD6MVuqx4brcoGicQpuiaww5k1abejqLIF1LwSQ2VA7H4tveMNNsGfa69OYg4PE9ybtLD18TySBuWvYZ1q8a6MDNGBHzcCEVYYeI%2BktIx6KxHKszmJ977Yvon7S0OkCpQCQ5ROAanFeWGPGVIrZX%2BvubpXFyiCj1icAOQBWo%2FhkXJnSCSRquGO9KMzGPqUECCY7PvuDftiARfPYdsqXgOrwP36uXNV3VQEAdkK0Ke%2FBofIbRx1M8uSQZU1OCPhPXak9JE4tB1EWLIpsYiInHBAtijfsrtXayKl0YNoVgcamzvZkvKUiGNEF8z6J1D4XzzeoYIfDqXzkYl7uFg03b8TzARV0WS00Iz7FX3VEC47UlCo2LdSU0zRrlf%2BfR2bedlO225l86sR%2FkNdMcGtZUTAck6%2FyqPWnG8svRyOdvMVHBh8ObjqyV8MU4MImjrMgGOqUBN1VzlU%2BFSUS1KLD1O8bugvLpHpnjxlZpXwAdW4hrFfTkMFPP75zOCwNmpNnXNWvdpYpCoqZEOG%2BBUzN5VoQqoPBeT3xYcUiMZmV76qM4j9VzwJx71eacM01YOgQ7LwbtgeYcsTOG%2FxjX80E8HvegLT2SkzW4Lhlsbq6gY1KgThZkQPKha0uOFBWeviNduyXCEeP8EBGc%2FvztDxhs%2FhEGNm6Oh607&X-Amz-Signature=8a619d3bacefb5775f571387d0ef4f4714841f2e21809eeff4a0fc090d0bdc83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

