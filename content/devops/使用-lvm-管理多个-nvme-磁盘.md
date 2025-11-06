---
title: 使用 LVM 管理多个 NVMe 磁盘
date: '2025-04-03T02:37:00.000Z'
lastmod: '2025-04-03T02:38:00.000Z'
draft: false
tags:
- Linux
categories:
- DevOps
---

> 💡 本文档将指导您如何使用逻辑卷管理器 (LVM) 将多个 NVMe 磁盘合并为一个逻辑卷，并将其挂载到 /data 目录。

---

## 1. 安装 LVM 工具

如果您的系统尚未安装 LVM，请根据您的发行版执行相应的命令：

Ubuntu/Debian:

```shell
sudo apt-get update
sudo apt-get install lvm2

```

CentOS/RedHat:

```plain text
sudo yum install lvm2

```

Fedora:

```plain text
sudo dnf install lvm2

```

## 2. 创建物理卷 (Physical Volume, PV)

为每个 NVMe 设备创建一个物理卷。假设您的 NVMe 设备分别为 /dev/nvme0n1, /dev/nvme1n1, /dev/nvme2n1, 和 /dev/nvme3n1。

```plain text
sudo pvcreate /dev/nvme0n1
sudo pvcreate /dev/nvme1n1
sudo pvcreate /dev/nvme2n1
sudo pvcreate /dev/nvme3n1

```

## 3. 创建卷组 (Volume Group, VG)

将创建的物理卷添加到一个卷组中。在本例中，我们将卷组命名为 vg_nvme。

```plain text
sudo vgcreate vg_nvme /dev/nvme0n1 /dev/nvme1n1 /dev/nvme2n1 /dev/nvme3n1

```

## 4. 创建逻辑卷 (Logical Volume, LV)

现在，在卷组 vg_nvme 内创建一个名为 lv_data 的逻辑卷。以下命令将使用卷组中的所有可用空间。

```plain text
sudo lvcreate -n lv_data -l 100%FREE vg_nvme

```

## 5. 格式化逻辑卷

将创建的逻辑卷格式化为所需的文件系统类型。这里以 ext4 为例。

```plain text
sudo mkfs.ext4 /dev/vg_nvme/lv_data

```

## 6. 创建挂载目录

如果 /data 目录尚不存在，请先创建它。

```plain text
sudo mkdir -p /data

```

## 7. 挂载逻辑卷

将逻辑卷挂载到 /data 目录。

```plain text
sudo mount /dev/vg_nvme/lv_data /data

```

## 8. 自动挂载

为了在系统启动时自动挂载逻辑卷，需要编辑 /etc/fstab 文件并添加一条新记录。

打开 /etc/fstab 文件（可以使用 nano, vim, 或 vi）：

```plain text
sudo nano /etc/fstab

```

在文件末尾添加以下行，确保文件系统类型与您格式化时使用的类型一致（这里是 ext4）：

```plain text
/dev/vg_nvme/lv_data /data ext4 defaults 0 2

```

保存文件并关闭编辑器。

## 9. 测试 fstab 记录

测试您的 fstab 配置，确保没有错误。

```plain text
sudo mount -a

```

如果没有任何错误消息输出，则说明您的配置是正确的。

完成以上步骤后，您就成功地使用 LVM 将多个 NVMe 磁盘合并为一个逻辑卷，并将其挂载到 /data 目录。请务必在操作前备份重要数据，并在非生产环境中进行测试。

---

