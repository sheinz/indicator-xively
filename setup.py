from setuptools import setup

setup(
    name="indicator-xively",
    version="0.1.0",
    packages=['indicatorxively'],
    scripts=['indicator-xively'],

    install_requires=['requests>=2.0.1'],

    package_data={
       'indicatorxively': ['temp-icon.png'],
    },

    author="Yuriy",
    author_email="email@email.com",
    description="This is a simple indicator application for xively service.",
    license="MIT",
    keywords="xively indicator",
    url="http://github.com/sheinz",
)
