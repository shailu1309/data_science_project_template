from setuptools import find_packages, setup

setup(
    name='sky_data_science_template',
    version='0.1',
    description='Sky Data Science Project Template',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'mlflow',
        'sqlalchemy',  # For PostgreSQL connection
        'gcsfs',       # If you plan to use GCP storage
    ],
)

