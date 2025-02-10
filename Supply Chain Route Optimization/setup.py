from setuptools import setup, find_packages

setup(
    name="supply_chain_optimizer",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pandas",
        "python-dotenv"
    ],
    author="Your Name",
    description="UPS Facility Route Optimization using Dijkstra and A*",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)