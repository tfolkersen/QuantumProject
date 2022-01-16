
run:
	python3 main.py > problemDict.txt
	python3 -i test.py

#data:
#	-rm problemDict.txt
#	python3 main.py > problemDict.txt
#	python3 test.py > output0.txt
#	-rm problemDict.txt
#	python3 main.py > problemDict.txt
#	python3 test.py > output1.txt
#	-rm problemDict.txt
#	python3 main.py > problemDict.txt
#	python3 test.py > output2.txt
#	-rm problemDict.txt
#	python3 main.py > problemDict.txt
#	python3 test.py > output3.txt
#	-rm problemDict.txt
#	python3 main.py > problemDict.txt
#	python3 test.py > output4.txt
#	-rm problemDict.txt

clean:
	rm problemDict.txt output*.txt
