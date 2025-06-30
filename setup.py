from setuptools import setup, find_packages

setup(
    name="emotion-detector",
    version="1.0.0",
    description="Emotion detection using Watson NLP",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "flask>=3.0.0",
        "watson-nlp>=0.1.0",
        "pytest>=7.4.3",
        "flake8>=6.1.0"
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'emotion-detector=emotion_detector.server:main'
        ]
    }
)
