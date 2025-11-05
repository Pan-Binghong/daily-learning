# Notion + Hugo 自动化博客系统

这是一个自动化的个人博客系统，可以将 Notion 笔记自动同步到 GitHub，并使用 Hugo 生成静态博客。

## 功能特性

- 从 Notion 数据库自动同步内容到 GitHub
- 支持多个 Notion 数据库，每个对应不同类型的笔记
- 使用 Hugo 构建静态博客
- 自动部署到 GitHub Pages
- 每天自动同步一次
- 支持手动触发同步

## 系统架构

```
Notion 数据库 → GitHub Actions → Hugo 构建 → GitHub Pages
     ↓              ↓                ↓            ↓
  5个数据库      定时同步        生成静态站点    自动部署
```

## 快速开始

### 1. 获取 Notion Integration Token

1. 访问 https://www.notion.so/my-integrations
2. 点击 "+ New integration"
3. 填写名称（如 "Hugo Blog Sync"）
4. 选择关联的 workspace
5. 点击 "Submit" 创建
6. 复制显示的 "Internal Integration Token"（格式：`secret_xxxxx`）

### 2. 授权 Notion 数据库访问

对你的 5 个 Notion 数据库，分别执行以下操作：

1. 打开数据库页面
2. 点击右上角 "..." → "Add connections"
3. 选择你创建的 Integration
4. 重复以上步骤，授权所有数据库

### 3. 获取数据库 ID

打开每个 Notion 数据库，从 URL 中获取数据库 ID：

```
URL 格式: https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=yyyyy
数据库 ID: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx（32位字符）
```

### 4. 配置数据库映射

编辑 `notion-config.yml` 文件，配置你的 5 个数据库：

```yaml
databases:
  - name: 技术博客
    database_id: YOUR_DATABASE_ID_1
    section: posts
    category: 技术

  - name: 学习笔记
    database_id: YOUR_DATABASE_ID_2
    section: notes
    category: 学习

  - name: 读书笔记
    database_id: YOUR_DATABASE_ID_3
    section: reading
    category: 阅读

  - name: 项目记录
    database_id: YOUR_DATABASE_ID_4
    section: projects
    category: 项目

  - name: 随笔
    database_id: YOUR_DATABASE_ID_5
    section: essays
    category: 随笔
```

### 5. 配置 GitHub Secrets

在 GitHub 仓库中添加 Secrets：

1. 进入仓库 `Settings` → `Secrets and variables` → `Actions`
2. 点击 `New repository secret`
3. 添加：
   - Name: `NOTION_TOKEN`
   - Value: 你的 Notion Integration Token

### 6. 配置 GitHub Actions 权限

1. 进入 `Settings` → `Actions` → `General`
2. 找到 `Workflow permissions`
3. 选择 `Read and write permissions`
4. 勾选 `Allow GitHub Actions to create and approve pull requests`
5. 点击 `Save`

### 7. 启用 GitHub Pages

1. 进入 `Settings` → `Pages`
2. Source 选择 `Deploy from a branch`
3. Branch 选择 `gh-pages` 分支，目录选择 `/ (root)`
4. 点击 `Save`

### 8. 安装 Hugo 主题（可选）

选择并安装一个 Hugo 主题：

```bash
# 推荐主题示例
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod

# 或其他主题
# git submodule add https://github.com/CaiJimmy/hugo-theme-stack.git themes/stack
```

然后编辑 `config.toml`，修改 `theme` 配置：

```toml
theme = "PaperMod"  # 或你选择的主题名称
```

### 9. 本地测试

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 设置环境变量
export NOTION_TOKEN="your_notion_token_here"

# 测试同步
python notion-sync.py

