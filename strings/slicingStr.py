# Python - Slicing String

# Slicing
"""
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon,
to return a part of the string .
"""
# Example:
b = "hello world"
print(b[2:3])   # Output : l
print (b[2:4])  # Output : ll



# Slice from Start
# By leaving out hte start index, the range will start at the first character:

# Example:

print(b[:5])  # Output: hello


# Slice to the end

# By leaving out the end index, the range will go to the end:

# Example:
print(b[2:]) # Output: llo world

# Negative Indexing
"""
Use negative indexes
to start
the slice form the end of the string: """

# Example

"""
get the characters:
 From: "o" in "World!" (position -5)
 To, but not included: "d: in "World" (Position-2) :
 """

print(b[-5:-2]) # Output : wor -> comes counting from backward of the string



















































