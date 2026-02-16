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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQN24ZSV%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQD1vji22W36m0NutbersIyCebeB5S1iBXk4DY8BD0OxBAIgY%2Bv2sB9pqiGgQdGLtl%2FDN3KHwRkJyKI0TGZ1PtIqcqwq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDOLFAoJx4Wx%2B0CdmWCrcAzDbxvJ4e6pF6izqWwb5XCkCME64fn%2BQre8AA1BCviP1isuq1qvR6LJrP50dEkB1%2BpjPqRzEamx4yj0%2F9vUcW2lYdx94pedyRJDPI3i%2Byips1%2B5HIlfLNtuU%2Ft3c8JVGHVN0W9rltENl7qdMdVE%2FQwlHjroI%2BoropNL34gEKrM5%2B6s0QxvCV3Jj3hDvVmcmAHKoWaAxMqgoqOqBiP0BDDA82tHJQqGogaEm7HE5rnn4g7ZUySX2Pu5vtxoJ665yBNXIqI3DzAk2ZJjJD0g8VF%2FTMqAvTDGrt4%2FH95jAVole0le6NqRO5y4mKhUkVYCCthfFyg0zja80RuuXtstb3%2FeHz5JfmTXATLaKedh8L4WDpd20wyZ9l741gEkfCpHrTna%2F6eNB0M%2BGVEcxX%2BC1ReCbtFAXxk3cc76zssULBk6uF6eEanfqYvpQ9WL31pHJAgnyZuCrY1i3GA1vvpF%2Bs9nD9MbxOfS4k1qI1AEROgnItYyS7rG5UBQUF1Z%2BSdhfJ8vPHN4nUIp3Q0%2Ba0SZ%2F2M2vXsI3lCYtV7nt9Hlp9DFdaHLpgf4Vtm0lP1%2Bh5pvfe29sgNIh6%2B6VGqOFhJP4VyxMZNvQVhV%2FNnKHK3H7F0%2FWOD%2BRuypX3RI4asloaMMyUyswGOqUBNf9DlYACFV6XRyQWhqDSaf364EIUbGfZsaRPEBDEROJoxzpCZFYrqrIJwJYSO7HlsmZXxZnNatwi9DYRPi2O07LqblTBdyc9d9GOfTG5m7CbFbyMfqSY1NfSV5W%2Fi63m6J5%2B8jDA485CWIbAGnEAp7pZ6oXoX6WM23Ebt2D7gCA1Y06Kyll5Td6IXTJOO2vgQtKe15lFmto6lgm10ClN0zz%2BY0R8&X-Amz-Signature=ef7bb65ea4f2cb2f8e2f5d3fcc940d2546a1018fbffe9b655e998a59d6d8ab34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

