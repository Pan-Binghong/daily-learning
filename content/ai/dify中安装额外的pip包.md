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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBBLSGFP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrT7hXoIio2%2FQyGM860FcIRiloK4U9BABWPJ9ouIhpawIgYPi2fEYSns1ha39tkMJTjsqWa6nZBawckK8GFLj2vFkqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGxTRLnpTNPNK1suOCrcA1xirMMb6JHILzBy3wwMqC3P8Onu%2FB3VVEcucltDWpJIbP2Nj5rbSmebglOtyJrL%2BZDfDJzT6mgeE%2BYrdqCnGjSRXD0X0%2BiJXuJ1KRDp5AXVLfrQjXBwJNLomhqoYB43%2BbqNdV0BlfekiXdF%2BKwtOZTO5DFxoZ3s2BlIUEujXXLTFDAZOy7686ylsHfZvlu6lBBDjqVmnPxKd4KrO4eDBlW%2B09cRCnEz4DbkpVrzuWWk%2B10LY%2BiRV%2FgaK54AO9sBaN4%2FqUBUB056Sv6MYkPE3gnUTsRVA7zykO6Qs9Yko8SPkNek%2BqSoVhxPZyHjSZBNxnHUj7fqOzgiwxqpnYGGqpV1KVziRHeTC1O7lv%2B6BfUZVVYm%2BXTfdoa7Y2kKLCvsbl01WmO53bRdCEfJd5I89R1l3q8va0uQZnV%2BEgkV8ktOiinRKKC1Ht%2BUFrHxPvGnCaNx6nHDHl%2FfSl39cEF8DC1ooSrWPMJw1QT2O8JpOut3bq62QtoyEL5KTE3eFrTGzkvYcBejTHHUp4Bb5TS5m1UbLXGQ1br3K1Zd6WgGgYMHEpG0OJBqc0ZbQIXrUAMwrls2Axz4s4BbiuEV4lrRelbmoNFJLJ%2FA8hDaFne%2FWRpDOzYEQ%2Bhpxs4sF3VgMLDyr8gGOqUBlVqOGCyNK5oSeHGzzevjNrPbiVUXATFm0rmPHesAD2q%2BntdZB3Vo9LItMVzzDiSFTwp2eHDRCWob%2FG3s0e%2BPf8BWzyvLRus5JqbzaZgloQoZkNJtQKNuMjSaMXJ3%2BhOH5ypJ8rCztTzdSuCLV634RI0baKLOCqQGCCdIO5wLUTCY%2BCtzbWEWLFEGQmyjAqmPN7PVdU5Z16mdSMydsvZU3ZbdRtr5&X-Amz-Signature=339ecd378b5b8b5d75b04aa9129743e1b97b7092298a0e52b0abb31dcbc89d62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

