---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BXXE34S%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC36nv4%2B5E5Cs8ELMHjPqyc5OYtq2%2B24dcE9tc%2FY7GSjgIgJB8wnRUds21syiokzz29Tc1WmdIfvW8sSz5mNfRMQysqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4FdLgU3ZnVkAv9tyrcA6WCHyhdDRN0l1ixEYrqnExvPajd351CDqml2SND0trOo%2FSqIp4nimFo0rJsJRrG6NP%2BY1nIK3VCfpKZuYd%2F1ZwcuYhPAFY74XPT8TojyUtN%2BYK22HYETNC2MaldtJqWVIh5I5gx1ew5LGFA5Ms7X0nj8HiJyOw%2BYJtI6N6zD09QEJrCEwqaE8yVRVuGPf2HFnHonWT1AzGkm9gRxxagSYpAENIC%2Fr5IRRUVJj06DiEQWnQ0zVk8oxJNuF5LZLlznjkVp5MseHtU5%2B3%2Fgj6W%2BTEIVbsrVRJcIhLWGwyoCBwGN%2B%2FN7%2Fl4mX8D%2BE1DjiRwhtFukRU4JYXqGLSiJgDVgI3Cu%2Bisqo5PbTffGObUttOZGihlI9rluEYVGuHw4N3uGeWEeJsjshdrlotlmtjH%2B6PCrsWi4JGMvFaSN5FyMTCYt2zFSxL9F6hQiC105nqLzNmLctUMmJbrDq46sq2lmuAz6Ht26hQqFZogT3BZI8TWgLx%2BUxrawKQsGBwc1nM1pEQUA0SYrqJFeXBKg0yeMrjuWlJiIdaYch7x40hYnfLggDjpZesJtJeaT6MYxMoCoYMrOduIwSDRkyGvh5jbk00bkxPG7vm2omg7P%2B24hGzD4UGVg78ygHTVEkZIMI%2F90skGOqUBj1rDGHmIyb3%2FfZFLnYopS5qlY0ZxFfBZ%2BqqFadKMmn2agPY7A2dqFmnZoK40HzJ2Is8CX4kPn1%2FlbtcXsyFeCfZmVi406QieQ5gjv3hNPVdV97jo9yMlqrR4lYPCGk5hwv7XwTxzNQ9%2FNjYe7i%2BsyvRgCJL51gaBio0w5xMN1MZQUb8k6%2FuzU3abSINSyWBxzvH0XfjGJVf0SpTe1HRvNlMmcHJX&X-Amz-Signature=d19cb95b3f3819f4ab696b8a8346e7e78087858bf0b4e75f9800dab226a572c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



