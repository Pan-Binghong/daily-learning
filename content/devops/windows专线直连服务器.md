---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TITXHTJI%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIDzEP%2FPFKPC1uhzc69rFYMEYxBt81VQ6Rcq6lqZ1VF7HAiB7wjOYI7rU4yao91h1QLR%2FJzrKuUJrlDdiop8xIz5wZyr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMmICSSdvpgA7aV29rKtwD5q4j9LcaeJQHnRhcCFjZ6HfwSmx4Z4D0e%2FQHcOxIYCiSpBXC%2BcVdIqFK2jm6C7PgXMksEPrnyCLf9PY7S%2B%2FpTgb29apMbeo0in8XS3QORoK9cu6hXY8zhw7A7JxdtRg3wZyILLjj4IMM2lV%2FFSQ2p2w2HhO%2B2w13ToWLV2uOVQxPwucVGSTuJm8ooFYbbH9G4v9MAx0VeFv9ew0DOcLscQ%2BNr9%2B7QRigSiME4b8JzArXCI53xEh6z4Ic3RgK26itkZ4SE%2BxwxRng10WNnc1SIwe0kEsJtU3G4iygVmd2hZsHRzR18pgqBdvypit%2Fs8W1cpVOXImgs3YeEwlHS6eNa5mYdvud%2FLOA%2FR1nuZaxvbLdAG9qO5u5n%2FgzSNYFzyYxatWic%2BPI1vAAMrGIYEEkHt3JZJBfP5TomXAxkLmEMh8f5UDhpLA46cw5eB7qWM9yUpIe0LfnqGJH9T9Wp18Sz15buNJQEXMx5UWzzOzXB8J6uRImrsxVFFDsw1EzBkvFQ4In3G%2B%2FAutr4WxojRdYlaX2jzAohbb7GZWFcn4Kt%2BG%2FNnZriC%2FnNEzxiENRsY54bWpBNO4j3X%2BWrWeK0ynU01AIk7M%2FPPr%2Fd8mgh0yIMn0tA3vP7C2%2FmqJq%2FBUw79TDyQY6pgErLMlWNMa2ARo2jXYN%2Fc%2BieZqqBgpeh7OfHTIrFOq6YFCbGI3unuzgMMDoO9XR%2FTdWGrFfl%2BlDEhZrdpT9Ae8U2bpTjnKTal4Cyo500Pdv0yi22iVS1Ge0C4f4YpnjjummbqsLJaS7RbkpwOzglj0BJSFmEzrTbFRtirNXQC6p3AVcpAfceLjd0qtk0n%2BmpvcXmcugVnzPkBYK6ga0p687hgIYztrF&X-Amz-Signature=eceb28fc76d7a484798531b7ddf11821f4ffb039c09b73f2ee44e748fd5bea9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

