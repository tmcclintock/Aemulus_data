from setuptools import setup,find_packages

setup(
    name='aemulus_data',
    version = "0.1",
    author = "Aemulus team.",
    description='Access to the Aemulus data.',
    py_modules=['aemulus_data'],
    include_package_data = True,    
    # adding packages
    packages=find_packages(),
    install_requires=['numpy'],
    setup_requires=['pytest_runner'],
    tests_require=['pytest']
)
