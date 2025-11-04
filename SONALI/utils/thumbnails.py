# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================


import os
import re
import aiohttp
import aiofiles
from SONALI import app
from config import YOUTUBE_IMG_URL
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from youtubesearchpython.__future__ import VideosSearch

def clear(text):
    return re.sub("\s+", " ", text).strip()

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(image.size[0] * min(widthRatio, heightRatio))
    newHeight = int(image.size[1] * min(widthRatio, heightRatio))
    return image.resize((newWidth, newHeight))

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        youtube = youtube.convert("RGBA")

        
        background = youtube.resize((1280, 720)).filter(ImageFilter.GaussianBlur(radius=10))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)  

        draw = ImageDraw.Draw(background)

    
        center_thumb_size = (942, 422)
        center_thumb = youtube.resize(center_thumb_size)

        border_size = 14
        bordered_center_thumb = Image.new("RGBA", (center_thumb_size[0] + 2 * border_size, center_thumb_size[1] + 2 * border_size), (255, 255, 255))
        bordered_center_thumb.paste(center_thumb, (border_size, border_size))

        
        pos_x = (1280 - bordered_center_thumb.size[0]) // 2
        pos_y = ((720 - bordered_center_thumb.size[1]) // 2) - 30  

        background.paste(bordered_center_thumb, (pos_x, pos_y))

        
        arial = ImageFont.truetype("SONALI/assets/font2.ttf", 30)
        font = ImageFont.truetype("SONALI/assets/font.ttf", 30)
        bold_font = ImageFont.truetype("SONALI/assets/font.ttf", 33)

    
        text_size = draw.textsize("@PurviBots   ", font=font)
        draw.text((1280 - text_size[0] - 10, 10), "PurviBots   ", fill="yellow", font=font)

    
        draw.text(
            (55, 580),  
            f"{channel} | {views[:23]}",
            (255, 255, 255),
            font=arial,
        )

        
        draw.text(
            (57, 620), 
            title,
            (255, 255, 255),
            font=font,
        )

        
        draw.text((55, 655), "00:00", fill="white", font=bold_font)

        
        start_x = 150
        end_x = 1130
        line_y = 670
        draw.line([(start_x, line_y), (end_x, line_y)], fill="white", width=4)

        
        duration_text_size = draw.textsize(duration, font=bold_font)
        draw.text((end_x + 10, 655), duration, fill="white", font=bold_font)

        
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass

        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
        
