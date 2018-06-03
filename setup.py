from setuptools import setup, Extension, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='sparse_rrt',
    version='0.0.1',
    description='Sparse stable trees planner',
    long_description=long_description,
    author='Oleg Sinyavskiy',
    author_email='olegsinyavskiy@gmail.com',
    url='https://github.com/olegsinyavskiy/sparse_rrt',
    download_url='',
    license='BSD License 2.0',
    install_requires=['numpy>=1.13.3'],
    extras_require={
      'tests': ['pytest>=2.7.2',
                'pytest-pep8>=1.0.6',
                'pytest-xdist>=1.13.1',
                'pytest-cov>=2.1.0'],
    },
    classifiers=[
      # 'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      # 'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Topic :: Software Development :: Libraries',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(),
    ext_modules=[Extension(
        'sparse_rrt._sst_module',
        extra_compile_args=['-std=c++1y', '-O3'],
        # define_macros = [('MAJOR_VERSION', '1'),
        #                  ('MINOR_VERSION', '0')],
        include_dirs = ['deps/pybind11/include',
                        'include'],
        sources = [
            'src/motion_planners/rrt.cpp',
            'src/motion_planners/sst.cpp',
            'src/nearest_neighbors/graph_nearest_neighbors.cpp',
            'src/systems/car.cpp',
            'src/systems/cart_pole.cpp',
            'src/systems/pendulum.cpp',
            'src/systems/point.cpp',
            'src/systems/rally_car.cpp',
            'src/systems/two_link_acrobot.cpp',
            'src/utilities/random.cpp',
            'src/utilities/timer.cpp',
            'src/image_creation/svg_image.cpp',
            'src/image_creation/planner_visualization.cpp',
            'src/systems/distance_functions.cpp'])
    ]
)
