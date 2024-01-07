from bs4 import BeautifulSoup

def convert_to_js(html):
    soup = BeautifulSoup(html, 'html.parser')
    js_render = ''

    tag_counts = {}

    def process_tag(tag):
        nonlocal js_render
        if tag.name not in tag_counts:
            tag_counts[tag.name] = 1
        else:
            tag_counts[tag.name] += 1

        tag_variable = f'{tag.name}{tag_counts[tag.name]}' if tag_counts[tag.name] > 1 else tag.name
        js_render += f'var {tag_variable} = document.createElement("{tag.name}")\n'

        for attr, value in tag.attrs.items():
            if attr == 'class':
                classes = ' '.join(value)
                js_render += f'{tag_variable}.classList.add("{classes}")\n'
            elif attr == 'id':
                js_render += f'{tag_variable}.id = "{value}"\n'
            else:
                js_render += f'{tag_variable}.{attr} = "{value}"\n'

        if tag.name != 'html':
            js_render += f'{tag_variable}.textContent = "{tag.get_text(strip=True)}"\n'

        if tag.parent and tag.parent.name in tag_counts:
            parent_variable = f'{tag.parent.name}{tag_counts[tag.parent.name]}'
            js_render += f'{parent_variable}.appendChild({tag_variable})\n'
        elif tag.parent:
            js_render += f'{tag.parent.name}.appendChild({tag_variable})\n'

    for tag in soup.find_all():
        process_tag(tag)

    return js_render

# Example usage
input_html = '''
    <div class="user-container">
        <div class="image-container">
            <img src="userimage.png" alt="">
        </div>
        <div class="status-container">
            <div class="detailscontainer">
                <div class="flex hstack">
                    <img src="gameimage.png" alt="">
                    <div class="text-container">
                        <div class="flex vstack">
                            <h1 class="username" id="username">Username</h1>
                            <p class="status" id="username">Status</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

js_render_output = convert_to_js(input_html)
print(js_render_output)
