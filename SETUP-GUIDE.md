# 详细配置指南

## 步骤 1: 在 GitHub 中添加 Notion Token

### 方法一：通过网页界面（推荐）

1. **打开你的 GitHub 仓库**
   - 访问：https://github.com/Pan-Binghong/daily-learning

2. **进入 Settings**
   - 点击仓库顶部的 `Settings` 标签页
   - （注意：这是仓库的 Settings，不是你账户的 Settings）

3. **找到 Secrets 设置**
   - 在左侧菜单中找到 `Secrets and variables`
   - 点击展开后，选择 `Actions`

4. **添加新的 Secret**
   - 点击右上角的 `New repository secret` 按钮
   - 在 Name 框中输入：`NOTION_TOKEN`（必须完全一致，大小写敏感）
   - 在 Secret 框中粘贴你的 Notion Integration Token（格式：`secret_xxxxx`）
   - 点击 `Add secret` 按钮保存

5. **验证**
   - 保存后，你会在 Secrets 列表中看到 `NOTION_TOKEN`
   - Secret 的值会被隐藏，显示为 `***`

### 方法二：通过 GitHub CLI（命令行）

如果你安装了 GitHub CLI (gh)，可以使用命令：

```bash
# 设置 secret
gh secret set NOTION_TOKEN

# 运行后会提示你输入 token 值，粘贴你的 Notion token 后按 Enter
```

### 详细路径

```
GitHub 仓库页面
  └─ Settings（顶部标签）
      └─ Secrets and variables（左侧菜单）
          └─ Actions
              └─ New repository secret（右上角按钮）
                  ├─ Name: NOTION_TOKEN
                  └─ Secret: secret_xxxxxxxxxxxxxx
```

## 步骤 2: 配置 GitHub Actions 权限

1. **在 Settings 页面**
   - 左侧菜单找到 `Actions`
   - 点击 `General`

2. **设置工作流权限**
   - 滚动到页面底部，找到 `Workflow permissions`
   - 选择 `Read and write permissions`
   - 勾选 `Allow GitHub Actions to create and approve pull requests`
   - 点击 `Save` 保存

## 步骤 3: 启用 GitHub Pages

1. **在 Settings 页面**
   - 左侧菜单找到 `Pages`

2. **配置部署源**
   - Source 选择：`Deploy from a branch`
   - Branch 选择：`gh-pages` 分支（如果还没有这个分支，先不用管，第一次工作流运行后会自动创建）
   - 文件夹选择：`/ (root)`
   - 点击 `Save`

3. **查看你的博客地址**
   - 配置完成后，页面顶部会显示：
   - `Your site is ready to be published at https://Pan-Binghong.github.io/daily-learning/`

## 获取 Notion Integration Token

如果你还没有获取 Token：

1. 访问：https://www.notion.so/my-integrations
2. 点击 `+ New integration`
3. 填写：
   - Name: `Hugo Blog Sync`（或任意名称）
   - Associated workspace: 选择你的工作区
4. 点击 `Submit`
5. 复制显示的 `Internal Integration Token`（格式：`secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

## 授权数据库访问

对于每一个你要同步的 Notion 数据库：

1. **打开数据库页面**
2. **点击右上角的 `...` 按钮**
3. **找到 `Add connections` 或 `连接`**
4. **选择你刚创建的 Integration**（如 `Hugo Blog Sync`）
5. **重复此操作，授权所有 5 个数据库**

## 获取数据库 ID

对于每个数据库：

1. **打开数据库页面**（可以是全页面数据库或页面内的数据库视图）
2. **查看浏览器地址栏的 URL**

URL 格式示例：
```
https://www.notion.so/workspace/a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6?v=xxxxx
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              这部分就是数据库 ID（32位字符）
```

3. **复制 32 位字符的数据库 ID**
   - 如果 URL 中有短横线（-），去掉短横线
   - 只保留字母和数字，共 32 位

示例：
- URL: `https://www.notion.so/12345678-1234-1234-1234-123456789abc?v=xxx`
- 数据库 ID: `12345678123412341234123456789abc`（去掉短横线）

## 测试配置

配置完成后，可以手动触发工作流测试：

1. 进入 GitHub 仓库的 `Actions` 标签页
2. 点击左侧的 `Notion 同步与 Hugo 部署`
3. 点击右侧的 `Run workflow` 按钮
4. 选择 `master` 分支
5. 点击 `Run workflow` 确认
6. 等待工作流执行完成（约 1-3 分钟）
7. 查看日志，确认是否成功

## 常见问题

### 问题 1: 找不到 Secrets 设置
- 确保你在仓库的 Settings，不是账户的 Settings
- 你必须是仓库的 owner 或有 admin 权限

### 问题 2: 工作流提示 "unauthorized"
- 检查 NOTION_TOKEN 是否正确添加
- 确认已授权 Integration 访问所有数据库
- Token 格式应该是 `secret_` 开头

### 问题 3: GitHub Pages 显示 404
- 等待几分钟，GitHub Pages 部署需要时间
- 确认 gh-pages 分支已创建
- 检查工作流是否成功执行

### 问题 4: 推送失败
- 确认 Workflow permissions 设置为 "Read and write permissions"
- 检查 Actions 日志中的错误信息

## 下一步

配置完成后：
1. 编辑 `notion-config.yml`，填入你的数据库 ID
2. 推送代码到 GitHub
3. 工作流会自动运行
4. 访问 https://Pan-Binghong.github.io/daily-learning/ 查看博客
