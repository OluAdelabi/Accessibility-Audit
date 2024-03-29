import os
os.system('pip install --upgrade pip')

packages = [
    'requests',
    'urllib3',
    'selenium',
    'axe_selenium_python'
]

def install_and_import(packages):
    for package in packages:
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            os.system('pip install {}'.format(package))
            # from pip._internal import main
            # main(['install', package])
        finally:
            globals()[package] = importlib.import_module(package)

install_and_import(packages)

