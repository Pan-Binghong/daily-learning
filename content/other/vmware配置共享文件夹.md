---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633UGREKB%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICn%2BScV6GNKEKVhOe2w4juvfsOrChMM52K7ucapV%2FczxAiEA3P4nOs7J%2FpaKH9WAOtWECKKUgKNbbY4iSnIto6nMXSAq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDN63azAY6J2bVvOakyrcA82hIaMvsInWEHV19ytLweJHrU6%2BAvfCu0o5YzW5avPwJ60nMnX5JgS8t1wxhBMaoSWAa%2BlDOZrOCNpqxT2iwux%2BIyueyiribAdd1XWnqM5xITxKBHdGU6EpR3QaFcihoCD7C1BsiIv%2FEJx1hnHKZMgOMQrNvfv%2FdppoXCVdFQN6m8C%2FjImoQ4ZUO0uUfHKDDVuJqw2LSLicmFrGHH%2FhCtugr6sqpA9l%2BEu7YetJ3aGkLjtlA5oVyVrty776URHwYBjbYYcMHkXPB%2FtnzD3tdeOYKAqhGlIabdNPjDp7cno%2F128ir9nh%2Fk%2F54MwJ1O1a4%2FfVZmyN1VFLeTY8gauSG9KaOP0qdUesXwJdu1abNStCOn27wmULCDKRXVDojOgKKvF0AUJCzoYhAJRphIy1DNosRrRBDs97AL0ilTTe8%2FbuVklKC3GeF2hJ57AkjrMi1mgdQKnyJwBYCWQ4j5s0Jz%2FQ5RqAhG11hUfrtOPaDus17ZoSbEfVGi1IKQRr8unO%2B1dryeNcN5Vc67OYMn6oV16s9OmUN2fuHjBEfV3NhaFBqc47Yr%2BayM34vrJIVcla7yho5TLZH0iQr0WOR0%2Fegq3JGugwH%2BPDvoqicTQhl1vtMSm8oyz8g%2BQQYOPoMMLl8coGOqUBJDJSd%2B67ydoNf%2B4pz2c1%2FCTnT9Ohei3BbiA1ADUTe%2FWHgxFuXDbH7qQ6TX2h85qEUlbP8o4rCoiPxiQeMjwz9834ZFj%2B%2FoL%2BZIItO83NGxyqiqSyvc1gCIO%2B6uytatWU%2Fv7KGeD88zqgbE1ytxRujNSW5BCon62r8lUNPy776fW4KQmNDs0eEFTqphdAKgNoZFRsH%2FHGZCdtZejs29cFoKs%2BfJcH&X-Amz-Signature=dec66ee7b9487c4650240be86df85aad66cd65b7f953edfb281dae24f6f2655c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



