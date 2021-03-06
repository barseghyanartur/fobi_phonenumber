from setuptools import setup, find_packages

with open('fobi_phonenumber/README.rst') as readme:
    long_description = readme.read()

setup(
    name='fobi-phonenumber',
    packages=find_packages(),
    long_description=long_description,
    install_requires=[
        'django-fobi>=0.6.5',
        'django-phonenumber-field>=1.0.0'
    ],
    version='0.2.0',
    author='James Fenwick',
    author_email='jfenwick@tecaz.com',
    url='https://github.com/jmsfwk/fobi_phonenumber',
    license='GPLv2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience::Developers',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)
