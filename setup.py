from setuptools import setup

setup(name='clean_folder_d_lyfenko',
      version='0.0.3',
      description='script for cleaning folders',
      url='https://github.com/Lyfenko/clean_folder_d_lyfenko',
      author='Dmytro Lyfenko',
      author_email='d.lyfenko@gmail.com',
      license='MIT',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )