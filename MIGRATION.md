# 博客迁移记录 - Publii → Hugo

## 迁移日期
2026 年 3 月 2 日 深夜

## 迁移原因
- 用户没有安装 Publii App
- Hugo 更轻量、更灵活
- PaperMod 主题简洁美观，支持深色模式

## 迁移步骤

### 1. 备份原有博客
```bash
cp -r blog blog-publii-backup-20260302_2358
```

### 2. 安装 Hugo
```bash
brew install hugo
```

### 3. 创建新 Hugo 站点
```bash
hugo new site blog-hugo --force
```

### 4. 安装 PaperMod 主题
```bash
cd blog-hugo
git clone https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
```

### 5. 配置 hugo.toml
- baseURL: https://blog.fuweineng.com/
- languageCode: zh-hk
- theme: PaperMod
- 启用深色模式、分享按钮、阅读时间等

### 6. 转换文章格式
编写转换脚本 `convert-to-hugo-v2.js`:
- 提取原标题、日期、标签
- 生成 Hugo frontmatter
- 保留 Markdown 内容

### 7. 迁移媒体文件
- 复制 224 张图片到 `static/media/`

### 8. 生成静态站点
```bash
hugo --minify
```

### 9. 部署到 GitHub Pages
```bash
cp -r public/* ../blog/
cd ../blog
git add -A
git commit -m "feat: 迁移到 Hugo + PaperMod 主题"
git push origin main
```

## 迁移结果

### 保留内容
- ✅ 19 篇文章
- ✅ 224 张图片
- ✅ 所有标签分类
- ✅ 关于页面

### 新增功能
- ✅ 自动生成标签页
- ✅ 自动生成归档页
- ✅ RSS 订阅
- ✅ JSON 搜索索引
- ✅ 站点地图
- ✅ 深色模式自动切换
- ✅ 阅读时间显示
- ✅ 分享按钮

### 技术栈
- Hugo v0.157.0 (extended)
- Theme: PaperMod
- 托管：GitHub Pages
- 域名：blog.fuweineng.com

## 文件结构

```
blog-hugo/
├── content/
│   ├── posts/        # 19 篇文章
│   └── about.md      # 关于页面
├── static/
│   └── media/        # 224 张图片
├── themes/
│   └── PaperMod/     # 主题
├── hugo.toml         # 配置文件
└── public/           # 生成的静态文件
```

## 后续维护

### 添加新文章
```bash
cd blog-hugo
hugo new content posts/新文章.md
# 编辑 content/posts/新文章.md
hugo --minify
cp -r public/* ../blog/
cd ../blog
git add -A && git commit -m "feat: 新增文章" && git push
```

### 更新主题
```bash
cd blog-hugo/themes/PaperMod
git pull
```

## 备份位置
- `/Users/fuweineng/.openclaw/workspace/blog-publii-backup-20260302_2358/`
- `/Users/fuweineng/.openclaw/workspace/blog-hugo/`

---

_迁移完成时间：2026-03-02 24:00_
