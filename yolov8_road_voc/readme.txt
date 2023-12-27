1. 打开项目目录，在搜索框内输入cmd打开终端

2. 新建一个虚拟环境（conda create -n yolo8 python=3.8）

3. 激活环境(conda activate yolov8)

4. 安装GPU版本torch(如果想要CPU版本则这一步直接跳过): pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html

5. 安装ultralytics库（yolov8官方库），pip install ultralytics -i https://pypi.tuna.tsinghua.edu.cn/simple

6. 安装图形化界面库pyside6：pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple

7.python base_camera.py