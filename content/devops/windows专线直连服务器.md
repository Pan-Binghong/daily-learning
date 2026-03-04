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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIDIKWH5%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC59FKV%2BdaMAmwaJmW0TS1HKp9eytVevG3feq7JaDOnBQIhAJ6Z%2BAMIC%2FLSBxKqY60r8czuLDlN3IpdCvIcrBTE1IURKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwweFvL0tQJXgZc34oq3AMP%2BNC1Zvhp5sJvm%2F8y9p11AIhlTizAFwecZZAbQkO82co6IamfkMEg1p5JEpHR0xvXaa4WvjgaDeCA7nRuRpDvFrwvtjZ0%2B9T3E93vgA559DbDsViVaUzligWByQON4lZDukcRsA%2B%2BwDwFrVR5IrqtzLZJux9zozhlopIoFMtBrDEHJD8n0vK%2BgTQUBuia4J2FRydtx52KxVa8fuxhE8QHyEez4woEGhKbHLOy4RwQhVM6TQBk26pCZR600lQIh969o5EgYXY4sRsk9kjYvSnurR2mphcIdSUZ%2BrxWAKwcN0RUcA2DsgHYpAImAQEaO4mLpBPkWvXlxlPXBMuxxg7T0xQIwoVa0%2B%2FSEzNb12j0xzntQCnPkhSj7Vpex0ttGRfTh%2BFKp%2BBQhrXqE5k5ixYZP50QmOfW%2BUUdUmO%2BBtjmtCfuyC5EgyKLFBlPQ8S7WZQ4DBUF9uRn98MNi2sQSAxFMSOW1%2FgdHnivr%2BJ7G8IFrsFeXfM3hR6RcT4hC9jQ6ISUD3Wdwyrwt5RXPDRiI821vBfoR%2Bd68Hf7%2BvHToZ3SQdCMam8y0NwFMKmnLFx3%2BMEAf0cJGD34IvAVljYRnC911NDbjbJnCFPLiKZ6cjkHtVtDSphthsCCgt1DMzCOmJ7NBjqkARAqynsrU8NG%2BMjIN0sDPn6A%2B0r7C0x1rY6Hsob5zy%2BLIE%2FpBvO6LUiK%2BC5PrQ8WbrTVJtDAzVBjtvuIVVVFhOjz2xf1TfaL%2FsCgG6NKy0JTHpVJhdZIwddcBdh5lgauI4uR%2BjFNPI9U6lHPI0CM0dNFjOF3stSC3UC0hEM%2BYkzBMc%2BzY7ZmWXsJfP4vM0iVlJwxTyzg9uxOWQTeOUW33qu742lT&X-Amz-Signature=27f74c80d5690b2c2932e90aa8fa82a6eebb5b69b46ecffd699bab9f677e4de2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

