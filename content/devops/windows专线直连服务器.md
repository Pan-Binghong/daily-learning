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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX7MJXE5%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPEVOhtHMSywC5lS9O2y716dBQYVJAXReiKV533m%2B5FAiAGbd%2BhZdoL9nrRHv%2FFayldjvqyP5kbG92OVza5riJNoCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2BVeJ7oT9HbclzXQKtwDlI3dFa9uO2PTEY03ZFqVdVTti7LPzKQAGJl8jp4btAb%2ByEkrG3UkW3IGa%2Ft%2Bh5VA8ZoVbpZxQO0bgzLpeqY1wSuQ4OmbutvYqFFkfobiXowCDs17LOMW%2B4I%2BPh%2BLDs7xheg%2BpK4r1cI2xwzB6W%2FiR8DI0vLY8w7NU3n8tJWi97sWtXCkGRC1ATx9ehUJi9HafUrpsfQc%2Flenio5sgEVXsVXw5HymsYIqJvyZOGKazRrh2RNogQ4L%2BAzsNL%2BgJ5DbbtA3cbj0MqatkACdm2zsvUNBXfErfPcp%2FihOO%2FcI5c2EtI7V4IVaNolG2wB5r2p8Fsft%2FHtt9ycyRwBc7sAraRLS7zLfGb2tbqHVT0xxkGG54LkUmKbiKSfoZMPLh2Wm1xNsX55pEwoAYipaJy5NULwEaTCsf6Cq5TFJW2nBpj%2BbqAG6hHDDC%2Fj5RhnSEv4uig5a3ZHz%2F5d3AzrF4Rso8COQsuDw6RQgsnDzX2rdlibhX9ngCByynTIuXbU9mdahm6tvATaYQbveCnF0CkoYtt%2BbWxwHS1IntBsVvXCBXoy1x4vqd5C3limPDgGjxYpgx4p%2FW3K9A0MXHgKOpQxqohtpEPuf2C5hqBW%2BMyBvPtPQEBE1%2BhdqxtQ2V%2FEwuL3kzAY6pgEk6VAJR28YFzqy1i2xSHoXe6PXDKhaAwDkC7OgnqJKj8vAo3H%2BNBMV%2Fp0CCaJw%2FXvuF%2BV5vziffByEPhGfJFZz0qBxPJdlD33XPVtY0kcrmiK%2F48MQ4mAhCEerYjUtsQBhYwue%2FLd526mQ%2FqtQAolC860m%2FhaTrYyJxxqEHbHo1KFn1mzOjqCj1WKrgcQucVc16ZO3wHpVEKAa9NZDGyJubFB%2BK8KK&X-Amz-Signature=d1ed67195d2f99fda7630a212e95d2bea6ecc6f721d0bd6f24aef7eb1dd68358&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

