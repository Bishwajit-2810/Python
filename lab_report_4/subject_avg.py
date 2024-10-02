subject_scores = { 
    'Math' : [90, 85, 88, 92, 95] , 
    'Physics' : [75, 80, 85, 90, 95] ,
    'Chemistry': [85, 90, 92, 88, 82]
    }
new_dict={}

for key in subject_scores.keys():
    new_dict[key] = sum(subject_scores[key])/len(subject_scores[key])

print(new_dict)
