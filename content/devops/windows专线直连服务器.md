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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDBRVPMY%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCj3IyERk9Dv%2B1ZmfQwUgyw7E6WNchlZI0xR4P5WLtYegIgL56IMI9zYkf0lFwNcZ5Vx1GbnEXqWHNUm2GdoMekcYcq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDCvS8KF7Q%2FzYEhpN9CrcA%2BtQzkBxPlEdPHtZaUtU56e6T5Mi%2BVTkYbCnHKCccgyQs%2BRc2524gZGSTYgkfzqCnmrv21kMMsra1knXWPMAHBWR7y3sPui7CXYwBksYPliu%2BumHS9R9dC0BMsaz4ziUXYHi87NrzfKokqzQV%2Fh9fEweSqniyk7rZIwDjGN2qDggbaok8tWW5Qi%2B7TvBM%2BNI0WizFWZ4XfuTewk2675Z851x2VZvToV3cEGGssmPL3FYaJ4nNV2hIxKqq1bYGltFjay0Rfvjd%2FdJxmVxPLwJBYemheTkNOX9jJ0yFmSIBwyfKRkpXas2qT3LcA2AhEdgZEYp5rN1zNBB706FIsQCtHbRVXSfXlPQV%2BJw769VxB02TusTU3Pbl41Oh%2BEJxH2Rj1i4BYZcR1HUbKptM%2B%2FPXlhUXsJBjdad2O29etmC73xAFeOH7y9skRKDqg1khdJqhOWg4A4RHFnAtzYHmkfWmiM2MtQXTJwuoTNXWs3fGE0AfoSZfFexpXZOTpsemZGVP7xg0OlXU08yX0zbostq7%2FLSWzrfv6KJaHp9bA1Zeu2HdYPFINub%2Bj2UTR8npQ%2FvK9m0WMdyPsjnN3Qj1%2BQUavtlAAujjGn1vcykVqGleYtTjC7L5rHLdbI7NIeTMPna%2FMkGOqUBjJi5cZd%2BOaEAwJzxKWWvX0VMhi6fF28Qfs1dyow4Wfi0jwVRe9sDRqC5ZlsGH%2B948pgi7Xoh5lNNJkQvv8%2BImsATH1UgWzUa1rWXdXlXkrVH5HzmreAhRAYSwpZtPqJwY570nP3v1U868NA7sq8ABw12GGf%2FHH8%2F3fcz8bWV%2B5pWgM3DuxAhwMSxe%2BhhZBgjSEmdVx%2BVMirSJhmoPCEE3UMEfUli&X-Amz-Signature=f2d7410c0056f1a0ebf7e7a0984b205a6dc59b41d7f799dd229b3c966edacb63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

