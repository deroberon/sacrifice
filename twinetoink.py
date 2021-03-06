from bs4 import BeautifulSoup
import re
import sys, getopt

STORY_DATA="tw-storydata"
PASSAGE_DATA="tw-passagedata"
OPTPREFIX="opc_"
CHAPTER="twine"
SET_VARIABLE_PATTERN=r'\(set:[ ]*\$([^ ]*)[ ]*to[ ]*([^ ]*)[ ]*\)'
IF_PATTERN=r'\(if:[ ]*([^\)]*)\)[ ]*\[([^\]]*)\]'
OPTION_PATTERN=r'\[\[[ ]*([^\]]*)[ ]*\]\]'


opt_index=0
variables={}

def print_chapter(passage):
    tmp=""
    options=0
    ## 2.1-) Analisar se existem opções e imprimir
    lines=passage.text.split("\n")
    for line in lines:
        variable_definition=re.findall(SET_VARIABLE_PATTERN,line)
        if_definition=re.findall(IF_PATTERN,line)
        option_definition=re.findall(OPTION_PATTERN,line)
        if len(variable_definition)>0:
            nline=variable_definition[0][0].replace("$","")+" = "+variable_definition[0][1].replace("$","")
            tmp=tmp+"~"+nline+"\n"
        elif len(if_definition)>0:
            condition=if_definition[0][0].replace("$","").replace("is","==")
            jump=option_definition[0]
            tmp=tmp+"* {"+condition+"}  ["+jump+"] ->"+CHAPTER+"."+jump+"\n"
        elif len(option_definition)>0:
            if option_definition[0].find("|"):
                parts=option_definition[0].split("|")
                tmp=tmp+"* ["+parts[0]+"] ->"+CHAPTER+"."+parts[1]+"\n"
            else:
                tmp=tmp+"* ["+option_definition[0]+"] ->"+CHAPTER+"."+option_definition[0]+"\n"
            options=options+1
            pass
        else:
            tmp=tmp+line+"\n"
    ## 2.5-) Se não tem como sair, imprimir ->END ao final
    if options==0:
        tmp=tmp+"->END\n"
    tmp=tmp+"\n"
    return tmp

def main(argv):
    filename=""
    filename2=""

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("Usage: python twinetoink -i <twinefilename.html> -o <inkfilename.ink>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("Usage: python twinetoink -i <twinefilename.html> -o <inkfilename.ink>")
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-o", "--ofile"):
            filename2 = arg  

    if filename=="" or filename2=="":
        print("Usage: python twinetoink -i <twinefilename.html> -o <inkfilename.ink>")
        sys.exit(2)

    file=open(filename, 'r',encoding="utf-8")
    lines=file.readlines()
    html=""
    for i in range(0,len(lines)):
        html=html+lines[i]
    soup = BeautifulSoup(html, 'html.parser')

    story=soup.find_all(STORY_DATA)
    passages=story[0].find_all(PASSAGE_DATA)

    # for passage in passages:
        #print(passage.get("name"))
        #print(passage.text)

    ## Parse para levantar nome de todas as variaveis

    ## 1-) Definir todas as variaveis
    tmp=""
    for passage in passages:
        vars=re.findall(SET_VARIABLE_PATTERN,passage.text) 
        for var in vars:
            if var[0] not in variables:
                variables[var[0]]=var

    for variable in variables.keys():
        tmp=tmp+"VAR "+variable+" = "+variables[variable][1]+"\n"

    tmp=tmp+"\n-> "+CHAPTER+".Start\n\n"
    ## 2-) Imprimir todos os capitulos
    tmp=tmp+"\n=== "+CHAPTER+"===\n"

    for passage in passages:
        tmp=tmp+"= "+passage.get("name")+"\n"
        tmp=tmp+print_chapter(passage)

    file2=open(filename2, 'w',encoding="utf-8")
    file2.write(tmp)
    file.close()
    file2.close()
    ##print(tmp)

if __name__ == "__main__":
   main(sys.argv[1:])