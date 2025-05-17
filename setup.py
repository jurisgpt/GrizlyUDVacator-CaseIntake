from setuptools import setup, find_packages

setup(
    name="grizlyudvacator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "python-dateutil"
    ],
    include_package_data=True,
    zip_safe=False
)
