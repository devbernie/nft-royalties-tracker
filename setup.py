from setuptools import setup, find_packages

setup(
    name="nft_royalties_tracker",
    version="1.0.0",
    description="A CLI tool for tracking NFT royalties on the Cardano blockchain.",
    author="Your Name",
    author_email="dev.bernie@gmail.com",
    url="https://github.com/devbernie/nft-royalties-tracker",
    packages=find_packages(),  # Tự động tìm các module trong thư mục
    include_package_data=True,
    install_requires=[
        "click>=8.0",
        "requests>=2.0",
        "reportlab>=3.0",
    ],
    entry_points={
        "console_scripts": [
            "nft-tracker=tracker.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)