# GitHub Actions 定时任务示例

这是一个最简单的 GitHub Actions 定时任务示例仓库。

## 功能说明

- 使用 GitHub Actions 的 `schedule` 触发器实现定时任务
- 当前配置为每天 UTC 时间 00:00（北京时间 08:00）自动执行
- 可以通过 GitHub Actions 界面手动触发

## 使用方法

### 1. 启用 GitHub Actions

1. 将此仓库推送到 GitHub
2. 在 GitHub 仓库页面，进入 `Settings` -> `Actions` -> `General`
3. 确保 `Allow all actions and reusable workflows` 已启用

### 2. 修改定时时间

编辑 `.github/workflows/scheduled-task.yml` 文件，修改 `cron` 表达式：

```yaml
- cron: '0 0 * * *'  # 每天 00:00 UTC
```

**Cron 表达式格式：**
- `分钟 小时 日 月 星期`
- 例如：`0 2 * * *` = 每天 02:00 UTC
- 例如：`0 9 * * 1-5` = 每周一到周五 09:00 UTC

**时区说明：**
- GitHub Actions 使用 UTC 时间
- 北京时间 = UTC + 8 小时

### 3. 修改任务内容

编辑 `script.py` 文件，实现你自己的任务逻辑。

### 4. 查看执行结果

1. 进入 GitHub 仓库的 `Actions` 标签页
2. 点击左侧的 `定时任务` 工作流
3. 查看执行日志和结果

## 手动触发

可以在 GitHub Actions 页面手动触发工作流执行，用于测试。

## 常见 Cron 表达式示例

- `0 0 * * *` - 每天 00:00 UTC
- `0 8 * * *` - 每天 08:00 UTC（北京时间 16:00）
- `0 0 * * 1` - 每周一 00:00 UTC
- `0 */6 * * *` - 每 6 小时执行一次
- `0 0 1 * *` - 每月 1 号 00:00 UTC

## 注意事项

- 定时任务可能会延迟几分钟执行
- 仓库需要设置为 public，或者有 GitHub Pro/Team/Enterprise 账户才能使用定时任务（对于 private 仓库）

