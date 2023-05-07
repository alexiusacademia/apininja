from setuptools import setup

setup(
    name='api_ninja',
    version='0.1.0',
    author='Alex Academia',
    author_email='alexius.sayco.academia@gmail.com',
    description='An api module generator.',
    long_description='An api module generator.',
    url='https://github.com/alexiusacademia/apininja',
    py_modules=['api_ninja'],
    entry_points={
        'console_scripts': [
            'apininja = main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='api generator'
)
