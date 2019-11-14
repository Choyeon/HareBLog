# HareBlog

#### 介绍
一个多人博客系统

#### 运行要求

#### 快速运行
内置了Pipfile文件推荐使用pipenv
pipenv安装
```shell script
# Windows系统
pip3 install pipenv
# Mac OS 
brew install pipenv
```
运行
```shell
cd HareBlong
pipenv install 
pipenv shell 
python3 ./manage.py makemigrations
python3 ./manage.py migrate
python3 ./manage.py runserver
```

#### 使用的开源软件
Django2.2.6 按时交付完美主义者的Web框架

#### LICENSE

MIT License

Copyright (c) 2019 雨过初晴

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
