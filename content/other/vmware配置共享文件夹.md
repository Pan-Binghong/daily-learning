---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664IM2TMM%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaBh9hRdSNTdTiq02El7oJCnx78h%2B6SUVr17fjb4E5twIgd2cor9WgXr5bgJ5ELdJW8boDkX2ERSjH%2FlLdNEXAipkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFkLOc8Wzob59EHlNircA1euwCWDHg2h%2FQJuFVm%2FyeyHoqU3GZJ34NFoz8QWNp%2B%2B1VhKfvXZ%2FghZytYtK3A5QzElFYq%2BVsp4yejZjvUqZy2bCcKlGgy4RESBdLkcUQaTdDyXijmaFpD4axMd9UYuyaB0J3E4dT49uDbbdRJon9WUnGqOSehVrSQEphDOnYwoQnVZqd9l4HYc36FFHYJU%2FCfSY5D5ewS5Qvf8zAgFmqpT7j5nohg3BT%2BbW8EbA09v7XgYfpSfw9QuRHw0jqvtupzYUIczD7ijiyKp9vaLObC%2BNndoMC75lq6ecxZ0hKqv8vqaJVJ7T1mXJJqF%2BSUL4jm9%2Fks5cIOAd2SKtkM1QYUA%2FJ%2FbYhbIRP7TkRQrcSMBh57JE1euwC%2Ft%2FqfVVIsPczHDBXAV4M%2Bjuy5E3IOY5h8OWnIDX2CX5d9D1yDbR0bAWJ%2BRy0fa0L0lLuxqPhm4LVTwHQEzBVLRwmEAa%2BBvbPcuwL%2FTaWeq35P4E3djkk9ejLnrYB%2FmiTreNVpJXny7QrHOQZJIdGUinYeY%2BjQ3LrBb6c8TLLk%2BtdExVvFNHFZI2X4XIqSrA3L0VHKMmbXIUG0SWuLfExcp1R6ulbkFwwZgik%2FZZ1n%2F0y4gOmHAc%2F9ZAIz7WyehykH0J6vRMKuXpcwGOqUBTIxJ5qX6aik45RTJgaDMyKWUHVqQm3b2KSWhDicSNYNdnmPCazwGi4VoFOtO%2BLGT8v5eoA2fv%2BYT6SL99cSRkAmuMvn7TOCK1mCkl6KFTMMXs5%2F8UQEXUPKv7AlqvOfsS4V9k45n1JVuzHRP9LbPS4wwrvF0Z3Y9JsiK40xJgusmpthxDaYhfE3j6nQN9B19%2FKGO48gE6gErSSbj3rAkcvn83Sjf&X-Amz-Signature=6439c5105e0d415cf902e2079de915af205073febd65c7a890af03ab27aa91a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



