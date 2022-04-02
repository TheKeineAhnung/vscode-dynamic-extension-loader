from os.path import isdir, exists

def generate_shell_file(author_name: str, save_path: str, extensions: dict, save_name: str = "vscode-extension-installer") -> bool:
  file_content = f'''#!/bin/bash
echo "$(tput setaf 6)Welcome to the extension installer!"
echo "You've got the extensions from {author_name}."
echo "You can install only all extensions or none of them."
read -p "Do you want to install all extensions? (y/n) " answer
case ${{answer:0:1}} in (n|N)
  echo "$(tput setaf 196)You decided to install none of them."
  read -n 1 -r -p "Press any key to close this window..."
  exit
esac
'''
  file_content += 'echo $(tput setaf 3) \n'
  for extension in extensions:
    file_content += f'''code --install-extension {extensions[extension]['author']}.{extensions[extension]['name']}@{extensions[extension]['version']} \n'''
  
  file_content += f'''echo "$(tput setaf 34)All extensions from {author_name} have been installed!"
read -n 1 -r -p "Press any key to close this window..."
exit'''
  
  if not isdir(save_path):
    print("The path you entered is not a directory.")
    return False
  
  if not save_path.endswith('\\'):
    save_path += '\\'
    
  if save_name.endswith('.sh'):
    save_name.removesuffix('.sh')
  
  if exists(save_path + save_name + '.sh'):
    number = 1
    new_save_name = save_name
    while exists(save_path + new_save_name + '.sh'):
      new_save_name = save_name + "_" + str(number)
      number += 1
    save_name += new_save_name
  
  save_name += '.sh'
  
  file = open(save_path + save_name, 'w')
  file.write(file_content)
  file.close()
  
  return True