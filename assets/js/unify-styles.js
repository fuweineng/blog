/**
 * 统一博客样式脚本
 * 功能：为 Hugo/自定义页面添加 Publii 风格的导航和页脚
 * 目标：让所有页面视觉风格一致
 */

(function() {
  'use strict';

  // 检查是否是 Publii 页面
  const isPublii = document.querySelector('.navbar') || document.querySelector('.header');
  
  // 如果不是 Publii 页面，添加统一导航和页脚
  if (!isPublii) {
    addUnifiedHeader();
    addUnifiedFooter();
    updatePageStyles();
  }

  /**
   * 添加统一导航栏
   */
  function addUnifiedHeader() {
    const header = document.createElement('header');
    header.className = 'header unified-header';
    header.innerHTML = `
      <a href="/" class="logo">符伟能的网络日志</a>
      <nav class="navbar">
        <button class="navbar__toggle" aria-label="Menu">
          <span class="navbar__toggle-box">
            <span class="navbar__toggle-inner">Menu</span>
          </span>
        </button>
        <ul class="navbar__menu">
          <li><a href="/">首页</a></li>
          <li><a href="/pc-qing-huai-ruan-jian-tui-jian.html">好用软件</a></li>
          <li><a href="/li-an-shang-xin-wen.html">链上新闻</a></li>
          <li><a href="/about.html">咋了</a></li>
        </ul>
      </nav>
    `;
    
    document.body.insertBefore(header, document.body.firstChild);
  }

  /**
   * 添加统一页脚
   */
  function addUnifiedFooter() {
    const footer = document.createElement('footer');
    footer.className = 'footer unified-footer';
    footer.innerHTML = `
      <div class="footer__copyright">
        <p>Powered by Publii · 小明的博客</p>
        <p>© 2026 符伟能 · All rights reserved</p>
      </div>
    `;
    
    document.body.appendChild(footer);
  }

  /**
   * 更新页面样式以匹配 Publii 风格
   */
  function updatePageStyles() {
    // 添加 body class
    document.body.classList.add('unified-page');
    
    // 包装 main 内容
    const main = document.querySelector('main');
    if (main && !main.classList.contains('wrapper')) {
      main.classList.add('wrapper');
    }
    
    // 更新文章样式
    const article = document.querySelector('article');
    if (article) {
      article.classList.add('post');
      
      // 包装标题
      const h1 = article.querySelector('h1');
      if (h1 && !h1.classList.contains('post__title')) {
        h1.classList.add('post__title');
      }
      
      // 包装内容
      const content = article.querySelector('.content');
      if (content && !content.classList.contains('post__content')) {
        content.classList.add('post__content');
      }
      
      // 包装 meta 信息
      const meta = article.querySelector('.meta');
      if (meta && !meta.classList.contains('post__meta')) {
        meta.classList.add('post__meta');
      }
    }
  }

  // 移动端菜单切换
  document.addEventListener('click', function(e) {
    if (e.target.closest('.navbar__toggle')) {
      const navbar = e.target.closest('.navbar');
      navbar.classList.toggle('navbar--open');
    }
  });

})();
