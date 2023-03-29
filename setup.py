from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def  get_requirments(file_path:str)->List[str]:
  '''

  this function return list of requirments
  '''
  requirments = []
  with open('requirments.txt') as file_obj:
      requirments=file_obj.readlines()
      requirments=[req.replace("/n","") for req in requirments]
      if HYPEN_E_DOT in requirments:
          requirments.remove(HYPEN_E_DOT)
         
  return requirments    
         

setup(name='mlproject',version='0.0.0.1',author='Tejas',author_email='tejabhai1395@gmail.com',packages = find_packages(),install_requirments=get_requirments('requirments.txt'))
