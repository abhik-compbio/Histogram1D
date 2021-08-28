# Bash script to run histogram.py code for different residues.
mkdir {1..123}
for i in `seq 1 123`
do
cp -r hist-all.py $i/
cd $i
echo $i
sed -i "s/res1/res$i/g" histogram.py
sed -i "s/Residue1/Residue$i/g" histogram.py
python3 histogram.py
cd ..
done
