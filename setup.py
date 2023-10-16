from setuptools import setup

setup(
    name="mrph",
    version="1.0.2",
    scripts=["bin/mrph"],
    py_modules=["flows.morph"],
    install_requires=['openai', 'python-dotenv', 'git+https://github.com/pysyun/pysyun_conversation_flow.git']
)
