import pip

_all_ = [
    'click>=8.1.3',
    'Flask>=2.2.3',
    'itsdangerous>=2.1.2',
    'Jinja2>=3.1.2',
    'MarkupSafe>=2.1.2',
    'pyodbc==4.0.34',
    'Werkzeug>=2.2.3',
]

others = ["pyodbc==4.0.35",]
darwin = ["pyodbc==4.0.34"]

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform

    install(_all_) 
    if platform == 'darwin': # MacOS
        install(darwin)
    else:
        install(others)