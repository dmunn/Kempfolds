CODE_PATH=./
TEST_EXCLUSIONS=bin/,lib/

clean-pyc:
	# Remove any errant python files to prevent sync issues when troubleshooting
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

install-deps:
	pip install -r requirements.txt

lint:
	# Stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude $(TEST_EXCLUSIONS) 
	# Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude $(TEST_EXCLUSIONS) 

test: clean-pyc
	pytest $(CODE_PATH)

coverage:
	coverage run -m pytest && coverage report -m