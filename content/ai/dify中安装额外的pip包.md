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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RFWC7NY%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAuhyctxrXNjJJQf03nniCSd5oMx4b6GRE1wzNyjmzE0AiEAn2nchhzcwrjqu9Z8oSvKQgaPfMU2RiV2VWsvaObDOR4qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ8HSXXDBXHYp3W6PSrcA2qc56vZz9kPOhLO%2Fd0U98mfVbiYneQ5xMYPMYDSmdsVmYtHL8KvH0DYG28YgSsl7Z2KQrBqB4DUMl%2F5g7npQSUQVIHoPbGq2aM%2Bar%2Fv%2FyfhWuUkXGYKcFbpw7M62GeCMH%2Bv7f1I2Z32gnPR9ngFELIEFNXnjI6BatOuuD7CkC3hNksiDnOLSAyo3VM41jK%2Fh6Pbc3g5fyVESxlvRsVZSQOVJKkXwowMZhmbYKakiijPZFkHlgIR0lDDL3L76zVHZ2EEZ3lxxvsF%2FApPZvsEct5IuifJU79l2cMmNTa2eVNlUnJRXdefZbx%2B0zpkyIcRL1FgpawUkDNYKbOg0Y8oOptcqnrQw2it6GXpPxIGUKxP4s84eWOzfkcqqYeawAyafa6f7bnihlMtRpfO67oe4aXDvE7xqMnyMfQZEopvizAnlcf4XidkPH3gWjLMoFID%2BDgV2CouqOBjDQveHnDymZbSWud6vYYE5t3fdifel%2FFVXHK5F%2B2EIwS9E95%2BGO0IprfOxd%2FUHU8XC4YnbVjlGt1GHlYEtr6K%2FpvhLf3UMyTaGFhT2r54rLjscvhW%2Biwh3OT8TAvwwt0ys2N9PgdAuwV2nXusbGZbucM2e0AIIvNglERe%2BIQKj6svG5rnMOC95MwGOqUB3eR9Y0iJ5XXIl%2BwOBDcwwMadykKH6roXk%2FDw%2FsUK1qnbHO2896mLO9crwHK5dQGrNW2w9jtMajrUFXaJG4YXZPzal%2BHSX8HrW1om3l0uaPlBiUoWx4ouCPhcF8Um6hIoaMLXs1AHRjKh86g%2FeS4%2BUMROAkjvdhPQZ3WtHcufIp%2Fr0ODOQjHWFSS837N8wtBjeKMChBxPFkO2GmQHXzW%2Bf4MbqnyB&X-Amz-Signature=da4b5070dddb44b8d43fdffb94e37a984728be0fded56a4338b096783f5e1c3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

