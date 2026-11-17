# wardrobe-model
A Python OOP practice project simulating a wardrobe with volume tracking, item caching, and state validation.
## Features

* *Lock Mechanism:* Open and close the wardrobe. Items cannot be added, removed, or inspected while the door is locked.
* *Smart Volume Catalog:* Automatically remembers the volume of newly added items so you don't have to specify their size again on subsequent additions.
* *Batch Operations:* Put or take multiple identical items at once using the count parameter.
* *Data Validation:* Prevents negative volumes, volume mismatches for existing items, and exceeding total wardrobe capacity.
* *Terminal Styling:* Uses ANSI escape codes for clear, color-coded console feedback.

## Usage Example

```python
from wardrobe import Wardrobe

# Create a wardrobe with a total volume of 500
my_wardrobe = Wardrobe(500)
print(my_wardrobe)

# Open the wardrobe and add items
my_wardrobe.open()
my_wardrobe.put("Hat", vol=10, count=2)
my_wardrobe.put("Jacket", vol=50, count=3)

# Add known items without specifying volume again
my_wardrobe.put("Hat")

# Inspect free space and stored items
my_wardrobe.show()

# Take items out or empty the wardrobe
my_wardrobe.take("Jacket", count=1)
my_wardrobe.clear()
my_wardrobe.close()
```


## Notes

* Built with standard Python 3 (no external libraries required).
* Developed on mobile (Pydroid 3) as a hands-on OOP learning project with AI mentorship.
