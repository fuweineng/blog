#!/bin/bash
# 生成简单占位图片（使用 ImageMagick）

# 检查是否有 ImageMagick
if ! command -v convert &> /dev/null; then
    echo "❌ ImageMagick 未安装，请先运行：brew install imagemagick"
    exit 1
fi

# 封面图 1200x630
convert -size 1200x630 xc:'#1a1a2e' \
    -gravity center \
    -pointsize 48 \
    -fill '#e94560' \
    -annotate 0 "时间流逝是观察" \
    -pointsize 24 \
    -fill '#ffffff' \
    -annotate +0+40 "当主体可以看到事物的出现和消亡" \
    featured.jpg

# 植物生命周期 800x600
convert -size 800x600 xc:'#0f3460' \
    -gravity center \
    -pointsize 36 \
    -fill '#e94560' \
    -annotate 0 "🌱 → 🌿 → 🌸 → 🍂" \
    -pointsize 20 \
    -fill '#ffffff' \
    -annotate +0+40 "Plant Lifecycle" \
    plant-lifecycle.jpg

# 老街变迁 800x600
convert -size 800x600 xc:'#16213e' \
    -gravity center \
    -pointsize 32 \
    -fill '#e94560' \
    -annotate 0 "🏚️ → 🏪 → 📦" \
    -pointsize 20 \
    -fill '#ffffff' \
    -annotate +0+40 "Street Change" \
    street-change.jpg

# 记录时间 800x600
convert -size 800x600 xc:'#1a1a2e' \
    -gravity center \
    -pointsize 32 \
    -fill '#e94560' \
    -annotate 0 "📸 📔 📏" \
    -pointsize 20 \
    -fill '#ffffff' \
    -annotate +0+40 "Time Recording" \
    time-recording.jpg

# 观察者 800x600
convert -size 800x600 xc:'#0f3460' \
    -gravity center \
    -pointsize 32 \
    -fill '#e94560' \
    -annotate 0 "🌅" \
    -pointsize 20 \
    -fill '#ffffff' \
    -annotate +0+40 "Observer at Sunset" \
    sunset-observer.jpg

echo "✅ 占位图片生成完成！"
ls -la *.jpg
