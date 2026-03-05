/**
 * 通用深色/浅色模式切换
 * 支持：Publii + Hugo + 自定义 HTML
 * 功能:
 * 1. 默认跟随系统设置
 * 2. 支持手动切换 (浅色/深色/自动)
 * 3. 保存用户偏好到 localStorage
 * 版本：v2026.03.05
 */

(function() {
  'use strict';

  const THEME_KEY = 'blog-theme-preference';
  const VALID_THEMES = ['light', 'dark', 'auto'];

  /**
   * 获取当前主题
   */
  function getTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (VALID_THEMES.includes(saved)) {
      return saved;
    }
    return 'auto'; // 默认跟随系统
  }

  /**
   * 保存主题偏好
   */
  function saveTheme(theme) {
    localStorage.setItem(THEME_KEY, theme);
  }

  /**
   * 应用主题
   */
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // 更新按钮图标
    updateSwitchButton(theme);
    
    // 通知页面主题已变化（用于自定义样式）
    window.dispatchEvent(new CustomEvent('theme-change', { 
      detail: { theme: theme } 
    }));
  }

  /**
   * 更新切换按钮图标
   */
  function updateSwitchButton(theme) {
    const btn = document.querySelector('.theme-switch');
    if (!btn) return;

    const isDark = theme === 'dark' || 
                   (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    
    btn.setAttribute('aria-label', isDark ? '切换到浅色模式' : '切换到深色模式');
    btn.setAttribute('title', isDark ? '切换到浅色模式' : '切换到深色模式');
  }

  /**
   * 切换到下一个主题
   */
  function toggleTheme() {
    const current = getTheme();
    const next = current === 'light' ? 'dark' : 
                 current === 'dark' ? 'auto' : 'light';
    
    saveTheme(next);
    applyTheme(next);
    
    // 添加动画反馈
    const btn = document.querySelector('.theme-switch');
    if (btn) {
      btn.style.transform = 'scale(0.9)';
      setTimeout(() => {
        btn.style.transform = '';
      }, 150);
    }
  }

  /**
   * 监听系统主题变化 (仅在 auto 模式下)
   */
  function listenSystemTheme() {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    const handler = (e) => {
      if (getTheme() === 'auto') {
        applyTheme('auto');
      }
    };

    mediaQuery.addEventListener('change', handler);
    return handler;
  }

  /**
   * 创建主题切换按钮
   */
  function createSwitchButton() {
    // 检查是否已存在
    if (document.querySelector('.theme-switch')) {
      return;
    }

    const btn = document.createElement('button');
    btn.className = 'theme-switch';
    btn.innerHTML = `
      <svg class="moon-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M21.407 12.829a9 9 0 0 1-9.828 9.574c-4.605-.386-8.137-4.55-7.979-9.177.148-4.349 3.647-7.903 7.99-8.051a9 9 0 0 1 9.817 7.654zm-9.818-7.654a.5.5 0 0 0-.489.49c-.002.276.222.5.499.5h5.002a.5.5 0 0 0 .5-.5.5.5 0 0 0-.5-.5h-5.002zm0 15.308a.5.5 0 0 0-.489.49c-.002.276.222.5.499.5h5.002a.5.5 0 0 0 .5-.5.5.5 0 0 0-.5-.5h-5.002zM7.5 12a.5.5 0 0 0-.5.5v5.002a.5.5 0 0 0 .5.5.5.5 0 0 0 .5-.5V12.5a.5.5 0 0 0-.5-.5zm0-10a.5.5 0 0 0-.5.5v5.002a.5.5 0 0 0 .5.5.5.5 0 0 0 .5-.5V2.5a.5.5 0 0 0-.5-.5zm13.107 10.807a.5.5 0 0 0-.707.707l3.536 3.536a.5.5 0 0 0 .707-.707l-3.536-3.536zM3.607 3.607a.5.5 0 0 0-.707.707l3.536 3.536a.5.5 0 0 0 .707-.707L3.607 3.607zm12.728 12.728a.5.5 0 0 0-.707.707l3.536 3.536a.5.5 0 0 0 .707-.707l-3.536-3.536zM7.143 7.143a.5.5 0 0 0-.707.707l3.536 3.536a.5.5 0 0 0 .707-.707L7.143 7.143z"/>
      </svg>
      <svg class="sun-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"/>
      </svg>
    `;
    btn.onclick = toggleTheme;
    
    document.body.appendChild(btn);
  }

  /**
   * 初始化
   */
  function init() {
    const theme = getTheme();
    applyTheme(theme);
    createSwitchButton();
    listenSystemTheme();
  }

  // DOM 加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
