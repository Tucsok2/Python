from bleach import clean

with open('kys.html', 'r', encoding='utf-8') as html_file:
    html = html_file.read()

    html_cleaned = clean(html)
    print(html)
