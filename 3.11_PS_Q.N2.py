# 2. Write a program to fill in a letter template given below with name and date.???
# # letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''



letter = ''' Dear <|NAME|>,
 You are selected!
 <|DATE|> '''

print(letter.replace("<|NAME|>", "Shreyansh").replace("<|DATE|>", "01-9-11-2026"))
