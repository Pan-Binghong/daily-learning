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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN27O5SD%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoKrH4mMLCF5UoIZL1H5p7gdOfS06oS9pXwwP92AggeAiEAn1yzlhbgXcy5BfUckcf3SzNqUTKIkVo89P5HuAHiyuwq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJtq9eqaeN4knB%2FCbCrcAy99w4%2Bx7mCOkk%2Fp5wvs0l9j9jbsr%2BRNM2kuVZwfND%2F9J5bbmDm1Xqwjl96sEnIEuUPc02PJO%2B2dwgk1ScCuO3%2FoLF9LCkz59Y5D3dGlzrc4oCUIOLxQIB0eR7ox3OuB8KGAvCPJE9MARteN59tnXN7HmXCbxO59ZqE0kYazaTrxY2%2BVeiBcPGrJD6S0bW954KXnS97rARYukdb5h%2FjPlZ%2BQYI3xYo32q25c0ASm4LlIH%2F%2B3ewnK%2BhI6k6z%2BqAldnYTFGHFsB6ybWAAie%2BW1SgCfWA0MUWMDjfUxcxNFf%2B2E1L%2BXwGflmM7oR1AW8KKgvpYfAGCbPD%2BnIdE6lljX%2F2Ah05RqGRLfew%2Btka6DoTI%2FqXvRZtAcW28s4tv48rkSx31XSONjX8kq4p0R8BMDsWvu%2BfrAn9CwLpeDxc4v7CKSfUgY9YexWrvYsGYthqhQcsBzmfCWo2vfK3ZY7YUtRxx4lun4DeFTq0kb95bd4dxsEnYLfd6yUArTR9UW2SJtnQy76HyfCmjvy4cD5sdEZPiJa%2F%2BBtkW141wkl8aJsrePHcAD8AdXVtZYF8wURjH%2FEEF%2BzFV%2FEmfJRV1bQyg4M5yaVx4niCSJ5AvoM%2BG1e8KmRbQGCXv%2FkVcbS4R2MJeut84GOqUBKSCSe%2FNwRfA7PHLMy9HFKihwcYB5uYVPpxx1kVcrHUbbhlTYC2PaQ4vcnwvzlhTXkM2%2FlWu1%2F2CCn5xZnp2iuNX0dteL8GKV%2BjcTgqvxbK2aEw10FKIygyea3QAB7tyNb%2Bw69OFyMneNbalnXhMCQXRg%2BmQlnRg3pJNu%2FkErW3rmaqZ6FlNCb1ZxYY0E2xWBTK1YotswpKxyG1hD46jVafk%2BBuDL&X-Amz-Signature=729303f2251aa89afdf54d870b577b87841370e2b52b802cb69d09e0a2685062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

