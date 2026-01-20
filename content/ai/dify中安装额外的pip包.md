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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q6TWXCZ%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbSMBbG3zSAnffE9g4ub7nCem3FMpfbV8ZG%2Fkthst%2BRAIgbMcJdgacaCGjWkmBQ35E0ogRwLlkR5RxQGJNJDCTH3kqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNd1v6hqMXIrMke7YircA2sneA4b8Nm1jkC79rvjD%2FMKyJpU4B%2FP9wkLhXgsJppA3zBkZdUkVDeEPAVlx11AGCCLDg712kmAI8P3tKrbWsyWH6tvBkorvctjMJck6fD%2B6dPS2o9dT8UO1QSREZ%2FSxE3ip7UB0bVBNm0ONzPDlj4hp%2F8CkF1atQ0svWXPoNEJD4pWpYVaf%2BajkhuQXOinljpLZlB1UdvabDzAbSDCR1Z9MR58v9%2FJwFFrVVKLb9ybaSwKRL0x%2BfpkSqtPJo3IBau7eZep6x2xXbm%2BTCoBtWHwHAf9Orlijm4QemXWd92CDIsTf7BhQ3HBLOp5duaOuL1xh%2BlI8BX%2B4%2FEqPo%2FZoxaHuqsxq6%2BnrIKnc3rp%2BEI3pMGYC61QSDFbPSFbbIgrV%2F0mQiLTe%2BwOqkKDZBxlvgwrXWV8b3t%2FbqjrueIk5nt1REy0pB8HjT%2BDD7VzBcvqdL2VbaveLjmKrv9yjyCH6WfzFA%2BsgfhwUMShN18tf%2FWJ6enbTVEWTWO0VinTHz8zExDXOJnj34CZpT87gACvmZkhtoVxDehNOG5bbajRUgOQ8gvC4WKhypoHlbE1nHy807tcfVcjIo6vbwfZ%2B2t1suTNBiHSJtnBGCzI%2Ft8hz6YBYMgxDl3qrLvs3tz2MI33ussGOqUBOc%2BjNty1P2gLkyR33wHg5P6IZFvWbOh926GyNKU6%2FDc8kOba%2FdZpX7h7qtpojYs0LPiiu4dgwlGmd8jR03qJSi0Eqs%2B3prpxmBu6fSAvGAcltx3uWJ9tk7%2FECG4UvLdzQmz5DpaHwjscdoznedBxS1FhFvnKBSsRFG%2FcaeaP6Dsg7Y2OQVaQseMvRePEPKP%2F3SDV5B9JO9JlddEEAy1YFdDxh%2Bcs&X-Amz-Signature=058981f371a785ddcd60aa508aa5486bbc4d3d969885c371de24c4b44ea028c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

