CODE_PATH=./
TEST_EXCLUSIONS=bin/,lib/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

lint:
	-flake8 --exclude $(TEST_EXCLUSIONS) $(CODE_PATH)

test: clean-pyc
	pytest $(CODE_PATH)

coverage:
	coverage run -m pytest && coverage report -m
