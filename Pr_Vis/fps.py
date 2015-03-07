import time
fps = 5
skipticks = 1/(fps*1.0)
i= 0
nextsnap=time.clock()
print skipticks, fps
while (True):
    tim= time.clock()
    i=i+1
    # this prints the fps
    #'print 'Fps at start',i, 1/(time.time()-tim)
    # this is the sleep that limits the fps
    nextsnap+=skipticks
    sleeptime = nextsnap-time.clock()
    if (sleeptime>0):
        time.sleep (sleeptime)
    else:
        print 'took too long'
    print 'Fps at end:#', i, 1/(time.clock()-tim)
