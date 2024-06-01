from PIL import Image
import numpy as np
from art import text2art
import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Print the provided content.")
    parser.add_argument("--content", type=str, required=True, help="Content to be printed")
    
    args = parser.parse_args()
    
    client = OpenAI()
    print("Generating image for Our conversation...")
    response = client.images.generate(
    model="dall-e-3",
    prompt="please make emotional paintting based on this conversation logs. when generate paintin please focus on human part. draw image" + args.content,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_path = "./tes.webp"
    image_url = response.data[0].url
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")

    # 이미지를 불러오기
    image = Image.open(image_path).convert('L')  # 그레이스케일로 변환
    image = image.resize((80, 40))  # 크기 조정
    image_np = np.array(image)
    # ASCII 문자 목록
    ascii_chars = "@%#*+=-:. "
    # 픽셀 값을 ASCII 문자로 변환
    def pixel_to_ascii(pixel):
        return ascii_chars[pixel // 32]
    # 이미지의 픽셀을 ASCII 문자로 변환
    ascii_image = "\n".join(
        "".join(pixel_to_ascii(pixel) for pixel in row)
        for row in image_np
    )
    # ASCII 아트를 터미널에 출력
    print(ascii_image)

    #print(args.content)

if __name__ == "__main__":
    main()
