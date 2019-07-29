import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fourcc",
    version="1.0.0",
    author="c0rp3n",
    author_email="",
    description="Combines four chars into an interger (fourcc).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c0rp3n/fourcc",
    packages= ['fourcc'],
    entry_points= {
        'console_scripts': [
            'fourcc = fourcc.__main__:main' 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
