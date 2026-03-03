# 配图说明 - 《时间流逝是观察》

## 需要生成的图片（5 张）

### 1. featured.jpg（封面图）
**尺寸**: 1200x630px
**描述**: 沙漏 + 枯萎/盛开的花朵对比
**风格**: 简约、深刻、温暖色调
**AI 提示词**:
```
A hourglass in the center, left side shows a blooming flower in full color, right side shows a withered flower in sepia tone, soft warm lighting, minimalist composition, philosophical mood, 1200x630
```

---

### 2. plant-lifecycle.jpg（植物生命周期）
**尺寸**: 800x600px
**描述**: 四格图展示种子→发芽→开花→凋谢
**风格**: 自然、纪实、时间序列
**AI 提示词**:
```
Four panel sequence showing plant lifecycle: seed in soil, sprout emerging, flower blooming, petals falling, natural photography style, soft daylight, 800x600
```

---

### 3. street-change.jpg（老街变迁）
**尺寸**: 800x600px
**描述**: 同一条街的新旧对比（split view）
**风格**: 怀旧、纪实、对比强烈
**AI 提示词**:
```
Split screen comparison: left side shows old street with traditional grocery shop and elderly owner, right side shows same street with modern milk tea shop, nostalgic vs contemporary, 800x600
```

---

### 4. time-recording.jpg（记录时间的方式）
**尺寸**: 800x600px
**描述**: 照片墙、日记本、刻度尺等记录时间的物品
**风格**: 温馨、生活化、拼贴感
**AI 提示词**:
```
Flat lay composition: polaroid photos arranged on wall, open diary with handwritten entries, growth chart on door frame, warm natural light, cozy home atmosphere, 800x600
```

---

### 5. sunset-observer.jpg（观察者）
**尺寸**: 800x600px
**描述**: 一个人望着日落或日出的剪影
**风格**: 诗意、宁静、哲理
**AI 提示词**:
```
Silhouette of a person standing alone watching sunset or sunrise, peaceful contemplation, warm golden hour light, minimalist landscape, philosophical mood, 800x600
```

---

## 使用方法

### 方案 A: AI 生成（推荐）
1. 用 Midjourney / DALL-E 3 / Stable Diffusion
2. 复制上面的提示词
3. 生成后保存到对应路径

### 方案 B: 免版权图库
- Unsplash.com
- Pexels.com
- Pixabay.com
搜索关键词：hourglass, plant lifecycle, old street, diary, sunset silhouette

### 方案 C: 暂时用占位图
先用纯色背景 + 文字，之后替换

---

## 图片路径
所有图片放在：`/Users/fuweineng/.openclaw/workspace/blog-temp/media/posts/shi-jian-liu-shi-shi-guan-cha/`

文件名必须匹配：
- `featured.jpg`
- `plant-lifecycle.jpg`
- `street-change.jpg`
- `time-recording.jpg`
- `sunset-observer.jpg`

---

**生成后执行**:
```bash
cd /Users/fuweineng/.openclaw/workspace/blog-temp
git add .
git commit -m "新文章：时间流逝是观察"
git push
```

GitHub Pages 会自动部署到 blog.fuweineng.com
