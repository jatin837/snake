activate: env
	source env/bin/activate

install: env, requirements.txt
	pip install -r requirements.txt

run: snake.py
	python snake.py