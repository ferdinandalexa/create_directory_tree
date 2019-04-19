from setuptools import setup


setup(
    name='course',
    version='0.1',
    py_modules=['course'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        course=course:cli
    ''',
)