
f1=open('SLM_r2.1_feature_table.txt')
next(f1)
dict1={}
for line in f1:
	seq=line.rstrip().split('\t')
	dict1[(seq[12])]=seq[-1]
	dict1[(seq[10])]=seq[-1]
f1.close()

fa=open('GCF_036512215.1_SLM_r2.1_protein.faa')
fb=open('SLM_r2.1.protein.fa','w')
for line in fa:
	if line.startswith('>'):
		protein_id=line.lstrip('>').split()[0]
		gene_id=dict1[protein_id]
		fb.write('>'+gene_id+'_'+protein_id+'\n')
	else:
		fb.write(line)
fa.close()
fb.close()

