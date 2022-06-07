import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Olivier Audet-Yang",
    long_description=long_description,
    project_urls={
        "Bug Tracker": "https://github.com/greentext01/ccl/issues",
        "Repository": "https://github.com/greentext01/ccl",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    scripts=["bin/ccl.py"],
    python_requires=">=3.9",
    license="MIT",
    keywords="scratch compiler framework library",
    name="ccl",
    version="0.0.1",
    author_email="oaudetyang@gmail.com",
    description="Python to Scratch compiler",
    long_description_content_type="text/markdown",
    url="https://github.com/greentext01/ccl",
    bug="https://github.com/greentext01/ccl/issues",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Software Development :: Compilers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries",
    ]
)
