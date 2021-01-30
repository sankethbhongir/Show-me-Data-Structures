from os import listdir
from os.path import join

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # getting all the directories from the root
    dirs = listdir(path)
    
    # segregatting suffix files and directories from the root
    files = [join(path,file) for file in dirs if '.'+suffix in file]
    folders = [file for file in dirs if '.' not in file]
    
    # recursivly iterating through sub-directories to find suffix files
    for folder in folders:
        files.extend(find_files(suffix, join(path, folder)) )
    return files

'''Test Case 1'''
'''
Input-
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
'''
print(find_files('c', 'testdir'))
# ['testdir/t1.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

'''Test Case 2'''
print(find_files('t', 'testdir'))
# [] since it .t files are not in testdir

'''Test Case 3'''
'''
Input-
./testdir
./testdir/subdir1
./testdir/subdir1/subsubdir1
./testdir/subdir1/subsubdir1/subsubsubdir1
./testdir/subdir1/subsubdir1/subsubsubdir1/r.c
./testdir/subdir1/subsubdir1/subsubsubdir1/subsubsubsubdir1
./testdir/subdir1/subsubdir1/subsubsubdir1/subsubsubsubdir1/t.c
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
'''
print(find_files('h', 'testdir'))
# ['testdir/t1.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/subdir1/a.h',
# 'testdir/subdir1/subsubdir1/subsubsubdir1/subsubsubsubdir1/t.h']
