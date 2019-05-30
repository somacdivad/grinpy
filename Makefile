lint:
	flake8 grinpy/

check-formatting:
	black --check grinpy/

format:
	black grinpy/

test:
	pytest -vv --cov=grinpy/ .

package:
	python setup.py sdist
	python setup.py bdist_wheel
