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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUIOEXNP%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC4NNH8NqXXzO92hD%2Bdk97K3Vo12rAh63ZqD%2B73RuOPdAIhANDoWRIWOeA%2BO4WE%2FBkY1k578ZZpfVjmEtDc9RknEvm4Kv8DCCsQABoMNjM3NDIzMTgzODA1IgxzQ9JQAgyle6Jag%2Fgq3APeD8f%2F6tSKTZ71BEZVfaHI%2B67N%2FKZH7RwLXUBNX7%2F61EpOG9xGW8cGVV0s8nXB8nmewsZVUBtUV%2FdcWmuLAup0iH%2B%2BXSoDNdxKFPc%2FgGeyNFLpRHnQnsMxCl1pyFj1gjlfVLw%2BqxB%2FnpUL3WicKw6gN%2Fn9kYirsbbSgt%2BJRAOCOv8CSgDLA3xmKG5la6OaSfFhQFrPqDELL4TMr4ZaBKejKWSdHHnCEh%2BfpN%2BmI1VNTiL1r76IWiDR52wiXbPd27nVW1FjBbHiFXk59KiqrRF90qJcAPddfUMk6XfiopmP1ME5VWS9C9V30OtDIv4KZS6OB1j14B5lBQzhlbK6E8wc7%2BlLNX7XtWipF1hoJRMGxy9eYi6wkE0r%2FtcRhooTs4Y%2BE%2BdJ3N%2FXxP6VcqsAXgk%2Bkj3FYqWyifXGYODVHrY%2F%2BeUcrPKqZBj%2Fkk1KWaffz%2FnBCjW%2BPFTRUEtItTTuu%2BKbHQTO0ubEb5yOoOF%2F9NSMrPEnSSdY%2FX0IL6NVeil4IEqMjFZiDViBD%2F8tDiwkTmamVBi78W%2BfF8XV7gY7lV%2FIwOQMiyXDnWO9KfPTwY%2FeyOhWoKG4TXqcrpe%2FNmRyXO922y5OWzdn%2FJUkKaLQdZ8Nt3idbNb9dBmEAn59SDCMnKHLBjqkAeYrvHtNOvCWNDq6a%2BGxbC%2B%2BOdEwyIAluoY8yhtENLttn%2BeQ%2BzqfNsoMnLJ0m4Rf6XocTsbMOTM6YwWaHc1VFFN1uwGTokScpJuEv28sNWIJn3FeUUBIBuyzrZM2jIfK2EQdWV5cf9NWrx9jockoCc49pXz5chqbxHaSZKR34sOipgVNTsRq8M205TO7a6C4rYwKz6rSaUyf%2FJNzIPSVVEozKJ%2Fj&X-Amz-Signature=b4cb0e79e8fe52c491d6c4af6f5f022a668a3564c53e72ca3faa5fbf9575e042&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

