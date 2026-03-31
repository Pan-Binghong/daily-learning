---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUT4N77C%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCRKk8Dn2VdvcwyOCpgYgXaAxi4ksz0eV%2FYe8pxIWQPwwIganclv%2BtqUQlnpl6CjHUeFj%2FNVOAUqftVeOu8N6TIn9Aq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDB3LY4QyEu4wjwblEyrcA5riDRBdumAp4cMWaSM9%2Bgyi%2BImpgl8WawCzDQEUY5qoes9DwoM0YVWMMKxgiScKCkSc8SbbN16lpTdDl4IwoW0wPaqArftlS%2F5iVQa0FaO9%2FnKQd6GAYISrNU7%2B4ZZLMim39XfAanWLuKur342IDO%2FOrx5bCjNuRr8BeaKqdYtwfSAma3bnaUSeIZmwq2DHzvMLI3i%2FpHUPDeP8046LBljAIiNB6tfrMG2NVb%2FnMke%2Fd2SsEESeXuYqbPO8DQsPtGVzS7SC6uVPtKqzI2CUCUHi8fyhXgy7I2ERiHwDLWz24Jv8tmapKLr9gQ%2BT6CK78PnjvTCaM0dcgfUHr0v0yhRYT%2BqRILYTMmqJ4HCj2FwSkTxTdJgDb689bIN5rnPUjejwSdZ3QlG8s9npVSnkMCTBWuTvZ6fu30r4IjnZxM3%2FP9bQPWegLMJQsAkuuJX%2FFb48v7Q0RXZz45RQgcaVyLDM14ZX63rfLt4Jt4IhEL2uY32VRnYqzIr0iUZax1gy4B4SrQTNdO6LeiKlsjav9otccg4tzbGHx9C7rYT7TZPj5MIjjcvMHf1wVCk%2Bg7oM05a%2Fda7NI3eD459kjQP%2BxtbAMT7pgsGJP1yrRCBAX%2BOVzykEx3J31RW%2Fx9xfMLvwrM4GOqUBQDylYx7w43RpvEW2wXaA1wTuRf5UeuRsG2J14%2Fllh4WHj7RQ9YA6Ios7NJhYejxZqAAvS%2F3FKVzhFqWFEzjSbkXF4mFZbgkLdzNJwWzNRHAto3q9oEawT5Y%2BbZOBWSOfiA%2FxgT6D%2FtUE4%2B7t1D%2BzlpZECkElt9uFNS8azuaX3KTHoJqEik8q3ncGKEjSE84IKexxwg9o%2FElBS2sx4PE6Jc4IUF%2Bf&X-Amz-Signature=e8433d4fb55cf2b2dae8de6a9299eb7cf7ce3ac998a0ead694e888492ed8075c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUT4N77C%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCRKk8Dn2VdvcwyOCpgYgXaAxi4ksz0eV%2FYe8pxIWQPwwIganclv%2BtqUQlnpl6CjHUeFj%2FNVOAUqftVeOu8N6TIn9Aq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDB3LY4QyEu4wjwblEyrcA5riDRBdumAp4cMWaSM9%2Bgyi%2BImpgl8WawCzDQEUY5qoes9DwoM0YVWMMKxgiScKCkSc8SbbN16lpTdDl4IwoW0wPaqArftlS%2F5iVQa0FaO9%2FnKQd6GAYISrNU7%2B4ZZLMim39XfAanWLuKur342IDO%2FOrx5bCjNuRr8BeaKqdYtwfSAma3bnaUSeIZmwq2DHzvMLI3i%2FpHUPDeP8046LBljAIiNB6tfrMG2NVb%2FnMke%2Fd2SsEESeXuYqbPO8DQsPtGVzS7SC6uVPtKqzI2CUCUHi8fyhXgy7I2ERiHwDLWz24Jv8tmapKLr9gQ%2BT6CK78PnjvTCaM0dcgfUHr0v0yhRYT%2BqRILYTMmqJ4HCj2FwSkTxTdJgDb689bIN5rnPUjejwSdZ3QlG8s9npVSnkMCTBWuTvZ6fu30r4IjnZxM3%2FP9bQPWegLMJQsAkuuJX%2FFb48v7Q0RXZz45RQgcaVyLDM14ZX63rfLt4Jt4IhEL2uY32VRnYqzIr0iUZax1gy4B4SrQTNdO6LeiKlsjav9otccg4tzbGHx9C7rYT7TZPj5MIjjcvMHf1wVCk%2Bg7oM05a%2Fda7NI3eD459kjQP%2BxtbAMT7pgsGJP1yrRCBAX%2BOVzykEx3J31RW%2Fx9xfMLvwrM4GOqUBQDylYx7w43RpvEW2wXaA1wTuRf5UeuRsG2J14%2Fllh4WHj7RQ9YA6Ios7NJhYejxZqAAvS%2F3FKVzhFqWFEzjSbkXF4mFZbgkLdzNJwWzNRHAto3q9oEawT5Y%2BbZOBWSOfiA%2FxgT6D%2FtUE4%2B7t1D%2BzlpZECkElt9uFNS8azuaX3KTHoJqEik8q3ncGKEjSE84IKexxwg9o%2FElBS2sx4PE6Jc4IUF%2Bf&X-Amz-Signature=3fa6212a1c051338ef6cf1ba68f21cb8442dcf4b9aabdc52e4d29c413f14a128&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUT4N77C%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCRKk8Dn2VdvcwyOCpgYgXaAxi4ksz0eV%2FYe8pxIWQPwwIganclv%2BtqUQlnpl6CjHUeFj%2FNVOAUqftVeOu8N6TIn9Aq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDB3LY4QyEu4wjwblEyrcA5riDRBdumAp4cMWaSM9%2Bgyi%2BImpgl8WawCzDQEUY5qoes9DwoM0YVWMMKxgiScKCkSc8SbbN16lpTdDl4IwoW0wPaqArftlS%2F5iVQa0FaO9%2FnKQd6GAYISrNU7%2B4ZZLMim39XfAanWLuKur342IDO%2FOrx5bCjNuRr8BeaKqdYtwfSAma3bnaUSeIZmwq2DHzvMLI3i%2FpHUPDeP8046LBljAIiNB6tfrMG2NVb%2FnMke%2Fd2SsEESeXuYqbPO8DQsPtGVzS7SC6uVPtKqzI2CUCUHi8fyhXgy7I2ERiHwDLWz24Jv8tmapKLr9gQ%2BT6CK78PnjvTCaM0dcgfUHr0v0yhRYT%2BqRILYTMmqJ4HCj2FwSkTxTdJgDb689bIN5rnPUjejwSdZ3QlG8s9npVSnkMCTBWuTvZ6fu30r4IjnZxM3%2FP9bQPWegLMJQsAkuuJX%2FFb48v7Q0RXZz45RQgcaVyLDM14ZX63rfLt4Jt4IhEL2uY32VRnYqzIr0iUZax1gy4B4SrQTNdO6LeiKlsjav9otccg4tzbGHx9C7rYT7TZPj5MIjjcvMHf1wVCk%2Bg7oM05a%2Fda7NI3eD459kjQP%2BxtbAMT7pgsGJP1yrRCBAX%2BOVzykEx3J31RW%2Fx9xfMLvwrM4GOqUBQDylYx7w43RpvEW2wXaA1wTuRf5UeuRsG2J14%2Fllh4WHj7RQ9YA6Ios7NJhYejxZqAAvS%2F3FKVzhFqWFEzjSbkXF4mFZbgkLdzNJwWzNRHAto3q9oEawT5Y%2BbZOBWSOfiA%2FxgT6D%2FtUE4%2B7t1D%2BzlpZECkElt9uFNS8azuaX3KTHoJqEik8q3ncGKEjSE84IKexxwg9o%2FElBS2sx4PE6Jc4IUF%2Bf&X-Amz-Signature=42bb9dd1a45d204385872e59aafc690eb026f066773c51fa3a9d9449390c8842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

