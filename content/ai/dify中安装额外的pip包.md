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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJC5SGIB%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpHqCpEimtkTNhYsuAZ270KV9ZfQvGLZ5p05%2BdCWQGSwIhAM3vj663J910u9NFUwlrxokIwNk9lD0dzLL%2BccZMDuuxKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFmQzh2yhgekJ5Sa4q3APwLNFWVnvoshvesRuqqNWpvAOgGusvCVqOlQXzH9Ksix%2BHTtdAPRHNhdbMjVbtbmaFwryiQ%2By9j5ySYLinHsJmGnbx%2F8MUD3lqj%2F1jclE5qH%2BVpE2ftUS2ZYUlIJtqi43jTLmM%2FcbjB7ENbgjcKTeqNO5SFlvs4OoJvsnFgbN0XZhRabHEKDu2o3v06%2ByXJPCrU3XQrhpLHVKIITTw7nvea3ahjx6rjSQYa5bDXyIxMTUIM6kV5wOwp%2BACrPkzEZV1HL1X2Cq8kpMHpAm0r%2B69jd5UAYhreexCTpSNSE5PrS9pWJLpBD8QrpwEFTyOBEgbE%2BqcJL5XHAKO%2FhHh2bby6ClKVPIYC5zoxMrqjRrEnq1kXFfcD4Z70rlJMpdxWBR3WsRKZX2of9M1WrLRfyV2mdkonqWn0Fd8TIygT33fga%2BdTtQQIn6YLM5bMW7yp%2FvUt3YKVVyRpqrSyQC2SwuNcMG5%2FMBQTae34O2fsIcpC2nCuaZGgX3LDWF0aXeMS61%2BBDPOzxCwipbtVF%2BXmZ3EU4FiFYY4FwW5RHDdVKhSVmfG1Tb3mrxpAIjHKM9%2Fz7FnDwAElNiY90tpmGHSvp344j1ha6oiNAhsMVgZTPetjfC20XmojCLPXz3cBzCAh%2BrIBjqkAcB5QznVlL9gzJKScQJdsxafuAGwJaw%2BEHHpmX5o3Pv%2BLec4ThkqSrK3yhFoEod9FmZCwbY1xeikh2osa9IRLNDCJR9oqT%2Fe%2FKprrfhdT5Pj%2FWsqTwBRtLSth9m4ylzhBTDZDuzFbl%2F1vRPKwSuukL5Otml5l4IqVaaFq0OuPqFhHVITKy5%2FHUI9upTrDGh27G3CyyyeATfiT8xINMLGNIbOVNpH&X-Amz-Signature=a5755115a1439347462c5c71edcac598656861f9a7cef950b16ea0e7fe8d21c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

