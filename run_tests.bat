python .\lmo.py -h

REM: obfuscate with five different methods without noise:
python .\lmo.py -s 12345 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out1.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out2.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out3.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out4.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out5.txt

REM: obfuscate with five different methods with noise:
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_noisy1.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_noisy2.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_noisy3.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_noisy4.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_noisy5.txt

REM: reverse obfuscation and recovery of the original input with five different methods without noise:
python .\lmo.py -v 1 -r 1 -t 1 -i .\data\output\out1.txt -o .\data\recovered\in1.txt
python .\lmo.py -v 1 -r 1 -t 2 -i .\data\output\out2.txt -o .\data\recovered\in2.txt
python .\lmo.py -v 1 -r 1 -t 3 -i .\data\output\out3.txt -o .\data\recovered\in3.txt
python .\lmo.py -v 1 -r 1 -t 4 -i .\data\output\out4.txt -o .\data\recovered\in4.txt
python .\lmo.py -v 1 -r 1 -t 5 -i .\data\output\out5.txt -o .\data\recovered\in5.txt

REM: reverse obfuscation and recovery of the original input with five different methods with noise:
python .\lmo.py -v 1 -r 1 -t 1 -i .\data\output\out_noisy1.txt -o .\data\recovered\in_noisy1.txt
python .\lmo.py -v 1 -r 1 -t 2 -i .\data\output\out_noisy2.txt -o .\data\recovered\in_noisy2.txt
python .\lmo.py -v 1 -r 1 -t 3 -i .\data\output\out_noisy3.txt -o .\data\recovered\in_noisy3.txt
python .\lmo.py -v 1 -r 1 -t 4 -i .\data\output\out_noisy4.txt -o .\data\recovered\in_noisy4.txt
python .\lmo.py -v 1 -r 1 -t 5 -i .\data\output\out_noisy5.txt -o .\data\recovered\in_noisy5.txt
