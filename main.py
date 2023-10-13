import Levenshtein
import time

from CustomLevenshtein import MyLevenshtein


if __name__ == '__main__':
    first_str = "hello worldsazdaewagftgb fqa ewaewqqewffewq"
    second_str = "wqeqweqweqwsasaassadbye world!"

    start_time = time.time()
    dist = Levenshtein.distance(first_str, second_str)
    library_func_time = (time.time() - start_time)
    print("--- %s seconds ---" % (library_func_time))
    print("Расстояние = ", dist)

    start_time = time.time()
    dist = MyLevenshtein.levenshtein_distance(first_str, second_str)
    my_func_time = (time.time() - start_time)

    print("--- %s seconds ---" % (my_func_time))
    print("Расстояние = ", dist)

    start_time = time.time()
    dist = MyLevenshtein.naive_levenshtein_distance(first_str, second_str)
    my_func_time = (time.time() - start_time)

    print("--- %s seconds ---" % (my_func_time))
    print("Расстояние = ", dist)
