import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastmath",
    version="0.0.4",
    author="Roshan Lamichhane",
    author_email="roshanlamichhanenepali@gmail.com",
    description="A math libary for easier use of math formulas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roshanlam/FastMath",
    packages=setuptools.find_packages(),
    keywords = ['ROSHAN LAMICHHANE', 'ROSHAN', 'FAST MATH', 'FASTMATH'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
