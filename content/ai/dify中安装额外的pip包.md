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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM5NLL4S%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCICxlf2I%2FLEavGQATdA0xmtVUgAOnVWUcLxbPyd%2BngxfVAiEA9skIHKoHjN6O7kn1OhkGpl%2FI%2BOXEHCNym8C1myEPWpwq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDIUDdzqOLenCk067XircA5rSWNc6jM6OAHe6KOhSEeCC4mF%2Fkdkz4Nxgw87L%2Betvdww3wa8HI3hZVJ02oqXqtDUvCtLn9XriLXH9Ktl%2Bc8jn9NDGtWCqOxDKWih2RkLF9wOtj%2FjpWqAu3Q6OZjXyQnuFiI5dX4UIJVPmeDUSYuJyt4%2FYR4RpDJ9K%2BkqZ08BgFiTxzIbXnAFC7djYJXnvL21PZvzJf7u3Mn2hS%2FMA%2FWEEN7OwFaasHyArdiGszEkK2%2FhFehiEDTAIvZJNaiXHTFt92jkDiAnivptqhyQZ22N1einkKoYR%2BQTUG%2BeKLmEI3%2B5YEt7009RH5pOSouG6MHjafJZQWqIE5VMyyjUvLakjGSaF%2FmLiEwWu5WPHHJ%2Bf8NxaF8ds5tH6kQy1Itfm%2Fkoj3IPDdkGwsOLLP%2B%2BgdJWPXW2Tj924ZJy9pBs1068SCKgAKk9rSAJ4AlrMkT7A40ApGFD2cmDbvcxIBUHGnnkyyGUcFQo8Wljmqw4RZNsI5Pvt0NGzK7cdtWh2EUk%2B%2BpQP1IXKL02gK2LleL%2B%2BeM2Z69%2BVcUndT4Bq35PqmIJrcLISIn8JDBVTDbXHyU8VAKKhk0pot1dJ3N2w3FlUOZ2FYQnDpD%2F%2B%2BZ6Q436KW9rj8ZEXvrG1BZzQ1MY%2FMKaHhM0GOqUB9CcHR5BUPrnjyH6%2B03XhFBJrUmMq7pp%2FjKBM3G5kDyKVPj%2FWirRHDChd10twpvnxC31NJiI37yme6kMdQmvrMyZoLT5dvmy75tWzXKwgKJKn5nKeJYtOEGOp8AihK5ldsfEji7cAWgTnY81rQMNCeNW1Mj%2BCFAjuj24WxhIDYmdMoRV3K21%2FfurY8ySSOaW9F16oQocWY0S7xthlHEexlJ3xPTqU&X-Amz-Signature=dffd7b17e594e76f812d9b4d411eef76f667e4b43711c5f579053c5805ccdfb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

