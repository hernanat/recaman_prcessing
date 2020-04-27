def setup():
    size(2500, 750)
    background(50, 75, 100)
    padding = 100
    global xStart, xEnd, numTicks, step
    xStart = 0 + padding
    xEnd = width - padding
    numTicks = 2300
    step = (xEnd - xStart) // (numTicks - 1)
    sequence = calculateSequence(500)
    drawNumberLine(tickers = False)
    drawSequenceArcs(sequence)
    #drawSequenceArcs(sequence, mode = 'x')
    
def calculateSequence(n):
    sequence = [0]
    if n == 0:
        return sequence
    else:
        sequence = sequence + [None] * (n - 1)

        for i in range(1, n):
            forward = sequence[i - 1] - i
            if forward > 0 and forward not in sequence:
                sequence[i] = forward
            else:
                sequence[i] = sequence[i - 1] + i
        
        return sequence

def drawNumberLine(tickers = True):
    global xStart, xEnd, step, numTicks
    line(xStart, height / 2, xEnd, height / 2)
    
    if tickers:
        #drawTicker(xStart)
        #drawTicker(xEnd)
        for i in range(numTicks + 1):
            drawTicker(xStart + i * step)
    
def drawTicker(x):
    pushMatrix()
    translate(x, height / 2)
    line(0, -5, 0, 5)
    popMatrix()
    
def drawSequencePoints(sequence):
    for x in sequence:
        drawPoint(x)
        
def drawSequenceArcs(sequence, points = False, mode = 'Normal' ):
    seqLen = len(sequence)
    if points:
        drawSequencePoints(sequence)
    for i in range(seqLen - 1):
        drawArc(sequence[i], sequence[i + 1], i % 2 != 0, mode)

def drawArc(fromX, toX, flip, mode = 'Normal'):
    noFill()
    ellipseMode(CORNER)
    translatedFromX = xStart + fromX * step
    translatedToX = xStart + toX * step
    
    pushMatrix()
    
    calculateTranslation(translatedFromX, translatedToX)
    
    diameter = abs(translatedToX - translatedFromX)
    
    if mode == 'Normal':
        drawFlippedOrNormalArc(diameter, flip)
    else:
        drawCircle(diameter, flip)
    
    popMatrix()
    
def calculateTranslation(translatedFromX, translatedToX):
    if translatedFromX < translatedToX:
        translate(translatedFromX, height / 2)
    else:
        translate(translatedToX, height / 2)

def drawFlippedOrNormalArc(diameter, flip):
    if flip:
        drawFlippedArc(diameter)
    else:
        drawNormalArc(diameter)

def drawFlippedArc(diameter):
    stroke(250, 100, 50)
    arc(0, -diameter / 2, diameter, diameter, PI, TWO_PI)

def drawNormalArc(diameter):
    stroke(100, 250, 100)
    arc(0, -diameter / 2, diameter, diameter, 0, PI)
    
def drawCircle(diameter, flip):
    if flip:
        stroke(250, 100, 50)
    else:
        stroke(100, 250, 100)
    arc(0, -diameter / 2, diameter, diameter, 0, TWO_PI)

def drawPoint(x):
    pushMatrix()
    translate(xStart + x * step, height / 2)
    circle(0, 0, 5)
    popMatrix()
    
    
