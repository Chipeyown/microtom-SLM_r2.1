f1=open('chromosome.txt')
dict={}
for line in f1:
	seq=line.split()
	dict[(seq[1])]=seq[0]
f1.close()

fa=open('GCF_036512215.1_SLM_r2.1_genomic.fna')
fb=open('SLM_r2.1.fa','w')
for line in fa:
	if line.startswith('>'):
		key=line.lstrip('>').split()[0]
		fb.write('>'+dict[key]+'\n')
	else:
		fb.write(line)
fa.close()
fb.close()
