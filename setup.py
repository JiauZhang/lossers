from setuptools import setup, find_packages

setup(
    name = 'lossers',
    packages = find_packages(exclude=['examples']),
    package_data={'': ['*/vgg_v0.1.pth']},
    version = '0.0.9',
    license='MIT',
    description = 'Deep Learning Loss Function',
    author = 'JiauZhang',
    author_email = 'jiauzhang@163.com',
    url = 'https://github.com/JiauZhang/lossers',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = 'text/markdown',
    keywords = [
        'Deep Learning',
        'Loss Function',
        'Artificial Intelligence',
    ],
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)