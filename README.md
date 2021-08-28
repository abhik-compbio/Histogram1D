# histogram-dihed
Protein dihedral angles are one of the major degree of freedom which can show any type of conformational change in protein. Protein dihedral angle distribution is best way to observe this.

Here python code to plot distribution of dihedral angle (along with bash script to run for different residues) is attached. Here we have compared angle distribution of protein Alpha Lactalbumine (PDB Code: 1a4v.pdb) at different ph 1 and ph 7. It is found that Alpha Lactalbumine works in a ph dependent way. Sample datasets are attached.

To run code :
1. Change bash file (hist.sh). Give residue range. Here we have done it for all (123 residues) residues.
2. chmod + x hist.sh
3. ./hist.sh
4. Data sets are as follows: dihed-res1-ph1.dat, dihed-res1-ph7.dat
5. We need python version 3 for this.
6. Run python3 histogram.py
One can use it for single trajectory also.
