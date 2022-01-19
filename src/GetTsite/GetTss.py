def main():
    """ 
    提取GTF文件所有基因的TSS位点信息,输出为bed格式
    适用ensembl,gencode,ucsc数据库的gtf注释文件

    注意:
        GTF/GFF 格式坐标为1-based
        BED格式的为0-based
    """

    # 引入库
    import argparse
    import sys

    parser = argparse.ArgumentParser(usage="GetTss --database ucsc --gtffile hg19.ncbiRefSeq.gtf --tssfile testTSS.bed",
                                    description="Get gene TSS site and export bed format from GTF annotation file.",
                                    epilog="Thank your for your support, if you have any questions or suggestions please contact me: 3219030654@stu.cpu.edu.cn.")
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0.0')
    # 读取注释类型文件
    parser.add_argument('-d','--database',type=str,action="store",dest="Database",choices=['ucsc','ensembl','gencode'],
                        default="ensembl",help='which annotation database you choose. (default="ensembl")')
    # 读取gtf文件
    parser.add_argument('-g','--gtffile', type=str,action="store",dest="GTFfile",help='input your GTF file. (ucsc/ensembl/gencode)')
    # 导出文件名称
    parser.add_argument('-t','--tssfile', type=str,action="store",dest="Tssfile",help='output your TSS file. (test-TSS.bed)')

    # parser.print_help()
    # parser.parse_args('-g test.gtf'.split())
    args = parser.parse_args()

    # 获取参数
    Database = args.Database
    GTFfile =  args.GTFfile
    Tssfile = args.Tssfile

    # 定义提取函数
    def GetTssBed(Database,GTFfile,Tssfile):
        print('Your job is starting, please wait!')
        # 储存文件
        outfile = open(Tssfile,'w')
        # 提取tss区间
        with open(GTFfile,'r') as gtfile:
            # gene数量
            target_number = 0
            # loop
            for line in gtfile:
                # 跳过开头注释
                if line.startswith('#'):
                    continue
                # 分割
                fileds = line.split()
                # 类型为gene
                type = fileds[2]
                # 选择注释来源
                if Database == 'ucsc':
                    # ucsc没有gene行,只有转录本
                    if type == 'transcript':
                        # 数转录本
                        target_number += 1
                        # 列信息
                        chr = fileds[0]
                        start = int(fileds[3])
                        end = int(fileds[4])
                        gene_id = fileds[9].replace('"','').replace(';','')
                        strand = fileds[6]
                        # 正链上的基因Tss为基因左边第一个碱基
                        if strand == '+':
                            start1 = start - 1
                            end1 = start
                            newline = chr + "\t" + str(start1) + "\t" + str(end1) + "\t" + gene_id + "\t" + "." + "\t" + strand
                            outfile.write(newline + '\n')
                        # 负链上的基因Tss为基因右边最后一个碱基
                        else:
                            start1 = end
                            end1 = end + 1
                            newline = chr + "\t" + str(start1) + "\t" + str(end1) + "\t" + gene_id + "\t" + "." + "\t" + strand
                            outfile.write(newline + '\n')
                else:
                    # ensembl和gencode注释文件有gene信息
                    if type == 'gene':
                        # 数基因
                        target_number += 1
                        # 列信息
                        chr = fileds[0]
                        start = int(fileds[3])
                        end = int(fileds[4])
                        gene_id = fileds[9].replace('"','').replace(';','')
                        strand = fileds[6]
                        # 正链上的基因Tss为基因左边第一个碱基
                        if strand == '+':
                            start1 = start - 1
                            end1 = start
                            newline = chr + "\t" + str(start1) + "\t" + str(end1) + "\t" + gene_id + "\t" + "." + "\t" + strand
                            outfile.write(newline + '\n')
                        # 负链上的基因Tss为基因右边最后一个碱基
                        else:
                            start1 = end
                            end1 = end + 1
                            newline = chr + "\t" + str(start1) + "\t" + str(end1) + "\t" + gene_id + "\t" + "." + "\t" + strand
                            outfile.write(newline + '\n')
        # 打印完成信息
        if Database == 'ucsc':
            print("You GTF file have: " + str(target_number) + " transcripts." + "\n")
        else:
            print("You GTF file have: " + str(target_number) + " genes." + "\n")

        print("Your task has done!\n")
        # 关闭文件
        outfile.close()

    # 运行函数
    GetTssBed(Database=Database,GTFfile=GTFfile,Tssfile=Tssfile)

# 测试code
# GetTssBed(Database='gencode',GTFfile='gencode.v19.annotation.gtf',Tssfile='testTSS.bed')
# GetTssBed(Database='ucsc',GTFfile='hg19.ncbiRefSeq.gtf',Tssfile='testTSS.bed')