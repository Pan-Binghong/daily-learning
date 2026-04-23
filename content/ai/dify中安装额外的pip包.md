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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AKANIVZ%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FKBwANOcsvYio2IbkK4%2FzSrjsveJsz%2BhIrt%2BLmf3QSgIgNfaoSvzysUkpcDUml3rr0AFGBYvMkQTtZFu%2Bb7onZVAq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDCdGhGZsEngCFhZ%2FJSrcAzU%2Betmd9z96rggtFyuOatF5FOrMiOgdJUcXo7eYIQVV4bpPCTpzLO4JoZ1KMICBpB7S1KxZkFE8P9bIqoFTim2paM8F8pSxIPLLg5I0lNxxwl%2BTMBBkcO%2B3T%2Fp9iTTcGdRd6pqUFDfHcgcvjdyP1gaG%2Bk3bi6z8UOydLRFXG2yLx7%2BCZhj%2FWrcySojdmYVSEQayzXpIRVdYXRiL7KOAl0uKGFDNGeE%2BPQRgZ3nRiRl305XoauO9o6EJWpD4TvyLePjThEt6aqV9X3IEIChblnk6PUBKSzyDwX2V8VYhBuI8pWMzGnA3aCDiCF%2BOztro5MOvTCd%2FOs5nWc47KFGBccKqF%2Bn7Rwwz8ep3gi9OtI1hIJBy3VhMqe72K4WODGcLbDEVtfdhP13QujXlERbhkvNOn5wRFQnDOcASobHSNPQ0wTiMFEwKNxTTZKGawNyH4ZE8SF299J63Lg1UJA7A4KQNrxhf9yAwrh39M8j3wPWjbWJYZ1C%2FF8VJFv69Vm8LbKGjbGeBFFrXFIgkWvWW2VEEvdT%2Bvx8OiRSUErSWUgeyIfkIKXpwwc0k%2BxYzsiVFkzjhpLnL9iOzUW4ox%2BAlqVG%2BC6ewett6TG13bJXP%2F5Ke4xmFVRHE4MlodX4dMKmjps8GOqUBUCElNyD7YbRWQD9LDRoKS79%2Bdc4D7mLnvHv5ZE%2B%2FAHTMGqEfSnNt31GwDTAOR6TKemGCVo%2F3DBPAyu3CpHilFeA%2FrK2xN2P4%2BR6qnPpa1%2FKcgO2Z85tSv34PAKY60t1596XFlKN867mPWZB%2BPt2EFUoyt7R9xvt6%2BBnUexW9C1tzpTUG7xbGLdNUOqlfF4cZGnmtvkReLuwWXlT9etox0NDXRqkT&X-Amz-Signature=7d997ac56aa53bdf44daac038dc015612f63719b034bbb28ea8dd3e838517a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

