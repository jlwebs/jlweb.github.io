import os
import re
import requests
from datetime import datetime
from urllib.parse import urlparse

def download_image(url, output_folder):
    filename = os.path.basename(urlparse(url).path)
    output_path = os.path.join(output_folder, filename)

    if os.path.exists(output_path):
        print(f"Image '{filename}' already exists. Skipping download.")
        return f"../images/{filename}"

    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        return f"../images/{filename}"
    return None

def create_blog_post(filepath):
    folder_name = os.path.basename(os.path.dirname(filepath))
    tags = [folder_name] if folder_name != '.' else []

    formatted_date = datetime.fromtimestamp(os.path.getctime(filepath)).strftime('%Y-%m-%d')

    filename = os.path.basename(filepath)
    title = os.path.splitext(filename)[0]

    new_filename = f"output/{formatted_date}-{title.lower().replace(' ', '-')}.md"
    output_folder = os.path.dirname(new_filename)
    os.makedirs(output_folder, exist_ok=True)

    front_matter = f'''---
layout: post
title: "{title}"
date: {formatted_date}
categories: jekyll
tags: {tags}
comments: true
---

'''

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        # Find and replace image links
        image_links = re.findall(r'!\[.*?\]\((.*?)\)', content)
        for link in image_links:
            if link.startswith('http'):
                local_path = download_image(link, os.path.join(output_folder, '..\images'))
                if local_path:
                    content = content.replace(link, local_path)

    with open(new_filename, 'w', encoding='utf-8') as new_file:
        new_file.write(front_matter)
        new_file.write(content)

    print(f"Created new blog post: {new_filename}")

def process_directory(directory):
    os.makedirs("output/../images", exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.md'):
                create_blog_post(file_path)

process_directory(".")
