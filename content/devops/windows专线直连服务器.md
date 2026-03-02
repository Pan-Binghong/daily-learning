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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTCS5VPL%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUmXgRb1Y4B2xES%2B6jLDcXuDBl9oNliTllG%2BCd3rDktQIgf7nxIYq4PBwXaTrJwYWBy5e%2FpUucWsf%2FJV7TZVdnt%2FUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDN5QyvvGsykBfliNcyrcA9dNHyZ76hL8b8k1pbJHdzkRs5oUQgin4t0JTq3Rl3TNLmaSSPR6zyuQtSbRClWVSdk%2FM%2FetVliAXGLY0Dc1yh0TfZ%2BC0jIfyBwCwORHAZ16Aev3M%2BdyhHett0cwOW9HZvb7dsOkdIf%2BBNUtMcm%2FrrIiMOmXQcf0w0JRrwLWRsB%2FHtzoeBuFau0tsV0uwRbBOEGEXN%2BdzGLMGkWhKRAOsJfQxUwCXEydREbCsnVD6Egb7iUFjL5ioErxNzXFTZkc6PMZmp9zSrEoo9QehQeY9zocd738zzrC%2FJMgJxzlzaQPhsnB2886jO0ra%2FUXmO%2BSjKUT34yWHFoQj431cAUR30jne%2F3BFZmL8faccD7%2FpkaV%2BRUU2RCYxqV19Aw97qHxHowFFaNBeC90hlMopp7P7CLXDA9XQ%2F99pQDhUtOXLvZ%2FiTbKV5m%2BQOremhhuVvyhgWuHsRTIfmXTEMr8isKW9JqxCzkAreD5vdmA6z0fkdyOapDozm8YbNC78kojbFNLHGkG5yNO70wBysXUoqqXhWawk85cS3FHcGSUFsGiojoMEZG5IexzqJtFkzrMdxaNB3dez2%2Fhkd64YG6hkW%2BOJVIlC%2F5xE1M3arN%2FefsCPOUAKSDO7d2HHeQWBhTUMJD9k80GOqUBJptDorfV9%2FKuI9%2FbesjgHS5p6bElHmtqyDNH6Xa3XzW8Y8Siqy6KpanJIeiWbvUjxXiYrLM77pyuWPt9MiG5DbF%2F%2BG%2F8Cvh7tIoIiilDR8wGQ%2FxkAdtD%2FdNgNucS6109bFG3LWLSeNYjU30GEsr20wJmLAbDkzrQZ1cnayplDNuVW9xxnt0gjMrPZ5LLsTtV62VQlMZ4yKG0o6zxMtHX9WUX7vsM&X-Amz-Signature=31282cdd2a5e04025a256a8c4438a2fa9f580391823684f476b349a1b47160fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

