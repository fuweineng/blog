#!/bin/bash
DIR="blog/media/videos/tmp"
FONT="/System/Library/Fonts/Hiragino Sans GB.ttc"

# Array of durations and titles/texts
durations=(16.25 20.62 21.28 23.59 19.67 16.80 21.41 11.57)
titles=("交易的底層邏輯：開場" "第一章：低買高賣與博弈" "第二章：繁榮與反轉" "第三章：市場狀態與能量" "第四章：支撐、阻力與心理" "第五章：性格、周期與趨勢" "第六章：複利與倉位控制" "結語：交易閉環")
texts=(
"新手死於追求確定性\n高手生於敬畏概率"
"價格波動是意見不合的體現\n風險是利潤的入場券"
"繁榮往往是欺騙性的信號\n機會誕生於枯竭後的反轉"
"激揚態 vs 萎靡態\n能量消散是轉折的信號"
"支撐與阻力是心理防線\n突破後的角色轉換"
"了解品種性格\n大周期看勢，小周期選位"
"複利的前提是活著\n遵循 2% 準則鎖定風險"
"看勢、選位、防騙、控倉\n在概率遊戲中穩步前行"
)

for i in "${!durations[@]}"; do
    dur=${durations[$i]}
    title=${titles[$i]}
    txt=${texts[$i]}
    echo "Generating segment $i (duration: $dur)..."
    
    # Generate abstract background with title and text overlay
    # Using mandelbrot for a "logic/math" feel
    ffmpeg -y -f lavfi -i "mandelbrot=s=1920x1080:rate=30" \
    -i "$DIR/${i}_audio.mp3" \
    -filter_complex \
    "[0:v]hue=s=0:b=-0.5,drawtext=fontfile='$FONT':text='$title':fontsize=80:fontcolor=white:x=(w-text_w)/2:y=h/2-100:shadowcolor=black:shadowx=2:shadowy=2, \
    drawtext=fontfile='$FONT':text='$txt':fontsize=50:fontcolor=yellow:x=(w-text_w)/2:y=h/2+50:shadowcolor=black:shadowx=2:shadowy=2[v]" \
    -map "[v]" -map 1:a -c:v libx264 -t "$dur" -pix_fmt yuv420p "$DIR/${i}_seg.mp4"
done
