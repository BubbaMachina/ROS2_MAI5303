from setuptools import find_packages, setup

package_name = 'turtle_circle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+ package_name + '/launch', ['launch/turtle_circle.launch.py']), # Copy launch file into launch folder
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='bubbasamuels@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'setup_node = turtle_circle.setup_node:main', # Added this node
        'circle_driver = turtle_circle.circle_driver:main'# Added this node
        ],
    },
)
