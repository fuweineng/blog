# 🌙 通用深色/浅色模式

支持 **Publii** + **Hugo** + **自定义 HTML** 的通用深色模式解决方案。

---

## 📦 文件说明

### CSS 文件
- `universal-dark-mode.css` - 通用深色模式样式（支持 Publii + Hugo）
- `dark-mode.css` - 旧版本（仅支持 Publii，保留向后兼容）

### JS 文件
- `universal-dark-mode.js` - 通用深色模式切换脚本
- `dark-mode.js` - 旧版本（保留向后兼容）

---

## 🚀 使用方法

### 方法 1: 直接引入（推荐）

在 HTML 的 `<head>` 中添加：

```html
<link rel="stylesheet" href="./assets/css/universal-dark-mode.css">
```

在 `</body>` 前添加：

```html
<script defer="defer" src="./assets/js/universal-dark-mode.js"></script>
```

### 方法 2: Publii 主题集成

编辑 Publii 主题的 `head.hbs` 或 `header.hbs`：

```handlebars
{{! 在 </head> 前添加 }}
<link rel="stylesheet" href="{{cssUrl}}/universal-dark-mode.css">
```

编辑 `footer.hbs`：

```handlebars
{{! 在 </body> 前添加 }}
<script defer="defer" src="{{jsUrl}}/universal-dark-mode.js"></script>
```

### 方法 3: Hugo 主题集成

编辑 Hugo 主题的 `layouts/_default/baseof.html` 或 `layouts/partials/head.html`：

```html
{{ if .Site.Params.darkMode.enable }}
  <link rel="stylesheet" href="{{ "/assets/css/universal-dark-mode.css" | relURL }}">
{{ end }}
```

在 `layouts/partials/footer.html`：

```html
{{ if .Site.Params.darkMode.enable }}
  <script defer="defer" src="{{ "/assets/js/universal-dark-mode.js" | relURL }}"></script>
{{ end }}
```

---

## 🎨 功能特性

### 三种模式
1. **浅色模式** - 始终使用浅色主题
2. **深色模式** - 始终使用深色主题
3. **自动模式** - 跟随系统设置（默认）

### 切换逻辑
```
页面加载 → 读取 localStorage → 应用偏好
点击按钮 → 浅色 → 深色 → 自动 → 循环
```

### 用户偏好保存
- 使用 `localStorage` 保存用户选择
- 下次访问自动应用偏好
- 支持系统主题变化监听（自动模式）

---

## 🎯 支持的主题类名

### Publii
- `.header`, `.navbar`, `.logo`
- `.post`, `.c-card`, `.post__title`
- `.content`, `.content__entry`
- `.footer`, `.pagination`

### Hugo
- `.main-content`, `.content-wrapper`, `.article`
- `.article-header`, `.article-title`, `.article-content`
- `.article-tags`, `.article-categories`
- `.site-footer`

### 通用元素
- `blockquote`, `code`, `pre`, `table`
- `input`, `textarea`, `button`
- 链接、列表、图片说明等

---

## 🎨 配色方案

### 浅色模式（默认）
```css
背景：#FFFFFF
卡片：#FFFFFF
文字：#000000
次要文字：#666666
链接：#ff4d6a (粉色)
```

### 深色模式
```css
背景：#1a1a1b (深灰黑)
卡片：#1a1a1b
文字：#E8E8E8 (浅灰白)
次要文字：#9D9D9D (中灰)
链接：#ff4d6a (保持品牌色)
```

---

## 📱 响应式设计

### 桌面端
- 切换按钮：右上角固定 (top: 2rem, right: 2rem)
- 按钮尺寸：56x56px

### 移动端（≤768px）
- 切换按钮：右上角 (top: 1rem, right: 1rem)
- 按钮尺寸：48x48px

---

## 🔧 自定义配置

### 修改主题色

编辑 `universal-dark-mode.css`：

```css
:root {
  --accent-color: #ff4d6a;  /* 主题色 */
  --link-color: #ff4d6a;    /* 链接颜色 */
  --link-hover: #ff7a92;    /* 链接悬停 */
}
```

### 修改深色模式背景

```css
[data-theme="dark"] {
  --bg-primary: #1a1a1b;    /* 主背景 */
  --bg-secondary: #252526;  /* 次要背景 */
  --bg-card: #1a1a1b;       /* 卡片背景 */
}
```

### 禁用切换按钮

如果你只想使用 CSS 变量，不想要切换按钮：

```css
.theme-switch {
  display: none;
}
```

然后用其他方式控制 `data-theme` 属性。

---

## 🧪 测试方法

### 强制刷新浏览器
- **macOS**: `Cmd + Shift + R`
- **Windows**: `Ctrl + Shift + R`

### 测试步骤
1. 访问网站
2. 点击右上角 🌙 按钮
3. 切换主题：浅色 → 深色 → 自动
4. 刷新页面，偏好应该被记住

### 清除缓存测试
```javascript
// 浏览器控制台执行
localStorage.removeItem('blog-theme-preference');
location.reload();
```

---

## 📊 浏览器兼容性

| 浏览器 | 版本 | 支持 |
|--------|------|------|
| Chrome | 60+ | ✅ |
| Firefox | 55+ | ✅ |
| Safari | 12+ | ✅ |
| Edge | 79+ | ✅ |
| iOS Safari | 13+ | ✅ |
| Android Chrome | 80+ | ✅ |

---

## 🐛 常见问题

### Q: 深色模式没有生效？
**A**: 
1. 检查 CSS 和 JS 文件是否正确引入
2. 强制刷新浏览器缓存 (`Cmd+Shift+R`)
3. 检查浏览器控制台是否有错误

### Q: 切换按钮不显示？
**A**:
1. 检查 JS 文件是否正确加载
2. 检查是否有其他脚本冲突
3. 查看浏览器控制台错误

### Q: 某些元素没有适配深色模式？
**A**:
1. 检查元素的 class 名是否在支持列表中
2. 可以自定义 CSS 添加支持
3. 提交 issue 请求添加支持

---

## 📝 更新日志

### v2026.03.05
- ✅ 支持 Publii 和 Hugo 主题
- ✅ 统一配色方案
- ✅ 优化移动端体验
- ✅ 添加事件通知机制
- ✅ 改进浏览器兼容性

### v2026.03.01 (旧版本)
- ✅ 初始版本（仅支持 Publii）

---

## 📄 许可证

MIT License - 可自由使用和修改

---

## 🌟 示例网站

- 小明的博客：https://blog.fuweineng.com/

---

_最后更新：2026-03-05_
