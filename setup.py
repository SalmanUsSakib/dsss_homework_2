from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    author="SalmanUsSakib",
    author_email="salmanussakib369@gmail.com",
    description="Math quiz game.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SalmanUsSakib/dsss_homework_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)