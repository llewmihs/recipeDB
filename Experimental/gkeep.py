import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('joeshimwell@gmail.com', 'lzurlkkrsfjomjbc')

glist = keep.createList('Title', [
    ('Item 1'), # Not checked
    ('Item 2')  # Checked
])
glist.pinned = True

# note = keep.createNote('Todo', 'Eat breakfast')
# note.pinned = True
# note.color = gkeepapi.node.ColorValue.Red
keep.sync()