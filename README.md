# video_analyzer

process-

extract bitrate from file:
ffmpeg -i filename

parse video into frames:
ffmpeg -i input.file thumb%04d.png -hide_banner

use python to do image analysis on frames-
find first frame with green LED
find last frame with green LED
use frame count + framerate to calculate time between the two
output time
