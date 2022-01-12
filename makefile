
run:
	python3 main.py > problemDict.txt
	python3 test.py

clean:
	rm problemDict.txt
