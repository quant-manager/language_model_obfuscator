python .\txt_obf.py -h

REM: obfuscate with different modes without noise/gaps:
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out1.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out2.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out3.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out4.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out5.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out6.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 7 -i .\data\input\in.txt -o .\data\output\out7.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 8 -i .\data\input\in.txt -o .\data\output\out8.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 9 -i .\data\input\in.txt -o .\data\output\out9.txt
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 10 -i .\data\input\in.txt -o .\data\output\out10.txt

REM: obfuscate with different modes with noise:
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_noisy1.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_noisy2.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_noisy3.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_noisy4.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_noisy5.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_noisy6.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 7 -i .\data\input\in.txt -o .\data\output\out_noisy7.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 8 -i .\data\input\in.txt -o .\data\output\out_noisy8.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 9 -i .\data\input\in.txt -o .\data\output\out_noisy9.txt
python .\txt_obf.py -s 54321 -n 25 -v 1 -r 0 -t 10 -i .\data\input\in.txt -o .\data\output\out_noisy10.txt

REM: obfuscate with different modes with gaps:
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_gaps1.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_gaps2.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_gaps3.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_gaps4.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_gaps5.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_gaps6.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 7 -i .\data\input\in.txt -o .\data\output\out_gaps7.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 8 -i .\data\input\in.txt -o .\data\output\out_gaps8.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 9 -i .\data\input\in.txt -o .\data\output\out_gaps9.txt
python .\txt_obf.py -s 67890 -g 1 -v 1 -r 0 -t 10 -i .\data\input\in.txt -o .\data\output\out_gaps10.txt

REM: obfuscate with different modes with noise and gaps:
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 1 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps1.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 2 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps2.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 3 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps3.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 4 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps4.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 5 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps5.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 6 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps6.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 7 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps7.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 8 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps8.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 9 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps9.txt
python .\txt_obf.py -s 54321 -g 1 -n 25 -v 1 -r 0 -t 10 -i .\data\input\in.txt -o .\data\output\out_noisy_gaps10.txt


REM: reverse obfuscation and recovery of the original input with different modes without noise/gaps:
python .\txt_obf.py -v 1 -r 1 -t 1 -i .\data\output\out1.txt -o .\data\recovered\in1.txt
python .\txt_obf.py -v 1 -r 1 -t 2 -i .\data\output\out2.txt -o .\data\recovered\in2.txt
python .\txt_obf.py -v 1 -r 1 -t 3 -i .\data\output\out3.txt -o .\data\recovered\in3.txt
python .\txt_obf.py -v 1 -r 1 -t 4 -i .\data\output\out4.txt -o .\data\recovered\in4.txt
python .\txt_obf.py -v 1 -r 1 -t 5 -i .\data\output\out5.txt -o .\data\recovered\in5.txt
python .\txt_obf.py -v 1 -r 1 -t 6 -i .\data\output\out6.txt -o .\data\recovered\in6.txt
python .\txt_obf.py -v 1 -r 1 -t 7 -i .\data\output\out7.txt -o .\data\recovered\in7.txt
python .\txt_obf.py -v 1 -r 1 -t 8 -i .\data\output\out8.txt -o .\data\recovered\in8.txt
python .\txt_obf.py -v 1 -r 1 -t 9 -i .\data\output\out9.txt -o .\data\recovered\in9.txt
python .\txt_obf.py -v 1 -r 1 -t 10 -i .\data\output\out10.txt -o .\data\recovered\in10.txt

