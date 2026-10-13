import os

ad_head = '''<script data-cfasync="false" src="https://bauval.org/14/8b865d247870399318aecd8b06eccc55"></script>
<script>
  atOptions = {
    'key' : '9ce4e6a09339b1ff4c0f893f4d0f53af',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/9ce4e6a09339b1ff4c0f893f4d0f53af"></script>
<script async="async" data-cfasync="false" src="https://bauval.org/21/3f26e92158b3cd86dfe89955ff799a0d"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-3f26e92158b3cd86dfe89955ff799a0d"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'combat.html', 'weapons.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '9ce4e6a09339b1ff4c0f893f4d0f53af' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-3f26e92158b3cd86dfe89955ff799a0d' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')