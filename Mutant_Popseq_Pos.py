# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:47:53 2016

@author: Allison Haaning
"""

#Script that uses SNP IDs to pull genetic (POPSEQ) positions of SNPs from new 
#reference genome for all mutants in collection

#File containing IDs for mutants and 9K SNP IDs in introgressed regions from 
#mutants (mutants backcrossed with Bowman)
Mut_Pos = open('Mutant_Pos.txt','r')

#File containing two columns: One with all SNP IDs formatted as in Mut_Pos 
#and another with corresponding SNP IDs formatted as in SNP_Pos_Popseq  
SNP_IDs = open('SNP_IDs.txt', 'r')

#File containing all SNP IDs with chromosome and POPSEQ position
SNP_Pos_Popseq = open('9K_SNPs_Map_Positions.txt', 'r')

#Opens output file and writes header line
outfile = open('Mutant_PopSeq_Pos.txt', 'w') 
outfile.write('Mutant_ID'+'\t'+'SNP_ID'+'\t'+'Chrom'+'\t'+'Popseq_cM'+'\n')

#Creates empty lists to hold file data
Mutant_Info = []
SNPs = []
SNPS_popseq = []

#Skip header info
Mut_Pos.readline()
SNP_IDs.readline()
SNP_Pos_Popseq.readline()

#Read in all info and append to list
for line in Mut_Pos:
    line = line.strip()
    line = line.split()
    Mutant_Info.append(line)

#Read in all info and append to list    
for line in SNP_IDs:
    line = line.strip()
    line = line.split()
    SNPs.append(line)

#Add alternative SNP ID for all SNPs in each mutant
for i, mutant in enumerate(Mutant_Info):
    for marker in SNPs:
        if(mutant[1] == marker[1]):
            Mutant_Info[i].append(marker[0])
        else:
            continue

#Add NA if SNP in mutant did not have alternative ID 
for i, mutant in enumerate(Mutant_Info):
    while len(mutant) < 5:
        Mutant_Info[i].append('NA')

#Read in all info and append to list
for line in SNP_Pos_Popseq:
    line = line.strip()
    line = line.split()
    SNPS_popseq.append(line)

#Add POPSEQ cM position for SNPs in mutants    
for i, mutant in enumerate(Mutant_Info):
    for line in SNPS_popseq:
        if(mutant[4] == line[0]):
            Mutant_Info[i].append(line[1])
            Mutant_Info[i].append(line[2])
        else:
            continue

#Add NA if POPSEQ position info was not available for SNP and write all info to 
#file. Final file contains mutant IDs, SNPs in mutants with the IDs corresponding to
#the format in the POPSEQ position file, Chromosome, and POPSEQ cM position.         
for i, mutant in enumerate(Mutant_Info):
    while len(mutant) < 7:
       Mutant_Info[i].append('NA')
    outfile.write(mutant[0] +'\t'+ mutant[4]+'\t'+ mutant[5] +'\t'+ mutant[6] + '\n')

#Close input and output files    
Mut_Pos.close()
SNP_IDs.close()
SNP_Pos_Popseq.close()
outfile.close()
    

    
        
