#!/usr/bin/env python3
"""
移除所有 HTML 文件中的深色模式和统一样式引用
恢复纯 Publii 样式
"""

import os
import re
from pathlib import Path

BLOG_DIR = '/Users/fuweineng/.openclaw/workspace/blog'

# 要移除的 CSS/JS 引用
CSS_TO_REMOVE = [
    r'<link rel="stylesheet" href="\.?/assets/css/universal-dark-mode\.css[^"]*">',
    r'<link rel="stylesheet" href="\.?/assets/css/dark-mode\.css[^"]*">',
]

JS_TO_REMOVE = [
    r'<script[^>]* src="\.?/assets/js/universal-dark-mode\.js[^"]*"[^>]*></script>',
    r'<script[^>]* src="\.?/assets/js/dark-mode\.js[^"]*"[^>]*></script>',
    r'<script[^>]* src="\.?/assets/js/unify-styles\.js[^"]*"[^>]*></script>',
]

def remove_references(filepath):
    """移除文件中的自定义样式引用"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 移除 CSS
    for pattern in CSS_TO_REMOVE:
        content = re.sub(pattern, '', content)
    
    # 移除 JS
    for pattern in JS_TO_REMOVE:
        content = re.sub(pattern, '', content)
    
    # 清理多余的空行
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    modified = 0
    skipped = 0
    
    # 处理所有 HTML 文件
    for file in Path(BLOG_DIR).glob('**/*.html'):
        # 跳过 assets 目录
        if 'assets' in str(file):
            continue
        
        if remove_references(str(file)):
            modified += 1
            print(f"✅ {file.relative_to(BLOG_DIR)}")
        else:
            skipped += 1
    
    print(f"\n🎉 完成！修改了 {modified} 个文件，跳过了 {skipped} 个文件")

if __name__ == '__main__':
    main()
