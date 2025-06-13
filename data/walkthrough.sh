# project directory
mkdir -p build

# make blast database
gunzip -c GCF_000005845.2_ASM584v2_protein.faa.gz | makeblastdb -in -\
	-dbtype prot -out build/ecoli -title ecoli -parse_seqids

# retrieve one sequence
blastdbcmd -db build/ecoli -entry NP_414608.1
blastdbcmd -db build/ecoli -entry NP_414608.1 > build/NP_414608.1.fa

# run blastp to find homologs
blastp -db build/ecoli -query build/NP_414608.1.fa -num_threads `nproc`\
	> build/blast.out
blastp -db build/ecoli -query build/NP_414608.1.fa -evalue 1e-5\
	-num_threads `nproc`> build/blast.out

# get good matches
grep "^>" build/blast.out | cut -f 1 -d " " | cut -f2 -d ">" > build/abc.txt
blastdbcmd -db build/ecoli -entry_batch build/abc.txt > build/abc.fa

# blast each sequence against the genome
blastp -db build/ecoli -query build/abc.fa -evalue 1e-5 -num_threads `nproc`\
	> build/abc.blast.out

# perform multiple alignment with clustalw
clustalw -infile=build/abc.fa -outfile=build/abc.aln -QUIET

