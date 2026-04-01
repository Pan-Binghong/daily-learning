---
title: Linux 定时任务配置指南：从 cron 到 systemd timers
date: '2026-04-01T01:58:00.000Z'
lastmod: '2026-04-01T01:58:00.000Z'
draft: false
tags:
- Linux
- Shell
- Systemd
categories:
- DevOps
---

> 💡 本文介绍如何在 Linux 中使用 systemd timers 配置定时任务，作为 cron 的现代替代方案，并附带实用示例。

# 一、为什么选择 systemd timers？

传统上 Linux 使用 cron 来配置定时任务，但现代 Linux 发行版（Ubuntu、CentOS 7+、Debian 等）默认使用 systemd 来管理服务和进程。systemd timers 相比 cron 有以下优点：

- 与 systemd 服务统一管理，日志通过 journalctl 查看
- 支持依赖关系，可在某服务启动后再执行
- 支持 monotonic 时钟（系统启动后 X 分钟执行）
- 可通过 systemctl 随时启用、禁用、查看状态
# 二、核心概念：.service + .timer

systemd timer 由两个文件组成，放在 /etc/systemd/system/ 目录下：

- xxx.service —— 定义要执行的任务（做什么）
- xxx.timer  —— 定义触发时间（什么时候做）
> 💡 两个文件名称前缀必须一致，例如 backup.service 对应 backup.timer。

# 三、实战示例：每天凌晨 2 点执行备份脚本

## 3.1 准备备份脚本

```shell
#!/bin/bash
# /usr/local/bin/backup.sh

DATE=$(date +%Y%m%d)
tar -czf /backup/data_${DATE}.tar.gz /var/data/
echo "backup done: /backup/data_${DATE}.tar.gz"
```

```shell
# 添加执行权限
chmod +x /usr/local/bin/backup.sh
```

## 3.2 创建 .service 文件

```shell
# /etc/systemd/system/backup.service
[Unit]
Description=Daily Backup Task

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
User=root
```

Type=oneshot 表示这是一次性任务，执行完即退出，非常适合定时脚本。

## 3.3 创建 .timer 文件

```shell
# /etc/systemd/system/backup.timer
[Unit]
Description=Run backup every day at 2am

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

> 💡 Persistent=true：若系统关机期间错过了触发时间，开机后会立即补执行一次。

## 3.4 启用并启动 timer

```shell
# 重新加载 systemd 配置
systemctl daemon-reload

# 启用并立即启动 timer
systemctl enable --now backup.timer

# 查看 timer 状态
systemctl status backup.timer
```

![](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=500&fit=crop&auto=format)

# 四、常用管理命令速查

```shell
# 查看所有 timer 及下次触发时间
systemctl list-timers --all

# 查看 timer 状态
systemctl status backup.timer

# 停止 timer
systemctl stop backup.timer

# 禁用 timer（取消开机自启）
systemctl disable backup.timer

# 手动立即触发一次任务
systemctl start backup.service

# 查看任务执行日志
journalctl -u backup.service -f
```

# 五、OnCalendar 时间格式速查

```plain text
OnCalendar=*-*-* 02:00:00      # 每天凌晨 2 点
OnCalendar=Mon *-*-* 09:00:00  # 每周一早上 9 点
OnCalendar=*-*-1 00:00:00      # 每月 1 号零点
OnCalendar=hourly              # 每小时
OnCalendar=daily               # 每天 00:00
OnCalendar=weekly              # 每周一 00:00
OnCalendar=monthly             # 每月 1 号 00:00
```

> 💡 验证时间格式：systemd-analyze calendar "*-*-* 02:00:00" 可查看下次触发时间。

# 六、Monotonic Timer（基于启动时间触发）

除了 OnCalendar，还可以使用 monotonic 方式，基于系统启动时间触发：

```shell
[Timer]
# 系统启动后 5 分钟执行一次
OnBootSec=5min
# 之后每隔 1 小时再执行
OnUnitActiveSec=1h
```

# 七、总结

- 创建 xxx.service 文件，定义执行的命令
- 创建 xxx.timer 文件，定义触发时间（OnCalendar）
- 执行 systemctl daemon-reload && systemctl enable --now xxx.timer
> 💡 小提示：个人简单脚本用 crontab -e 也完全够用，不必强制使用 systemd timer。systemd timer 更适合系统级服务管理场景。

---

# 参考文献

---

[https://www.freedesktop.org/software/systemd/man/systemd.timer.html](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)

[https://wiki.archlinux.org/title/Systemd/Timers](https://wiki.archlinux.org/title/Systemd/Timers)

[https://www.freedesktop.org/software/systemd/man/systemd.time.html](https://www.freedesktop.org/software/systemd/man/systemd.time.html)

