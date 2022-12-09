# This is a directional map. By input the coordinates, Python will 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input('Where do you want to put the treasure? Pick column (vertical) first and row (horizontal) second. Just type your answer in a two digit number, such "23" for column 2 row 3.')
# This one took me a minute to realize. While the user is picking the number of which column they want, they are actually indicating on what horizontal vertice they decide. The opposite is of course true for the row choice as well. 
horizontal = int(position[0])
vertical = int(position[1])
# Because the columns and rows start with 1, as opposed to 0, how the machine will understand it, we have to remove 1 from the answer to get the appropriate column and row. 
selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"
# Now that we have changed the output, we reprint with the chosen index marked.
print(f"{row1}\n{row2}\n{row3}")
