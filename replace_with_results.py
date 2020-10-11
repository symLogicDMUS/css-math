from test_objects.lambda_num_lists import lambda_num_lists
from test_objects.result_num_lists import result_num_lists
from test_objects.source_strs_lambda import lambda_source_strs
from pprint import pprint


def replace_with_results(source_strs, old_num_lists, result_num_lists):
    """Step 6. replace original values with results of operations"""
    for i in range(len(source_strs)):
        for j in range(len(old_num_lists)):
            for k in range(len(old_num_lists[j])):
                source_strs[i] = source_strs[i].replace(old_num_lists[j][k], str(result_num_lists[j][k]))
    return source_strs


if __name__ == "__main__":
    pprint(replace_with_results(lambda_source_strs, lambda_num_lists, result_num_lists))
