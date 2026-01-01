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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJ67F5L%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDItGsKzqWe5mYmKeXxqLRcyJmJ72Uq43ONsseClsWEVAIhAPzkfUTWREQPhbt8lQxiSxbSa%2FPTYYAln%2BnQVIOMDuPjKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYUCz9sCyvaVIaitwq3AMBDj21vRTL6cRWbUXolMJn0kJJNNuWWHLGA0c6DV8%2FnIKOyra2x2IsOB%2BUtizbiHqIPF0kWLQTdCdbGhBeGXTEwaIC4OzT7HtXMlJ1sPJfXL1IZ8QExb354LAWgcwE5QZUfqecQysYSR1U3tt5e6aLY80%2BJKyQv5bj8bN2Z9nxfu4YX018sRRK5fta0kIksdezZV%2B2GYDN8Z2nD8iAcEX6tQ3r5YnDv0cigy1dkQ1f7cuHm4V%2F%2BjuPfVgz4C2gaPqnINmmCMKUsQWtX5yH9mEXO2RglA9OkaqqopJzPniY59V949cG7Aa87ZidhoGRaE2T3iQTD%2B6quv79rzgpA2PDr7%2Fo8aWn%2BqXfZ1EgxBqFNKbGHduKueK2dtlQbMfqpDgI9Hda0APXaJwqjvcIJ%2FzuhehqCZ%2BDqRQR0MNHJTUMJb8jg%2BsmOiCa9I3ETwQ8em%2FZxfy2CoJKvTS%2BasJGSVbmZ4t18k4mMd6V33gHIrGOd5bC3K1e5pI1WDP6dP24%2FqDacZF58hP433CHY1flhg0oHisgVorYC7URntRss1uSFwlSZm6MIG71TPVi0oJaCGorTRqWVuj0ZrLtzRXMf8gP6hb1dPMOL0Wkq1%2FaT200m74PLJh%2F%2BXcX8GfNaTDmm9fKBjqkAflvyCd34d7VNX26pS5LeQn73S14RmvhhviNu%2BdZrF7d6SvVzd1wkmwlvnJL6lmz8s7RKESd2XnbFjD%2BckHlZ2E1gFSEyWpiAunnFeXoKIULvgpkrshmtUbiS%2BbUZzdJ27ouBl3u%2FRbjGyeFboU1Vsmn4st1GxxEovpW%2FvTiPIfIzKUhlzymVMqYSu1dosk3%2Fi21TjmroJaTBrhuw5esoSa360Km&X-Amz-Signature=6c5f4e0ea62854711de9710497b8e648a3737756a570cfa12e89c0257e943ca6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

