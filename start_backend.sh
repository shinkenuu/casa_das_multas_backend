cd /home/pi/Projects/backend/
pwd

git pull origin master

set -a
. ./.env
printenv | grep DB
printenv | grep FLASK


. /home/pi/.venv/backend/bin/activate
which python

# pip install -r requirements.txt
python run.py
