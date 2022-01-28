make clean
for i in `seq 1 30`
do
 make all MAIN=main.cpp TARGET=oka_own${i}
done
