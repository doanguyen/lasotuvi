from setuptools import setup

setup(name='lasotuvi',
      version='0.1.1',
      description='Chương trình an sao tử vi mã nguồn mở',
      url='https://github.com/doanguyen/lasotuvi',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
