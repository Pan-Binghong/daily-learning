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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIBOZEHC%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDPJ3jb7uGDXDdO0eQUBw1rsvp1ZZO9lDH0Z6%2Bvhf9p7gIhAIcVutrXyaDrcSkyP2ez9V6OIoeqGic9txtypA%2Bl4JAuKv8DCDIQABoMNjM3NDIzMTgzODA1IgxuPbZ9BZCe5p1hG7Mq3APEl0FBylQvY7hGczMqnjK3%2B3Yrxhdc54pjpAZ%2FEGbigjYDo21Q4GLylWQsTSP5pbcc2yYfizmPLMeaIIidhf948y1vjBQx9No6BX6Yu0pzcKaDc4kPV%2BfF5IqIOD6NG4gR19UczfXmHJKHIGHaadrYfEeoORH%2FaK07KDMsxh%2BPpHvfOZQNRW4TKZ00R%2BxLgnsa8lVrAN6HDkEsWpmirniq8kdnTJP5X1G7h4l1NwqTtDDHREWXkRMxmeSuGNXpmPJJV%2FyjoZfFCDuMtugnCdoaZDTA8ddydNhEN2ImdWvm%2Fu%2FjA4PKPkMy7vVDHxxIJmFYKl7V9UaUJo%2BVvJxggYEODH9G6h%2F%2BwqUQghJBr58wf6jPUL2CLzoS3DX8pvPMIiMlCzOJgekcct%2F%2B47eLkPkupUGi%2BFiHd%2BEJXKUPuMdEY6ep7b0PmpRMgTZ3zs50ZtxfftX5LGiPqt8nxMoKN6bCJWnn0FPWV76clhGvQqeLKaL3dvKymqAwk03vQOZ7%2Ba%2BAT43bWqsBPV84LgHyB5xnHvkO5YZRrS22uXXW0uJ%2Fntn%2FT%2BY0pH3%2F4oACsh0XG3wQmXvDIOfK%2Bhrfg2Vx6z3%2BxfW0crykyV1UNTq3Tdgy2WM5YfN5nHupYXGmyTDysInJBjqkAYI7G8TKPBm5k04AY5PUNoG%2BfzHAJWy262dmSq9qKacLDwXmnq5%2FvMEIK%2FS64Urxn%2FI2h6W5tPhn0eP3SOYMFdXAyk2kLrsTZnvaQTtXmulTJOWf%2FAuYYR6Ya8oQcV88cAxCZVO5%2FzzinStOsKowOlKu2GzOlPTjbicHhd1KrcpJpMSR1Pmf4c0ZZqGZvjCM4N6VpUVAsSCmX89C%2Bn4zkT9XrZtQ&X-Amz-Signature=30106e513faf58a5ba1c08ab7fa59532e4c4669e5563a17cb9bdd965d4995b25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIBOZEHC%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDPJ3jb7uGDXDdO0eQUBw1rsvp1ZZO9lDH0Z6%2Bvhf9p7gIhAIcVutrXyaDrcSkyP2ez9V6OIoeqGic9txtypA%2Bl4JAuKv8DCDIQABoMNjM3NDIzMTgzODA1IgxuPbZ9BZCe5p1hG7Mq3APEl0FBylQvY7hGczMqnjK3%2B3Yrxhdc54pjpAZ%2FEGbigjYDo21Q4GLylWQsTSP5pbcc2yYfizmPLMeaIIidhf948y1vjBQx9No6BX6Yu0pzcKaDc4kPV%2BfF5IqIOD6NG4gR19UczfXmHJKHIGHaadrYfEeoORH%2FaK07KDMsxh%2BPpHvfOZQNRW4TKZ00R%2BxLgnsa8lVrAN6HDkEsWpmirniq8kdnTJP5X1G7h4l1NwqTtDDHREWXkRMxmeSuGNXpmPJJV%2FyjoZfFCDuMtugnCdoaZDTA8ddydNhEN2ImdWvm%2Fu%2FjA4PKPkMy7vVDHxxIJmFYKl7V9UaUJo%2BVvJxggYEODH9G6h%2F%2BwqUQghJBr58wf6jPUL2CLzoS3DX8pvPMIiMlCzOJgekcct%2F%2B47eLkPkupUGi%2BFiHd%2BEJXKUPuMdEY6ep7b0PmpRMgTZ3zs50ZtxfftX5LGiPqt8nxMoKN6bCJWnn0FPWV76clhGvQqeLKaL3dvKymqAwk03vQOZ7%2Ba%2BAT43bWqsBPV84LgHyB5xnHvkO5YZRrS22uXXW0uJ%2Fntn%2FT%2BY0pH3%2F4oACsh0XG3wQmXvDIOfK%2Bhrfg2Vx6z3%2BxfW0crykyV1UNTq3Tdgy2WM5YfN5nHupYXGmyTDysInJBjqkAYI7G8TKPBm5k04AY5PUNoG%2BfzHAJWy262dmSq9qKacLDwXmnq5%2FvMEIK%2FS64Urxn%2FI2h6W5tPhn0eP3SOYMFdXAyk2kLrsTZnvaQTtXmulTJOWf%2FAuYYR6Ya8oQcV88cAxCZVO5%2FzzinStOsKowOlKu2GzOlPTjbicHhd1KrcpJpMSR1Pmf4c0ZZqGZvjCM4N6VpUVAsSCmX89C%2Bn4zkT9XrZtQ&X-Amz-Signature=24fd0ff9e78758bf292ecb18e11cc11c268d3064f83c69a81b1cc7748df7c7b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIBOZEHC%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDPJ3jb7uGDXDdO0eQUBw1rsvp1ZZO9lDH0Z6%2Bvhf9p7gIhAIcVutrXyaDrcSkyP2ez9V6OIoeqGic9txtypA%2Bl4JAuKv8DCDIQABoMNjM3NDIzMTgzODA1IgxuPbZ9BZCe5p1hG7Mq3APEl0FBylQvY7hGczMqnjK3%2B3Yrxhdc54pjpAZ%2FEGbigjYDo21Q4GLylWQsTSP5pbcc2yYfizmPLMeaIIidhf948y1vjBQx9No6BX6Yu0pzcKaDc4kPV%2BfF5IqIOD6NG4gR19UczfXmHJKHIGHaadrYfEeoORH%2FaK07KDMsxh%2BPpHvfOZQNRW4TKZ00R%2BxLgnsa8lVrAN6HDkEsWpmirniq8kdnTJP5X1G7h4l1NwqTtDDHREWXkRMxmeSuGNXpmPJJV%2FyjoZfFCDuMtugnCdoaZDTA8ddydNhEN2ImdWvm%2Fu%2FjA4PKPkMy7vVDHxxIJmFYKl7V9UaUJo%2BVvJxggYEODH9G6h%2F%2BwqUQghJBr58wf6jPUL2CLzoS3DX8pvPMIiMlCzOJgekcct%2F%2B47eLkPkupUGi%2BFiHd%2BEJXKUPuMdEY6ep7b0PmpRMgTZ3zs50ZtxfftX5LGiPqt8nxMoKN6bCJWnn0FPWV76clhGvQqeLKaL3dvKymqAwk03vQOZ7%2Ba%2BAT43bWqsBPV84LgHyB5xnHvkO5YZRrS22uXXW0uJ%2Fntn%2FT%2BY0pH3%2F4oACsh0XG3wQmXvDIOfK%2Bhrfg2Vx6z3%2BxfW0crykyV1UNTq3Tdgy2WM5YfN5nHupYXGmyTDysInJBjqkAYI7G8TKPBm5k04AY5PUNoG%2BfzHAJWy262dmSq9qKacLDwXmnq5%2FvMEIK%2FS64Urxn%2FI2h6W5tPhn0eP3SOYMFdXAyk2kLrsTZnvaQTtXmulTJOWf%2FAuYYR6Ya8oQcV88cAxCZVO5%2FzzinStOsKowOlKu2GzOlPTjbicHhd1KrcpJpMSR1Pmf4c0ZZqGZvjCM4N6VpUVAsSCmX89C%2Bn4zkT9XrZtQ&X-Amz-Signature=c5b8d02266f779293356bbd3ad6998531a91bb7da73ccda2eef05205295f3ba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

