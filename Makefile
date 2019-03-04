CODE_PATH=./
TEST_EXCLUSIONS=bin/,lib/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

build:
	python3 setup.py sdist bdist_wheel

lint:
	-flake8 --exclude $(TEST_EXCLUSIONS) $(CODE_PATH)

test: clean-pyc
	python -m unittest discover $(CODE_PATH)