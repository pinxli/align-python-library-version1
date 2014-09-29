from distutils.core import setup

files = ["session/*","config.ini"]

setup(
    name              = "align-python-library",
    version             = "0.0.1",
    description         = "Align Commerce API wrapper for Python",
    author              = "https://github.com/pinxli",
    author_email        = "pinky.liwanagan@gmail.com",
    url                 = "https://github.com/pinxli/aligncommerce-api-python-lib",
    packages            = ['Align'],
    package_data        = {'package' : files },
    scripts             = ["runner","README.txt","README.md","example.py","Align/config.ini"],
    long_description    = open('README.txt').read(),
    classifiers         =[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP'
    ]
) 