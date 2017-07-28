from distutils.core import setup, Extension

example_module = Extension('_cpython',
                           sources=['cpython_wrap.c', 'cpython.c'],
                           )

setup(name='cpython',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[example_module],
      py_modules=["cpython"],
      )