# Demonstrates list functions

results = ["Mario", "Luigi"]

# Append adds an entry to the end of a list
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# We can't add multiple entries using append with a list
results.append(["Bowser", "Donkey Kong Jr."])
# This will add the list to the end of the results list
print(results)
# We will remove it with Remove
results.remove(["Bowser", "Donkey Kong Jr."])
# We can instead use Extend
results.extend(["Daisy", "Donkey Kong Jr."])
print(results)

# We can use Insert to add an entry at an index that we provide
# We will use this to allow Bowser to cheat to first place
results.insert(0, "Bowser")
print(results)

# We can use Reverse to... reverse the list
results.reverse()
print(results)