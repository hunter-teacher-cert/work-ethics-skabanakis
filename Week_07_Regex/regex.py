import re


def find_name(line):
  #they are looking for the fist letter of the m, and then trying to find either the mr, mrs, or misss followed by a "." then giving the length of the alphabet to make sure to accomidate for the different characaters either capital or lowercase from the program for any length

   pattern = r"([M]?(r|s|rs|iss)?\.?\ ?[A-Z][a-z]*\ [A-Z][a-z]*)
    result = re.findall(pattern,line)

    pattern = r"(Mr|Ms|Mrs|Dr)\.?([\ ][A-Z][a-z]*\ [A-Z][a-z]*)"
    result = re.findall(pattern,line)
    #this is trying to find a regular name without a proper title such as mrs,ms,mr,dr,miss.
    pattern = r"([A-Z][a-z]+)( [A-Z][a-z]*)"
    result2 = re.findall(pattern, line)
    result.extend(result2)
  
  print("Result: " + str(result))
  return result
   
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)