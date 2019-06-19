# 基于RASA+Flask框架构建的中文任务型对话机器人 Basic Chatbot using RASA + Flask

## 基本介绍
用新版rasa框架（1.0.3）构建了一个简单的旅游信息咨询对话机器人，该机器人功能如下：

1） 查询给定省份的5A级旅游景点

2) 介绍旅游景点

3）推荐各个省份的特色美食

并结合FLASK做了一个简单的UI界面。

基本环境： python 3.7； rasa 1.0.3


## 环境配置
安装requirements.txt中列出的包(可能有些没有列出，到时候报错提示缺什么就装什么就好)
```
pip install -r requirements.txt
```
window环境下mitie可能不是很好安装，可以参考 http://rowl1ng.com/%E6%8A%80%E6%9C%AF/chatbot.html

## 文件说明
- data目录下存储训练所需数据，nlu.md是nlu模块的训练数据，story.md是core模块的训练数据，训练采用预训练词向量，total_word_feature_extractor.dat文件较大，需要自己下载放到这个目录下 https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases

- models 存放训练完的模型。新版rasa直接一起训练两个模型并打包。之后调用flask ui界面前需要把模型解压缩，形成core和nlu子文件夹

- static UI界面需要的代码

- static ori 初始的比较简单的一个UI界面， 可以忽略

- templates UI界面的模板设置

- actions.py 自定义的机器人动作

- config.yml core模型policy设定和nlu模型pipeline的设定

- domain.yml 定义机器人整体操作环境

- endpoints.yml 运行自定义action需要

- web_config.py, web_forms.py, web_model.py, web_run.py Flask UI界面文件，web_flask_main.py是初始的比较简单的一个界面，可以忽略

- rasa introduction.pptx 学习rasa过程整理的一个ppt，对rasa框架以及这个机器人demo了进行简单介绍

## 使用说明

### 模型训练
```
rasa train
```
### 终端启用对话
1. 需要在一个终端运行action
```
rasa run actions --actions actions
```
2. 在另外一个终端运行模型
```
rasa shell -m models/20190618-115023.tar.gz (your model name) --endpoints endpoints.yml 
```

### 交互式学习
1. 需要在一个终端运行action
```
rasa run actions --actions actions
```
2. 在另外一个终端运行模型
```
rasa interactive -m models/20190618-115023.tar.gz (your model name) --endpoints endpoints.yml 
```

### 启用UI界面
1. 需要在一个终端运行action
```
rasa run actions --actions actions
```
2. 在另外一个终端运行flask
```
python web_run.py
```
打开给出的url即可开始对话

## TODO

- 增大数据量。

- 增加功能

- 分词、实体识别有待完善，较长的景点名称会出现识别错误。

- 支持在线测试训练

## note
rasa interactive learning的时候之前不定时会遇到一个text wrapper error： invalid width，后来采取的策略是根据报错提示，进到这个函数源码 把对应的判断条件去掉就好了。

网上很多资源都是基于rasa旧的版本，主要差别在于训练模型的命令，之前的是core模型和nlu模型分开训练，以及一些函数名称变更，这些训练的时候会出来提示，问题不是很大

## 建议学习路径

1. 官方文档： https://rasa.com/docs/

2. 找一个比较完整的demo对照着学习， 比如我这个hhhh

3. 对于rasa模型pipeline及policy可以看源码， 了解原理 https://github.com/RasaHQ/rasa

4. 自己上手写一个demo， 实践过程逐渐深入

## 参考资料

官方文档： https://rasa.com/docs/

源码： https://github.com/RasaHQ/rasa

Rasa使用指南01： https://terrifyzhao.github.io/2018/09/17/Rasa%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%9701.html

Rasa使用指南02： https://terrifyzhao.github.io/2019/02/26/Rasa%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%9702.html

用Rasa NLU构建自己的中文NLU系统： http://www.crownpku.com/2017/07/27/%E7%94%A8Rasa_NLU%E6%9E%84%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AD%E6%96%87NLU%E7%B3%BB%E7%BB%9F.html

UI界面参考： https://github.com/LutherTeh/Insight_chatbot

医院信息咨询机器人demo： https://github.com/RasaHQ/medicare_locator

中文例子：https://github.com/crownpku/Rasa_NLU_Chi

天气查询机器人：https://github.com/howl-anderson/WeatherBot

## Paper
Bocklisch, Tom, et al. "Rasa: Open source language understanding and dialogue management." arXiv preprint arXiv:1712.05181 (2017). （整体介绍, 各个部分使用的方法）

J. D.Williams, K. Asadi, and G. Zweig. Hybrid code networks: practical and efficient end-to-end
dialog control with supervised and reinforcement learning. arXiv preprint arXiv:1702.03274,
2017. （core管理模块与这篇论文相似， 但添加了一些近些年的方法）

Vlasov, Vladimir, Akela Drissner-Schmid, and Alan Nichol. "Few-Shot Generalization Across Dialogue Tasks." arXiv preprint arXiv:1811.11707 (2018). (处理uncooperative user behavior)

Williams, Jason D., and Geoffrey Zweig. "End-to-end lstm-based dialog control optimized with supervised and reinforcement learning." arXiv preprint arXiv:1606.01269 (2016).















