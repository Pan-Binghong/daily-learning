---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCSAYKCZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIFKQMQda%2BRgoedReMBQOGxN%2B1I2yAIfv001NjfdDsTepAiEAqIKh9kDUKoPVXf%2BIYLvwpbc%2F%2FYdwPevnHzyr92sWsIEqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEcTuPfWurFBJeOfircAwgiCUL4eiT4EImgRIhzkMZrTBZt6HxnMORva2uhRRiHdOe0OVMJ4Iwge0%2FfkeaFRi0XuWofYzaAq15SzbIJhT3tIzFcQAE7Jm7M27VD8jSElXj4S1%2FNV1wr%2BHKsvamd1FaKt6BhuWCvOQtdF1vAduOmWNKX7K1%2BvXUa%2BkwgzmxkPFZXjyWiOipG3LSEY9p%2B92SDJOFi97Z9%2FykD79m69rGUWRECP9VW02vrdp8q0ukdXRDizofpdWkRQ2YDxrwL33iGvKtBDsqleKSmywjhWhUZLUK0eXOKYyiQ%2FsC2UCMBYxn5cTbc5zEEQfwAu1F6na2AB%2BWDNkzYKDIVdZdZ4TvvZcGNw%2F4kC2HQggGLCPb8EjH8Axw0NSFNSzVFyMGTP69mUOyun9poGgQB6DFxqjJ1yqkMwck8p%2F9lMRfWueKnufsf4DHM4Rty%2Fg2RBzpCLYWdXZNGpWd6EMMfXfh8feak3dLPDzglLukUUyHrIilyyM880u%2FFhEIZNr95G%2FkVfNVcGzU%2BWm59Shca2Wy7FHfGx0nuBSjtJfSCUmKQKEwwp%2FZXmFWBH4SPMvVmgVsQko9OzDD3TKeHCuQpUPAUPT5j%2BkvRLf%2FO3eeXaKjX%2FzN4fE3%2F8AFl%2B%2FQpkRAWMLHYhcwGOqUBasH%2BFf6F0K%2F4%2F2I4kbTG5hMMT9avAdelyayFO37zGIKrR8EXPSuXHQ6GV1Loi2f%2B6yC46WjEX78ofBJ3dFhgsbS1eMwFmNKnHHxty%2Bi00t%2FsSk%2FQbp%2BWuzElJBjdJ1%2F6QZAZYLEBCgbG1dZytAaiVPdERXYGhAznQUl1K9Hp0cp0a9KQ69ZeZyzfdnuSdxAEmA%2FYvhfvSPtH2eD803T9eCdtLzjm&X-Amz-Signature=5723cbbd53a324ef219b242cd50c0a72a9adaae390b059f7ce5ede1250c36483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCSAYKCZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIFKQMQda%2BRgoedReMBQOGxN%2B1I2yAIfv001NjfdDsTepAiEAqIKh9kDUKoPVXf%2BIYLvwpbc%2F%2FYdwPevnHzyr92sWsIEqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEcTuPfWurFBJeOfircAwgiCUL4eiT4EImgRIhzkMZrTBZt6HxnMORva2uhRRiHdOe0OVMJ4Iwge0%2FfkeaFRi0XuWofYzaAq15SzbIJhT3tIzFcQAE7Jm7M27VD8jSElXj4S1%2FNV1wr%2BHKsvamd1FaKt6BhuWCvOQtdF1vAduOmWNKX7K1%2BvXUa%2BkwgzmxkPFZXjyWiOipG3LSEY9p%2B92SDJOFi97Z9%2FykD79m69rGUWRECP9VW02vrdp8q0ukdXRDizofpdWkRQ2YDxrwL33iGvKtBDsqleKSmywjhWhUZLUK0eXOKYyiQ%2FsC2UCMBYxn5cTbc5zEEQfwAu1F6na2AB%2BWDNkzYKDIVdZdZ4TvvZcGNw%2F4kC2HQggGLCPb8EjH8Axw0NSFNSzVFyMGTP69mUOyun9poGgQB6DFxqjJ1yqkMwck8p%2F9lMRfWueKnufsf4DHM4Rty%2Fg2RBzpCLYWdXZNGpWd6EMMfXfh8feak3dLPDzglLukUUyHrIilyyM880u%2FFhEIZNr95G%2FkVfNVcGzU%2BWm59Shca2Wy7FHfGx0nuBSjtJfSCUmKQKEwwp%2FZXmFWBH4SPMvVmgVsQko9OzDD3TKeHCuQpUPAUPT5j%2BkvRLf%2FO3eeXaKjX%2FzN4fE3%2F8AFl%2B%2FQpkRAWMLHYhcwGOqUBasH%2BFf6F0K%2F4%2F2I4kbTG5hMMT9avAdelyayFO37zGIKrR8EXPSuXHQ6GV1Loi2f%2B6yC46WjEX78ofBJ3dFhgsbS1eMwFmNKnHHxty%2Bi00t%2FsSk%2FQbp%2BWuzElJBjdJ1%2F6QZAZYLEBCgbG1dZytAaiVPdERXYGhAznQUl1K9Hp0cp0a9KQ69ZeZyzfdnuSdxAEmA%2FYvhfvSPtH2eD803T9eCdtLzjm&X-Amz-Signature=5a12f320356f36754fb4a0e21fb7c9627fdd0cdeb453c2c5ba08cea0c1b6dc3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









