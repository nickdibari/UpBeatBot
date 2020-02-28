import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="upbeatbot",
    version="0.0.2",
    author="Nicholas DIbari",
    author_email="ndibari@fordham.edu",
    description="Twitter bot to tweet uplifting images at twitter users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickdibari/UpBeatBot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4==4.4.0',
        'envparse==0.2.0',
        'python-twitter==3.5',
    ]
)
