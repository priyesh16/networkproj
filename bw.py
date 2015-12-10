#!/usr/bin/python

import sys
import getopt
import subprocess
from subprocess import call
import re
import matplotlib.pyplot as bwplt
import numpy as np

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


def bwplot(files, outfile):
    color = 'blue'
    maxlist = [0, 0]
    find = re.compile("-")
    protobw = [] 
    prototime = []
    bwarray = [];
    timearray = [];
    bwcol = -6
    lenwords = 13

    bwplt.figure(figsize=(15, 15))
    for i in xrange(len(files)):
        filename = files[i]
        maxdata = 0;
        j = 0;
        with open(filename, "r") as f:
            for line in f:
                j = j + 1;
                if j < 8:
                    continue;
                words = line.split()
                if len(words) != lenwords:
                    continue;
                try:
                    bw = float(words[bwcol])
                except ValueError:
                    continue; 
                if bw > maxdata:
                    maxdata = bw
                    
            maxlist[i] = maxdata
            print maxlist

    for i in xrange(len(files)):
        filename = files[i]
        j = 0;
        with open(filename, "r") as f:
            for line in f:
                j = j + 1;
                if j < 8:
                    continue;
                words = line.split()
                if len(words) != lenwords:
                    continue;
                timestr = words[1]
                try:
                    bw = float(words[bwcol])/1000
                except ValueError:
                    continue; 
                time = float(timestr) 
                timearray.append(time);
                if time > 4 and time < 5:
		    print time, bw
                bwarray.append(bw);
        protobw.append(bwarray)
        prototime.append(timearray)
        bwarray = []
        timearray = []

    i = 1;
    for filename in files:
        if "tcp" in filename and "phys" in filename:
		tcpx = [4, 5]
	        tcpy = [0, 150]
                sub = bwplt.subplot(2,1,i)
                sub.set_title("Physical Machine - TCP Throughput")
                bwplt.xlabel("Time")
                bwplt.ylabel("TCP Throughput (Mbps)")
                bwplt.xlim(tcpx)
                bwplt.ylim(tcpy)
                bwplt.plot(prototime[0], protobw[0], 'yo-')
                bwplt.grid(True)
        if "tcp" in filename and "virt" in filename:
		tcpx = [25, 35]
	        tcpy = [0, 150]
                sub = bwplt.subplot(2,1,i)
                sub.set_title("Virtual Machine - TCP Throughput")
                bwplt.xlabel("Time")
                bwplt.ylabel("TCP Throughput (Mbps)")
                bwplt.xlim(tcpx)
                bwplt.ylim(tcpy)
                bwplt.plot(prototime[0], protobw[0], 'yo-')
                bwplt.grid(True)
        if "udp" in filename and "phys" in filename:
	        udpx = [37, 47]
	        udpy = [0, 150]
                sub = bwplt.subplot(2,1,i)
                sub.set_title("Physical Machine - UDP Throughput")
                bwplt.xlabel("Time")
                bwplt.ylabel("UDP Throughput (Mbps)")
                bwplt.xlim(udpx)
                bwplt.ylim(udpy)
                bwplt.plot(prototime[1] , protobw[1], 'r-')
                bwplt.grid(True)
        if "udp" in filename and "virt" in filename:
	        udpx = [45, 55]
                udpy = [0, 150]
                sub = bwplt.subplot(2,1,i)
                sub.set_title("Virtual Machine - UDP Throughput")
                bwplt.xlabel("Time")
                bwplt.ylabel("UDP Throughput (Mbps)")
                bwplt.xlim(udpx)
                bwplt.ylim(udpy)
                bwplt.plot(prototime[1], protobw[1], 'yo-')
                bwplt.grid(True)
        i = i + 1;
    bwplt.savefig(outfile)
    bwplt.show()

if __name__ == "__main__":
    tcpfile = sys.argv[1]
    udpfile = sys.argv[2]
    outfile = sys.argv[3]
    files = [tcpfile, udpfile]
    bwplot(files, outfile)
