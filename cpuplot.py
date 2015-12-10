#!/usr/bin/python

import sys
import getopt
import subprocess
from subprocess import call
import re
import matplotlib.pyplot as loopplt

linesize=2000
linescale=linesize/10

def main(filename):
    prevline = 0;
    max = 0;
    i = 0;
    j = 0;

    for i in xrange(len(files)):
        filename = files[i]
        with open(filename, "r") as f:
            for line in f:
                j = j + 1;
                if j > linesize:
                    break;
                words = line.split()
                curline = int(words[1])
                if max < curline - prevline:
                    max = curline - prevline
                    pos = words[0]
                prevline = curline 
        print (pos, max)

def timevsloop(files):
    looppng = "loopplot.png"
    colors = ['red', 'blue']
    """
    offsets = [0.02,0.08]
    """
    offsets = [0.0,0.0]
    maxlist = [0, 0]
    minlist = [0, 0]
    cpushare = [0.0, 0.0]
    loopplt.figure(figsize=(10,6.6));
    loopplt.tick_params(axis='x', labelsize=10, )
    loopplt.tick_params(axis='y', labelsize=10, )

    loopplt.xlabel("Loop Number * 2000", fontsize=10, fontweight='bold')
    loopplt.ylabel("Timestamp(s)", fontsize=10, fontweight='bold')
    loopplt.ylim([0, 0.6])
    loopplt.xlim([0, 10])
    """
    loopplt.xlim([0, 2])
    """
    for i in xrange(len(files)):
        filename = files[i]
        maxdata = 0;
        j = 0;
        with open(filename, "r") as f:
            for line in f:
                if j == 0:
                    words = line.split()
                    minlist[i] = int(words[1]); 
                j = j + 1;
                pass
            words = line.split()
            maxlist[i] = int(words[1]) 
            if i == 0:
                physshare = str(float(words[8]) * 100) + "%";
            else:
                virtshare = str(float(words[8]) * 100) + "%";
            j = j + 1;
            if j > linesize:
                break;

    for i in xrange(len(files)):
        j = 0;
        color = colors[i]
        filename = files[i]
        offset = offsets[i]
        j = 0;
        with open(filename, "r") as f:
            for line in f:
                j = j + 1;
                if j > linesize:
                    cpushare = float(words[2])
                    break;
                words = line.split()
                loop = j 
                timestamp = int(words[1])
                x = loop/float(linescale)
                y = (timestamp - float(minlist[i]))/(maxlist[i] - minlist[i])
                if j == 0:
                    print loop, timestamp, x, y
                loopplt.scatter(x , y - offset , c=color, label=color, alpha=0.5)
                j = j + 1;
    """
    cpushare1 = float(cpushare[0])
    sh = str(cpushare1)
    """
    physshare = "Physical machine CPU Share = " + physshare 
    virtshare = "Virtual machine CPU Share = " + virtshare

    loopplt.figtext(0.15,0.80, physshare, fontsize=10, ha='left', fontweight='bold')
    loopplt.figtext(0.15,0.78, virtshare, fontsize=10, ha='left', fontweight='bold')
    loopplt.grid(True)
    loopplt.savefig(looppng, dpi=615)
    loopplt.show()
    

if __name__ == "__main__":
    physfile = sys.argv[1]
    virtfile = sys.argv[2]
    files = [physfile, virtfile]
    main(files)
    timevsloop(files)
