# 配置检查清单

## ✅ 已完成的配置

- [x] **数据库配置**：`notion-config.yml` 已配置 5 个数据库
  - AI: 12e57052b4908178a1fcc2957b644d44
  - Knowledge: 12e57052b49081869730e11b5d1d0711
  - BackEnd: 12e57052b49080f7b180d8dce1e6f395
  - DevOps: 12e57052b49081bbba54c2d78910ae37
  - Other: 4428d2572e404c5886da83b971e85f98

- [x] **Hugo 配置**：`config.toml` 已更新
  - baseURL: https://Pan-Binghong.github.io/
  - 导航菜单已配置 5 个分类
  - 作者信息已更新

- [x] **目录结构**：内容目录已创建
  - content/ai/
  - content/knowledge/
  - content/backend/
  - content/devops/
  - content/other/

## 🔲 需要你完成的步骤

### 步骤 1: 获取 Notion Integration Token

1. 访问：https://www.notion.so/my-integrations
2. 点击 `+ New integration`
3. 填写名称：`Hugo Blog Sync`
4. 选择你的 workspace
5. 点击 `Submit`
6. **复制 Token**（格式：`secret_xxxxxxxxxx...`）

### 步骤 2: 授权数据库访问（重要！）

对以下 5 个数据库，分别授权：

1. **AI 数据库**
   - 打开：https://panbinghong.notion.site/12e57052b4908178a1fcc2957b644d44
   - 点击右上角 `...` → `Add connections` → 选择你的 Integration

2. **Knowledge 数据库**
   - 打开：https://panbinghong.notion.site/12e57052b49081869730e11b5d1d0711
   - 点击右上角 `...` → `Add connections` → 选择你的 Integration

3. **BackEnd 数据库**
   - 打开：https://panbinghong.notion.site/12e57052b49080f7b180d8dce1e6f395
   - 点击右上角 `...` → `Add connections` → 选择你的 Integration

4. **DevOps 数据库**
   - 打开：https://panbinghong.notion.site/12e57052b49081bbba54c2d78910ae37
   - 点击右上角 `...` → `Add connections` → 选择你的 Integration

5. **Other 数据库**
   - 打开：https://panbinghong.notion.site/4428d2572e404c5886da83b971e85f98
   - 点击右上角 `...` → `Add connections` → 选择你的 Integration

### 步骤 3: 在 GitHub 添加 Secret

1. 访问：https://github.com/Pan-Binghong/daily-learning/settings/secrets/actions
2. 点击 `New repository secret`
3. 填写：
   - Name: `NOTION_TOKEN`
   - Secret: 粘贴你的 Notion Token
4. 点击 `Add secret`

### 步骤 4: 配置 GitHub Actions 权限

1. 访问：https://github.com/Pan-Binghong/daily-learning/settings/actions
2. 找到 `Workflow permissions`
3. 选择 `Read and write permissions`
4. 勾选 `Allow GitHub Actions to create and approve pull requests`
5. 点击 `Save`

### 步骤 5: 启用 GitHub Pages

1. 访问：https://github.com/Pan-Binghong/daily-learning/settings/pages
2. Source 选择：`Deploy from a branch`
3. Branch 选择：`gh-pages`（第一次运行后会自动创建）
4. 点击 `Save`

### 步骤 6: 安装 Hugo 主题（推荐）

在本地执行：

```bash
# 推荐使用 PaperMod 主题（简洁美观）
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod

# 然后修改 config.toml
# theme = "PaperMod"
```

或者选择其他主题：
- Hugo Stack: https://github.com/CaiJimmy/hugo-theme-stack
- Hugo Book: https://github.com/alex-shpak/hugo-book
- 更多主题：https://themes.gohugo.io/

### 步骤 7: 推送代码

```bash
git add .
git commit -m "配置 Notion + Hugo 自动博客系统"
git push
```

### 步骤 8: 测试工作流

1. 访问：https://github.com/Pan-Binghong/daily-learning/actions
2. 点击 `Notion 同步与 Hugo 部署`
3. 点击 `Run workflow`
4. 选择 `master` 分支
5. 点击 `Run workflow` 确认
6. 等待执行完成（约 1-3 分钟）

### 步骤 9: 查看博客

执行成功后，访问：
- https://Pan-Binghong.github.io/daily-learning/

## 📝 本地测试（可选）

在推送到 GitHub 之前，可以本地测试：

```bash
# 1. 安装 Python 依赖
pip install -r requirements.txt

# 2. 设置环境变量（Windows）
set NOTION_TOKEN=your_token_here

# 或 Linux/Mac
export NOTION_TOKEN=your_token_here

# 3. 测试同步脚本
python notion-sync.py

# 4. 安装 Hugo（如果还没安装）
# Windows: choco install hugo-extended
# Mac: brew install hugo
# Linux: sudo apt install hugo

# 5. 本地运行 Hugo
hugo server -D

# 6. 访问 http://localhost:1313
```

## ⚠️ 常见问题

### Token 放在哪里？
- **不要**把 Token 直接写在代码里
- **不要**提交 Token 到 Git
- **一定要**在 GitHub Secrets 中配置

### 数据库授权失败？
- 确保在每个数据库页面都执行了 `Add connections`
- 确保选择了正确的 Integration

### 工作流执行失败？
1. 检查 Actions 日志查看错误信息
2. 确认 NOTION_TOKEN 已正确配置
3. 确认所有数据库已授权
4. 确认 Workflow permissions 已设置

### GitHub Pages 显示 404？
- 等待 3-5 分钟，GitHub Pages 需要时间部署
- 确认 gh-pages 分支已创建
- 检查 Pages 设置是否正确

## 🎉 完成后

每天北京时间 9:00，系统会自动：
1. 从 Notion 同步 5 个数据库的内容
2. 转换为 Markdown 格式
3. 提交到 GitHub
4. 使用 Hugo 构建静态博客
5. 部署到 GitHub Pages

你只需要在 Notion 中写笔记，博客会自动更新！
