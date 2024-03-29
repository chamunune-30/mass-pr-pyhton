import datetime
import yaml

def replace_words_move_file(source_path, targate_path, words_to_replace):
with open(source _path) as f:
file_data = f.read()

for serach_text, replace_text in words_to_replace.items():
file_data = file_data.replace(search_text, replace_rext)

with open(target_path, 'W') as f :
f.write(file_data)