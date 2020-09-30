try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='envtest',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Playing with virtual environments.",
      long_descritpion="""Playing with virtual environments.""",
      url='https://github.com/acse-2020',
      author="Imperial College London",
      author_email='rhodri.nelson@imperial.ac.uk',
      packages=['envtest'])
