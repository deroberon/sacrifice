import codecs
TAB="    "
DEBUG=False
SEPARATOR="__"


class Command:
    def __init__(self,rps):
        self.renpystory=rps
        self.command=""
    
    def to_str(self,tabs):
        tmp=tabs+self.command+"\n"
        return tmp
class End:
    def __init__(self,rps):
        self.renpystory=rps
    
    def to_str(self,tabs):
        tmp=tabs+"return\n"
        return tmp
class Line:
    def __init__(self,rps):
        self.content=""
        self.tags=[]
        self.whois=""
        self.renpystory=rps
        self.conditional=""
        pass

    def to_str(self,tabs):
        tmp=""
        if not self.content=="":
            if not self.conditional=="":
                tmp=tmp+tabs+"if "+self.conditional+" :\n"
                tabs=tabs+TAB
            if self.whois=="":
                tmp=tmp+tabs+self.content+"\n"
            else:
                tmp=tmp+tabs+self.whois+" "+self.content+"\n"
        return tmp

class Menu:
    def __init__(self,rps):
        self.title=""
        self.options=[]
        self.renpystory=rps
    
    def to_str(self,tabs):
        tmp=tabs+"menu "+self.title+":\n"
        for option in self.options:
            tmp=tmp+option.to_str(tabs+TAB)
        return tmp

class Option:
    def __init__(self,rps):
        self.title=""
        self.lines=[]
        self.jump=""
        self.great_chapter=""
        self.renpystory=rps
        self.conditional=""

    def to_str(self,tabs):
        tmp=""
        if not self.conditional=="":
            tmp=tmp+tabs+self.title+" if "+self.conditional+" :\n"
        else:
            tmp=tmp+tabs+self.title+":\n"
        for line in self.lines:
            tmp=tmp+line.to_str(tabs+TAB)
        if(self.jump in self.renpystory.labels) or (self.jump in self.renpystory.menus):
            tmp=tmp+tabs+TAB+"jump "+self.jump
        else:
            tmp=tmp+tabs+TAB+"jump "+self.great_chapter+SEPARATOR+self.jump
        return tmp+"\n"

class Label:
    def __init__(self,rps):
        self.title=""
        self.lines=[]   ##Pode ser linhas ou menus
        self.jump=""
        self.great_chapter=""
        self.renpystory=rps

    def to_str(self,tabs):
        tmp="\n"+tabs+"label "+self.title+":\n"
        tmp=tmp+tabs+TAB+"$ "+self.title+"="+self.title+"+1\n"
        for line in self.lines:
            tmp=tmp+line.to_str(tabs+TAB)
        if not self.jump=="":
            if(self.jump in self.renpystory.labels) or (self.jump in self.renpystory.menus):
                tmp=tmp+tabs+TAB+"jump "+self.jump
            else:
                tmp=tmp+tabs+TAB+"jump "+self.great_chapter+SEPARATOR+self.jump
        tmp=tmp+"\n\n\n"
        return tmp    

class RenpyStory:
    def __init__(self):
        self.script=[]
        self.menus={}
        self.labels={}
        self.options={}

    def to_str(self):
        tmp=""
        for label in self.labels.keys():
            tmp=tmp+"define "+label+"=0\n"
        tmp=tmp+"\n"
        for command in self.script:
            tmp=tmp+command.to_str("")
        return tmp
    

