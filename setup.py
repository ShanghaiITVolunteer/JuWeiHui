import setuptools


long_description = "Currently a very ugly but usable script to covert group purchase results to printable sheets for delivery during the pandemic in Shanghai"

setuptools.setup(
    name="group_purchase",
    version="0.0.1",
    author="ShanghaiITVolunteer",
    author_email="gzwu.jack1997@gmail.com",
    description="JuWeiHui group purchase helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShanghaiITVolunteer/JuWeiHui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)