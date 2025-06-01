from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(    name="diffeomorphic",
    version="0.1.0",
    author="Mohammad Ahsan Khodami",
    author_email="ahsan.khodami@gmail.com",
    description="Diffeomorphic transformations for image and video morphing in psychological experiments",    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AhsanKhodami/diffeomorphic",
    packages=["diffeomorphic"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib",
        "pillow",
        "scipy",
        "opencv-python",
    ],    entry_points={
        "console_scripts": [
            "diffeomorphic-image=diffeomorphic.cli:run_diffeomorphic",
            "diffeomorphic-movie=diffeomorphic.cli:run_diffeomorphic_movie",
            "diffeomorphic-warpshift=diffeomorphic.cli:run_diffeomorphic_movie_warpshift",
        ],
    },
)
