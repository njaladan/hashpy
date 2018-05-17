from setuptools import setup

setup(name='hashpy',
      version='0.1',
      description='Pure Python implementation of common hash functions',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Topic :: Security :: Cryptography'
      ],
      keywords='hash hashing security pure-python',
      url='https://github.com/njaladan/hashpy',
      author='Nagaganesh Jaladanki',
      author_email='ganesh.jaladanki@gmail.com',
      license='MIT',
      packages=['hashpy'],
      include_package_data=True,
      zip_safe=False)
