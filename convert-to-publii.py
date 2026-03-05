#!/usr/bin/env python3
"""
将 Hugo 风格页面转换为标准 Publii 格式
目标：统一所有页面为 Publii 的标准结构
"""

import os
import re
from datetime import datetime

# Hugo 风格页面列表
hugo_files = {
    'yi-lai-de-li-liang.html': {
        'title': '依赖的力量',
        'date': '2026-02-27',
        'tags': ['思考'],
        'image': 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1200&h=630&fit=crop',
        'excerpt': '一个人可以走得快，一群人才能走得远',
    },
    'wen-ding-shi-zui-zhong-yao-de-cai-fu.html': {
        'title': '稳定是最重要的财富',
        'date': '2026-02-27',
        'tags': ['思考'],
        'image': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=1200&h=630&fit=crop',
        'excerpt': '在这个不确定的时代，稳定才是最稀缺的资源',
    },
    'li-cha-shi-yi-xiang-chu-lai-de.html': {
        'title': '离差是想出来的',
        'date': '2026-02-27',
        'tags': ['思考'],
        'image': 'https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=1200&h=630&fit=crop',
        'excerpt': '人与人之间的差距，往往是从想法开始分化的',
    },
    'nai-cha-xian-huo-qu-de-she-xiang.html': {
        'title': '奶茶线获取的设想',
        'date': '2026-02-27',
        'tags': ['技术'],
        'image': 'https://images.unsplash.com/photo-1558857498-940f6fa3000c?w=1200&h=630&fit=crop',
        'excerpt': '关于自动化获取奶茶优惠线的技术探讨',
    },
}

def get_publii_head(title, description, keywords, image):
    """生成 Publii 风格的 head 部分"""
    return f'''<!DOCTYPE html>
<html lang="zh-hk">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - 符伟能的网络日志</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index,follow">
    <meta name="generator" content="Publii Open-Source CMS for Static Site">
    <link rel="alternate" type="application/atom+xml" href="https://blog.fuweineng.com/feed.xml" title="符伟能的网络日志 - RSS">
    <link rel="alternate" type="application/json" href="https://blog.fuweineng.com/feed.json" title="符伟能的网络日志 - JSON">
    <link rel="stylesheet" href="https://blog.fuweineng.com/assets/css/style.css">
    <link rel="stylesheet" href="./assets/css/universal-dark-mode.css?v={get_version()}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✨</text></svg>">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{image}">
</head>
<body class="post-template">'''

def get_publii_header():
    """生成 Publii 风格的导航栏"""
    return '''<header class="header" id="js-header">
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
</header>'''

def get_publii_footer():
    """生成 Publii 风格的页脚"""
    return '''<footer class="footer">
<div class="footer__copyright">Powered by Publii</div>
</footer>'''

def get_version():
    """获取 Git 版本号"""
    import subprocess
    try:
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, cwd='/Users/fuweineng/.openclaw/workspace/blog')
        return result.stdout.strip()
    except:
        return 'latest'

def convert_hugo_to_publii(filepath, metadata):
    """将 Hugo 格式转换为 Publii 格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取正文内容
    content_match = re.search(r'<div class="post__content">(.*?)</div>\s*</main>', content, re.DOTALL)
    if not content_match:
        content_match = re.search(r'<div class="content">(.*?)</div>\s*</article>', content, re.DOTALL)
    
    if content_match:
        article_content = content_match.group(1)
    else:
        print(f"⚠️  {filepath}: 无法提取内容")
        return False
    
    # 提取特色图片
    image_match = re.search(r'<figure class="post__image">(.*?)</figure>', content, re.DOTALL)
    if not image_match:
        image_match = re.search(r'<figure class="featured-image">(.*?)</figure>', content, re.DOTALL)
    
    featured_image = ''
    if image_match:
        featured_image = image_match.group(1)
    
    # 生成新的 Publii 格式
    new_content = f'''{get_publii_head(
        metadata['title'],
        metadata['excerpt'],
        ','.join(metadata['tags']),
        metadata['image']
    )}
{get_publii_header()}
<main class="main">
<div class="wrapper">
<article class="post">
<header class="post__header">
<h1 class="post__title">{metadata['title']}</h1>
<div class="post__meta">
<time datetime="{metadata['date']}">{metadata['date']}年</time>
<span class="post__tags">{"".join([f'<a href="https://blog.fuweineng.com/tags/{tag.lower()}/">{tag}</a>' for tag in metadata['tags']])}</span>
</div>
</header>
{featured_image}
<div class="post__content">
{article_content}
</div>
</article>
</div>
</main>
{get_publii_footer()}
<script>window.publiiThemeMenuConfig = {{ mobileMenuMode: 'sidebar', animationSpeed: 300, submenuWidth: 'auto', doubleClickTime: 500, mobileMenuExpandableSubmenus: true, relatedContainerForOverlayMenuSelector: '.navbar', }};</script>
<script defer="defer" src="https://blog.fuweineng.com/assets/js/scripts.min.js"></script>
<script defer="defer" src="./assets/js/universal-dark-mode.js?v={get_version()}"></script>
</body>
</html>'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

if __name__ == '__main__':
    os.chdir('/Users/fuweineng/.openclaw/workspace/blog')
    
    success = 0
    for filename, metadata in hugo_files.items():
        if os.path.exists(filename):
            if convert_hugo_to_publii(filename, metadata):
                print(f"✅ {filename}")
                success += 1
        else:
            print(f"❌ {filename} not found")
    
    print(f"\n完成！成功转换 {success}/{len(hugo_files)} 个页面")
