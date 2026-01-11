---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VN6UJHS%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCtK9u%2F3rqr9Pi324QX1WjWpzjj%2FPdD12pWisSVvsJa3wIhANc%2FJbNjXnYq61nWVNwOBNlGqehJtRd7m%2FihJKZMvuXXKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwcy%2Fbkf9lVqF90ujUq3AN9HUG9BP%2BIevZW49KiW06GJScUo3pIlxb%2Fz5QtC299E1%2B3RdgAo4YeC%2FKPkAG71C2o9S2m%2F1ehU%2BFXss2fz1VJEcgX4r01mTYLBV4UAs6FJpWYtT9VJy6iJC4JzEXBF0zDDRhdZWEmO682RHlAeyR927m1yt6omehA8KKjAId%2FRXG5Hjea6Z3L9vlsgXgX1AERxGYyWNjDcYFJSf7xhVo%2BI8XzPlBJ5wrBvLSSiUnsK7gsC%2FhoSaEU4caxo0o71VELb75fwJOEONCOMhzjE%2Fx%2BQ8XnfQLGGXcbR3yVPW0uT2QJUUGcDxeJV4b7frp2nrJllveRpWAGRyCdyVU8waVEh9uFiNmKL1GF4%2BmHyxDrALGIKIsCkFHA4SCJKoIHuNX%2Fdhey3NAmh0IDff9nmpMFqHK2olNjzcLPl0ddxYhLGYy6lgsE%2FVP4AtYzpyVv2DY3n7xyUxkqNwB6vmBGpJuDRzmWiK98cnmyRoJm6TkMn3FsbP%2B7uJka%2FCo3Upsw5LDFnrfB8HAo4fvozdmUaCdyY5KtNUe5YnJF77hln4CqzqESDR3KIqEFtfJhOYjp4PHuB56%2BeeLL0d%2ByDDMyDUgDY1ThMLzgYU1bcZAC%2FWdUkJOKZxouCwHZJIhhaDDy%2BovLBjqkAVfECy7dbMm%2B4vab4tSfUvJgb3at50TwZNmHvbYrWK25LvmzqxhGfW8I8DzpEOLe%2Fv168NLl7g5YvkzBLrpb1dwjhxGGr9R7kykm%2B%2FlfKqQJi8R7B42lY%2FHwS9EUKazFAidob8D5ZBX5lLxsJR8og2mXmFJXRw05U88LdaEc4OFxYuWVkp4jkAO%2BLl5ws%2BOIuBVWB80gvhzm%2BvfTWmqfPMTEg60O&X-Amz-Signature=ba5e1e5fdd9095066a439b4fecc453b19053a02b18b3db807f5c9661bac64546&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```



