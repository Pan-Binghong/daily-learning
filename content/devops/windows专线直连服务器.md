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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMSW5FJN%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCj0jbway%2BTYjF2rvio9fvVxujDJmeTQYjziQx7r0pWvQIgb%2FWf0%2FErv6R%2BHTH863M86akkCt10OSpJbjy9Llm8th0q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDJ05ySbP5ddbdQ0g2SrcA7zNoogISCdwjUqJBiaX%2BCj55PEh%2BVHhb2iUVt1mM9pEtN%2BORmVDYCji3G7BxLjBJaSjnuXKnEPfYoCkBp1J8ZqX2VqQRqYie0peslVo6gvFgBEtesA7Pr7lfFv55WDKWbU2OMGm1nz6hZG2KG8Z43Vk2WQPcVrSsv57dALpUvT2KQJd69cxOr111YpsMhgYYZaym%2F2yXnkiaG0dEJP464r%2FHJgVU2Tj5acXwh65afckaz272PywmKLBBn3BrUYuMhOVgmzFgNYyUAvMIUqvS0chqvl4jInON80rMJbda0iUPav7W52nItPS5qXWEJX8J5Nc%2BiAdcmzZ8Z46n2nrehW8jyMPyXRgjkoSSnIO2fbGfCEQUreaLMIRaIKYx2TcYOcM6B0f%2Ftix0zqvfw6NduGXRs1OTuwM2sPgWsQXTsv%2BS%2BZiDj17NjxPryed4ysLtI%2Bez3YT7l9e%2BWQVXHBmmuaniV%2BWIzIBFt%2B%2FgFdM%2B8TxF5xhh6uQ7%2B%2BHib3Hib8diESJdZNBpzTBaMK1UaCuHLNuC4fUPBt5EMNvZnZVuuipUNCMGsVpFvxR9xAvIEg2uGOeI5iSNQJ7bwQCYsRbbpR8nJ7chptTZjbaKVgrqej62bObHlPuSbxHFhd1MJLSt8oGOqUBdBQM3QpR53J1MT8Z3bgRy%2BVfp7Hem1ylMYMdfpnPz6g2E5Uhq2wkps%2FS7Aw%2F4z6HtDe8UP61gTT8bZHPCHrrF0Hob76lKhJsNYdsk8%2BvMrB4VXyVjCFKTD58eCuTkBYaEtzvFOjYF4thcFRwOyjwRMn1%2Fl82%2F6nKhwfvT%2BHLE0fZpPSWSUTfSJePARijfFgurcoUIJmoYZtDkNZNTQDh3zYfrMkw&X-Amz-Signature=429949567a946efddb026b36cc7c0096e454bbd38eb5949fc7ed20600c00d632&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

