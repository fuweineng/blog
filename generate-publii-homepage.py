#!/usr/bin/env python3
"""
生成完整的 Publii 风格首页
显示所有文章，带分页（每页 12 篇）
"""

import os
import re
from datetime import datetime
from pathlib import Path

POSTS_PER_PAGE = 12
BLOG_DIR = '/Users/fuweineng/.openclaw/workspace/blog'

def get_version():
    """获取 Git 版本号"""
    import subprocess
    try:
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, cwd=BLOG_DIR)
        return result.stdout.strip()
    except:
        return 'latest'

def extract_article_info(filepath):
    """从 HTML 文件中提取文章信息"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取标题
    title_match = re.search(r'<title>(.*?) - 符伟能的网络日志</title>', content)
    if not title_match:
        title_match = re.search(r'<h1 class="post__title">(.*?)</h1>', content)
    title = title_match.group(1) if title_match else filepath.replace('.html', '')
    
    # 提取摘要
    excerpt_match = re.search(r'<meta name="description" content="(.*?)">', content)
    if not excerpt_match:
        excerpt_match = re.search(r'<p class="post__excerpt">(.*?)</p>', content)
    excerpt = excerpt_match.group(1) if excerpt_match else ''
    
    # 提取日期
    date_match = re.search(r'<time datetime="(\d{4}-\d{2}-\d{2})">', content)
    if not date_match:
        # 从文件名提取日期
        name_match = re.search(r'(\d{4}-\d{2}-\d{2})', filepath)
        if name_match:
            date_match = type('obj', (object,), {'group': lambda x: name_match.group(1)})()
    date = date_match.group(1) if date_match else '2026-03-01'
    
    # 提取标签
    tags_match = re.search(r'<span class="post__tags">(.*?)</span>', content)
    tags = tags_match.group(1) if tags_match else '<a href="#">文章</a>'
    
    # 提取图片
    image_match = re.search(r'<a href=".*?" class="post__image"><img src="(.*?)"', content)
    if not image_match:
        image_match = re.search(r'<figure class="post__image">.*?<img src="(.*?)"', content, re.DOTALL)
    image = image_match.group(1) if image_match else './media/default.jpg'
    
    # 提取文件名作为链接
    filename = filepath.replace('.html', '') if filepath.endswith('.html') else filepath
    
    return {
        'title': title,
        'excerpt': excerpt,
        'date': date,
        'tags': tags,
        'image': image,
        'link': f'{filename}.html' if not filename.endswith('.html') else filename,
    }

def generate_post_card(article, page=1):
    """生成文章卡片 HTML"""
    # 分页页面使用绝对路径，首页使用相对路径
    link = article['link'] if page == 1 else f"https://blog.fuweineng.com/{article['link']}"
    image = article['image'] if page == 1 else article['image'].replace('./', 'https://blog.fuweineng.com/')
    
    return f'''
<article class="post">
<a href="{link}" class="post__image"><img src="{image}" alt="{article['title']}" loading="lazy"></a>
<div class="post__content">
<h2 class="post__title"><a href="{link}">{article['title']}</a></h2>
<p class="post__excerpt">{article['excerpt']}</p>
<div class="post__meta">
<time datetime="{article['date']}">{article['date']}</time>
<span class="post__tags">{article['tags']}</span>
</div>
</div>
</article>
'''

def generate_pagination(current_page, total_pages):
    """生成分页导航"""
    if total_pages <= 1:
        return '<nav class="pagination"><span class="pagination__current">1 / 1</span></nav>'
    
    pagination = '<nav class="pagination">'
    
    # 上一页
    if current_page > 1:
        pagination += f'<a href="{"index.html" if current_page == 2 else f"page/{current_page-1}/index.html"}">上一页</a>'
    
    # 页码
    for i in range(1, total_pages + 1):
        if i == current_page:
            pagination += f'<span class="pagination__current">{i} / {total_pages}</span>'
        else:
            pagination += f'<a href="{"index.html" if i == 1 else f"page/{i}/index.html"}">{i}</a>'
    
    # 下一页
    if current_page < total_pages:
        pagination += f'<a href="page/{current_page+1}/index.html">下一页</a>'
    
    pagination += '</nav>'
    return pagination

def generate_homepage(page=1):
    """生成首页 HTML"""
    os.chdir(BLOG_DIR)
    
    # 收集所有文章
    articles = []
    for file in Path(BLOG_DIR).glob('*.html'):
        filename = file.name
        # 跳过特殊页面
        if filename in ['index.html', 'about.html', '404.html', 'notion-collection.html']:
            continue
        if filename.startswith('page-'):
            continue
        
        try:
            info = extract_article_info(filename)
            articles.append(info)
        except Exception as e:
            print(f"⚠️  {filename}: {e}")
    
    # 按日期排序（最新的在前）
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    # 分页
    total_pages = (len(articles) + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE
    start_idx = (page - 1) * POSTS_PER_PAGE
    end_idx = start_idx + POSTS_PER_PAGE
    page_articles = articles[start_idx:end_idx]
    
    # 生成文章卡片
    posts_html = '\n'.join([generate_post_card(article, page) for article in page_articles])
    
    # 生成分页
    pagination_html = generate_pagination(page, total_pages)
    
    # 生成完整 HTML
    version = get_version()
    homepage_html = f'''<!DOCTYPE html>
<html lang="zh-hk">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>符伟能的网络日志 - 首页</title>
<meta name="description" content="小明的个人博客 - 分享思考、技术、生活">
<meta name="robots" content="index,follow">
<meta name="generator" content="Publii Open-Source CMS for Static Site">
<link rel="alternate" type="application/atom+xml" href="https://blog.fuweineng.com/feed.xml" title="符伟能的网络日志 - RSS">
<link rel="alternate" type="application/json" href="https://blog.fuweineng.com/feed.json" title="符伟能的网络日志 - JSON">
<link rel="stylesheet" href="https://blog.fuweineng.com/assets/css/style.css">
<link rel="stylesheet" href="./assets/css/universal-dark-mode.css?v={version}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✨</text></svg>">
</head>
<body class="home-template">
<header class="header" id="js-header">
<a href="https://blog.fuweineng.com/" class="logo">符伟能的网络日志</a>
<nav class="navbar js-navbar">
<button class="navbar__toggle js-toggle" aria-label="Menu">
<span class="navbar__toggle-box"><span class="navbar__toggle-inner">Menu</span></span>
</button>
<ul class="navbar__menu">
<li><a href="https://blog.fuweineng.com/pc-qing-huai-ruan-jian-tui-jian.html" target="_self">好用软件</a></li>
<li><a href="https://blog.fuweineng.com/lian-shang-xin-wen.html" target="_self">链上新闻</a></li>
<li><a href="https://blog.fuweineng.com/about.html" target="_self">咋了</a></li>
</ul>
</nav>
</header>
<main class="main">
<div class="wrapper">
<div class="page-header">
<h1 class="page-title">符伟能的网络日志</h1>
<p class="page-description">分享思考、技术、生活 · 共 {len(articles)} 篇文章</p>
</div>
<div class="posts-list">
{posts_html}
</div>
{pagination_html}
</div>
</main>
<footer class="footer">
<div class="footer__copyright">Powered by Publii</div>
</footer>
<script>window.publiiThemeMenuConfig = {{ mobileMenuMode: 'sidebar', animationSpeed: 300, submenuWidth: 'auto', doubleClickTime: 500, mobileMenuExpandableSubmenus: true, relatedContainerForOverlayMenuSelector: '.navbar', }};</script>
<script defer="defer" src="https://blog.fuweineng.com/assets/js/scripts.min.js"></script>
<script defer="defer" src="./assets/js/universal-dark-mode.js?v={version}"></script>
</body>
</html>'''
    
    return homepage_html, total_pages, len(articles)

if __name__ == '__main__':
    # 生成首页
    homepage_html, total_pages, total_articles = generate_homepage(page=1)
    
    with open(f'{BLOG_DIR}/index.html', 'w', encoding='utf-8') as f:
        f.write(homepage_html)
    
    print(f"✅ 首页生成完成！")
    print(f"   总文章数：{total_articles}")
    print(f"   总页数：{total_pages}")
    print(f"   每页显示：{POSTS_PER_PAGE} 篇")
    
    # 生成分页目录
    for page in range(2, total_pages + 1):
        page_html, _, _ = generate_homepage(page=page)
        page_dir = f'{BLOG_DIR}/page/{page}'
        os.makedirs(page_dir, exist_ok=True)
        
        with open(f'{page_dir}/index.html', 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"✅ 生成第 {page} 页：page/{page}/index.html")
    
    print(f"\n🎉 完成！共生成 {total_pages} 页，{total_articles} 篇文章")
