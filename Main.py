import library
import two_pointers
import two_sums
import word_counter

def main():
    print("----- 1. Тест библиотеки -----")
    lib = library.Library()
    lib.add_book("Война и мир", "Толстой")
    lib.add_book("Кладбище домашних животных", "Кинг")
    print("Все книги:", lib.get_all_books())
    print()

    print("----- 2. Тест удаления повторяющихся элементов -----")
    arr = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    print(two_pointers.delete_identical(arr))
    print()

    print("----- 3. Тест поиска пар с заданной суммой -----")
    arr1 = [1, 2, 5, 6, 7, 8]
    target_sum1 = 10
    print("Пары:", two_sums.find_pairs(arr1, target_sum1))
    print("----------")
    arr2 = [1, 4, 5, 6, 7, 10]
    target_sum2 = 11
    print("Пары:", two_sums.find_pairs(arr2, target_sum2))
    print()

    print("----- 4. Тест поиска слов по количеству совпадений -----")
    text = "hello world hello"
    n = 2
    print(f"Слова, встречающиеся {n} раз(а):", word_counter.find_words_with_count(text, n))

if __name__ == "__main__":
    main()