REM: reverse obfuscation and recovery of the original input with different modes with noise:
python .\txt_obf.py -v 1 -r 1 -t 1 -i .\data\output\out_noisy1.txt -o .\data\recovered\in_noisy1.txt
python .\txt_obf.py -v 1 -r 1 -t 2 -i .\data\output\out_noisy2.txt -o .\data\recovered\in_noisy2.txt
python .\txt_obf.py -v 1 -r 1 -t 3 -i .\data\output\out_noisy3.txt -o .\data\recovered\in_noisy3.txt
python .\txt_obf.py -v 1 -r 1 -t 4 -i .\data\output\out_noisy4.txt -o .\data\recovered\in_noisy4.txt
python .\txt_obf.py -v 1 -r 1 -t 5 -i .\data\output\out_noisy5.txt -o .\data\recovered\in_noisy5.txt
python .\txt_obf.py -v 1 -r 1 -t 6 -i .\data\output\out_noisy6.txt -o .\data\recovered\in_noisy6.txt
python .\txt_obf.py -v 1 -r 1 -t 7 -i .\data\output\out_noisy7.txt -o .\data\recovered\in_noisy7.txt
python .\txt_obf.py -v 1 -r 1 -t 8 -i .\data\output\out_noisy8.txt -o .\data\recovered\in_noisy8.txt
python .\txt_obf.py -v 1 -r 1 -t 9 -i .\data\output\out_noisy9.txt -o .\data\recovered\in_noisy9.txt
python .\txt_obf.py -v 1 -r 1 -t 10 -i .\data\output\out_noisy10.txt -o .\data\recovered\in_noisy10.txt

REM: reverse obfuscation and recovery of the original input with different modes with gaps:
python .\txt_obf.py -g 1 -v 1 -r 1 -t 1 -i .\data\output\out_gaps1.txt -o .\data\recovered\in_gaps1.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 2 -i .\data\output\out_gaps2.txt -o .\data\recovered\in_gaps2.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 3 -i .\data\output\out_gaps3.txt -o .\data\recovered\in_gaps3.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 4 -i .\data\output\out_gaps4.txt -o .\data\recovered\in_gaps4.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 5 -i .\data\output\out_gaps5.txt -o .\data\recovered\in_gaps5.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 6 -i .\data\output\out_gaps6.txt -o .\data\recovered\in_gaps6.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 7 -i .\data\output\out_gaps7.txt -o .\data\recovered\in_gaps7.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 8 -i .\data\output\out_gaps8.txt -o .\data\recovered\in_gaps8.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 9 -i .\data\output\out_gaps9.txt -o .\data\recovered\in_gaps9.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 10 -i .\data\output\out_gaps10.txt -o .\data\recovered\in_gaps10.txt

REM: reverse obfuscation and recovery of the original input with different modes with noise and gaps:
python .\txt_obf.py -g 1 -v 1 -r 1 -t 1 -i .\data\output\out_noisy_gaps1.txt -o .\data\recovered\in_noisy_gaps1.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 2 -i .\data\output\out_noisy_gaps2.txt -o .\data\recovered\in_noisy_gaps2.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 3 -i .\data\output\out_noisy_gaps3.txt -o .\data\recovered\in_noisy_gaps3.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 4 -i .\data\output\out_noisy_gaps4.txt -o .\data\recovered\in_noisy_gaps4.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 5 -i .\data\output\out_noisy_gaps5.txt -o .\data\recovered\in_noisy_gaps5.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 6 -i .\data\output\out_noisy_gaps6.txt -o .\data\recovered\in_noisy_gaps6.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 7 -i .\data\output\out_noisy_gaps7.txt -o .\data\recovered\in_noisy_gaps7.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 8 -i .\data\output\out_noisy_gaps8.txt -o .\data\recovered\in_noisy_gaps8.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 9 -i .\data\output\out_noisy_gaps9.txt -o .\data\recovered\in_noisy_gaps9.txt
python .\txt_obf.py -g 1 -v 1 -r 1 -t 10 -i .\data\output\out_noisy_gaps10.txt -o .\data\recovered\in_noisy_gaps10.txt


REM: obfuscate README file without noise/gaps:
python .\txt_obf.py -s 12345 -v 1 -r 0 -t 4 -i .\data\input\readme_in.txt -o .\data\output\readme_out.txt

REM: reverse obfuscation and recovery of the original README file without noise/gaps:
python .\txt_obf.py -v 1 -r 1 -t 4 -i .\data\output\readme_out.txt -o .\data\recovered\readme_rec.txt
