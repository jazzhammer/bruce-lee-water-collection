# a problem solving exercise.

problem: 

on a 2d plane, a series of parallel walls of an assortment of heights are 
placed along a base at integral points, with variable integral distances 
between them, eg: 

```
   |       |         
   | |     |      
   | |     |   
  _|_|___|_|_____|___ 
```
water (*) falls from the top of the plane:

```
   **     ***
   |* *** *|**         
   |*|*** *|*****   
  *|*|*** *|*******
  *|*|***|*|*****|** 
```

but water being water, only stays where it is captured by walls on both its sides: 

```
   |* *** *|        <- all water units have 1 wall segment on each side 
   |*|*** *|        <- all water units have 1 wall segment on 1 side, 2 on the other
   |*|*** *|
   |*|***|*|*****| 
```

the objective of the exercise is to create a calculator that receives an input of
an array or list of wall heights, and produces a count of water collected.

we assume: 
1. water falls until all available volumes are filled
2. walls have 0 thickness, ie. water does not pile up on top of a wall
3. a unit of water(*) stays if and only if it is between 1 or more wall segments (|) on both sides
