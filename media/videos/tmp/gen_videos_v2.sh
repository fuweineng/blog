#!/bin/bash
DIR="blog/media/videos/tmp"

durations=(16.25 20.62 21.28 23.59 19.67 16.80 21.41 11.57)
# Filters for each segment
filters=(
"showwaves=s=1920x1080:mode=line:colors=cyan"
"showwaves=s=1920x1080:mode=p2p:colors=green"
"avectorscope=s=1920x1080:colors=red"
"showfreqs=s=1920x1080:colors=yellow"
"showvolume=s=1920x1080:c=blue"
"showwaves=s=1920x1080:mode=line:colors=magenta"
"showwaves=s=1920x1080:mode=p2p:colors=white"
"showwaves=s=1920x1080:mode=line:colors=yellow"
)

for i in 1 2 3 4 5 6 7; do
    dur=${durations[$i]}
    flt=${filters[$i]}
    echo "Generating segment $i..."
    ffmpeg -y -i "$DIR/${i}_audio.mp3" -f lavfi -i "mandelbrot=s=1920x1080:maxiter=256:rate=30" \
    -filter_complex "[1:v]hue=s=0:b=-0.7[bg];[0:a]$flt:rate=30[waves];[bg][waves]overlay=shortest=1[v]" \
    -map "[v]" -map 0:a -c:v libx264 -t "$dur" -pix_fmt yuv420p "$DIR/${i}_seg.mp4"
done
