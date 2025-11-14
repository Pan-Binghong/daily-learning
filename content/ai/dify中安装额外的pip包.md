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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655WSVI4K%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKiaVxF9x65ZCVeWHc36s3aVv1tXNXWG20CKw6OdX0QAIgH7Kzs2gfMCev6zsC3pXcjlxDgWXOE%2BaowZLoU038RJ4q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDBVIkEMFpt3aNyD8myrcA0K0v0KbbV3Bz6E99BcHuJ06DMNmJsupWAreXG4jhDFGoo%2BxJp7vkSgwmxu5yJ62v8i4sG9CdLG9ZGFgMJ%2FTio2HZ2bkCgpWLTB3wTEDtvIhccF5uyXhInr8Z0yI0OEaJQlavy6QKl3xQsxrP0RH%2F7JnRKEqdx8dx7sq7o35lGI2N6bQvi3RQHwmjvpAXd7NEt%2BA4MjnvxZ3ab4qddxe2RXOYCPl%2FuYCTQTxARLs%2F8LhtnpN87J4vx2F8AqfxbjiTV2%2BBWp2yKg%2BSVeQAOfsJRz%2FvsmgS7l8AeNch4ey6iAY%2B2GP2C5lDSZhdhdd1kh%2FaYi3pFoffUzwysKiD52H25G1FbbzjDsEX%2BxaKWKJj%2FIY%2Fio8B2gHG83%2FTa2EOZM3BQ05m9cJUkKy%2F4fnusdJHbyyS0X7xBRve0LYsGjjPjPLbWO5Twp9TQOvA6uTcQhlH%2Bb227k3lyJX3AbjJo7HgoVay7R%2BkQNTxmuLXmCtIhwL2IZqV9zXptXN1lifEMKAP8wpG9UUt9CPSTfBA04ZJaeQ0wPhVdrqdqqW4qdSAWSIuHXhDyTFQVq3gORrenx%2F2r9PFd3ftSxKmIKmplxHaKZIAgzoVrEykWQj12YOaHom3P2Y9WA3Ji12Sd3%2FMKeJ2sgGOqUBB5c4UiD2YNnq1o70mEaFTx8zBmNyBjkuZkZzyDjRuDOfXybB6sM6CdAHOii%2BX81ry%2Bj7nxD6qsLNqx6B2AM0zRtnKzRoNP4cssuSl%2B%2B0SfLo4kDUr0IPtGzxpRYBnN7xB6nv0IGjtZw8vsaoBngxnMhyB249kVxFB5UseYqmdqw%2F6AnfaYc6eoKqMtGjlsuQFLZNYjqF80gYk3SeqBbJ4qgxrAFt&X-Amz-Signature=98090524171ce1ce24e5a1cab3c8c4c6e0f098bef7172e4a9ac91f6bc24f7f95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

