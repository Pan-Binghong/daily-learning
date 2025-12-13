---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGZVEQXD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIF5IuL0p5oF54p%2FruzMD1%2Fruj4wZp5u%2FIj1pYTey7wcgAiEAoXvGutu5tJtmVAaET4KS1jLYXr%2Fe0OnI4esUX1EriHkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDAplRIsl7X1cqQfluCrcAy82ncL%2Fr38hO%2FrZvSxeVtUuoJycP1pWJsroV4%2FgdiegTXArLBOYUdCCQdXvOTHWEIcP4pOKyTa77TOHTRtbIRe7OqZJJm40oN99J3d45eXrt2ABZwo%2Fn3GHG4VGa5H8hPUCbxW%2B9kfWKgOSKTOUOxnbydik9GHrfEU37Diy2q8pahOx6krpTGxy4IZ0w6kFnsemdtPDyRmYTOCmD%2BxbRhGzTm%2FSbiWsfdH1bYirwoCMtFKQyEzDRDQk6O2Yfu5LB8HSN7EX69ntIv4UGV0%2Bx9dM1vw0teL9SJ0oGiCEijA%2B%2FulXXWeKSWLyVTCq7TSTXNeaApHg78KwPOARuyNB8lCDESmf3uLr1%2F0AA2ldVgesSsU7kfuhGJV69PnvJxFrtjW6AHL3ykvb2EjIK8nWbTuIB7ArRKtE8S9PHnaiEXxFItWaEFiqMzeeQm3tPKJ0OTUIi93nXiUllicx8FtfvE3IeIivA%2FVDXLH26T1DHI3YP6YpYVBqPOacYUCe4yu4STwuxyfs5Fr8XTtkHeMFOY%2Br%2F03mK9EXktjrzuAwsjD0KH%2Fv311u6Xs7%2FsMJvNVGIQnAFFZDuucneXbaFjskLx%2F%2F%2FrzHp%2FBXRwYz3bdNxG%2BHu119BSgvz3vcwVrzMJaM88kGOqUBe7VRhZswW5cf9sXOmYvaLJO4SkeQThukEbfywAM1bcq1jwOserS9HHBbDEtjGikpARfw1iLUotZuSdi5o8nzoUoQudS7divh0ehLxuHan%2Ffl%2Bkhbv9tXJhAYl4cKnV7SN9CKOUiI0iFiUwzL6NIVp8BxEcZojV%2Bip5SSkxJYlW3MFYRkxtWCZ56hWhnkWrfdqM6D6REmJMN%2B6jh1z8tyDLnOxX06&X-Amz-Signature=3e9e3b917f41a183ff7dc5ab8b8d6ff63e66d4d6134647d20ed6b659e67cd768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