class Story:
    def __init__(self):
        self.STORY_PATH="./ink"
        self.story_lines=[]

    def read_file(self,filename):
        file_lines=[]
        file=open(self.STORY_PATH+"/"+filename, 'r',encoding="utf-8")
        lines=file.readlines()
        for line in lines:
            include_line=True
            if line.startswith("INCLUDE"):
                include_line=False
            if line.startswith("//"):
                include_line=False    
            if include_line:
                file_lines.append(line)
        for line in lines:
            if line.startswith("INCLUDE"):
                new_file_name=line.split(" ")[1].replace("\n","")
                file_lines=file_lines+self.read_file(new_file_name)
        return file_lines

    def load_story(self, filename):
        self.story_lines=self.read_file(filename)

    def print_lines(self):
        for i in self.story_lines:
            print(i)

    def process_story(self):
        i=0
        chapter=""
        subchapter=""
        separator=SEPARATOR
        opt=False
        label_activo=None
        option_activo=None
        menu_activo=None
        renpy_story=RenpyStory()
        initial_label=Label(renpy_story)
        initial_label.title="start"
        renpy_story.script.append(initial_label)
        renpy_story.labels["start"]=initial_label
        final_label=Label(renpy_story)
        final_label.title="end"
        renpy_story.script.append(final_label)
        renpy_story.labels["end"]=final_label
        final_label.lines.append(End(renpy_story))
        
        while i<len(self.story_lines):
            line=self.story_lines[i].replace("\n","").strip().replace("\t","")
            if line.startswith("==="):
                chapter=line.replace("===","").strip()
                i=i+1
            elif line.startswith("="):
                opt=False
                sub_chapter=line.replace("=","").strip()
                i=i+1
                if DEBUG:
                    print("=========================================")
                    print(chapter+separator+sub_chapter)
                if not label_activo==None:
                    renpy_story.script.append(label_activo)
                    renpy_story.labels[label_activo.title]=label_activo
                label_activo=Label(renpy_story)
                label_activo.title=chapter+separator+sub_chapter
                label_activo.great_chapter=chapter

            elif line.startswith("->"):
                jump=line.replace("->","").replace(".",separator).strip()
                if DEBUG:
                    print("   -> " + jump)
                i=i+1
                if opt:
                    if jump=="END":
                        jump="end"
                    option_activo.jump=jump
                else:
                    if not label_activo==None:
                        if jump=="END":
                            jump="end"
                        label_activo.jump=jump
                    else:
                        if not jump=="END":
                            initial_label.jump=jump
            elif line.startswith("**"):
                i=i+1
            elif line.startswith("*") or line.startswith("+"):
                option=Option(renpy_story)
                if DEBUG:
                    print("OPT LINE:"+line[0:10])
                if line.startswith("*"):
                    parts=line.replace("*","").replace("[","").split("]")
                if line.startswith("+"):
                    parts=line.replace("+","").replace("[","").split("]")
                part0=parts[0].strip()
                if (not part0.find("{")==-1) and (not part0.find("}")==-1):
                    parts_of_part0=part0.replace("{","").split("}")
                    option.conditional=parts_of_part0[0].replace(".",SEPARATOR).strip()
                    option.title="\""+parts_of_part0[1].strip()+"\""
                else:
                    option.title="\""+part0.strip()+"\""     
                option.great_chapter=chapter
                if not parts[1].strip()=="":
                    renline=Line(renpy_story)
                    if not line.find("#")==-1:
                        renline.content="\""+line[0:line.find("#")]+"\""
                        if not line.find("#CH:")==-1:
                            renline.whois=line[line.find("#CH:")+4:].strip()
                            renline.content="\""+line[0:line.find("#")].strip()+"\""
                    else:
                        renline.content="\""+line+"\""
                option_activo=option
                menu_activo.options.append(option)
                renpy_story.options[option.title]=option_activo
                i=i+1
            elif line.startswith("-("):
                if DEBUG:
                    print("START OPTIONS")
                opt=True
                menu_title=line.replace("-(","").replace(")","").strip()
                menu_activo=Menu(renpy_story)
                menu_activo.title=menu_title
                if not label_activo==None:
                    label_activo.lines.append(menu_activo)
                    renpy_story.menus[menu_title]=menu_activo
                i=i+1
            elif line.startswith("~"):
                command_text=line.replace("~","").strip()
                command=Command(renpy_story)
                command.command="$ "+command_text
                if opt:
                    option_activo.lines.append(command)
                else:
                    if not label_activo==None:
                        label_activo.lines.append(command)
                i=i+1
            elif line.startswith("{"):
                parts=line.replace("{","").replace("}","").strip().split(":")
                line=parts[1].strip()
                renline=Line(renpy_story)
                renline.conditional=parts[0].strip()
                if not line.find("#")==-1:
                    renline.content="\""+line[0:line.find("#")]+"\""
                    if not line.find("#CH:")==-1:
                        renline.whois=line[line.find("#CH:")+4:].strip()
                        renline.content="\""+line[0:line.find("#")].split(":")[1].strip()+"\""
                else:
                    renline.content="\""+line+"\""
                label_activo.lines.append(renline)
                i=i+1
            elif line.startswith("VAR"):
                comand_text=line.replace("VAR ","").strip()
                command=Command(renpy_story)
                command.command="define "+comand_text
                renpy_story.script.append(command)
                i=i+1
            elif line.startswith("#"):
                if line.startswith("##CH:"):
                    comand_text=line.replace("##CH:","").strip()
                    command=Command(renpy_story)
                    command.command=comand_text
                    renpy_story.script.append(command)
                if line.startswith("##CO:"):
                    comand_text=line.replace("##CO:","").strip()
                    command=Command(renpy_story)
                    command.command=comand_text
                    label_activo.lines.append(command)
                i=i+1
            elif line=="":
                i=i+1
            else:
                renline=Line(renpy_story)
                if not line.find("#")==-1:
                    renline.content="\""+line[0:line.find("#")]+"\""
                    if not line.find("#CH:")==-1:
                        renline.whois=line[line.find("#CH:")+4:].strip()
                        renline.content="\""+line[0:line.find("#")].strip()+"\""
                else:
                    renline.content="\""+line+"\""
                if opt:
                    option_activo.lines.append(renline)
                else:
                    if not label_activo==None:
                        label_activo.lines.append(renline)    

                if DEBUG:
                    print("LINE: "+line[0:10])
                i=i+1
        

        if not label_activo==None:
            renpy_story.script.append(label_activo)
            renpy_story.labels[chapter+separator+sub_chapter]=label_activo
        
        return renpy_story            

    def export(self):
        rs=st.process_story()
        file = open("script.rpy", "w",encoding="utf-8")
        file.write(rs.to_str())
        file.close()

st=Story()
st.load_story("sacrifice.ink")
st.export()
