from test_objects.source_strs_sub_results import source_strs_sub_results
from test_objects.css_file_paths import css_file_paths


def save_results(file_paths, result_strs, test=False):
    """Step 7. save the result strings to files"""
    for i in range(len(file_paths)):
        path = file_paths[i]
        if test:
            path = file_paths[i].replace('test_dir', 'result_dir')
        f = open(path, 'w')
        f.write(result_strs[i])
        f.close()


if __name__ == "__main__":
    save_results(css_file_paths, source_strs_sub_results, test=True)