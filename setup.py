import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Extracting-Handwritten-Text-Using-Gemini-1.5-Pro-API"
AUTHOR_USER_NAME = "Sujitsarkar16"
SRC_REPO = "GeminiTextExtract"
AUTHOR_EMAIL = "sarkarsujit9052@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="GeminiTextExtract utilizes the Gemini 1.5 Pro API to accurately extract text from handwritten documents. This project streamlines the processing and analysis of unstructured handwritten data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
