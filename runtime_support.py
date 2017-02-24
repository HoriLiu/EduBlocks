def distance_to_player(x, y, z):
  global mc, math
  pp = mc.player.getPos()
  xd = x - pp.x
  yd = y - pp.y
  zd = z - pp.z
  return math.sqrt((xd * xd) + (yd * yd) + (zd * zd))

def buildPumpkin(x, y, z):
  mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, 35, 1)
  mc.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, 0, 1)
  mc.setBlock(x-1, y+1, z-2, 0)
  mc.setBlock(x+1, y+1, z-2, 0)

  mc.setBlocks(x+1, y-1, z-2, x-1, y-1, z-2, 0, 0)
  mc.setBlock(x-1, y+1, z+2, 0)
  mc.setBlock(x+1, y+1, z+2, 0)

  mc.setBlocks(x+1, y-1, z+2, x-1, y-1, z+2, 0, 0)
  mc.setBlock(x-2, y+1, z-1, 0)
  mc.setBlock(x-2, y+1, z+1, 0)

  mc.setBlocks(x-2, y-1, z+1, x-2, y-1, z-1, 0, 0)
  mc.setBlock(x+2, y+1, z-1, 0)
  mc.setBlock(x+2, y+1, z+1, 0)

  mc.setBlocks(x+2, y-1, z+1, x+2, y-1, z-1, 0, 0)
  mc.setBlock(x, y+3, z, 35, 5)

print('Starting...')
