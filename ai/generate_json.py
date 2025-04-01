import os
import json

def find_md_files(root_dir):
    """
    Recursively find all .md files in the given directory.
    """
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                full_path = os.path.join(dirpath, filename)
                md_files.append(full_path)
    return md_files

def convert_path(file_path, root_dir, domain='https://docs.hypernode.com'):
    """
    Convert the file path to the desired URL format.
    """
    relative_path = os.path.relpath(file_path, root_dir)
    html_path = os.path.splitext(relative_path)[0] + '.html'
    url = os.path.join(domain, html_path).replace('\\', '/')
    return url

def create_json(md_files, root_dir):
    """
    Create a list of dictionaries with URL and markdown body.
    """
    data = []
    for file_path in md_files:
        url = convert_path(file_path, root_dir)
        with open(file_path, 'r', encoding='utf-8') as f:
            body = f.read()
        data.append({
            "url": url,
            "body": body
        })
    return data

def main():
    root_dir = '../docs'
    md_files = find_md_files(root_dir)
    data = create_json(md_files, root_dir)
    with open('hypernode-docs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"JSON file created with {len(data)} entries.")

if __name__ == '__main__':
    main()
