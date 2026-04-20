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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SEBKOT%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB8UGwkaocDojc6AoGMK2ugTpKIlVsbJQLkdWDuj1c2CAiBghmuS2M%2BQ3STBd%2F5VP5%2BMHofuQEpSKpHD5%2BlY509%2FJCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMuYkXf3vg3QlmiAI9KtwDahsnLKudPhLZs0rPVqND3FunrGYA7HXZ1AL03hVRm1fKk67B0M3vvKy3UniKqONfrYaoK1WC4gXvY6RFdpTmveABRYwR0aZEqREWckDKs7TzjjY%2BMyGTOwEQEotchWIQm%2BtjPp6K7eaWwF8hHQZvo3KDm2aCemtnbrLB9LxTWPJKnYycqczRvdTEIRWsHeRCNVHMnzBiWwIjZhJ1ic0pZBMgJ7suYxn%2B%2B7tnsJtpXOZ8Kmir8Lg9BxoGgYcbOL%2FDUpycEKohUJAuKV8%2By2Au06PzbxW2euG0GN8EnVpfh2eY6RsdUo7fdD%2B73j0kfOM68rows%2BJrf0%2FgSy2ZflEXLSSw8Gx1JFxWo4nLeY6%2Fj%2FKVPWGnq9nrK9LDeviC6tSh6%2BoFDded%2BZhnw6V%2FFLd%2BnHykt6ldzueeXL31%2FM7kuY%2FEYKYJn58zu6XGNHZsy0OZSjf0tBylrkUW1e3cWUdXkVSnDgTTQ4IH7K4ZCrz6LTJ%2FkPLEI7ER6R4c4Xr9okVcHoxoUlw8Ki2uIMhWFabD3%2FCPODOMces%2FDMngvRxW5oXS%2BzsuyY4oVCe3Xsd5on2ydpaDnexp7scNIIHT2F5zrN5jDf8Ps%2FjAK9ooZPFC%2FJsVu7VMFSc1vmBgAiEwjZeWzwY6pgGM7VeH4Hf%2FtOnmaZOWZLBktDTuGC8DHuYgv0XyoGbC9QyA5CAxbyNftbl9NrFt%2Fnii9iaVu%2FnyjuJK1ikZAsFlAHF0UEVPimhfLC068LX6n%2BuueA%2FJm%2FKOL9pzmMvr6TASTKQp0NHYR0ReHFHVbb4SjZ%2FzKs6VVSqNhGyeXmAEMAATtToa7O3Btb%2B5fbqg9QJcT2FZXwUN4KQs3YEA4zl71EaPiCBg&X-Amz-Signature=1750cfa0008804818387f1eaea8bff84415db577604a988b1d4f460695c4b1e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SEBKOT%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB8UGwkaocDojc6AoGMK2ugTpKIlVsbJQLkdWDuj1c2CAiBghmuS2M%2BQ3STBd%2F5VP5%2BMHofuQEpSKpHD5%2BlY509%2FJCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMuYkXf3vg3QlmiAI9KtwDahsnLKudPhLZs0rPVqND3FunrGYA7HXZ1AL03hVRm1fKk67B0M3vvKy3UniKqONfrYaoK1WC4gXvY6RFdpTmveABRYwR0aZEqREWckDKs7TzjjY%2BMyGTOwEQEotchWIQm%2BtjPp6K7eaWwF8hHQZvo3KDm2aCemtnbrLB9LxTWPJKnYycqczRvdTEIRWsHeRCNVHMnzBiWwIjZhJ1ic0pZBMgJ7suYxn%2B%2B7tnsJtpXOZ8Kmir8Lg9BxoGgYcbOL%2FDUpycEKohUJAuKV8%2By2Au06PzbxW2euG0GN8EnVpfh2eY6RsdUo7fdD%2B73j0kfOM68rows%2BJrf0%2FgSy2ZflEXLSSw8Gx1JFxWo4nLeY6%2Fj%2FKVPWGnq9nrK9LDeviC6tSh6%2BoFDded%2BZhnw6V%2FFLd%2BnHykt6ldzueeXL31%2FM7kuY%2FEYKYJn58zu6XGNHZsy0OZSjf0tBylrkUW1e3cWUdXkVSnDgTTQ4IH7K4ZCrz6LTJ%2FkPLEI7ER6R4c4Xr9okVcHoxoUlw8Ki2uIMhWFabD3%2FCPODOMces%2FDMngvRxW5oXS%2BzsuyY4oVCe3Xsd5on2ydpaDnexp7scNIIHT2F5zrN5jDf8Ps%2FjAK9ooZPFC%2FJsVu7VMFSc1vmBgAiEwjZeWzwY6pgGM7VeH4Hf%2FtOnmaZOWZLBktDTuGC8DHuYgv0XyoGbC9QyA5CAxbyNftbl9NrFt%2Fnii9iaVu%2FnyjuJK1ikZAsFlAHF0UEVPimhfLC068LX6n%2BuueA%2FJm%2FKOL9pzmMvr6TASTKQp0NHYR0ReHFHVbb4SjZ%2FzKs6VVSqNhGyeXmAEMAATtToa7O3Btb%2B5fbqg9QJcT2FZXwUN4KQs3YEA4zl71EaPiCBg&X-Amz-Signature=a741e554ab3e4f717d1061713ad7211642426e2e92026c6c1344c2839acf570b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SEBKOT%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB8UGwkaocDojc6AoGMK2ugTpKIlVsbJQLkdWDuj1c2CAiBghmuS2M%2BQ3STBd%2F5VP5%2BMHofuQEpSKpHD5%2BlY509%2FJCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMuYkXf3vg3QlmiAI9KtwDahsnLKudPhLZs0rPVqND3FunrGYA7HXZ1AL03hVRm1fKk67B0M3vvKy3UniKqONfrYaoK1WC4gXvY6RFdpTmveABRYwR0aZEqREWckDKs7TzjjY%2BMyGTOwEQEotchWIQm%2BtjPp6K7eaWwF8hHQZvo3KDm2aCemtnbrLB9LxTWPJKnYycqczRvdTEIRWsHeRCNVHMnzBiWwIjZhJ1ic0pZBMgJ7suYxn%2B%2B7tnsJtpXOZ8Kmir8Lg9BxoGgYcbOL%2FDUpycEKohUJAuKV8%2By2Au06PzbxW2euG0GN8EnVpfh2eY6RsdUo7fdD%2B73j0kfOM68rows%2BJrf0%2FgSy2ZflEXLSSw8Gx1JFxWo4nLeY6%2Fj%2FKVPWGnq9nrK9LDeviC6tSh6%2BoFDded%2BZhnw6V%2FFLd%2BnHykt6ldzueeXL31%2FM7kuY%2FEYKYJn58zu6XGNHZsy0OZSjf0tBylrkUW1e3cWUdXkVSnDgTTQ4IH7K4ZCrz6LTJ%2FkPLEI7ER6R4c4Xr9okVcHoxoUlw8Ki2uIMhWFabD3%2FCPODOMces%2FDMngvRxW5oXS%2BzsuyY4oVCe3Xsd5on2ydpaDnexp7scNIIHT2F5zrN5jDf8Ps%2FjAK9ooZPFC%2FJsVu7VMFSc1vmBgAiEwjZeWzwY6pgGM7VeH4Hf%2FtOnmaZOWZLBktDTuGC8DHuYgv0XyoGbC9QyA5CAxbyNftbl9NrFt%2Fnii9iaVu%2FnyjuJK1ikZAsFlAHF0UEVPimhfLC068LX6n%2BuueA%2FJm%2FKOL9pzmMvr6TASTKQp0NHYR0ReHFHVbb4SjZ%2FzKs6VVSqNhGyeXmAEMAATtToa7O3Btb%2B5fbqg9QJcT2FZXwUN4KQs3YEA4zl71EaPiCBg&X-Amz-Signature=e3c36ede66122a58610806a6c781b3d1ed4582d8325dbda59ff31cce511348ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

