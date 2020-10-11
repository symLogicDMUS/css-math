from get_css_file_paths import get_css_file_paths
from get_source_strs import get_source_strs
from tag_matchs import tag_matches
from get_matches import get_matches
from do_arithmetic import do_arithmetic
from replace_with_results import replace_with_results
from save_results import save_results


def css_math(dir_path, op, x, test=False):
    """Top. scale numbers in css files up or down by the same arithmitic operation"""
    css_file_paths = get_css_file_paths(dir_path)
    source_strs = get_source_strs(css_file_paths)
    source_strs = tag_matches(source_strs)
    num_lists = get_matches(source_strs)
    result_num_lists = do_arithmetic(op, x, num_lists)
    result_strs = replace_with_results(source_strs, num_lists, result_num_lists)
    save_results(css_file_paths, result_strs, test=test)


if __name__ == "__main__":
    css_math("./test_dir", "*", 2)