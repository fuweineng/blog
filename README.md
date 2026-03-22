# 符伟能的个人博客

这是一个基于 Hugo + Blowfish 的个人博客源码仓库。

## 本地开发

```bash
hugo server -D
```

本地构建：

```bash
hugo --gc --minify
```

构建产物会输出到 `public/`。

## Cloudflare Pages 配置

把 GitHub 仓库导入 Cloudflare Pages 时，建议使用以下设置：

- Framework preset: `Hugo`
- Build command: `hugo --gc --minify`
- Build output directory: `public`
- Environment variable: `HUGO_VERSION=0.157.0`

## 自定义域名

当前站点域名为 `blog.fuweineng.com`。

Cloudflare Pages 连接完成后：

1. 在 Pages 项目里绑定 `blog.fuweineng.com`
2. 确认 Cloudflare DNS 中已为该域名添加对应记录
3. 仓库中的 `static/CNAME` 会在构建时一并输出

## 内容结构

- `content/`: 博客正文与页面
- `static/`: 静态资源
- `themes/blowfish/`: 当前主题
- `.github/workflows/`: 构建检查