# 本地运行 Hugo
hugo server -D
```

访问 http://localhost:1313 查看博客。

### 10. 推送到 GitHub

```bash
git add .
git commit -m "配置 Notion + Hugo 博客系统"
git push
```

## 工作流说明

### 自动同步工作流 (`notion-hugo-deploy.yml`)

- **触发时机**：
  - 每天北京时间 9:00（UTC 01:00）自动执行
  - 手动触发
  - 推送配置文件更新时

- **执行步骤**：
  1. 从 Notion 同步内容到 `content/` 目录
  2. 如有更新，自动提交到 GitHub
  3. 使用 Hugo 构建静态站点
  4. 部署到 GitHub Pages

### 手动触发同步

1. 进入 GitHub 仓库的 `Actions` 标签页
2. 点击左侧的 `Notion 同步与 Hugo 部署`
3. 点击右侧的 `Run workflow` 按钮
4. 选择分支，点击 `Run workflow` 确认

## 目录结构

```
.
├── .github/
│   └── workflows/
│       ├── notion-hugo-deploy.yml  # Notion 同步 + Hugo 部署
│       ├── scheduled-task.yml      # 基础定时任务（示例）
│       └── auto-commit.yml         # 自动提交（示例）
├── content/                        # Hugo 内容目录
│   ├── posts/                      # 技术博客
│   ├── notes/                      # 学习笔记
│   ├── reading/                    # 读书笔记
│   ├── projects/                   # 项目记录
│   └── essays/                     # 随笔
├── notion-sync.py                  # Notion 同步脚本
├── notion-config.yml               # Notion 数据库配置
├── config.toml                     # Hugo 配置文件
├── requirements.txt                # Python 依赖
├── script.py                       # 定时任务示例脚本
├── auto-commit.py                  # 自动提交示例脚本
└── README.md                       # 本文件
```

## Notion 数据库建议结构

每个 Notion 数据库建议包含以下属性：

- **Title**（标题）：必需，文章标题
- **Status**（状态）：可选，用于过滤（如 "Published"、"Draft"）
- **Tags**（标签）：可选，文章标签
- **Category**（分类）：可选，文章分类
- **Date**（日期）：可选，发布日期

### 过滤配置示例

如果只想同步已发布的文章，在 `notion-config.yml` 中添加过滤条件：

```yaml
databases:
  - name: 技术博客
    database_id: YOUR_DATABASE_ID
    section: posts
    category: 技术
    filter:
      property: Status
      select:
        equals: Published
```

## 常见问题

### 1. 同步失败，提示 "unauthorized"

- 检查 NOTION_TOKEN 是否正确配置
- 确认已授权 Integration 访问所有数据库

### 2. GitHub Actions 推送失败

- 检查 Workflow permissions 是否设置为 "Read and write permissions"

### 3. Hugo 构建失败

- 检查是否安装了主题
- 确认 `config.toml` 中的主题配置正确

### 4. GitHub Pages 无法访问

- 检查 Pages 设置是否正确
- 确认 `gh-pages` 分支已创建
- 等待几分钟让 GitHub Pages 部署完成

### 5. 想要更改同步时间

编辑 `.github/workflows/notion-hugo-deploy.yml` 中的 cron 表达式：

```yaml
schedule:
  - cron: '0 1 * * *'  # 每天 UTC 01:00（北京时间 09:00）
```

## 支持的 Notion 功能

- ✅ 标题（Heading 1/2/3）
- ✅ 段落（Paragraph）
- ✅ 列表（Bulleted/Numbered）
- ✅ 待办事项（To-do）
- ✅ 代码块（Code）
- ✅ 引用（Quote）
- ✅ 分隔线（Divider）
- ✅ 图片（Image）
- ✅ 书签（Bookmark）
- ✅ 标注（Callout）
- ⚠️ 表格（Table）- 部分支持
- ⚠️ 数据库（Database）- 不支持内嵌

## 进阶配置

### 自定义 Hugo 主题

1. 浏览 Hugo 主题库：https://themes.gohugo.io/
2. 选择喜欢的主题并安装
3. 根据主题文档配置 `config.toml`

### 添加自定义域名

1. 在域名服务商处添加 CNAME 记录指向 `yourusername.github.io`
2. 编辑 `.github/workflows/notion-hugo-deploy.yml`，取消注释并修改：
   ```yaml
   cname: your-domain.com
   ```

### 添加评论系统

参考你使用的 Hugo 主题文档，通常支持：
- Disqus
- Giscus
- Utterances

## 其他示例功能

本仓库还包含其他 GitHub Actions 示例：

### 基础定时任务 (`scheduled-task.yml`)
- 每天 UTC 00:00 执行
- 运行 `script.py` 脚本

### 自动提交代码 (`auto-commit.yml`)
- 每天 UTC 01:00 执行
- 自动生成随机代码并提交

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 相关资源

- [Notion API 文档](https://developers.notion.com/)
- [Hugo 文档](https://gohugo.io/documentation/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
