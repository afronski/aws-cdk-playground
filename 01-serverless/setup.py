import setuptools

setuptools.setup(
    name="serverless",
    version="1.0.0",

    description="An example that shows with use of AWS CDK and Python how to create a serverless infrastructure",

    author="Wojciech Gawroński (wojciech.gawronski@pattern-match.com)",

    package_dir={"": "serverless"},
    packages=setuptools.find_packages(where="serverless"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws_lambda",
        "aws-cdk.aws_apigateway",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
