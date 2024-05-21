import glob, os, math, zipfile, sys

def prepare(prefix, fname, diffname,timings,bpms):
    og = open(fname, "r")
    Line = og.readlines()
    hit = False
    col = False
    tim =False
    bak = False
    with open(os.getcwd()+"/"+prefix +"["+ diffname+"].osu", "w") as new:
        for line in Line:
            if (line.split(':')[0]=="Version"):
                new.write("Version:"+diffname+"\n")
            elif (line.split(':')[0]=="CircleSize"):
                new.write("CircleSize:4\n")
            elif (line.split(':')[0]=="ApproachRate"):
                new.write("ApproachRate:10\n")
            elif (line.split(':')[0]=="StackLeniency"):
                new.write("StackLeniency:0.8\n")
            elif  bak == False:
                new.write(line.strip()+"\n")
            elif (hit==False)  and (col==False) and (tim==False) and (bak==True):
                if (line.strip()=="//Storyboard Layer 0 (Background)") or (line.strip()=="//Storyboard Layer 1 (Fail)") or (line.strip()=="//Storyboard Layer 2 (Pass)") or (line.strip()=="//Storyboard Layer 3 (Foreground)") or (line.strip()=="//Storyboard Layer 4 (Overlay)") or (line.strip()=="//Storyboard Sound Samples") or (line.strip()=="") or (line.strip()=="[TimingPoints]"):
                    new.write(line.strip()+"\n")
            elif  (hit==False)  and (col==False) and (tim==True)  :
                if (("[HitObjects]" not in line) and ((line.strip()=="") or (line.strip()=="[Colours]") or(line.split(',')[6]=="1"))):
                    new.write(line.strip()+"\n")
                    if (line.strip()!="") and (line.strip()!="[Colours]"):
                        timings.append(float(line.strip().split(',')[0]))
                        bpms.append(float(line.strip().split(',')[1]))
            elif  (hit==False)  and (col==True) and (tim==True)  :
                    new.write(line.strip()+"\n")
            elif (hit==True):
                lasttime = float(line.strip().split(',')[2])
            if "[TimingPoints]" in line:
                tim = True
            if "//Break Periods" in line:
                bak = True
            if "[Colours]" in line:
                col = True
            if "[HitObjects]" in line:
                hit = True
    return lasttime

def stream(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac stream", timings, bpms)
    print(timings)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    with open(os.getcwd()+"/"+prefix +"[tprac stream].osu", "a") as map:
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counter%16==0):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counter+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def quints(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac quints", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    with open(os.getcwd()+"/"+prefix +"[tprac quints].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%6==0):
                    counter+=1
                elif (counterm%6==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counter+=1
                counterm+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def triples(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac triples", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    with open(os.getcwd()+"/"+prefix +"[tprac triples].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%4==0):
                    counter+=4
                elif (counterm%8==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counterm+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def triplesingles(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac triplesingles", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    counterm2 = 1
    with open(os.getcwd()+"/"+prefix +"[tprac triplesingles].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%6==0) or (counterm%6==4):
                    counter+=4
                elif (counterm%6==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counterm+=1
                if (counterm2%58==0):
                    counterm = 1
                counterm2+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def quintsingles(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac quintsingles", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    counterm2 = 1
    with open(os.getcwd()+"/"+prefix +"[tprac quintsingles].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%8==0) or (counterm%8==6):
                    counter+=1
                elif (counterm%8==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counterm+=1
                if (counterm2%78==0):
                    counterm = 1
                counter+=1
                counterm2+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def quinttriples(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac quinttriples", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    counterm2 = 1
    with open(os.getcwd()+"/"+prefix +"[tprac quinttriples].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%10==0) or (counterm%10==6):
                    counter+=3
                elif (counterm%10==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                    counter+=1
                elif ((counterm%10>1) and (counterm%10<6)) or (counterm%10==9):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                    counter+=1
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counterm+=1
                if (counterm2%96==0):
                    counterm = 1
                counterm2+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def single(prefix, fname):
    timings = []
    bpms = []
    lasttime = prepare(prefix, fname, "tprac singletap", timings, bpms)
    time = timings[0]
    currentPoint = 0
    done = False
    counter = 0
    counterm = 1
    with open(os.getcwd()+"/"+prefix +"[tprac singletap].osu", "a") as map:      
        while (done == False):
            if (currentPoint+1<len(timings) and  (time < timings[currentPoint+1])) or (currentPoint+1==len(timings) and time < lasttime):
                if (counterm%2==0):
                    counter+=2
                elif (counterm%8==1):
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",5,0,0:0:0:0:\n")
                else:
                    map.write(str(round(150*math.cos((counter/32)*2*math.pi)+256))+","+str(round(150*math.sin((counter/32)*2*math.pi)+192))+","+str(round(time))+",1,0,0:0:0:0:\n")
                counterm+=1
                time += bpms[currentPoint]/4
            elif currentPoint+1<len(timings):
                currentPoint+=1
                time = timings[currentPoint]
            else:
                done = True

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

if(len(sys.argv)==1):
    print('Missing argument: For information and usage instructions, run \'pyhton osutrainermap.py --help\' you silly goose')
elif(len(sys.argv)==2):
    if(sys.argv[1]=='--help'):
        print('\nWelcome to osutrainermap v0.1! This program sucks ass.\n\nTo make a set of practice maps out of a map, simply run \'pyhton osutrainermap.py --generate \'[FULL PATH TO MAP FOLDER]\'\'\n\nMake sure to wrap the path in \'\', or it won\'t work. Also, LEAVE OUT THE FINAL \\ OR / OUT OF THE PATH!!!\n\nAwesome example: python osutrainermap.py --generate \'/home/ivan/.local/share/osu-wine/osu!/Songs/24949 The Prodigy - Smack My Bitch Up\'\n\nAfter that, simply F5 in the osu client and it *SHOULD* work I think. Have fun.')
    else:
        print('Invalid argument: For information and usage instructions, run \'pyhton osutrainermap.py --help\' you silly goose')
elif(len(sys.argv)==3):
    if(sys.argv[1]=='--generate'):
        os.chdir(sys.argv[2])
        for file in glob.glob("*.osu"):
            fname = file
        prefix = fname.split('[')[0]

        stream(prefix, fname)
        quints(prefix, fname)
        triples(prefix, fname)
        quintsingles(prefix, fname)
        triplesingles(prefix, fname)
        quinttriples(prefix, fname)
        single(prefix, fname)

        lastdir = os.getcwd().split('/')[len(os.getcwd().split('/'))-1]
        dirname = os.getcwd()
        os.chdir(os.getcwd().replace(lastdir, ''))
        print(lastdir)
        print(os.getcwd())
        with zipfile.ZipFile(lastdir+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(dirname, zipf)

        pre, ext = os.path.splitext(lastdir+'.zip')
        os.rename(lastdir+'.zip', pre + '.osz')
    else:
        print('Invalid argument: For information and usage instructions, run \'pyhton osutrainermap.py --help\' you silly goose')
else:
    print('Invalid argument: For information and usage instructions, run \'pyhton osutrainermap.py --help\' you silly goose')
