from setuptools import setup


setup(
    name='course',
    version='1.0',
    py_modules=['course', 'services'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        course=course:cli
    ''',
)