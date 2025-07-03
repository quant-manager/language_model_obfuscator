python .\lmo.py -h

REM: obfuscate with 5 different methods:
python .\lmo.py -s 12345 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out1.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out2.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out3.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out4.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out5.txt

REM: reverse obfuscation and recover the original input with 5 different methods:
python .\lmo.py -v 1 -r 1 -t 1 -i .\data\output\out1.txt -o .\data\recovered\in1.txt
python .\lmo.py -v 1 -r 1 -t 2 -i .\data\output\out2.txt -o .\data\recovered\in2.txt
python .\lmo.py -v 1 -r 1 -t 3 -i .\data\output\out3.txt -o .\data\recovered\in3.txt
python .\lmo.py -v 1 -r 1 -t 4 -i .\data\output\out4.txt -o .\data\recovered\in4.txt
python .\lmo.py -v 1 -r 1 -t 5 -i .\data\output\out5.txt -o .\data\recovered\in5.txt
