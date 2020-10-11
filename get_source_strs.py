import os
from pprint import pprint


def get_source_strs(file_paths):
    """Step 2. get files in form of strings"""
    source_strs = []
    for file_path in file_paths:
        f = open(file_path, 'r')
        source_strs.append(str(f.read()))
    return source_strs


if __name__ == "__main__":
    pprint(get_source_strs(
        ['./test_dir/Bottom/CustomiseOk.css',
         './test_dir/Bottom/PromoList.css',
         './test_dir/Bottom/PromoListScrollArrow.css',
         './test_dir/Bottom/SubList.css',
         './test_dir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplayBoard.css',
         './test_dir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplayPiece.css',
         './test_dir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplaySquare.css',
         './test_dir/Profile/ProfileWB/ExpandModal.css',
         './test_dir/Profile/ProfileWB/NewGameProfileWBHeader.css',
         './test_dir/Profile/ProfileWB/NewGameRangeTable.css',
         './test_dir/Profile/ProfileWB/NewGameScrollArrow.css',
         './test_dir/Profile/ProfileWB/ProfileWB.css',
         './test_dir/Profile/CheckBox.css',
         './test_dir/Profile/NameTooltip.css',
         './test_dir/Profile/PieceNameLabel.css',
         './test_dir/Profile/Profile.css',
         './test_dir/Profile/SubDropdown.css',
         './test_dir/Customize.css',
         './test_dir/HelpText.css',
         './test_dir/NewGamePlayerType.css',
         './test_dir/PromoAll.css',
         './test_dir/SearchBar.css']
    ))