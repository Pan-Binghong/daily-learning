---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QB35BTP%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIHNdKLM%2FF1BSrIFIetvWTKgCHAI8T%2FuCq9lteoHy6E%2ByAiEA6lCjsoFuyfH1XZUGyhmL8CzoObvrE4baHHQc12rpbUUq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDM7JH%2FCn5V0%2ByEecFCrcA2Pcty78ZsOCe6wTUzkNY7kWRIhx4Yi6DHOvS28xRE7VwHE6Zk%2FMiSiwj%2F2R9Qjqjzsc0fi52PQ4xn3BY35UJ%2FjI6aYQiH1GXapE2Te%2Faoywk95HATzWMhtslxZeWbggNFHHCkcTi5C%2FhErqzJT1oH2m8%2F56q9Ex7wz0rZARkjsO4G4FsZ2GTrMmK8w8xuoWDtjLU%2FPzETrGAFxS0199Lqv%2BjHnyK3yiDoIijtFUt7Z3uqdB50ijmx4PIhg4zrZDq7qLZZ%2FKn4t2oSGcCT6Y5mBx39EZU%2FxJtoFzJvIk9M16VXeLhEHfQqwuquoVkukLLHyqzsdqmrrIJ2x%2Bf9hjZEKb8aaL13JSP4NoEYCq2wNFGtwfWNfNDtbk1B%2FA2BsQNOAaTtHTp%2FQntBcGEQq6Y0Us8zUpbKF5Tzygwzlj4yOI4D5UBpC0ypxtS8fgqlBNH0N5uH2Kt9c0MHoYBo741mEKEFtz2WNsZW2PtCdmgB0ijTxNlPddgp%2Bj%2FhreKWvatl37ZteCpaEL1r9g3BY31z45EbxXm0%2F3yyZvpkQuwTcwkYhQeGRQEK6Vk1reWW5%2BiSsfcfifIwYPQJ0AF%2B5OXnaK2O6Gn5uf4RHJRuyfIOwdf4oOowctcp4EdHDlMN3Uw8kGOqUB9GTFgrKzca8qbzLw1qZ8Z0pmk4VusRkDbUZDIm0hU6zGcw4hC%2ForLpAsFDQTpT5PYRlXx8JOJYei%2FAJSdWB31r9LmWqf7%2FH85w4cVfmSWA4dpS3cgoGElcNZ5JOODfC04nRvtueqARkIvYyX64kAe9LLzynF91Xv31ScKOGBhUHrxlfQzQPRsQd3Sz5cE4wv9NSw4Zg2n7N2Sb7HhURLoFrvOO4x&X-Amz-Signature=1a5f37068923d3816ce07e6a8819a5bca86d1e24c11793072da5a4df70a2c898&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



