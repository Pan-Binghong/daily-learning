# GitHub Actions 定时任务示例

这是一个最简单的 GitHub Actions 定时任务示例仓库。

## 功能说明

本仓库包含两个定时任务示例：

### 1. 基础定时任务 (`scheduled-task.yml`)
- 使用 GitHub Actions 的 `schedule` 触发器实现定时任务
- 当前配置为每天 UTC 时间 00:00（北京时间 08:00）自动执行
- 可以通过 GitHub Actions 界面手动触发

### 2. 自动提交代码 (`auto-commit.yml`)
- 每天自动生成随机代码并推送到仓库
- 当前配置为每天 UTC 时间 01:00（北京时间 09:00）自动执行
- 生成的代码会保存在 `auto_commits` 目录中

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

#### 方法一：查看工作流运行列表
1. 进入 GitHub 仓库的 `Actions` 标签页
2. 左侧会显示所有工作流，点击 `定时任务`
3. 右侧会显示所有运行记录，点击最新的运行记录

#### 方法二：查看单次运行的详细日志
1. 在 `Actions` 标签页，找到 `定时任务` 工作流
2. 点击最新的运行记录（通常显示为黄色圆圈 ⏳ 表示运行中，绿色 ✓ 表示成功，红色 ✗ 表示失败）
3. 在运行详情页面：
   - **左侧**：可以看到所有步骤（Steps）
   - **右侧**：可以看到详细的日志输出
4. 点击左侧的每个步骤（如 `📅 显示执行信息`、`⚙️ 执行定时任务`），可以查看该步骤的详细输出

#### 工作流状态说明
- ⏳ **黄色圆圈** = 正在运行中
- ✅ **绿色对勾** = 执行成功
- ❌ **红色叉号** = 执行失败
- ⚪ **灰色圆圈** = 等待中

#### 手动触发测试
1. 在 `Actions` 标签页，点击左侧的 `定时任务` 工作流
2. 点击右侧的 `Run workflow` 按钮（右上角）
3. 选择分支，点击 `Run workflow` 确认
4. 刷新页面，可以看到新的运行记录

## 手动触发

可以在 GitHub Actions 页面手动触发工作流执行，用于测试。

## 常见 Cron 表达式示例

- `0 0 * * *` - 每天 00:00 UTC
- `0 8 * * *` - 每天 08:00 UTC（北京时间 16:00）
- `0 0 * * 1` - 每周一 00:00 UTC
- `0 */6 * * *` - 每 6 小时执行一次
- `0 0 1 * *` - 每月 1 号 00:00 UTC

## 自动提交代码功能

### 启用自动提交

1. **推送代码到 GitHub**
   ```bash
   git add .
   git commit -m "添加自动提交功能"
   git push
   ```

2. **配置工作流权限（重要！）**
   - 进入 GitHub 仓库的 `Settings` -> `Actions` -> `General`
   - 找到 `Workflow permissions` 部分
   - 选择 `Read and write permissions`
   - 勾选 `Allow GitHub Actions to create and approve pull requests`
   - 点击 `Save` 保存

3. **测试运行**
   - 进入 `Actions` 标签页
   - 点击左侧的 `自动提交代码` 工作流
   - 点击 `Run workflow` 手动触发一次测试

4. **查看结果**
   - 工作流执行成功后，可以在仓库中看到 `auto_commits` 目录
   - 目录中会包含自动生成的随机代码文件
   - 每次执行都会创建一个新的文件并提交到仓库

### 自定义自动提交

- **修改执行时间**：编辑 `.github/workflows/auto-commit.yml` 中的 `cron` 表达式
- **修改代码生成逻辑**：编辑 `auto-commit.py` 文件，自定义代码生成规则
- **修改提交信息**：编辑 `auto-commit.py` 中的 `generate_commit_message()` 函数

## 注意事项

- 定时任务可能会延迟几分钟执行
- 仓库需要设置为 public，或者有 GitHub Pro/Team/Enterprise 账户才能使用定时任务（对于 private 仓库）
- **自动提交功能需要配置写权限**，否则会推送失败（见上面的配置步骤）

