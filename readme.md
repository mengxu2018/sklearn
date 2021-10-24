上传文件到github不需要带上sklearn-venv

只要事先pip freeze > requirements.txt
下次下载下来再安装pip install -r requirements.txt

但是有个问题，代码下载下来重建venv环境的时候得先
python -m venv sklearn-venv
sklearn-venv\Scripts\activate
然后再执行pip install -r requirements.txt
确保安装的文件再venv的lib目录下面

还有个问题就是pycharm新建python venv环境比较容易，但是打开现成的会有找不到interpreter的问题，需要下面步骤设置下找到sklearn-venv\scripts下面的解释器
pycharm open existing virtualenv code example
Open >> File
>> Settings(Ctrl+Alt+S)
>> Project: > Python Interpreter
>> Right side of the Browse path select location of existing venv path