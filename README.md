# sphinx_test
trying sphinx on github pages

## init sphinx project
sphinx-apidoc -F -o docs/ src/

## add api
sphinx-apidoc -o source/ ./api-directory

## build
sphinx-build -b html source/ build/

## open 
open build/index.html

## test
python -m pytest tests/test_numbers.py
