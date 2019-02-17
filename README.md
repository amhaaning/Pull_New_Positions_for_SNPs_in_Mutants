# Pull_New_Positions_for_SNPs_in_Mutants

Python script that:
1) Reads in three files (1) a file containing IDs of mutants and all SNPs contained in mutant introgressions (from Druka et al. (2011) Plant Phys 155:617–627), (2) a file containing two columns: one with SNP IDs formatted as in file 1 and the other with SNP IDs formatted as in file 2, and (3) a file containing SNPs with genetic positions (POPSEQ cM) from new barley reference genome (2016 version). 
2) Pulls POPSEQ cM positions for all SNPs in all mutant introgressions (mutants backcrossed with Bowman)
3) Outputs a new file with mutant IDs, SNP IDs formatted as in file 3, chromosome, and POPSEQ cM position.
