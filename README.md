# sphinx_test
trying sphinx on github pages

## add api
sphinx-apidoc -o source/ ./api-directory

## build
sphinx-build -b html source/ build/

## open 
open build/index.html

