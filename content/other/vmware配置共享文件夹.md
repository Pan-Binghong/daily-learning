---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUNQ35DN%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqIFJET7V0vBUwtAluqYR1gyr%2BdT0HW4SfmJEmW%2Bk6ugIhAJBplheLvaGk7fIxGXmiE6BsBIlxH7ZvtAqWVihpGUR9Kv8DCFUQABoMNjM3NDIzMTgzODA1Igwx38BChosyahxszbgq3ANPwq4C4BvJ2eUevPHrDn1u3vaXNBqiTmz9F5Zwf7o5jtSSv48E5rE%2BDSq%2BBL5MQnidm6HvhfWs9%2Fo6lbnX261%2Fi9%2Fu9zlL%2B9IQL3CgpgB1pfRyMcljb5p7dgacc6xR7htCoSE218DZNCVUkX16rurRC4Nm2msEmfsUusrY%2BN1AMS1dprWqdrUfR6haZXdmrGbjGx3YbArUQD48HOGk%2FDroAxUpL9FWc4x9%2Fmhz8UG8n1dyjJChdsDMOE0k2esbExFyJgR0KfMJAQ8I9DMVk1Q%2FAn0HDL25FaWn6d7CldYdCGTy2gujhAHYluIsGnm0%2FXM%2FRCN6nuIGAndrzQ6aaO6pxkXqYzpmj0dqsIwCFXnmg57gIbR36jD%2FMUI%2BJDNdeYAXNwIPubCsDUEF6fzPXziY6LMLm95%2FZZglVXRafgWeDAyDHpQOGKu9X8Q04zEiTW6AvLcznnpdcz9dq70tOIOa8FtvBFCJKa8olhl6G0XZ7NiUmrqaVmWxYUNPYL2wBsWrohfy3rEnzs4QYwSlN2fajUGFQue6Sf%2BoE0wUrHKapZLB6i7HkmaG%2BJtz5sG858Y2learcfSB4y1QlbKSxoLorWmr2XoIGH6fGmrgAujCgvW9muQZv1IGMNqvSDCKpezOBjqkAaUROxQ%2FM2sHnClIDqE%2FzUxncO2wY27Zh2pc4CyS4X0pdZ2oFO7LnfVXSUTMk0bvfMNfgEjZeB7ElQVZZWAJEDHdJJ0ZWujsvw6yzaWDvNcawfI1h2Zfto4B1%2BvJZf7hrT0EnAr7M1ZGwZpnt5q1mGS7Yobx7UzdizvCOR7utUCf3WhjCyTcQpvUhM70OiQ5mkMCe7Von0hUVuGfIxtHh%2BIVQ2ep&X-Amz-Signature=c838b1323c16c1c0928753066d44b044ed3855af57a1e6375977cfc6d31ce3b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



