from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='minesweeper_model',
      version='0.0.1',
      description='Tools to model a Minesweeper game and interact with it programmatically.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Ilkut Kutlar',
      author_email='ilkutkutlar@gmail.com',
      url='https://github.com/ilkutkutlar/minesweeper_model',
      download_url='https://github.com/ilkutkutlar/minesweeper_model/archive/v0.0.1.tar.gz',
      keywords=['minesweeper', 'model'],
      license='MIT',
      packages=['minesweeper_model'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6'
      ],
      )
