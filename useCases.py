import pythonGraphicalManipulator as pgm 

pixelGrid = pgm.imageToPixelGrid("testInputImage.jpg")
# pgm.pixelGridToImage(pixelGrid, "tetsOutput.jpg")

# fhPG = pgm.flipHoriz(pixelGrid)
# pgm.pixelGridToImage(fhPG, "tetsOutput.jpg")
# pgm.pixelGridToImage(pgm.flipVert(pixelGrid), "tetsOutput.jpg")
# pgm.pixelGridToImage(pgm.singleColorPop(pixelGrid, 0, 255, 0, 254), "tetsOutput.jpg")
pgm.pixelGridToImage(pgm.changeColor(pixelGrid, 0, 255, 0, 255, 0, 0, 200), "tetsOutput.jpg")
# pgm.adjustBrightness()
# pgm.adjustShadownIntensity()
# pgm.adjustBlackPoint()
# pgm.adjustWarmth()