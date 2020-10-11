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
        ['./testDir/Bottom/CustomiseOk.css',
         './testDir/Bottom/PromoList.css',
         './testDir/Bottom/PromoListScrollArrow.css',
         './testDir/Bottom/SubList.css',
         './testDir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplayBoard.css',
         './testDir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplayPiece.css',
         './testDir/Profile/ProfileWB/NewGameDisplayBoard/NewGameDisplaySquare.css',
         './testDir/Profile/ProfileWB/ExpandModal.css',
         './testDir/Profile/ProfileWB/NewGameProfileWBHeader.css',
         './testDir/Profile/ProfileWB/NewGameRangeTable.css',
         './testDir/Profile/ProfileWB/NewGameScrollArrow.css',
         './testDir/Profile/ProfileWB/ProfileWB.css',
         './testDir/Profile/CheckBox.css',
         './testDir/Profile/NameTooltip.css',
         './testDir/Profile/PieceNameLabel.css',
         './testDir/Profile/Profile.css',
         './testDir/Profile/SubDropdown.css',
         './testDir/Customize.css',
         './testDir/HelpText.css',
         './testDir/NewGamePlayerType.css',
         './testDir/PromoAll.css',
         './testDir/SearchBar.css']
    ))