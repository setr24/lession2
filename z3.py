students_scores = [{"school_clas": "4a", "scores": [1, 2, 5, 1, 4]}, 
                    {"school_clas": "5a", "scores": [5, 3, 1, 2, 3]}
                        ]
average_sum_spisok = [] 
average_sum_len = []
average_sum_clas = []

for score in students_scores:
    average_sum = sum(score["scores"])
    average_len = len(score["scores"])
    average_sum_spisok.append(average_sum)
    average_sum_len.append(average_len)

    average_clas = (score["school_clas"], sum(score["scores"]) / len(score["scores"]))
    average_sum_clas.append(average_clas)
   
    average_clas_all = sum(score["scores"]) / len(score["scores"])
print(average_sum_clas)

average_all = sum(average_sum_spisok) / sum(average_sum_len)
print("Средний бал по всей школе:", average_all)
print("Средний бал в классе:", average_sum_clas)
