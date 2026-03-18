---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ETTSKC2%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDgc%2Bi37cK58RO0adoTw8oVWVuvdlPbSoRJxyGnKkb2vgIhAN5MMXg8tyqt%2FgDJICReeMC%2FGW%2B%2FJo1k6pgMQepK2SOeKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrtBpNFvjTZLGjTtcq3ANyUR5F2Z69u1%2Bo1%2FsF8Hc9gJDuf%2Fqqy9tvJnG99RyCxlXaO%2Fy0J%2F4XjolGe%2BKNq%2FFpceXINJJ2PGMbR%2BHshPNs1pBtKmFN72gw%2B8pSKcz5xO5wp8Ejkxy9hxtXOU5vvYYBCFh3UmXSMxsVDsLZ3JYhZS69GJIcTxnhFuaFxhZJSMM886K%2BxzNCuVe0HiP3MB%2B4NT95YBikhg4DUwdTEMosgD30EMB3Q6mQzHBQ8S%2FXN1tqMFMQsg%2FfhNaYNMVMujjDoHp1l8XGkn8c7DXt9t6dqZ%2BdBXqYADJcMNmM2DZjTUjNxrecT9uv%2B5CIcPB1%2FbPHawk%2BM7VPbkoMQNF7VoKH4JdN7y9s%2FTQm2nnZVWJPPlvxb8qAr0wIRgkEXlygaQlYjFSosxRhzBw9j4AsYhrhQWe7DBUice%2FDZ9Fp%2BDIv47P8bdENm7gQ7TkABMoqzhUIP9YIWZFjpRHmsM7Q1gOyL1dcjdYiRfW%2FFiPdqDZzyhgHMMkrahAmTjdjfdiO9Jhtfi3oU81Ou%2FFuvsS2bnbCDTQKln610h%2BTHrL9Qq2L1n6Z1BUoY%2FPAePawpioExC7RLVynXX04Ou44Dkd1DGAf7HS3XLmXV1FpU5CowpbVnrUeSLSd%2B1EAbCfMUTC1pujNBjqkAdsl4bsd1Tg4WKKcR1RrkBhXWwXdVZTtwCjCGWeWXpH0JqqIugugvM%2FM34zc2KZiq1bf8JkMyQwXYdf045VYbBkBYIOhhDxMQsvMF05YQPVZ4qLAGE%2Bh%2Bgwq17gJ9akF3gn%2FmxoJuSZokMQutzSJAAxB4xxKX4xX4917w54S2SfsQrAFkdowpeBDqJbwU63WTgRA69wW%2F3VT4%2BoIUq36ZNJkNC%2F0&X-Amz-Signature=2e797ce31da619d788712d30210ef80e5c268efacc60c72cd95534616fe1b67f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



