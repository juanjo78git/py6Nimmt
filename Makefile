init:
	pip install -r requirements.txt

test:
	python -m unittest 'tests/test_main.py' -v

coverage:
	coverage erase
	coverage run -a -m unittest 'tests/test_main.py'
	coverage html

pre:
	coverage run -a -m unittest 'tests/test_main.py'
	coverage html

flake8:
	flake8 py6Nimmt
    
po:
	xgettext --language=Python --output=py6Nimmt/locale/messages.pot py6Nimmt/py6Nimmt.py
	msgmerge --update --no-fuzzy-matching --backup=off py6Nimmt/locale/en/LC_MESSAGES/py6Nimmt.po py6Nimmt/locale/messages.pot
	msgmerge --update --no-fuzzy-matching --backup=off py6Nimmt/locale/es/LC_MESSAGES/py6Nimmt.po py6Nimmt/locale/messages.pot

mo:
	msgfmt py6Nimmt/locale/en/LC_MESSAGES/py6Nimmt.po -o py6Nimmt/locale/en/LC_MESSAGES/py6Nimmt.mo
	msgfmt py6Nimmt/locale/es/LC_MESSAGES/py6Nimmt.po -o py6Nimmt/locale/es/LC_MESSAGES/py6Nimmt.mo

pypi:
	python setup.py clean --all
	python setup.py sdist bdist_wheel
	twine upload dist/*
