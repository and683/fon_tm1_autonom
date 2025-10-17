
from setuptools import find_packages, setup

package_name = 'zsakuca_recognizer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/launch', ['launch/zsakuca.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bandi',
    maintainer_email='bandi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'image_generator_node = zsakuca_recognizer.image_generator_node:main',
        'recognizer_node = zsakuca_recognizer.recognizer_node:main',
    ],
},


)

