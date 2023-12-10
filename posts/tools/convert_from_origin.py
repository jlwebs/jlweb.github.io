import os
from datetime import datetime

def create_blog_post(filepath):
    # Extract folder name as tags (if not in root directory)
    folder_name = os.path.basename(os.path.dirname(filepath))
    tags = [folder_name] if folder_name != '.' else []

    # Construct the date string in YYYY-MM-DD format
    formatted_date = datetime.fromtimestamp(os.path.getctime(filepath)).strftime('%Y-%m-%d')

    # Extract the title from the original filename
    filename = os.path.basename(filepath)
    title = os.path.splitext(filename)[0]

    # Construct the new filename with the date and title
    new_filename = f"output/{formatted_date}-{title.lower().replace(' ', '-')}.md"

    # Construct the Front Matter for the blog post
    front_matter = f'''---
layout: post
title: "{title}"
date: {formatted_date}
categories: jekyll
tags: {tags}
comments: true
---

'''

    # Read content from original file
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Write new post file with Front Matter and content
    with open(new_filename, 'w', encoding='utf-8') as new_file:
        new_file.write(front_matter)
        new_file.write(content)

    print(f"Created new blog post: {new_filename}")

# Recursive function to process all .md files in a directory
def process_directory(directory):
    os.makedirs("output", exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.md'):
                create_blog_post(file_path)

# Usage example: Provide the current directory
process_directory(".")
