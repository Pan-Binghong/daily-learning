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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIHJDN56%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDj%2B2hLSEUIfKyXPMyNA6v3N%2FsUZz%2Fq%2BQCRdNd%2BMSmdiwIhAIfFXizf834RFfqhp%2BjDNAOhgEtWyXxwCt25ubRyOV3ZKv8DCBkQABoMNjM3NDIzMTgzODA1IgwtCMzk34JkfwWJkDgq3APFunGunxnmLEVaycvpjlL78jh6oDJ6cg%2B2zh9uZgR353JUUjrV%2BwRVj%2B%2FNHk79eu6KTj5gJAQ2bi3aztBvccbt4OlsuSsmo2GmvdXqOB50iFcjzXsIsy%2F6VDexAe%2Ffk8%2BZXuincecaxrwdIgtfmk5oULFa98XMhvnlYhLxOm%2FKwXCWbpDq2XLMfCLnKmTiDY2lTvopzuZUbx9KAfTQee6dbiSl2JQVlwzZ074Jrq%2BSasqtbHJxOVYP9gRdcOAmOA7737lpwrq43e%2F4KIzR3apVaZRsjmnC3ctYdohgtPME9N%2BeGyF0F2X4Twya5JUukFybjNcyeEQduN%2FMTEMVPRbI0L5tloGST5fMbzAoUigIRM2AM0cNtryT3iUfVV6AwjqQsaChoo40FS6ioAJR0Ztx5T1QfSRQt6KHSbzZA97hoXw4KY1O6YV9yKHy%2BYbVJ%2F95uxb6wcAuHJjHCiyTKQzS8mMnTJKbN6ZjdnaKqr%2Fa1QfrTYY0QU2oYxALmYLvIFMkxxzQZR63lek6O5PAHegV0WPrpCucNNRWEK6KL1Rlf9cNzlSWxMjUEB1jEm6%2B0uAqCEf9v0U%2BzkI3TR9R%2Ff7JUaCiqKpwvuhj5haN1aYhXque7Sqh4V1JN2IPeDDe4KzKBjqkAfxtIJ0tdSh6uyFaQ6S346PfHd%2FFPytkTmvxJxp9CJExFvYFKanz7TpAATRhPXtvkYA%2BDVoiTougp%2FHt3IO0Q3FTndPW7X2ZX9Ll0SJce1g8rNtCbeU%2FSya%2Be3a6TodXyn660tYgyI6fBk7jq%2B69gEttQ9rGT7nswhxqDZ7V7NvtEaAT371y%2FpGJukmWTAR3DnNlS7OpVrzsYjUKJI1xboWFUTaL&X-Amz-Signature=4a0df966bb9b77897e41a42066ef1f704b71da467031dd35b1a0fc1ff2673d6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

