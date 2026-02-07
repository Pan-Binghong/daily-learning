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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDFEXJNM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCohpZ%2FIBUo%2FgGFdj7BRMw0zTB%2BeHdGBIMmq9hhfetw4wIgX0Gfkln8k6U4lljmb5J%2FtavAmNXNc7ZSq7JsCH4upqoq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDGpI3jF6rVdIjot1QircA0ZlFrB7AwG%2FJfM3EAU%2BSknpGBTrtL%2Ff%2BRJeo8rxqaDxgyFuqIfqO8bAKT%2Fz%2Fr17QkScu%2B7%2FW%2BQf4CC0boj9NiMwr4bDqipGIe0YGMa73BZOSrEJ2ZAEfOtfDiqb3TtPEzb%2F%2BOY%2FjiVQ0D9Hpk8tCky5XSDayXRx%2BEcUjsNJlkIXRg67jAKb98nnJsHKocYVzCzrO1y%2BcGJz%2FW2A6jfc%2FqGaY8VOVaEMHF1Tn91KsgzNytRCgUPSAQTgxJtnbCFzGnSP4bZeLmoYq%2BOzBpcQirOoePUSnMvlnC4UpemFCSHxR6HGLuPtMaq7dtWdWl5OWgwhEtjoMEur6Qcb%2BaBvCiRvNlkTEZ3zJb3YOOQqODjVu8uI2T8QFFIWmpWDIRwVEB7oa7ZcFe4W6srfoTYqgYAvUjhC7yKVm05eeAXA8piXcCtQvwRmHYRGQ4Cfd1RhLENRW5wPd7%2FI7UlsFBYqRYrjS8rYfxCjnn6mt7Xbc7ObxC6KTS8%2Bb4tiBjmKK7DTmBLK1CqVmESwZQb9yA6M2ZnqTgmudrIPsng2g0%2BdG%2Bb%2Bw6GXcx9UvaQ6svQd90MuxAurPiTtJcAdUYA%2BHtkHN3oQkCAgxFiMi%2BFedRva8t0c6%2FqayqgQGr539sq%2FMO7DmswGOqUBu3bGhwqcHGJmTG%2Bv%2BO9CuXEag1D7O8z9piL9d3DanS8q6XS1M%2FHdT%2B13dYaCCtqQZzDvUYDKpC6ZzS8hR%2BUKVqsIGyLr%2FgydsuaqSGoTxOm%2FgCjIfs6gx%2F5O0oGjvgayFeVGdBBtlOxQYzoBI4NaKE1rDGFU7ckIDyveo9ssJh9xI9T%2FPW%2FHLh%2BtuYEYRfPqiI24LhWvqa6e71Rba82Ma2YsxH3y&X-Amz-Signature=12848f0808f0b7bd069cf14c0a7478d223ee6c87339c757ae04629174cdbdb93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

