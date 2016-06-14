import webbrowser
import os


def open_in_browser(html):
    path = os.path.abspath('temp.html')
    with open(path, 'w') as f:
        f.write(html)
    url = 'file://' + path
    webbrowser.open(url)



