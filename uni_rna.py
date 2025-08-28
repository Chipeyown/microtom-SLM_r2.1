import re

f1=open('SLM_r2.1_feature_table.txt')
next(f1)
dict1={}
for line in f1:
	seq=line.rstrip().split('\t')
	dict1[(seq[10])]=seq[-1]
f1.close()
f2=open('chromosome.txt')
dict2={}
for line in f2:
	seq=line.split('\t')
	dict2[(seq[1])]=seq[0]
f2.close()

fa=open('GCF_036512215.1_SLM_r2.1_rna_from_genomic.fna')
fb=open('SLM_r2.1.cdna.fa','w')
for line in fa:
	if line.startswith('>'):
		if 'transcript_id' in line:
			transcript_id=re.findall('\[transcript_id=(.+?)\]',line)[0]
		else:
			transcript_id=re.findall('\[product=(.+?)\]',line)[0]
			transcript_id='-'.join(transcript_id.split())
		chro='_'.join(line.split('|')[1].split('_')[:2])
		chro=dict2[chro]
		gene_id='SL'+chro[-2:]+'G'+re.findall('GeneID:(\d+)',line)[0]
		fb.write('>'+gene_id+'_'+transcript_id+'\n')
	else:
		fb.write(line)
fa.close()
fb.close()

