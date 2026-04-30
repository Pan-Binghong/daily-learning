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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466636A4PLS%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDbGcJUuoa8vFpDAg3xN4lpsODhgiY7coPSgOU8J3E9LAIgEF0OERqehYihnbyIh2GRpGmpzG0w5SzES9Hn5QZ0wzgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDNUlBpbkgLUIntfCJCrcA6xK%2BNBaD3pvS89hgoMBwrbAhnERxIIuSMHDsE6tAdkZlEuemVtGgc%2FvpFKRLdMLAf8snkos3QwYFKN5XZEqPnAMFKKK84zIvwz0sMyyDxKOYNMNxcEkvVCp5btGfVv5n67kx2FguwHDhr8Ob72TilAJF4FR0fNajHzYsh1YTYUMMrEQuQAQkt6LDbmMGhwK170STqnOGQoktY59vNwC5z1DHC2cHh%2ByevFLhBW%2B60LrlW6e3ev2WgG2QKFPEmFclAzcqjDxCFO0Au0tf0NHzxRYRercu45JthC8kd%2FHT1D%2BbBN8xk0EmwTbELSpNwbB8z%2BONIL7jENLszK%2FJ%2BCschLD9rKXpmOGyZs6d2Bm8XWFlsWRCzguoBxfnZWHpO96lpUi92zZHAyc6loETj1uWd%2BgP%2F%2BA5Ad7Js2r7Rx6m0L%2FtffsJg8UeMMYAin02fHqjJ157%2BEblRkuDNw9gaz5718uj0ChyDmd3YW2zjk4HqbgOBYwObyMA8V2ON7pXHOpp06xJAz479fg7rcASHukqq%2Fy2fIatUMTb2HTA5xTvRccsMRqMUp%2BQF5nw6SXsdF0FDLR6cSfb6rTOFXOTHdSgULUodcv1qFH%2BNkXOCLp462oM2mitJUn6FwPAsIhMNebzM8GOqUBiccEKso3BZ6zuCcCsP7BGOsbKQapoxQVXI4Ox3r5n8nlhW6UpfdsNF3n1gqGVZG790VPFeWQN4QxJnlMUFaGISJXDTCjZWQyqsHsKj%2FC416xwuUmMc3j0gOz5dSUVcwm77KreTFQH%2Bz6GWafNgwvGYD82WoY2qjwXMbZKnsGvOL446Aggj3P3e62rPY2mVJqH8pCQrSQr8E3yXsO5pqVre9NKAxo&X-Amz-Signature=385fd814776bf23286f6ce4c2f545f94ccd4765c295342cca0f9033d24a1c8f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

