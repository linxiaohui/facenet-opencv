import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facenet-opencv",
    version="0.0.0",
    author="linxiaohui",
    author_email="llinxiaohui@126.com",
    description="FaceNet face features using OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linxiaohui/facenet-opencv",
    packages=setuptools.find_packages(),
    install_requires=['mtcnn_opencv'],
    package_data={
        'facenet_cv2': ['graph_final.pb']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires='>=3.6',
)
