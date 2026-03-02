---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RU5AQXO%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIFKY22ro0cIQW%2FYezoL4dzCMBAadwOXpksolXJMHI7AiEAvYEq4gjSD2KbSW0G8UIwxDonrC7dSStk88GCIK%2BU62Yq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDFfJ0E4PAvuEHc8PcCrcA0UmBice38RW1G7%2Fxca6FXEh%2BMhKoItrtaKDL4tFn4DQd4VLAj1CQfiR6VelopdFzA6btMZ9BVJkJHlpFajOLksA4ltqn87SBj%2BT%2BHnet7L5qCj4bXWEFSw67ajpxSqL1PWgsocfFIGJ%2FuUi24RRmR6dYPCKrvZ0sE6U5yxAt2w3gF%2FADMIF1lQ%2Fp4UAM%2B9wcLqEvL0DpgNUOFL1tAMcYvUfWOpgdeQ7a%2BBMJ3EcYk14DWe0CepkjsG8GRNykcji3fxVS9v4TQWvNCBn6ezxJgk6a31YCsHd%2BSRjNXLf2BXv2sNy%2Bq%2B1mwEwpFI0zi72JPaMPQ1Wl7qBx85xGZ1RWmyyu8pdHYLl0N6wbBAEF%2FJMQmIxhkAWapmhmOQ8V6qlETathcJYOrk0%2BSo2WEetvMuFrTRYqaOPEYmbUEu8F9ctXJG%2Fg30RKf5XrIhR6Wm0gZjUa4KKl%2B6qiptD%2FBKClFjVSFDTUBJjCGzqAqGU2s77RTIRqSDHnhgRpQSEWB74WtURhYkW%2F%2BlFdBke4k19nHsKgsoLTMHyMOq%2BObJ%2F5R4YeJGIL0D23kQOFJ%2Fs1vzCriP81n7Gixeq0nmDEkcoeDoLc3r7fqvTM4%2BDKEe%2FHXJ6YDzOXlbkrTJ6sCfTMPX8k80GOqUBRhBP0uMEMvliDYaitqHSw%2F8yNhqathh0lSpqapOrtzk8%2F1CEKkAgX8PTxNCeAugPxnlaiufcjDcZUiRVh78efPkUORhr4cU2NrqXUjo%2BfvECeGRqp%2BENfPXqjaYyS0Qn7tWSUGkqJgOEh2p7zaqZkEzc9S4LW6q9eXbvhCiGHqq0kU6eFOWK7vtwFvBIl3YepoLlXZSBuDJuxuCY9ycEW4i0anUT&X-Amz-Signature=9ef24c0cde94e2838733c56355422ad7975d6c3d354e215a8ed82d6434c95ded&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



