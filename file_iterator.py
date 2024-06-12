def iterate_files(directory, excluded_dirs):
    """
    Recursively iterates over all files in the directory,
    skipping specified excluded directories.
    """
    for item in directory.iterdir():
        # Check if the item is a directory and should be skipped
        if item.is_dir() and item in excluded_dirs:
            continue

        if item.is_file():
            yield item
        elif item.is_dir():
            # Recursively yield files from subdirectories
            yield from iterate_files(item, excluded_dirs)
