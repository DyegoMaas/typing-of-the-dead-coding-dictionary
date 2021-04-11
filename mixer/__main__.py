import os
from mixer import mix

def load_set_from_file(file_abs_path: str) -> set:
    print(f'Loading terms from {file_abs_path}')
    with open(file_abs_path) as reader:
        lines = set({
            str.strip(line)
            for line in reader.readlines() 
            if line != ""
        })
        return lines

def load_full_set(dir_path: str) -> set:
    files = os.listdir(dir_path)

    terms_set = set({})
    for file in files:
        abs_path = os.path.join(dir_path, file)
        file_set = load_set_from_file(abs_path)

        terms_set |= file_set
    return terms_set

def save_combined_set(result_set, abs_result_path: str):
    with open(abs_result_path, 'w') as writer:
        for term in result_set:
            writer.write(f'{term}\n')

def main():
    themes_abs_path = os.path.abspath('themes')
    initial_set = load_full_set(themes_abs_path)
    print(f'-> Initial set:{os.linesep}{initial_set}')
    
    mixed_set = mix(initial_set)
    print(f'-> Mixed set:{os.linesep}{mixed_set}')
    
    result_file_abs_path = os.path.join(os.path.abspath('dictionary'), 'coding-dictionary.txt')
    save_combined_set(mixed_set, result_file_abs_path)

if __name__ == '__main__':
     # execute only if run as a script
    main()
    