import re

fa=open('chromosome.txt')
dict1={}
for line in fa:
	seq=line.split()
	dict1[(seq[1])]=seq[0]
fa.close()

f1=open('GCF_036512215.1_SLM_r2.1_genomic.gtf')
f2=open('SLM_r2.1.gtf','w')
for line in f1:
	seq=line.split('\t')
	try:
		chro=dict1[(seq[0])]
		GeneID=re.findall('GeneID:(.+?)"',line)[0]
		gene_id='SL'+chro[-2:]+'G'+GeneID
		des='gene_id "'+gene_id+'"; '+' '.join(seq[8].split(' ')[2:])
		f2.write(chro+'\t'+'\t'.join(seq[1:8])+'\t'+des)
	except:
		if '#' in line:
			f2.write(line)
		print(line)
f1.close()
f2.close()
