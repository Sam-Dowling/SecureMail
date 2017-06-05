
PC=python3
DI=pip install
AF=src/Driver.py
TF=tests/TestDriver.py
CACHE=src/__pycache__
DEP=PyGObject pyotp requests

dependencies:
	${DI} ${DEP}

test:
	${PC} -m unittest ${TF}

run:
	${PC} ${AF}

clean:
	rm -r ${CACHE}
