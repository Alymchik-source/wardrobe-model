# Colors 
RED = "\033[91m"
PINK = "\033[35m"
GREEN = "\033[92m"
RESET = "\033[0m"


class Wardrobe:
    
    def _init_(self, vol):
        
        if vol < 0: 
            raise ValueError(f"{PINK}Invalid Volume!{RESET}")
        self.total_vol = vol
        self.free_vol = vol
        self.locked = True
        self.items = []
        self.catalog = {}
    
# Standart Attribute Output

    def _str_(self):
        if self.locked:
            return f"Wardrobe {RED}closed{RESET}, total vol: {self.total_vol}"
        return f"Wardrobe {GREEN}open{RESET}, total vol: {self.total_vol}"

#  to open a wardrobe

    def open(self):
        
        if not self.locked:
            print(f"already {GREEN}open{RESET}!")
            return 
        self.locked = False
        
#   to close a wardrobe

    def close(self):
        
        if self.locked:
            print(f"already {RED}closed{RESET}!")
            return
        self.locked = True
        
#  to put an item

    def put(self, name, vol=None, count=1):
        if self.locked:
            print(f"wardrobe is {RED}locked{RESET}!")
            return

        if count <= 0:
            print(f"{PINK}invalid count!{RESET}")
            return

        if name in self.catalog:
            if vol is not None and vol != self.catalog[name]:
                print(f"wrong volume for {name}! expected {self.catalog[name]}")
                return
            vol = self.catalog[name]
        else:
            if vol is None or vol <= 0:
                print(f"{PINK}invalid volume for new item!{RESET}")
                return
            self.catalog[name] = vol

        needed_vol = vol * count
        if needed_vol > self.free_vol:
            print("not enough volume!")
            return

        self.free_vol -= needed_vol
        self.items.extend([name] * count)


#  to take an item

    def take(self, name, count=1):
        if self.locked:
            print(f"wardrobe is {RED}locked{RESET}!")
            return

        if count <= 0:
            print(f"{PINK}invalid count!{RESET}")
            return

        if self.items.count(name) < count:
            print(f"not enough {name} in wardrobe!")
            return

        for _ in range(count):
            self.items.remove(name)
        self.free_vol += self.catalog[name] * count


# shows Volume and items

    def show(self):
        if self.locked:
            print(f"wardrobe is {RED}locked{RESET}!")
            return

        print(f"Free Volume = {self.free_vol}")

        if not self.items:
            print("Empty")
            return

        summary = ", ".join(f"{name} {self.items.count(name)}" for name in dict.fromkeys(self.items))
        print(summary)
        
# to clear a wardrobe (for fun)

    def clear(self):
    
        self.items = []
        self.free_vol = self.total_vol

# End of the class Wardrobe
