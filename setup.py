import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bittrex_api",
    version="0.0.8",
    author="Kristof",
    description="bittrex_api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/py_bittrex_api",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)