import random

def generate_lines(num_lines, max_depth=4):
   lines = []
   for i in range(num_lines):
       num_tabs = random.randint(0, max_depth)
       line = '\t'*num_tabs + f"{i}:{random.choice(['root', 'node', 'leaf'])}"
       lines.append(line)
   return lines


def remove_lines(lines, start_index):
   num_tabs = lines[start_index].count('\t')
   i = start_index
   while i < len(lines) and lines[i].count('\t') >= num_tabs:
       i += 1
       if (lines[i].count('\t') == num_tabs):
         break
   del lines[start_index:i]
   return lines


# Example usage
lines = generate_lines(20)
print("Generated lines:")
for line in lines:
   print(line)


start_index = 3
lines = remove_lines(lines, start_index)
print(f"\nLines with starting index {start_index} removed:")
for line in lines:
   print(line)

"""
Generated lines:
         0:leaf
   1:node
2:leaf               <--------- to be retained
3:leaf               <--------- to be removed [start]
         4:leaf
   5:root
   6:root
      7:root         <--------- to be removed [end]
8:leaf               <--------- to be retained
9:root
   10:node
            11:root
      12:root
            13:root
   14:node
            15:leaf
   16:root
         17:node
      18:root
            19:leaf

Lines with starting index 3 removed:
         0:leaf
   1:node
2:leaf               <--------- to be retained
8:leaf               <--------- to be retained
9:root
   10:node
            11:root
      12:root
            13:root
   14:node
            15:leaf
   16:root
         17:node
      18:root
            19:leaf
"""