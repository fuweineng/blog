#!/usr/bin/env python3
"""
统一 Hugo 页面结构为 Publii 风格
目标：让所有页面有相同的导航、页脚和布局
"""

import os
import re

# 需要更新的 Hugo 风格页面
hugo_files = [
    'li-cha-shi-yi-xiang-chu-lai-de.html',
    'nai-cha-xian-huo-qu-de-she-xiang.html',
    'wen-ding-shi-zui-zhong-yao-de-cai-fu.html',
    'yi-lai-de-li-liang.html',
]

# Publii 风格的导航栏
publii_nav = '''
<header class="header" id="js-header">
  <a href="/" class="logo">符伟能的网络日志</a>
  <nav class="navbar js-navbar">
    <button class="navbar__toggle js-toggle" aria-label="Menu">
      <span class="navbar__toggle-box">
        <span class="navbar__toggle-inner">Menu</span>
      </span>
    </button>
    <ul class="navbar__menu">
      <li><a href="/pc-qing-huai-ruan-jian-tui-jian.html" target="_self">好用软件</a></li>
      <li><a href="/li-an-shang-xin-wen.html" target="_self">链上新闻</a></li>
      <li><a href="/about.html" target="_self">咋了</a></li>
    </ul>
  </nav>
</header>
'''

# Publii 风格的页脚
publii_footer = '''
<footer class="footer">
  <div class="footer__copyright">Powered by Publii · 小明的博客</div>
</footer>
'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 替换简单的 header 为 Publii 风格
    simple_header_pattern = r'<header>\s*<nav>.*?</nav>\s*</header>'
    content = re.sub(simple_header_pattern, publii_nav.strip(), content, flags=re.DOTALL)
    
    # 2. 替换简单的 footer 为 Publii 风格
    simple_footer_pattern = r'<footer>.*?</footer>'
    content = re.sub(simple_footer_pattern, publii_footer.strip(), content, flags=re.DOTALL)
    
    # 3. 添加 wrapper 到 main
    content = re.sub(r'<main>', '<main class="main"><div class="wrapper">', content)
    content = re.sub(r'</main>', '</div></main>', content)
    
    # 4. 添加 post class 到 article
    content = re.sub(r'<article>', '<article class="post">', content)
    
    # 5. 更新 meta 信息样式
    content = re.sub(r'<div class="meta">', '<div class="post__meta">', content)
    
    # 6. 更新标题样式
    content = re.sub(r'<h1>', '<h1 class="post__title">', content)
    
    # 7. 更新内容区域样式
    content = re.sub(r'<div class="content">', '<div class="post__content">', content)
    
    # 8. 更新特色图片样式
    content = re.sub(r'<figure class="featured-image">', '<figure class="post__image">', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filepath}")

if __name__ == '__main__':
    for filename in hugo_files:
        filepath = filename
        if os.path.exists(filepath):
            update_file(filepath)
        else:
            print(f"❌ {filepath} not found")
    
    print("\n完成！所有 Hugo 页面已更新为 Publii 风格结构")
