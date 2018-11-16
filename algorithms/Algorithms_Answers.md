Add your answers to the Algorithms exercises here.

## Excercise I
1. Should be O(n) due to it just being a single loop
2. Looks to be O(n^3) due to there being 3 nested loops
3. Should be O(n) since it seems to only grow in a linear fashion

## Excercise II
- Lets start by dropping the egg from half the stories of the building (n/2)

  if egg is broken:
    - lets move to the floor between the current floor (n/2 in this case)  and the bottom floor
    - now throw an egg again to see if it is broken
      + if so, repeat "if egg is broken" again
  
  elif egg is not broken:
    - lets move to the floor between the current floor and top-most floor
    - now throw an egg again to see if it is broken
      + if not broken, repeat "if egg is broken again"

- it will loop over and over again, until precise floor is found
#AlgorithmsAreEvil
#SaveTheEggs
#ChickensMatter
