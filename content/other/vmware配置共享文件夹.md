---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UOCM225%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIASm7vz%2B%2B1XaGw51dmAnBKCYO7wgMMtfvT1z9hosC8rfAiBfTL%2BmNw2kPTqzWO70b%2F5YS2AADVD2FV0LJnvuOeOE%2FCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh%2BoLO6KFnKaoE%2FWgKtwDJ0N1Yv975xDAxVBXdsh2g%2BfZpJeNnZzFnUBLkeJ6AdTx%2B3JGwSHpW2AUG2fbvOwnFFnOGybA%2FgHiXgUhddXdRzEHV%2FGpIJf1XjgMauII3GeZAjwHKwxDg%2FtRUgfpAoXH5gEf30Gxh9F71631aeeNaiTReSE11Us0U%2BrjholObf5rJXdYe%2B6xr393ZWxTj%2FnCDZFPrTix4tMRxMLBvtOfieUhztJ003mNLrxHT7SBI6csMwNLwZnBwChENDjUZBGgERVKowYcOdqrKR3s56BevG2usIw1CIdkqPJ76Li6CjK%2Bc%2Fijr%2FxfbsvmHNWw5hQfjsxZpCnBwOMTKbq%2B0y%2Bx6Ps5ymbLJiwtZ%2BujhrWv98mZibL%2B86NYRv%2FwJtJskCemJ4Lzr0FClG8ZEXG%2BqeA3TpGtfnyerZmq%2FPDkr%2BR%2Fy54m6rxlPNRtEk2NtQM8V4Tojegafrqh78rGHhQnlfSt6d%2F74sydN0R1fElBlyRCEoOXRg6b0bF4Tn27I51ZPYEg%2FbsD7Br0wyo8nGeYnyPlzVB22HJytiUEPpcbOkC5ebILfhLHKGCAx5K4pRKSLZ7MYZSwmqfdvrh8gX4PgBT7HjjS0btJj%2Bx%2BqOP7Xcpkhfu%2BRr8X4rztkBPy4xsw4PqjyQY6pgE4Z7ChfVg5%2BgzQbEnEJ0jNfAFccEQInDKmSI7oa8P%2FDsl%2F7CcOtUinttpSAEHFf8Itt8ifjkB0YTvKY2QhmuRh0kNjOEIdo3pvAE%2BSStVtllBqQwd%2F3jCizyMqqHtGDIz4RIifAlefLQzG26OQzQdtyiHO0E9n300xpxuQ97EjD8IHV5fRXNXtaaILTVcDs7kztG%2FZx0Utd5up02tv2gsoRk8mrqfV&X-Amz-Signature=92d2586e1031c4e1ed188004b9e80c9eb75bb6fe3f2de51d1ded6b8208be0ef3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



