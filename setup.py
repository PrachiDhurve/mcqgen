from setuptools import find_packages, setup

setup(
    name= 'mcqgenerator',
    version='0.0.1',
    author='Prachi Dhurve',
    author_email='prachidhurve2001@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv","PyPDF"],
    packages=find_packages(),
)