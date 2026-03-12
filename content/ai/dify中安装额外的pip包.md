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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOPUHZTB%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3b7S3iJeQwfZkzBHCfSYrTZkthVKtSitvm7nbRiIXBQIgc0DwbZsh%2BIcbdEwaK30x5AkLLfj0YTB5OGBk0Z0kRjYq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDFtg0sXgtHfh64FtZCrcA1QgYbRxtXUZ%2F1zXagzdlOBb22P4D2oBscdDrjsCwhMvQ3yGAkNRDhCrZzMeAL62y%2F53wTSxZBzlr7%2FT184GFuX1OjPcTpodil96wHLQDUAToNhaJUPMVJzK8r4vDNUBBAN6jICqiQVWNED1UneOXQKCRgjDqLrSkrUOibnWArBBYlIrTdtx7BOTpL1z%2BArpNTxp1vZVt9BGPVQWiEofM0BfZL14PikgYTiuOXTsgFA88x4M%2B1eSFhdKVHobzrl1KKP0MIL%2F7%2BDJbhWE4rEsN5a9%2FulWAkL6XDhhRkdmp9F8SpFsdvzXvgIuijQmYCEo1xylg2y6zObs73DHANggbVoNORBep%2B73CW0dmW7HcP3ToZjcboS%2Feq7KO8AYZcqAx8tf503FKh5Od190C4qLPjL%2FDqGJnHQMdAKDAm7Hyf2OZKUJaP7nRhu3p964i12sOcT7wd6mIxkVStKhkRbe%2FuR29KuRcJRSZA6O3pbIRhWX%2FLD4ZoD6ceUf%2FKzAYTn5mMdL1e1ZFOlhn5G9YRo5qOlHafgATFOh5audcHUsBZRuzhKIkzEVMJ6l2o4FpSc%2BgVxLCPXzfht40ZvMYFLK1y9IgL0v%2BEYboEZ12vsAVjW5BfN04H9My7hxc733MImyyM0GOqUBWZJBzKfdvU%2B8FqLFOrMKceVJRHPOEe%2FnY%2BHwENAVCzP9VntJvdno9Kdvdd6Zo74dtPO4nAb8uKgXvVPPru3tqEnc0%2Fxq5exqlj1b8pU1eYdk8VIJYj7l%2BbgmcbCauplzX7U4NCZaeQ0qsJXFF9vGUsYwLRTzwEErAspaKAqI7qynPFYE61nRV%2F5OJU%2FvKQ1boGR4wR291NNz8T9bdWZ%2F%2BrPFf5%2By&X-Amz-Signature=7d2256db8623856a9cf5c3686a60309d0d43689e6654749731efc0086c559803&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

