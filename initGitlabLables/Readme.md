# 说明
- 批量在 gitlab（公有／私有）的代码库中添加或者删除labels

# 使用说明
1. 填写配置文件
2. python 版本：3+
3. python main.py # 执行后，程序默认将配置中 `[labels]` 中的所有 label 都添加到代码库中，及时出错也会执行下去；。

## 配置文件说明
```conf
[labels] ### labes_name=color
Status/Verified = lightseagreen
Status/WIP = lightseagreen
Status/Block = lightseagreen
Status/More dtail=lightseagreen
Status/Invalid = lightseagreen
Status/Duplicate = lightseagreen
Status/Wontfix = lightseagreen
Type/Bug = seashell
Type/Feature = seashell
Type/Refactor = seashell
Type/Performance = seashell
Type/Enhancement = seashell
Priority/High = purple
Priority/Medium = purple
Priority/Low = purple

[global]
api=http://10.186.18.21/api/v4 # gitlab api 地址
project=86 # project Id 或者 project 名字，project 参考 gitlab 官方文档
private-token=XoKdxo4cVyT2 # gitlab private-token，参考[private-token](https://docs.gitlab.com/ee/api/#private-tokens)
```

## 参数说明
```bash
> python3.6 main.py -h
usage: main.py [-h] [--delete] [--raise_error]

Operator Gitlab labels.

optional arguments:
  -h, --help     show this help message and exit
  --delete       delete labels listed in config instead of add
  --raise_error  program will abend if meet any error
```