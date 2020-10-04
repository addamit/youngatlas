pep:
	autopep8 -i src/yamagics/yamagicscore.py
	autopep8 -i src/yaserver/yaservercore.py

test:
	pytest -s tests --html=report.html
	
lint:
	pylint --rcfile=.pylintrc --reports=y --exit-zero src | tee pylint.out

release:
	python setup.py sdist bdist_wheel


