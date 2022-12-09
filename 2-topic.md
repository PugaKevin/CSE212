# SET
Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data. 

One very important concept is that a set() is, it cannot have duplicates! 

 Indexing does NOT work with set(). If you try to index you will get an error message. Don't do it.  

![Sets Rules](Images/sets.jpg)

## Terms to know
* Creates set. <br>
 my_set = {1,2,3}

*  Add element to set. <br>
    my_set.add(2) <br>
    Add multiple elements use update()<br>
    my_set.update([2, 3, 4])

* Removing elements. There are 2 ways to do this, discard() function leaves a set unchange if the element is not there. If you use remove(), and the element is not ther an error will be raised. 

    my_set.discard(4)<br>


    my_set.remove(6)<br>    



# Syntax

```

# Integers
my_set = {1, 2, 3}
print(my_set)

#  Mixed Datatypes
my_set = {1.0, "gucci", (1, 2, 3)}
print(my_set)
```
OUTPUT

```

{1, 2, 3}
{1.0, (1, 2, 3), 'gucci'}

```


# Examples
```

sample_set = {'Peter', 'Globin', 19, 42.25}
print(sample_set)
# Output {42.25, 19, 'Peter', 'Goblin'}


book_set = set(("Harvey Porter", "Space Wars", "Twinight"))
print(book_set)
# output {'Space Wars', 'Twinight', 'Harvey Porter'}



```
YOUR TURN! 

![Confused](Images/tryit.gif)

# Problem to Solve
Print each individual number in the set.<br>
Look for 69 in the set.<br>
```
    my_set = {21, 68, 112, 11, 5, 3, 102032, 12}
```



[Link to the solution](solution2.py)