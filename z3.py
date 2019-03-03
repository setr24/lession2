students_scores = [{"school_clas": "4a", "scores": [1, 2, 5, 1, 4]}, 
                    {"school_clas": "5a", "scores": [5, 3, 1, 2, 3]}
                        ]

for score in students_scores:
    average_all = sum(score["scores"])/len(score["scores"])
    print("Средний бал в школе:", average_all)
   
    for score_class in students_scores:
        class_sum = score_class["school_clas"], sum(score_class["scores"])/len(score_class["scores"])
        print("Средний бал в классе:", class_sum)


