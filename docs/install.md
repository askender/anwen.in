安装说明 how to install
========

## Install

```bash
git clone https://github.com/askender/anwen.in.git
cd anwen.in
pip install -r conf/requirements.txt
```

## Start Anwen service
### edit db/db_config.py to choose database type
if you choose mysql, you should open mysql service and create the database.
python hello.py -h  # you can find some help
```bash
python hello.py -c
python hello.py
```

## Testing

```bash
python tests.py
```