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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RUL3WB5%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC0gHwzDQx0%2FPN9C4FZOmL9bkVn3NN3pHgkmbHQRlPJdAIgLY2QlCmRRDg6rOT3bIkUO%2B5%2BnPGrI21zbeuh4skzgLoqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIf6Yazyxo83uXzv%2FCrcA%2BokY2xlq%2Fmyn7veP83ee6wj6IFTg8JSm2zZK4xSpMZ%2FUhR05OgvpuucqtuFl28SKNugztEXKR7FnNsibrtbsLSW6ge1nufNYLMDYogPah8kld3wQ0I%2FTH%2F9IAgBPQTpVqzSDWSRtWzK7DRt1283gwSXMYcXe%2FQ11kSnrzvDARUshS4Ieh%2BkY74XwL7n1eDrAwFUF0CwpDg6Wk6aAO%2BCyAp49p3fYKundUAhbR5icy3VS3rCyH0qxAMTKMKSnICYmOgF2qu5ZTgS%2FzCFnqH1%2Fy506PmqYllIfZXP3kHwrhV%2BegFR%2FHAbsI%2BgT4SNi2thB4UEDFIaJjztrZCt4PnmMG6PFY7msxWHhkuMH2yAgueE2IHxEy%2BWoYBE%2FhCi%2BVYcv7pMrETadBQVrGr5WMhjv%2Bm3%2F%2BWd4wgVp9lxEpoj5BxrBeYxws7pr2N8yUT%2FSAUPk964U7QOaeWNP%2BvDr98sTWKlEq%2FVTEruWp6Rnu7WdKqIB7LGrL3JggREbqvcwixoe3ADhr84KUX7b2wi6jJZq%2Bh9uyV0epF3rUNx8eeedH%2FKgpozEqPG7619iazy49QnXH6x69mBjV%2B3LtsDHGDu%2FG3aIrNbHQpKTVfOPgyg%2FbmKlMTLogaE%2FSgVFshQMMXuwM8GOqUB8orRbKDDORtz3RO3wRUVsMzlzyobRxqmq%2F%2BQNeYeaESFvyN4T6%2FnPUVE5KFx%2BGQViIp8kyIp8iQoFL%2BXIbsKW8atP1MCZqQb2cUXham0CjUmQub6lnAmOJC6BHy7WbNcJVOkzIHdkwffxHVmI5IVr3jK8OimkmNKlyhk2zsveUhNRG7pUQ9G6LaAl6hU8klc5jW7IcBW8j1rl1HsfhjMr2%2FV08Mr&X-Amz-Signature=e3e7ab1d74c74e1650d0f18b9625238aa0a0db0b4a737acb1a4859bf15827160&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

