import os
from PIL import Image

import os
from PIL import Image

def compress_image(image_path, max_resolution=128, quality=80):
    """
    压缩图片

    Args:
        image_path (str): 图片文件路径
        max_resolution (int): 最大分辨率限制，默认为128
        quality (int): 压缩质量，默认为80

    Returns:
        int: 压缩量，单位为KB
    """
    image = Image.open(image_path)
    width, height = image.size

    if width > height:
        if width > max_resolution:
            new_width = max_resolution
            new_height = int(height * max_resolution / width)
        else:
            new_width = width
            new_height = height
    else:
        if height > max_resolution:
            new_height = max_resolution
            new_width = int(width * max_resolution / height)
        else:
            new_width = width
            new_height = height

    resized_image = image.resize((new_width, new_height))
    original_size = os.path.getsize(image_path)
    resized_image.save(image_path, quality=quality)
    compressed_size = os.path.getsize(image_path)
    compression_amount = original_size - compressed_size
    return compression_amount/1000

# 读取原始图片
dirname = "src/.vuepress/public/assets/sign"
imgs = os.listdir("src/.vuepress/public/assets/sign")
for img in imgs:
    image_path = os.path.join(dirname, img)
    comp = compress_image(image_path, max_resolution=128, quality=80)

    print(f"Compression amount: {comp/1000} KB.")

