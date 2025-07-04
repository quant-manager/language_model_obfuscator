python .\lmo.py -h

REM: obfuscate with five different methods without noise/gaps:
python .\lmo.py -s 12345 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out1.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out2.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out3.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out4.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out5.txt
python .\lmo.py -s 12345 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out6.txt

REM: obfuscate with five different methods with noise:
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_noisy1.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_noisy2.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_noisy3.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_noisy4.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_noisy5.txt
python .\lmo.py -s 54321 -n 25 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_noisy6.txt

REM: obfuscate with five different methods with gaps:
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_gaps1.txt
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_gaps2.txt
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_gaps3.txt
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_gaps4.txt
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_gaps5.txt
python .\lmo.py -s 67890 -g 1 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_gaps6.txt

REM: obfuscate with five different methods with noise and gaps:
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps1.txt
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps2.txt
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps3.txt
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps4.txt
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps5.txt
python .\lmo.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps6.txt


REM: reverse obfuscation and recovery of the original input with five different methods without noise/gaps:
python .\lmo.py -v 1 -r 1 -t 1 -i .\data\output\out1.txt -o .\data\recovered\in1.txt
python .\lmo.py -v 1 -r 1 -t 2 -i .\data\output\out2.txt -o .\data\recovered\in2.txt
python .\lmo.py -v 1 -r 1 -t 3 -i .\data\output\out3.txt -o .\data\recovered\in3.txt
python .\lmo.py -v 1 -r 1 -t 4 -i .\data\output\out4.txt -o .\data\recovered\in4.txt
python .\lmo.py -v 1 -r 1 -t 5 -i .\data\output\out5.txt -o .\data\recovered\in5.txt
python .\lmo.py -v 1 -r 1 -t 6 -i .\data\output\out6.txt -o .\data\recovered\in6.txt

REM: reverse obfuscation and recovery of the original input with five different methods with noise:
python .\lmo.py -v 1 -r 1 -t 1 -i .\data\output\out_noisy1.txt -o .\data\recovered\in_noisy1.txt
python .\lmo.py -v 1 -r 1 -t 2 -i .\data\output\out_noisy2.txt -o .\data\recovered\in_noisy2.txt
python .\lmo.py -v 1 -r 1 -t 3 -i .\data\output\out_noisy3.txt -o .\data\recovered\in_noisy3.txt
python .\lmo.py -v 1 -r 1 -t 4 -i .\data\output\out_noisy4.txt -o .\data\recovered\in_noisy4.txt
python .\lmo.py -v 1 -r 1 -t 5 -i .\data\output\out_noisy5.txt -o .\data\recovered\in_noisy5.txt
python .\lmo.py -v 1 -r 1 -t 6 -i .\data\output\out_noisy6.txt -o .\data\recovered\in_noisy6.txt

REM: reverse obfuscation and recovery of the original input with five different methods with gaps:
python .\lmo.py -g 1 -v 1 -r 1 -t 1 -i .\data\output\out_gaps1.txt -o .\data\recovered\in_gaps1.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 2 -i .\data\output\out_gaps2.txt -o .\data\recovered\in_gaps2.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 3 -i .\data\output\out_gaps3.txt -o .\data\recovered\in_gaps3.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 4 -i .\data\output\out_gaps4.txt -o .\data\recovered\in_gaps4.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 5 -i .\data\output\out_gaps5.txt -o .\data\recovered\in_gaps5.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 6 -i .\data\output\out_gaps6.txt -o .\data\recovered\in_gaps6.txt

REM: reverse obfuscation and recovery of the original input with five different methods with noise and gaps:
python .\lmo.py -g 1 -v 1 -r 1 -t 1 -i .\data\output\out_noisy_gaps1.txt -o .\data\recovered\in_noisy_gaps1.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 2 -i .\data\output\out_noisy_gaps2.txt -o .\data\recovered\in_noisy_gaps2.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 3 -i .\data\output\out_noisy_gaps3.txt -o .\data\recovered\in_noisy_gaps3.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 4 -i .\data\output\out_noisy_gaps4.txt -o .\data\recovered\in_noisy_gaps4.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 5 -i .\data\output\out_noisy_gaps5.txt -o .\data\recovered\in_noisy_gaps5.txt
python .\lmo.py -g 1 -v 1 -r 1 -t 6 -i .\data\output\out_noisy_gaps6.txt -o .\data\recovered\in_noisy_gaps6.txt
