from os import popen

def get_own_extentions() -> dict:
  extensions = popen('code --list-extensions --show-versions')
  extensions = extensions.readlines()
  extensions_list = {}
  for extension in extensions:
    extension = extension.removesuffix('\n')
    author = extension.split('.')[0]
    name = extension.split('.')[1].split('@')[0]
    version = extension.split('@')[1]
    extensions_list[f'{author}.{name}'] = {'author': author, 'name': name, 'version': version}
  return extensions_list