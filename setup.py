from setuptools import setup,find_packages

dist = setup(
    name='aemulus_data',
    version = "0.1",
    author = "Aemulus team.",
    description='Access to the Aemulus data.',
    py_modules=['aemulus_data'],
    
    # adding packages
    packages=find_packages(''),
    #package_dir = {'':''},
    
    # trying to add files...
    include_package_data = True,
    package_data = {'': ["building_box_cosmologies.txt"]}
)
