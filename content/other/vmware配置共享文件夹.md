---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZZFJXYF%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPLfGPA7ZXA%2BkIoxKKADBNWXlxuLEQDoRn2SikuWm8rQIhAKtNViqou7JG6hP%2F9Wsn%2F6y9PsCKPonYYBHmnxregoV6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyq4DY%2Bn4jpMOLQ9HIq3ANa6TRwA2bKkh4cZ4XydQRlgf94hOFlV9SohdEo72oLKqZAwvM0F0udc3iYOZIYqVObUtBlFOnrYB3KZgRsN8%2BIPCG0Kq4mBH1Qsvu5C3GBN1JPpkDm2H9aJHeqYMh0lJ3RAO13sJ%2BzyOm3Zd72b07KE3r24guVxZVCoTETj8JheUo2KfvMmEBCu%2Bgxq2GznRD4soAMGoBNYSP27bCieJ3RzBGayoncvFEZRJO%2FJLKDE6J3MLiaICNxsddLuST%2BNPSpWN8UQNGKnqH3UIo8ZRQgWlslHbWE23agDEgHHoTQvAsoUzBsXW1YITcKP1%2FVsSZa12%2BdGNj5sqybz50Gz0F3WlHoNnpL6CgAGx3hTPb1wRXJM9pSM7mwo%2B6f4M%2FnXSpufKFL9%2FyXNWufZHgksW%2FDnzzsaLuwe2MW9NMWlkCrwwTvCoOzJltfcnfgFhdKxKbh%2FIhDmIHM0NZ%2FPzKSHxWtzFOlHGBPW5isyxu8am%2FkJ5P4hoHLPgSrKWOtO4EqvyFs7k4Tr5ZZEPfXAHkNlDl7hDnlltQaB6XmbvFaUT8qLQq5g0tuR5xxuAXsTfuaFfonli1wWYCtNtfi7dGEETYircQAMcnvjUtzX0K0y8N3PM73vZ4STXWtkZ0OjDDAyY3KBjqkAYtL%2F7VGxiT7hvCPsx7UK2VI2l0bHs%2F%2BtRDqO%2BxL8Vww15SsBDMzayAky9zLEUum%2FsFLje8Rsebz5G7a0sITZQQNnn6iZpheIz68FTMdfWukH1my5X94wF5ag%2FNR9yPpxEyU9Z13NpO%2F49pCvco1zdGWbna17bt3qgBsuGQ6PyIcit7LlPpAkDfWWiZyMo9D0SqsPg2xwGKJE%2BFtXyhlrWvWkiTS&X-Amz-Signature=33f0cc84fa05cad91e879de311c8aaac334e960ab36e76356001e9cef5ab3c8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



