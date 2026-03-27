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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGL4WH2M%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC4v6Ya30LV7G1I3lurkxGMbNm7TuEpSfP1GE6wNgNKkgIhAMbHL3ZfE0ftLoBIa0FRizPrj%2FO8aMnfu6fn6bXvkoKhKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxm69%2B1Zlj0lDO6nP8q3AORiOB0TcrthrlNF%2FQAoao%2B0lshi6fddIXZVxoK%2FQTBvsrf1ZEKIw2KGVITkI8%2FrgmtEbm4pKsJXqWDSQhd3hA%2FQH8mKx3%2BdRUCLulAVrIc3%2BYWvYHinx3YqkyoBrvOYEnnrzPa2z%2FHlUJ6lleeUnuh5J23GjOHiAJMHJWZJ5eSckWpAaY%2F%2BNuZqkC%2BEg4yUP7bfa%2BJSjeuZ26F4zZhvfwNDRftxVM8MuPCHD7CRPMWpuhKUTid2T%2BPGmkaSUn%2BdWK0uA5IivBQcYRa0MklIwumFiEq6AbLk9nDVbUPXCwQNgtjbLB9dpWGbqoctZDeATjWt6aVHSvsrqaFEcT6ElYjN1pfSyJfLTEp8UzU0ZKxwMFSacCruQOIm%2FC1vwzUiSg43UsRh9DkdEdITHBw2nKh1FqNbyaDm7QHHT4HEKPwJCjpbh1lTFSrZJOTXR%2FXQVflDEcp91PfXw4BseGLJqzypmpTK5ZbwW9VJnveHO66rWLAXi40mDr3mq5BnSVS48WYaJ1tbynP3nQB6khpipnMu69NwZXkSMQ%2Bz7b9o6VxOm%2Fei0B4Qr3DtQZCPDcl9HoTylqiMlggac5l8xNjsX5u9U%2BMuMKJkQTcnBuCLQPf%2BNuilu%2BxGUh3fiTqejDH6ZbOBjqkAakKTfQwO3d8sUB1UHz0OyOAARui3W5ToZT5MoDhtztY8RlfkzyWurhGmqgH5%2BkKsddUuuJJvD5haWoPtOivsmFT3KOnHJE%2FElXh5UrIaFIgwx8WWDCxoYHvjsds9HUxvan%2FdRabKl22aHoirGPBgmYxs95aUQi1747eQSyu5QFAe2sqaZMinXK2GFl2c8IWeUU%2F3aYq2qj97aKf%2B0FubHTQ9ppP&X-Amz-Signature=74c137e00f4a58c4b9f86a5a59a18669bd3c278898fb57a823c67cbfb96a87ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

