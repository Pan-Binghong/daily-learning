---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SDO3PLZ%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIGRQrF3RmqCdS4mSgWAmdgIimHmkGWXW8Uiv7LI4A%2FTbAiBGDAeFnzPiaCMGOODKbyaP0wxOwEJK9eRqIKR5j4wg0ir%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIM41r65TDOvTVD4Ik2KtwDb9zNDe1B7ixa6ZFMyApvNtsQQvC0G%2BIPebRSAPrazZIfbwQ9i%2FgQglT6YCFfJlZHcaBA750mgSiL%2BU0Q5ZSF5sl%2FuEu6MzZJyENTSrfL5YesNQcgsf95VbtJGWfYfxBG8EUrVi0W3doqE9pCp1x1rLfSGrWWWV2U7TkggbS7Tmoo1uvWLXPEwX0xC%2Fn2g%2Fj39s%2BTFpx0%2BmWeL3fwwPHUaN3KN%2FtsL1WblW5aXPXejlw7qeeFbVeOV7HSSPtbBm73okYNrAv4XLdYzsR3hiLJOVAahymDm77eK6YuwLK4TBJNpl0XbCB5G4lnSbXHvObEG2NcDqInqHJEfRmwFUEeEH%2BTPAxaaa9R1X%2FtafvdiPB4jI5oW%2BwVa1TV8a%2FMmmX%2FWDaI1II2xFXTLiB%2FICm7L4ZfHLrM4VyFiZsC7a7suCnBYYi3GZ%2BQabj65G3rPR%2Fp2i%2FWgkqez%2BLVFZLgK7AIcF3bBnwR6RfzD9968WJRONhhFFm2RSwChMn%2FkbgnLF0MFZQ4ddIvR6aHMdXP6yGaWTvcngQ2YhdUcCfvYGEfhS93m0rBGh3RbovIZTHqZ1%2B6Adk1XmLGWPgKUkJ48QktTAAsQNSzBi31sV5xqE2XxCen3NlMK89WubthiFwwjb%2FPzAY6pgGsgJysHQ5mcYqmCewHO7Q2kHvQNvaHWgO68evKkE9hwKTSAtLt4491IGU4FR9HzvGSXyFso4ohWOkMywlhDowp%2FBMCIy7p1GlL9n%2FQdXy36qtb4vEHMeODdWrrT9uzbosg9c%2BBJNRmE%2FaRaK06ioC2cIXJ9tGEKKusCmcpFRCwWAmnzW0LFzpDwpeutlRVKp3tHMu0tqFtzXAmH0z0475JMehBYHFA&X-Amz-Signature=68c2b9de5155ea1b11199e2847979cd56d9003ef06f0c0553b8b1b48ecdc11ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

