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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U5CB35S%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFroysswQQi5BhjCKT%2Fg92ku5HRHGuNl1uvAvQghkH6LAiBmiwgAKx%2F4j7KBwztcF17GvsJ06St%2Fl5QHWHDUsL85hiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM65%2B7tj59aCtWltL4KtwDDo4MpyBEmsRQ1OPoETw14Hfdel4IhNSoRDjDX1jU4b%2F3XdjuKZvimIucj6EdAJkp2gvlud4itoRipqdNwEW4PxAOVSjsGj0Fyr8EPg95c4wky8My18Ts14MzF43LGeNq%2BkNAIhf6U%2FLohO4poZcbHacduq9zOZyliC4dEXomiZ8H0%2Fwxw%2Fcjmbna58y0lkqqoem1Q3cYyQOLCUWYtJbiaOm7g1NvaF9aDDaXbz%2BeJC2MioPWLA7pN3QrbB9WcTmJ5%2BvrFQsSkZ8duUEybrs9Ye00d7JakI%2FBIDpDeJojuSy%2Bh60dM5MLJ3DCSxGOQfzqjOB%2FvPRYXLu%2FRd9i7T1gmolwK8y35jOyOhLejxaiwrpPjrapd7RGFFBnOEsD%2F4mzRvpRHD%2FDIGe9q6%2B8Ljgjefg2jamwJgA8PGHW%2FBlSpnVA0KaZ14tXDwhb0ksJWqjPaOFhhWhhb5e%2FJYPTtX2OZV8ZNJpgHipKvzJU2gte%2BeTsc11eu%2FUNJ4D2PN87MveD8hXHzO75mFYcKW6YO20cuzLSPoLyt4N2IGgOt7XiGQVb0sPb50t6%2F5z5RryMHGu8QeIjkruVItIM02fR60K1dWETzpPlqsgSpfaxKKQE1BSe8SGxpuTY3Q7a1okwzLm6zAY6pgEUwrgxAR8Gm%2BCywZeF6nbBaU%2BsCQSqtdAjDRZ35KtUaoj2gjcHg8HKA05O%2B8V3h8s1ATS4s18dzTr9gdfP6lEb3mtNiDNcNE%2FiXgy784hIGtHkYqiKUdYr%2Bkz0MDkQ9b4%2FWqyWOMJv4RWxE6IuYESvxMAAJdwi%2F4gbUZpIxYLAiIFRL%2Fof3YIJ%2FnPuO3qlqqfHeZUjvAA%2BxLXjwt66HDX9ED85QqlZ&X-Amz-Signature=7024ba1a9f56423bd47bc89a18e1442e2769b8ab477e570c9f72f7ffc5be7c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U5CB35S%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFroysswQQi5BhjCKT%2Fg92ku5HRHGuNl1uvAvQghkH6LAiBmiwgAKx%2F4j7KBwztcF17GvsJ06St%2Fl5QHWHDUsL85hiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM65%2B7tj59aCtWltL4KtwDDo4MpyBEmsRQ1OPoETw14Hfdel4IhNSoRDjDX1jU4b%2F3XdjuKZvimIucj6EdAJkp2gvlud4itoRipqdNwEW4PxAOVSjsGj0Fyr8EPg95c4wky8My18Ts14MzF43LGeNq%2BkNAIhf6U%2FLohO4poZcbHacduq9zOZyliC4dEXomiZ8H0%2Fwxw%2Fcjmbna58y0lkqqoem1Q3cYyQOLCUWYtJbiaOm7g1NvaF9aDDaXbz%2BeJC2MioPWLA7pN3QrbB9WcTmJ5%2BvrFQsSkZ8duUEybrs9Ye00d7JakI%2FBIDpDeJojuSy%2Bh60dM5MLJ3DCSxGOQfzqjOB%2FvPRYXLu%2FRd9i7T1gmolwK8y35jOyOhLejxaiwrpPjrapd7RGFFBnOEsD%2F4mzRvpRHD%2FDIGe9q6%2B8Ljgjefg2jamwJgA8PGHW%2FBlSpnVA0KaZ14tXDwhb0ksJWqjPaOFhhWhhb5e%2FJYPTtX2OZV8ZNJpgHipKvzJU2gte%2BeTsc11eu%2FUNJ4D2PN87MveD8hXHzO75mFYcKW6YO20cuzLSPoLyt4N2IGgOt7XiGQVb0sPb50t6%2F5z5RryMHGu8QeIjkruVItIM02fR60K1dWETzpPlqsgSpfaxKKQE1BSe8SGxpuTY3Q7a1okwzLm6zAY6pgEUwrgxAR8Gm%2BCywZeF6nbBaU%2BsCQSqtdAjDRZ35KtUaoj2gjcHg8HKA05O%2B8V3h8s1ATS4s18dzTr9gdfP6lEb3mtNiDNcNE%2FiXgy784hIGtHkYqiKUdYr%2Bkz0MDkQ9b4%2FWqyWOMJv4RWxE6IuYESvxMAAJdwi%2F4gbUZpIxYLAiIFRL%2Fof3YIJ%2FnPuO3qlqqfHeZUjvAA%2BxLXjwt66HDX9ED85QqlZ&X-Amz-Signature=5a0b06ba6fd65c2f486218f0389f404e9c9fe8617d4c461054a377f62dd6579c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U5CB35S%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIFroysswQQi5BhjCKT%2Fg92ku5HRHGuNl1uvAvQghkH6LAiBmiwgAKx%2F4j7KBwztcF17GvsJ06St%2Fl5QHWHDUsL85hiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM65%2B7tj59aCtWltL4KtwDDo4MpyBEmsRQ1OPoETw14Hfdel4IhNSoRDjDX1jU4b%2F3XdjuKZvimIucj6EdAJkp2gvlud4itoRipqdNwEW4PxAOVSjsGj0Fyr8EPg95c4wky8My18Ts14MzF43LGeNq%2BkNAIhf6U%2FLohO4poZcbHacduq9zOZyliC4dEXomiZ8H0%2Fwxw%2Fcjmbna58y0lkqqoem1Q3cYyQOLCUWYtJbiaOm7g1NvaF9aDDaXbz%2BeJC2MioPWLA7pN3QrbB9WcTmJ5%2BvrFQsSkZ8duUEybrs9Ye00d7JakI%2FBIDpDeJojuSy%2Bh60dM5MLJ3DCSxGOQfzqjOB%2FvPRYXLu%2FRd9i7T1gmolwK8y35jOyOhLejxaiwrpPjrapd7RGFFBnOEsD%2F4mzRvpRHD%2FDIGe9q6%2B8Ljgjefg2jamwJgA8PGHW%2FBlSpnVA0KaZ14tXDwhb0ksJWqjPaOFhhWhhb5e%2FJYPTtX2OZV8ZNJpgHipKvzJU2gte%2BeTsc11eu%2FUNJ4D2PN87MveD8hXHzO75mFYcKW6YO20cuzLSPoLyt4N2IGgOt7XiGQVb0sPb50t6%2F5z5RryMHGu8QeIjkruVItIM02fR60K1dWETzpPlqsgSpfaxKKQE1BSe8SGxpuTY3Q7a1okwzLm6zAY6pgEUwrgxAR8Gm%2BCywZeF6nbBaU%2BsCQSqtdAjDRZ35KtUaoj2gjcHg8HKA05O%2B8V3h8s1ATS4s18dzTr9gdfP6lEb3mtNiDNcNE%2FiXgy784hIGtHkYqiKUdYr%2Bkz0MDkQ9b4%2FWqyWOMJv4RWxE6IuYESvxMAAJdwi%2F4gbUZpIxYLAiIFRL%2Fof3YIJ%2FnPuO3qlqqfHeZUjvAA%2BxLXjwt66HDX9ED85QqlZ&X-Amz-Signature=5919579c32a3a30d7a20fe142264c1e1d4330835c95f875325fdcec7fcb8f737&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

