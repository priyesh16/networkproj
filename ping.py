#!/usr/bin/python

import sys
import getopt
import subprocess
from subprocess import call
import re
import matplotlib.pyplot as rttplt
import numpy as np

linesize=2000
linescale=linesize/10

def main(filename):
    prevline = 0;
    max = 0;
    i = 0;

    for i in xrange(len(files)):
        filename = files[i]
        with open(filename, "r") as f:
            for line in f:
                words = line.split()
                curline = int(words[1])
                if max < curline - prevline:
                    max = curline - prevline
                    pos = words[0]
                prevline = curline 
        print (pos, max)


def rttplot(files, outfile):
    color = 'blue'
    maxlist = [0, 0]
    find = re.compile("-")
    protortt = []
    prototime = []
    rttarray = [];
    timearray = [];
    lenwords = 8 
    rttcol = -2
    timex = [0, 500]
    rtty = [0, 10]

    for i in xrange(len(files)):
        filename = files[i]
        maxdata = 0;
        j = 0;
        count = 0;
        with open(filename, "r") as f:
            for line in f:
                j = j + 1;
                if j < 8:
                    continue;
                words = line.split() 
                if len(words) != lenwords:
                    continue;
                rttstr = words[rttcol]
                try:
                    pos = rttstr.index("=")
                except ValueError:
                    continue; 
                try:
                    rtt = float(rttstr[pos + 1:])
                except ValueError:
                    continue; 
                count = count + 1;
                rttarray.append(rtt);
        xarr = list(xrange(count))
        prototime.append(xarr)
        protortt.append(rttarray)
        rttarray = []
        xarr = [] 

    rttplt.figure(figsize=(20,20));
    for filename in files:
        if "phys" in filename:
                sub = rttplt.subplot(2,1,i)
                sub.set_title("Physical Machine Latency", fontsize=30)
                rttplt.tick_params(axis='x', labelsize=20, )
                rttplt.tick_params(axis='y', labelsize=20, )
                rttplt.xlabel("Measurement", fontsize=20, fontweight='bold')
                rttplt.ylabel("RTT(ms)", fontsize=20, fontweight='bold')
                rttplt.bar(prototime[0], protortt[0], width=0, bottom=0, color='b')
                rttplt.xlim(timex)
                rttplt.ylim(rtty)
                rttplt.grid(True)
        if "virt" in filename:
                sub = rttplt.subplot(2,1,i)
                sub.set_title("Virtual Machine Latency", fontsize=30)
                rttplt.tick_params(axis='x', labelsize=20, )
                rttplt.tick_params(axis='y', labelsize=20, )
                rttplt.xlabel("Measurement", fontsize=20, fontweight='bold')
                rttplt.ylabel("RTT(ms)", fontsize=20, fontweight='bold')
                rttplt.bar(prototime[1], protortt[1], width=0, bottom=0, color='b')
                rttplt.xlim(timex)
                rttplt.ylim(rtty)
                rttplt.grid(True)
        i = i + 1;
    rttplt.savefig(outfile)
    rttplt.show()

if __name__ == "__main__":
    tcpfile = sys.argv[1]
    udpfile = sys.argv[2]
    outfile = sys.argv[3]
    files = [tcpfile, udpfile]
    rttplot(files, outfile)
