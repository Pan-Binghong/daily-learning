---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSKZGCRB%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCKyRbRP4N4%2FwjvE4VW2o6kR47QzDFJFKfsUOMd%2BrDrCwIgYdObiAC6UHcORbDOJAlVWmYqVQ4OOUcU%2FeEStmI0c8wq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDEXsGsbHSN%2BdbszCvircA7q4j8mkOyCOVALGedtfUVN0l220hjdmg0W7jqtRayXz%2B64X%2FufHSJwgDWCU%2FL2Cf9L7Gz6F7uvTByQe%2BDkXvs6nk1%2FQYIMGRoYvr9CpnNS1TWpXOzUKhG1ghJukeZMDA6stNEUDkwGp67xjlZ1W6iMpb5YN8Uu520SC8PYsrAKwujjvahnZEitiFDGW4M%2F58Iu%2BBXQZjPhvscp%2FB3q2sGaEvtuAAF%2BxrYWe9JSrEsBy5VYuKYGqJ1O82hcl3lsU2CJl3JRelIsK34cgu1gN5PylEOZmMN8eE1GMuYsCAb4SXFIs6Bmf66v4zlIdDByujiSDhuIp%2FNmX%2BPGHaFvY8lcCmRT6Dt6UKKEICdoEIWzO5VxnRfcuChNd2jOiic%2BglFthydfCs23FaPJAo%2B5YiTI1ozm9YKcMYAKBAeOSZm8ucBFdvsskVbQAIvqGYqymoTtzULEG6vU0Ltdrtk2Bb322ng5J2Rvs%2BLIiSfjPulVL%2BWsfQXGKEd%2F1GDOYy3vg4Y6bPHe7JCdLcS0jEQveC9Hj52HziRoRR9JAC%2FV%2F%2FK3RwUisVkfv4orny08rA7evzDQPJ5Mhc7vIVFgJ7cM8eVU%2BzeY2jSSp1pYOdON5h1TNm%2FgsHYtcegiF%2BTUfMLK9ysgGOqUBN2Si3McUgtuofrbcQ72dxffS8ZGqUD8iHC6S3zv34iTyhGOoy9lG9foFUzfhUrK6ahh30ib2sEv8TEAsOMh5JwDoqN6%2Fxke%2B4rl0snq2KG3XMpAJNl%2BZs3pB4copZn3nRY58QvHvPc0GAAPvF4k%2FExgTl0fv0qhKqv52LyRyUQFvZMWAI6qAMP%2BsrEMGFJbTg3EB6WJtsyPXdYixH6U%2BDeyK06V5&X-Amz-Signature=9a6be6c5e25273296dfcc11a03ddc5c87aa5de71c01961e13d66e2e8df932c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSKZGCRB%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCKyRbRP4N4%2FwjvE4VW2o6kR47QzDFJFKfsUOMd%2BrDrCwIgYdObiAC6UHcORbDOJAlVWmYqVQ4OOUcU%2FeEStmI0c8wq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDEXsGsbHSN%2BdbszCvircA7q4j8mkOyCOVALGedtfUVN0l220hjdmg0W7jqtRayXz%2B64X%2FufHSJwgDWCU%2FL2Cf9L7Gz6F7uvTByQe%2BDkXvs6nk1%2FQYIMGRoYvr9CpnNS1TWpXOzUKhG1ghJukeZMDA6stNEUDkwGp67xjlZ1W6iMpb5YN8Uu520SC8PYsrAKwujjvahnZEitiFDGW4M%2F58Iu%2BBXQZjPhvscp%2FB3q2sGaEvtuAAF%2BxrYWe9JSrEsBy5VYuKYGqJ1O82hcl3lsU2CJl3JRelIsK34cgu1gN5PylEOZmMN8eE1GMuYsCAb4SXFIs6Bmf66v4zlIdDByujiSDhuIp%2FNmX%2BPGHaFvY8lcCmRT6Dt6UKKEICdoEIWzO5VxnRfcuChNd2jOiic%2BglFthydfCs23FaPJAo%2B5YiTI1ozm9YKcMYAKBAeOSZm8ucBFdvsskVbQAIvqGYqymoTtzULEG6vU0Ltdrtk2Bb322ng5J2Rvs%2BLIiSfjPulVL%2BWsfQXGKEd%2F1GDOYy3vg4Y6bPHe7JCdLcS0jEQveC9Hj52HziRoRR9JAC%2FV%2F%2FK3RwUisVkfv4orny08rA7evzDQPJ5Mhc7vIVFgJ7cM8eVU%2BzeY2jSSp1pYOdON5h1TNm%2FgsHYtcegiF%2BTUfMLK9ysgGOqUBN2Si3McUgtuofrbcQ72dxffS8ZGqUD8iHC6S3zv34iTyhGOoy9lG9foFUzfhUrK6ahh30ib2sEv8TEAsOMh5JwDoqN6%2Fxke%2B4rl0snq2KG3XMpAJNl%2BZs3pB4copZn3nRY58QvHvPc0GAAPvF4k%2FExgTl0fv0qhKqv52LyRyUQFvZMWAI6qAMP%2BsrEMGFJbTg3EB6WJtsyPXdYixH6U%2BDeyK06V5&X-Amz-Signature=a27b1637a26018075a791a90d94ffcd35d5e220aa95a1ed36505a68f2ed57241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



