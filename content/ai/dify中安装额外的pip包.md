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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7GANEBF%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCrKLZlyJ0fe89N%2FtqHDqK8ipR2%2Bvj2FpOJXr0TNKop4QIhAJ1jZJNyw247y6ziKRK6TLYfP%2BJhaX4dwMvIRWCZimVTKv8DCBMQABoMNjM3NDIzMTgzODA1IgxvKzB6%2Fpj5aF637oAq3AMrAjPJG2L1%2FeRsyNQf5Z61LIJX0dMttBljcBvR1fVElUQ%2FkzwJZxZ4Yj5U3jnYvUrti%2FFKjir77NXgwzCHia%2BO45%2BVMXVA%2BEE1CwImscepwFbIXn4VLnyOiQsx7Xby4XjEjIZeqlTzrnniu2iao15hZglBarPehMoZHIxvg8iZzZgFmFlrN2J6SdMZn%2B3UM84wAm5Y%2FsUpwBDAyzrSnVxQ5imFcovXHukHar4uk3Exx8uG0ydBiJWgBIhV6y8CumFstHtWdkTrF437TE1i2PD3wc2svt6STWYcCOTLb1Nfrtp6HqnzmaBkgLu1yypWQzUqmz7EwvwMklEVpWlFMbrh75AOQcQ53BoINLENntYFjRPHqXzKjwitEHMaBr0a9UwajbgzCFmCoplh2zCiqhUHc9F0jhWg10yWTNzvlGfSDCddCNnurFXEDWGLHMCrMJzvR6fruMSk3rY9VIlao915zhzDXpIIOTa7QhIglpFWyYwB8DUo2mDwxXhf3NDsq7yfZ1bQFt%2BJCfPVXolKsvFnrr8KdhQMfbxSNAePQq%2Bjxju%2BRlf%2BSRypj8ReVBFUxi9Rc7t5SiR%2B%2FVZgwat7WmUmMnfPuNktidagWm6bePcC8Cek1HcR145q7XighzDyl5bPBjqkAajwNE9NHIMGAYA2E3pFg7i90YcHTa5xT%2FDNtde0Q%2BcUfvysaBplcbIZZezYvse386lr8PFEsIc4ShCwLqtqy3j6GmMbnahQ2lvOgO4uO77yA3vkuLwmhj9qEOAm8HY%2BJND0ugaiVEtc4RUcleRMY0rj7%2FcamPNY2SmMv3OPanW42wGoVis6UD9FhqT0vBS7wJnUY8PvoSJX%2Bsj3rty8tlAAJseL&X-Amz-Signature=df75b359e3a2f73c7cac4672108f6a69757cf57db056239435339077fa199caf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

