# GetTsite python Package

### extract gene TSS/TES site form gencode/ensembl/gencode database GTF file and export bed format file.

## Install

```shell
$ pip install GetTsite
```

## Usage

help infomation:

```shell
$ GetTss -h
usage: GetTss --database ucsc --gtffile hg19.ncbiRefSeq.gtf --tssfile testTSS.bed

Get gene TSS site and export bed format from GTF annotation file.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d {ucsc,ensembl,gencode}, --database {ucsc,ensembl,gencode}
                        which annotation database you choose. (default="ensembl")
  -g GTFFILE, --gtffile GTFFILE
                        input your GTF file. (ucsc/ensembl/gencode)
  -t TSSFILE, --tssfile TSSFILE
                        output your TSS file. (test-TSS.bed)

Thank your for your support, if you have any questions or suggestions please contact me: 3219030654@stu.cpu.edu.cn.
```

for ucsc gtf file:

```shell
$ GetTss -d ucsc -g hg19.ncbiRefSeq.gtf -t ucsc-TSS.bed
Your job is starting, please wait!
You GTF file have: 104178 transcripts.
 
Your task has down!

$ head -n 3 ucsc-TSS.bed
chrMT   16023   16024   TRNP    .       -
chrMT   15887   15888   TRNT    .       +
chrMT   14746   14747   CYTB    .       +
```

for gencode/ensembl gtf file:

```shell
$ GetTss -d gencode -g gencode.v19.annotation.gtf -t test-TSS.bed
Your job is starting, please wait!
You GTF file have: 57820 genes.

Your task has down!

$ head -n 3 test-TSS.bed
chr1    11868   11869   ENSG00000223972.4       .       +
chr1    29806   29807   ENSG00000227232.4       .       -
chr1    29553   29554   ENSG00000243485.2       .       +
```

the usage of GetTes is same as GetTss:

```shell
$ GetTes -d ucsc -g hg19.ncbiRefSeq.gtf -t ucsc-TSS.bed

$ GetTes -d gencode -g gencode.v19.annotation.gtf -t test-TES.bed
```
## plot peaks density around TSS

compute matrix:

```shell
$ computeMatrix reference-point -S normal.bw treat.bw \
                -R myTSS.bed \
                --referencePoint center \
                -a 3000 -b 3000 -p 25 \
                -out matrix.tab.gz
```

plot Profile:

```shell
$ plotProfile -m matrix.tab.gz \
              -out profile.pdf \
              --perGroup \
              --plotTitle 'test profile'
```