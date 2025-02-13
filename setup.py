from setuptools import setup, find_packages

setup(
  name='package_name',
  version='1.0.0',
  author='your_nickname',
  description='This is my first module',
  long_description_content_type='text/markdown',
  url='https://github.com/DGaliaf/pkg',
  packages=find_packages(),
  install_requires=["build==1.2.2.post1","certifi==2025.1.31","charset-normalizer==3.4.1","docutils==0.21.2","id==1.5.0","idna==3.10","jaraco.classes==3.4.0","jaraco.context==6.0.1","jaraco.functools==4.1.0","keyring==25.6.0","markdown-it-py==3.0.0","mdurl==0.1.2","more-itertools==10.6.0","multis==1.0.3","nh3==0.2.20","packaging==24.2","Pygments==2.19.1","pyproject_hooks==1.2.0","readme_renderer==44.0","requests==2.32.3","requests-toolbelt==1.0.0","rfc3986==2.0.0","rich==13.9.4","twine==6.1.0","urllib3==2.3.0"],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'https://github.com/DGaliaf/pkg'
  },
  python_requires='>=3.7'
)