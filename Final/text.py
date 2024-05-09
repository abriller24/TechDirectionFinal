import maya.cmds as mc

window = mc.window(title="Lego Piece Builder", menuBar=True, width=300)
mc.columnLayout("Block")
mc.intSliderGrp("blockWidth", label = "Block Width:", field=True, min=1, max=10, v=4)
mc.intSliderGrp("blockDepth", label = "Block Depth:", field=True, min=1, max=10, v=2)
mc.intSliderGrp("blockHeight", label = "Block Height", field=True, min=1, max=10, v=1)
mc.button(label="Create Block", c="CreateBlock()")
mc.showWindow(window)

def CreateBlock():
    width = mc.intSliderGrp("blockWidth", q=True, v=True)
    depth = mc.intSliderGrp("blockDepth", q=True, v=True)
    height = mc.intSliderGrp("blockHeight", q=True, v=True)
    sizeY =height * 0.8
    sizeX= width * 0.8
    sizeZ = depth * 0.8

    block = mc.polyCube(h=sizeY, w=sizeX, d=sizeZ, sx=width, sz=depth, sy=height)

    for i in range(width):
        for j in range(depth):
            nub = mc.polyCylinder(r=0.25, h=0.2)
            mc.move(sizeY/2.0 + 0.1, moveY=True, a=True)
            mc.move((-sizeX/2.0 + (i+0.5) * 0.8), moveX=True, a=True)
            mc.move((-sizeZ/2.0 + (j+0.5) * 0.8), moveZ=True, a=True)

            block = mc.polyCBoolOp(block, nub, op=1, ch=False)

    temp = mc.polyCube(h=sizeY, w=sizeX-0.12 * 2, d=sizeZ-0.12 * 2, sx=1, sz=1)
    mc.move(-0.1, moveY=True)
    block = mc.polyCBoolOp(block, temp, op=2, ch=False)

    for i in range(width - 1):
        for j in range(depth - 1):
            for k in range(height -1):
                innerNubs = mc.polyCylinder(r=0.3255, h=0.7, sx=10)
                center = mc.polyCylinder(r=0.25, h=1, sx=10)
                innerNubs = mc.polyCBoolOp(innerNubs, center, op=2, ch=False)

                mc.move(-(-sizeY/2.0 + (k+0.5) * 0.8), moveY=True, a=True)
                mc.move((-sizeX/2.0 + (i+1) * 0.8), moveX=True, a=True)
                mc.move((-sizeZ/2.0 + (j+1) * 0.8), moveZ=True, a=True)

                block = mc.polyCBoolOp(block, innerNubs, op=1, ch=False)
                
    return block