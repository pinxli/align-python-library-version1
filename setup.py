from distutils.core import setup

files = ["things/*"]
setup(
    name                = "align-python-library",
    version             = "0.1",
    description         = "Align Commerce API wrapper for Python",
    author              = "https://github.com/pinxli",
    author_email        = "pinky.liwanagan@gmail.com",
    url                 = "https://github.com/pinxli/aligncommerce-api-python-lib",
    packages            = ['Align'],
    package_data        = {'package' : files },
    long_description    = open('README.md').read()
    # scripts           = ["runner"],
    #classifiers        = []     
) 