echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py migrate
echo "BUILD END"